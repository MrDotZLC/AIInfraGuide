#!/usr/bin/env python3
"""题库 markdown 与中间表(TSV)互转,支持分批增量与断点续跑。

TSV 列:category  topic  subtopic  question  sources(; 分隔)

  python bank_io.py export --bank docs/interview-bank --out bank.tsv
  python bank_io.py generate --in bank.tsv --bank docs/interview-bank
"""

from __future__ import annotations

import argparse
import re
from collections import OrderedDict
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
TITLES = {
    "01-cpp.md": "# C++ / Linux / 系统编程",
    "02-algorithm.md": "# 算法与编程题",
    "03-ai.md": "# AI / 模型与算法",
    "04-gpu.md": "# GPU / CUDA / Kernel",
    "05-ai-infra.md": "# AI Infra",
    "06-other-language.md": "# 其他语言基础",
    "07-behavioral.md": "# 行为面 / HR",
}
EMPTY_NOTE = "本次输入未涉及该分类。"
QUESTION_RE = re.compile(r"^[-*]\s+(.*\S)\s*$")
H2_RE = re.compile(r"^##\s+(.*\S)\s*$")
H3_RE = re.compile(r"^###\s+(.*\S)\s*$")
SOURCE_PATH_RE = re.compile(r"`([^`]+?\.md)(?::\d+(?:-\d+)?)?`")
PUNCT_MAP = str.maketrans({"，": ",", "；": ";", "：": ":", "（": "(", "）": ")", "？": "?", "！": "!"})


def normalize_text(text: str) -> str:
    return text.translate(PUNCT_MAP)


def export(bank: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for name in CATEGORY_FILES:
        path = bank / name
        if not path.is_file():
            continue
        topic = subtopic = ""
        current: list[str] | None = None
        pending_sources: list[str] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            h2 = H2_RE.match(line)
            h3 = H3_RE.match(line)
            question = QUESTION_RE.match(line)
            if h3:
                subtopic = h3.group(1)
                continue
            if h2:
                topic, subtopic = h2.group(1), ""
                continue
            if question:
                if current is not None:
                    rows.append([name, current[2], current[3], current[0], ";".join(current[1])])
                current = [question.group(1), [], topic, subtopic]
                continue
            if current is not None:
                current[1].extend(SOURCE_PATH_RE.findall(line))
        if current is not None:
            rows.append([name, current[2], current[3], current[0], ";".join(current[1])])
    return rows


def load(tsv: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        while len(parts) < 5:
            parts.append("")
        rows.append(parts[:5])
    return rows


def generate(rows: list[list[str]], bank: Path) -> None:
    grouped: dict[str, "OrderedDict[str, OrderedDict[str, list[tuple[str, list[str]]]]]]"] = {}
    for category, topic, subtopic, question, sources in rows:
        if category not in CATEGORY_FILES:
            continue
        topics = grouped.setdefault(category, OrderedDict())
        subs = topics.setdefault(topic or "未分组", OrderedDict())
        subs.setdefault(subtopic or "", []).append(
            (question, [s for s in sources.split(";") if s])
        )

    for name in CATEGORY_FILES:
        lines = [TITLES[name], ""]
        topics = grouped.get(name)
        if not topics:
            lines.append(EMPTY_NOTE)
            lines.append("")
            (bank / name).write_text("\n".join(lines), encoding="utf-8")
            continue
        for topic, subs in topics.items():
            lines.append(f"## {topic}")
            lines.append("")
            for subtopic, questions in subs.items():
                if subtopic:
                    lines.append(f"### {subtopic}")
                    lines.append("")
                for question, sources in questions:
                    lines.append(f"- {normalize_text(question)}")
                    for source in sources:
                        lines.append(f"  - 来源:`{source}`")
                    lines.append("")
        (bank / name).write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_export = sub.add_parser("export")
    p_export.add_argument("--bank", default="docs/interview-bank")
    p_export.add_argument("--out", required=True)
    p_generate = sub.add_parser("generate")
    p_generate.add_argument("--in", dest="src", required=True)
    p_generate.add_argument("--bank", default="docs/interview-bank")
    args = parser.parse_args()

    if args.cmd == "export":
        rows = export(Path(args.bank))
        Path(args.out).write_text(
            "\n".join("\t".join(r) for r in rows) + "\n", encoding="utf-8"
        )
        print(f"导出 {len(rows)} 条 -> {args.out}")
    else:
        rows = load(Path(args.src))
        generate(rows, Path(args.bank))
        print(f"写入 {len(rows)} 条 -> {args.bank}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
