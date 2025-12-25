#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cleans up Bitrix course lessons for Markdown-vault use (VS Code / Obsidian).

Typical parser artifacts in `docs/courses/**/lesson_*.md`:
- UI metadata block right after H1 (views/date/author/difficulty/editions).
- Trailing page number + "scroll to top" image.
- Standalone "Подробнее..." lines from tooltip widgets.

This script removes only those artifacts and keeps lesson content intact.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


UP_IMAGE_RE = re.compile(r"!\[Прокрутить вверх\]\((?:\.\./)+images/courses/up\.png\)")
FOOTER_RE_WITH_NUMBER = re.compile(
    r"\n\s*\d+\s*\n\s*!\[Прокрутить вверх\]\((?:\.\./)+images/courses/up\.png\)\s*\n*\Z",
    re.S,
)
FOOTER_RE_NO_NUMBER = re.compile(
    r"\n\s*!\[Прокрутить вверх\]\((?:\.\./)+images/courses/up\.png\)\s*\n*\Z",
    re.S,
)

LEVEL_RE = re.compile(r"^\*\*\s*\d+\s+уровень\s*\*\*\s*$")
RATING_RE = re.compile(r"^\*\*\s*[1-5]\s*\*\*\s*$")
MORE_RE = re.compile(r"^Подробнее\.{3,}\s*$")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@dataclass
class CleanStats:
    processed: int = 0
    changed: int = 0
    header_cleaned: int = 0
    footer_cleaned: int = 0
    removed_more_lines: int = 0


def _clean_footer(text: str) -> tuple[str, bool]:
    original = text
    text = FOOTER_RE_WITH_NUMBER.sub("\n", text)
    text = FOOTER_RE_NO_NUMBER.sub("\n", text)
    # In case a page number was removed, but the image remains (or vice-versa).
    if UP_IMAGE_RE.search(text):
        # Only strip if the up-image is at the very end.
        text = re.sub(rf"\n\s*{UP_IMAGE_RE.pattern}\s*\n*\Z", "\n", text)
    return text, (text != original)


def _clean_header(lines: list[str]) -> tuple[list[str], bool]:
    """
    Removes the UI metadata block placed right after the H1.
    Only triggers when typical markers are present near the top of the file.
    """
    if not lines:
        return lines, False

    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or not lines[i].startswith("# "):
        return lines, False

    # Only run when we actually see the metadata markers.
    lookahead = "\n".join(lines[i + 1 : i + 1 + 90])
    if (
        "Просмотров:" not in lookahead
        and "Дата последнего изменения:" not in lookahead
        and "Информация о сложности" not in lookahead
        and "Информация о редакциях" not in lookahead
    ):
        return lines, False

    out: list[str] = [lines[i].rstrip()]

    j = i + 1
    in_difficulty = False
    in_license = False
    license_removed = 0

    while j < len(lines):
        s = lines[j].strip()

        if not s:
            # After removing license values, a blank line usually separates the
            # metadata block from the real lesson content.
            if in_license and license_removed > 0:
                in_license = False
            j += 1
            continue

        if s.startswith("Просмотров:"):
            j += 1
            continue

        if s.startswith("Дата последнего изменения:"):
            j += 1
            continue

        if s == "Информация об авторе":
            j += 1
            continue

        if s == "Информация о сложности":
            in_difficulty = True
            j += 1
            continue

        if s == "**Сложность урока:**":
            in_difficulty = True
            j += 1
            continue

        if LEVEL_RE.match(s):
            j += 1
            continue

        if in_difficulty and s.startswith("-"):
            j += 1
            continue

        if RATING_RE.match(s):
            j += 1
            continue

        if s == "Информация о редакциях":
            in_difficulty = False
            j += 1
            continue

        if s == "**Недоступно в лицензиях:**":
            in_license = True
            license_removed = 0
            j += 1
            continue

        if in_license:
            # Usually a single line like "Ограничений нет" or "Старт, Стандарт, ...".
            license_removed += 1
            j += 1
            if license_removed >= 10:
                in_license = False
            continue

        # Reached the real lesson content.
        break

    out.append("")
    out.extend(lines[j:])
    return out, True


def _remove_standalone_more(lines: list[str]) -> tuple[list[str], int]:
    removed = 0
    out: list[str] = []
    for line in lines:
        if MORE_RE.match(line.strip()):
            removed += 1
            continue
        out.append(line)
    return out, removed


def _normalize_tail(lines: list[str]) -> list[str]:
    # Trim trailing whitespace, collapse excessive blank lines at EOF, keep 1 newline in file.
    lines = [l.rstrip() for l in lines]
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def clean_lesson(path: Path) -> tuple[bool, dict[str, int]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    original = text

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text, footer_changed = _clean_footer(text)

    lines = text.split("\n")
    lines, header_changed = _clean_header(lines)
    lines, removed_more = _remove_standalone_more(lines)
    lines = _normalize_tail(lines)

    text = "\n".join(lines).rstrip() + "\n"

    if text == original:
        return False, {"header": 0, "footer": 0, "more": 0}

    path.write_text(text, encoding="utf-8")
    return True, {"header": int(header_changed), "footer": int(footer_changed), "more": removed_more}


def iter_lessons(docs_dir: Path) -> list[Path]:
    return sorted((docs_dir / "courses").rglob("lesson_*.md"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-files", type=int, default=0, help="Limit processed files (0 = no limit).")
    args = parser.parse_args()

    root = repo_root()
    docs_dir = root / "docs"

    stats = CleanStats()
    lessons = iter_lessons(docs_dir)
    if args.max_files and args.max_files > 0:
        lessons = lessons[: args.max_files]

    for path in lessons:
        stats.processed += 1
        changed, detail = clean_lesson(path)
        if changed:
            stats.changed += 1
            stats.header_cleaned += detail["header"]
            stats.footer_cleaned += detail["footer"]
            stats.removed_more_lines += detail["more"]

    print(
        "[cleanup-courses] "
        f"processed={stats.processed} changed={stats.changed} "
        f"header_cleaned={stats.header_cleaned} footer_cleaned={stats.footer_cleaned} "
        f"removed_more_lines={stats.removed_more_lines}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
