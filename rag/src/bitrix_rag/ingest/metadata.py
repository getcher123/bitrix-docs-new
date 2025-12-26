from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


COURSE_RE = re.compile(r"course_(\\d+)")
LESSON_RE = re.compile(r"lesson_(\\d+)\\.md$")


@dataclass(frozen=True)
class DocMetadata:
    path: str
    section: str
    module: str
    title: str
    heading_path: str
    course_id: str | None = None
    lesson_id: str | None = None


def classify_section(rel_path: Path) -> str:
    top = rel_path.parts[0] if rel_path.parts else ""
    if top == "d7":
        return "D7"
    if top == "bitrix24_api":
        return "REST"
    if top == "courses":
        return "courses"
    if top == "user_help":
        return "user_help"
    return "classic"


def infer_module(rel_path: Path) -> str:
    if not rel_path.parts:
        return ""
    top = rel_path.parts[0]
    if top == "d7" and len(rel_path.parts) > 2 and rel_path.parts[1] == "bitrix":
        return rel_path.parts[2]
    return top


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def parse_course_ids(rel_path: Path) -> tuple[str | None, str | None]:
    course_id = None
    lesson_id = None
    for part in rel_path.parts:
        match = COURSE_RE.search(part)
        if match:
            course_id = match.group(1)
            break
    match = LESSON_RE.search(rel_path.name)
    if match:
        lesson_id = match.group(1)
    return course_id, lesson_id
