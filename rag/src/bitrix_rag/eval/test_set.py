from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


LINK_RE = re.compile(r"\(([^)]+)\)")


@dataclass(frozen=True)
class TestCase:
    id: str
    question: str
    expected: list[str]


def parse_test_set(path: Path) -> list[TestCase]:
    rows: list[TestCase] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| Q"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        qid = parts[0]
        question = parts[1]
        expected_raw = parts[3]
        expected = []
        for link in LINK_RE.findall(expected_raw):
            if link.startswith("http"):
                continue
            expected.append(_normalize_link(link))
        rows.append(TestCase(id=qid, question=question, expected=[e for e in expected if e]))
    return rows


def _normalize_link(link: str) -> str:
    link = link.strip().replace("\\", "/")
    while link.startswith("../"):
        link = link[3:]
    if link.startswith("./"):
        link = link[2:]
    if link.startswith("docs/"):
        link = link[5:]
    return link
