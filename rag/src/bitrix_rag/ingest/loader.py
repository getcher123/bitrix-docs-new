from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterator


VAULT_NAV_RE = re.compile(
    r"<!--\s*vault-nav:start\s*-->.*?<!--\s*vault-nav:end\s*-->",
    flags=re.DOTALL | re.IGNORECASE,
)


@dataclass(frozen=True)
class MarkdownDocument:
    path: Path
    text: str


def iter_markdown_files(vault_root: Path) -> Iterator[Path]:
    for path in vault_root.rglob("*.md"):
        if path.name.startswith("RAG_"):
            continue
        yield path


def load_markdown(path: Path) -> MarkdownDocument:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = VAULT_NAV_RE.sub("", text)
    return MarkdownDocument(path=path, text=text)

