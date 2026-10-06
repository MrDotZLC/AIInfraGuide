#!/usr/bin/env python3
"""校验 docs/interview-bank 题库结构是否符合 skill 的输出约定。

检查项:
  error - 七个分类文件缺失、题目没有来源、来源文件不存在
  warn  - 分类目录外的 .md、来源未写成文件路径、跨文件完全重复的题目、
          docs/interview 下出现改动(需要 git)、来源块里的条目缺少文件路径

题目按顶层列表项("- " 开头、无缩进)识别;`##` / `###` 标题视为主题分组。

来源支持两种写法:
  1) 题目下方缩进的条目:  `  - 来源:`docs/interview/x.md``
  2) 单独一行 `来源:` 标记 + 缩进的来源列表(列表与下一条问题之间空一行)
顶层列表项如果不是这两种写法,会被当成下一条问题。

用法:
  python check_interview_bank.py --bank docs/interview-bank --sources docs/interview
  python check_interview_bank.py --reconcile        # 额外做漏提对账
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
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
APPENDIX_FILES = ("00-tech-stack.md",)
QUESTION_RE = re.compile(r"^[-*]\s+(.*\S)\s*$")
HEADING_RE = re.compile(r"^#{1,6}\s")
BLANK_RE = re.compile(r"^\s*$")
SOURCE_PATH_RE = re.compile(r"`([^`]*\.md)(?::\d+(?:-\d+)?)?`")
SOURCE_MARKER_RE = re.compile(r"^\s*(?:[-*]\s*)?(?:来源|出处)\s*[:：]\s*$")
SOURCE_INLINE_RE = re.compile(r"^\s*(?:[-*]\s*)?(?:来源|出处)\s*[:：]\s*\S")
QUESTION_HINT_RE = re.compile(r"[?？]")
SOURCE_ITEM_RE = re.compile(r"(?m)^\s*\d+[\.、]\s*(.+)$")


def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "scripts" / "convert-interview.mjs").is_file():
            return candidate
    return start


def parse_questions(path: Path) -> tuple[list[tuple[int, str, list[str]]], list[str]]:
    """返回 (questions, notes)。

    questions: [(行号, 题目文本, 题目块的行)]
    notes:     解析过程中发现的可疑写法(如来源条目缺少文件路径)
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    questions: list[tuple[int, str, list[str]]] = []
    notes: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        match = QUESTION_RE.match(line)
        if not match or HEADING_RE.match(line):
            index += 1
            continue
        block: list[str] = []
        cursor = index + 1
        in_source_list = False
        while cursor < len(lines):
            current = lines[cursor]
            if HEADING_RE.match(current):
                break
            if SOURCE_MARKER_RE.match(current):
                in_source_list = True
                block.append(current)
                cursor += 1
                continue
            if SOURCE_INLINE_RE.match(current):
                block.append(current)
                cursor += 1
                continue
            if QUESTION_RE.match(current):
                if not in_source_list:
                    break
                # 来源块内:空行 + 带问号的条目视为下一条问题,其余并入本块
                previous = block[-1] if block else ""
                if BLANK_RE.match(previous) and QUESTION_HINT_RE.search(current):
                    break
                if not SOURCE_PATH_RE.search(current):
                    notes.append(
                        f"{path.name}:{cursor + 1} 来源块中的条目没有文件路径;"
                        "若这是下一条问题,请把来源列表缩进、并与问题之间空一行"
                    )
                block.append(current)
                cursor += 1
                continue
            block.append(current)
            cursor += 1
        questions.append((index + 1, match.group(1), block))
        index = cursor
    return questions, notes


def normalize_question(text: str) -> str:
    return re.sub(r"[\s?？。.,、,;；:：!！]+", "", text)


def check_sources_modified(repo_root: Path, sources_dir: Path):
    try:
        relative = sources_dir.relative_to(repo_root).as_posix()
        result = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain", "--", relative],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError, ValueError):
        return None
    if result.returncode != 0:
        return None
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def count_source_questions(path: Path) -> tuple[int, int]:
    """粗算源文件里的编号条目数与问句数(按问号计)。"""
    text = path.read_text(encoding="utf-8")
    body = re.sub(r"^---\r?\n.*?\r?\n---\r?\n", "", text, count=1, flags=re.S)
    items = [match.group(1) for match in SOURCE_ITEM_RE.finditer(body)]
    marks = sum(item.count("?") + item.count("？") for item in items)
    return len(items), marks


