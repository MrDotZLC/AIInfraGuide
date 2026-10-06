#!/usr/bin/env python3
"""规范化分类表,避免手工写错列:
  1) 第二列以 @ 开头(锚点写到了分类列)→ 并回 id 列
  2) 去掉越界 id 与重复 id(越界指超过 --max-id,默认不限)
  3) 报告分类非法或缺少分类的行

  python normalize_classify.py --in classify.tsv [--max-id 343]
"""

from __future__ import annotations

import argparse
from pathlib import Path

CATEGORY_FILES = (
    "01-cpp",
    "02-cpp-algorithm",
    "03-ai",
    "04-gpu",
    "05-ai-infra",
    "06-other-language",
    "07-other-language-algorithm",
    "08-project",
    "09-behavioral",
    "10-irrelevant",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="src", required=True)
    parser.add_argument("--max-id", type=int, default=0, help="允许的最大条目 id(0 表示不限)")
    parser.add_argument("--min-id", type=int, default=0, help="允许的最小条目 id")
    args = parser.parse_args()

    path = Path(args.src)
    out_lines = []
    joined = 0
    dropped_ids = 0
    problems = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1].startswith("@"):
            parts = [parts[0] + "," + parts[1]] + parts[2:]
            joined += 1
        ids, anchors, kept = [], [], []
        for token in parts[0].split(","):
            token = token.strip()
            if not token:
                continue
            if token.startswith("@"):
                anchors.append(token)
                continue
            if not token.isdigit():
                problems.append(f"{number}: id 非数字 {token!r}")
                continue
            if args.max_id and int(token) > args.max_id:
                dropped_ids += 1
                continue
            if args.min_id and int(token) < args.min_id:
                dropped_ids += 1
                continue
            if token in ids:
                dropped_ids += 1
                continue
            ids.append(token)
        kept = ids + anchors
        if not kept:
            continue
        parts = [",".join(kept)] + parts[1:]
        if len(parts) > 1 and parts[1] and parts[1] not in CATEGORY_FILES:
            problems.append(f"{number}: 分类 {parts[1]!r} 非法")
        out_lines.append("\t".join(parts))

    path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"规范化 {path.name}:合并锚点列 {joined} 行;丢弃 id {dropped_ids} 个;输出 {len(out_lines)} 行")
    for problem in problems:
        print("WARN  " + problem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
