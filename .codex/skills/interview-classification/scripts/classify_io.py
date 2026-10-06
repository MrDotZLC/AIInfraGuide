#!/usr/bin/env python3
"""把分类表(按 id 引用条目)展开成题库中间表。

分类表列:id[,id...]  category  topic  subtopic  text(可选,留空则用原文)
id 列里可以用 @锚点 合并到已有题目:锚点优先匹配本次新建的题目,再匹配现有中间表,
例如 `123,@bank conflict`。也支持 @N 按现有中间表的行号引用。
输出中间表列:category  topic  subtopic  question  sources(; 分隔)

  python classify_io.py --worklist worklist.tsv --in classify.tsv --out bank.tsv [--bank-tsv bank.tsv]
"""

from __future__ import annotations

import argparse
from pathlib import Path

CATEGORY_FILES = (
    "01-cpp.md",
    "02-algorithm.md",
    "03-ai.md",
    "04-gpu.md",
    "05-ai-infra.md",
    "06-other-language.md",
    "07-behavioral.md",
)


def load_worklist(path: Path) -> dict[str, tuple[str, str, str]]:
    items = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    for line in lines[1:]:
        parts = line.split("\t")
        row = dict(zip(header, parts))
        items[row["id"]] = (row["file"], row["text"], row["company"])
    return items


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worklist", required=True)
    parser.add_argument("--in", dest="src", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--bank-tsv", help="现有中间表(支持 @N 合并,并保留未合并的行)")
    parser.add_argument("--source-prefix", default="docs/interview/", help="来源文件路径前缀")
    args = parser.parse_args()

    items = load_worklist(Path(args.worklist))
    existing: list[list[str]] = []
    if args.bank_tsv and Path(args.bank_tsv).is_file():
        for line in Path(args.bank_tsv).read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing.append((line.split("\t") + ["", "", "", "", ""])[:5])
    consumed: set[int] = set()
    created: dict[str, int] = {}
    rows = []
    missing = []
    for line in Path(args.src).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = (line.split("\t") + ["", "", "", ""])[:5]
        tokens = [t.strip() for t in parts[0].split(",") if t.strip()]
        if not tokens:
            continue
        ids = [t for t in tokens if not t.startswith("@")]
        ref_tokens = [t[1:] for t in tokens if t.startswith("@")]
        unknown = [i for i in ids if i not in items]
        if unknown:
            missing.append(f"{parts[0]}: 未知 id {unknown}")
            continue
        base = None
        anchor_hit: int | None = None
        anchor_key: str | None = None
        anchor_error = False
        # 先看锚点是否已在本轮创建过(重复引用同一条合并目标)
        for token in ref_tokens:
            if not token.isdigit() and token in created:
                anchor_hit = created[token]
                anchor_key = token
        if anchor_hit is not None:
            text_seed = rows[anchor_hit][3]
        else:
            text_seed = None
        for token in ref_tokens:
            if token in created:
                continue
            if token.isdigit():
                ref = int(token)
                if 1 <= ref <= len(existing):
                    consumed.add(ref - 1)
                    if base is None:
                        base = existing[ref - 1]
                else:
                    missing.append(f"{parts[0]}: 行号 @{ref} 超出中间表范围,该行已丢弃")
                    anchor_error = True
                continue
            hit_new = [idx for idx, r in enumerate(rows) if token in r[3]]
            if hit_new:
                anchor_hit = hit_new[0] if anchor_hit is None else anchor_hit
                anchor_key = token
                continue
            hit_existing = [
                idx for idx, r in enumerate(existing) if idx not in consumed and token in r[3]
            ]
            if not hit_existing:
                missing.append(f"{parts[0]}: 找不到锚点 @{token},该行已丢弃")
                anchor_error = True
                break
            if len(hit_existing) > 1:
                missing.append(
                    f"{parts[0]}: 锚点 @{token} 命中 {len(hit_existing)} 条,已取第一条"
                )
            consumed.add(hit_existing[0])
            if base is None:
                base = existing[hit_existing[0]]
            anchor_key = token
        if anchor_error:
            continue
        text = parts[4].strip()
        sources = []
        for i in ids:
            file = args.source_prefix + items[i][0]
            if file not in sources:
                sources.append(file)
        if base:
            for s in base[4].split(";"):
                if s and s not in sources:
                    sources.append(s)
        merge_target = None
        if anchor_hit is not None:
            merge_target = anchor_hit
        elif not text:
            for token in ref_tokens:
                if token in created:
                    merge_target = created[token]
                    break
        if merge_target is not None:
            current = rows[merge_target][4].split(";") if rows[merge_target][4] else []
            for s in sources:
                if s not in current:
                    current.append(s)
            rows[merge_target][4] = ";".join(current)
            if anchor_key:
                created.setdefault(anchor_key, merge_target)
            continue
        if not text:
            text = text_seed or (base[3] if base else (items[ids[0]][1] if ids else ""))
        category = parts[1].strip() or (base[0] if base else "")
        if category.startswith("@"):
            missing.append(f"{parts[0]}: @N 写到了分类列(应写成 `id,@N`),该行已丢弃")
            continue
        if category and not category.endswith(".md"):
            category += ".md"
        if category not in CATEGORY_FILES:
            missing.append(f"{parts[0]}: 分类 {category!r} 非法,该行已丢弃")
            continue
        topic = parts[2].strip() or (base[1] if base else "")
        subtopic = parts[3].strip() or (base[2] if base else "")
        rows.append([category, topic, subtopic, text, ";".join(sources)])
        for token in ref_tokens:
            created.setdefault(token, len(rows) - 1)

    kept = [r for idx, r in enumerate(existing) if idx not in consumed]
    final = kept + rows
    Path(args.out).write_text(
        "\n".join("\t".join(r) for r in final) + ("\n" if final else ""), encoding="utf-8"
    )
    print(f"展开 {len(rows)} 条(合并引用 {len(consumed)} 条,保留旧表 {len(kept)} 条)-> {args.out}")
    for m in missing:
        print("WARN  " + m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