def main() -> int:
    parser = argparse.ArgumentParser(description="校验面试题库输出结构")
    parser.add_argument("--bank", default="docs/interview-bank", help="题库目录")
    parser.add_argument("--sources", default="docs/interview", help="原始面经目录")
    parser.add_argument("--repo", help="仓库根目录(默认从脚本位置向上查找)")
    parser.add_argument(
        "--reconcile",
        action="store_true",
        help="按来源文件对账:原文问句数(按问号计)与入库条目数,粗筛漏提",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo).resolve() if args.repo else find_repo_root(Path(__file__).resolve().parent)
    bank = Path(args.bank)
    if not bank.is_absolute():
        bank = repo_root / bank
    sources_dir = Path(args.sources)
    if not sources_dir.is_absolute():
        sources_dir = repo_root / sources_dir

    if not bank.is_dir():
        print(f"ERROR  题库目录不存在:{bank}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    for name in CATEGORY_FILES:
        if not (bank / name).is_file():
            errors.append(f"缺少分类文件 {name}")

    for path in sorted(bank.glob("*.md")):
        if path.name not in CATEGORY_FILES and path.name not in APPENDIX_FILES:
            warnings.append(f"分类目录外的文件:{path.name}")

    seen: dict[str, list[str]] = {}
    total_questions = 0
    counts: Counter[str] = Counter()
    entries_per_source: Counter[str] = Counter()

    for name in CATEGORY_FILES:
        path = bank / name
        if not path.is_file():
            continue
        questions, notes = parse_questions(path)
        counts[name] = len(questions)
        total_questions += len(questions)
        warnings.extend(notes)
        for line_number, text, block in questions:
            location = f"{name}:{line_number}"
            block_text = "\n".join(block)
            if "来源" not in block_text:
                errors.append(f"{location} 缺少来源:{text}")
            source_paths = SOURCE_PATH_RE.findall(block_text)
            if "来源" in block_text and not source_paths:
                warnings.append(f"{location} 来源未写成文件路径:{text}")
            for source in source_paths:
                candidate = Path(source)
                resolved = candidate if candidate.is_absolute() else repo_root / candidate
                if not resolved.is_file():
                    errors.append(f"{location} 来源文件不存在:{source}")
                else:
                    entries_per_source[resolved.resolve().as_posix()] += 1
            seen.setdefault(normalize_question(text), []).append(location)

    for _, locations in seen.items():
        if len(locations) > 1:
            warnings.append("完全相同的题目出现在多处:" + "、".join(locations))

    modified = check_sources_modified(repo_root, sources_dir)
    if modified is None:
        warnings.append("跳过 git 检查:无法读取仓库状态")
    elif modified:
        warnings.append(
            "docs/interview 下存在改动(原始面经应保持只读):" + ";".join(modified[:5])
        )

    for line in errors:
        print(f"ERROR  {line}")
    for line in warnings:
        print(f"WARN   {line}")

    print("\n分类统计:")
    for name in CATEGORY_FILES:
        print(f"  {name:<32} {counts[name]}")
    print(f"\n题目总数:{total_questions};{len(errors)} 个 error,{len(warnings)} 个 warning")

    if args.reconcile:
        print("\n来源对账(原文问句数按问号计 / 该来源下挂的入库条目数):")
        rows = []
        for resolved_posix, entry_count in entries_per_source.items():
            source_path = Path(resolved_posix)
            if not source_path.is_file():
                continue
            item_count, mark_count = count_source_questions(source_path)
            try:
                label = source_path.relative_to(repo_root).as_posix()
            except ValueError:
                label = str(source_path)
            rows.append((mark_count - entry_count, label, item_count, mark_count, entry_count))
        rows.sort(reverse=True)
        for diff, label, item_count, mark_count, entry_count in rows:
            if diff > 0:
                flag = "  <= 问句多于入库,可能漏提"
            elif diff < 0:
                flag = "  <= 条目多于问句(拆分或原文无问号),抽查即可"
            else:
                flag = ""
            print(
                f"  {label:<52} 原编号条目 {item_count:>3} / 原文问句 {mark_count:>3} / 入库 {entry_count:>3}{flag}"
            )
        print("  该对账是粗筛:只按问号计数,能发现整条漏提,拆并引起的差异需要人工抽查。")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
