#!/usr/bin/env python3
"""把面经里的编号条目抽成工作清单,便于分批分类。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ITEM_RE = re.compile(r"^\s*(\d+)[\.、]\s*(.+?)\s*$")
HEADING_RE = re.compile(r"^#{2,4}\s+(.+?)\s*$")


def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    fm = {}
    body = text
    if fm_match:
        for line in fm_match.group(1).split("\n"):
            kv = re.match(r"^(\w+):\s*(.*)$", line.rstrip("\r"))
            if kv:
                fm[kv.group(1)] = kv.group(2).strip().strip("'\"")
        body = fm_match.group(2)
    heading = ""
    rows = []
    for line in body.split("\n"):
        head = HEADING_RE.match(line)
        if head:
            heading = head.group(1)
            continue
        item = ITEM_RE.match(line)
        if item:
            rows.append((heading, item.group(1), item.group(2)))
    return fm, rows


def sort_key(tier: str) -> int:
    if tier == "综合":
        return 0
    if tier.startswith("T") and tier[1:].isdigit():
        return int(tier[1:])
    return 9


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="docs/interview")
    parser.add_argument("--out", default="worklist.tsv")
    parser.add_argument("--tier", help="只导出某个梯队,如 T0")
    parser.add_argument("--company", help="只导出某家公司")
    args = parser.parse_args()

    root = Path(args.sources)
    records = []
    for path in sorted(root.glob("*.md")):
        fm, rows = parse(path)
        tier = fm.get("tier", "?")
        if args.tier and tier != args.tier:
            continue
        if args.company and fm.get("company") != args.company:
            continue
        for heading, number, text in rows:
            records.append((sort_key(tier), tier, fm.get("company", ""), fm.get("interviewType", ""), path.name, heading, number, text))

    # 保持文档内原始顺序,只按梯队与文件名排序
    records.sort(key=lambda r: (r[0], r[2], r[4]))
    lines = ["id\ttier\tcompany\ttype\tfile\theading\tno\ttext"]
    counter = 0
    for r in records:
        counter += 1
        lines.append("\t".join([str(counter), r[1], r[2], r[3], r[4], r[5], r[6], r[7]]))
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")

    files = {r[4] for r in records}
    print(f"条目 {len(records)} 条,来自 {len(files)} 个文件 -> {args.out}")
    from collections import Counter
    for tier, count in sorted(Counter(r[1] for r in records).items(), key=lambda kv: sort_key(kv[0])):
        print(f"  {tier:<6} {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
