from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

from .loader import MarkdownDocument


HEADING_RE = re.compile(r"^(#{1,3})\\s+(.+?)\\s*$")
FENCE_RE = re.compile(r"^```")
WORD_RE = re.compile(r"[A-Za-zА-Яа-я0-9_]+")
WORD_OR_PUNCT_RE = re.compile(r"[A-Za-zА-Яа-я0-9_]+|[^A-Za-zА-Яа-я0-9_\\s]+")


@dataclass(frozen=True)
class Chunk:
    doc_path: str
    chunk_id: str
    text: str
    title: str
    heading_path: str


def _estimate_tokens(text: str) -> int:
    return len(WORD_RE.findall(text))


def _normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \\t]+\\n", "\n", text)
    text = re.sub(r"\\n{3,}", "\n\n", text)
    return text.strip()


def _split_sections(doc: MarkdownDocument) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    heading_stack: list[str] = []
    buf: list[str] = []
    in_fence = False

    def flush() -> None:
        if not buf:
            return
        heading_path = " / ".join(heading_stack) if heading_stack else ""
        sections.append((heading_path, _normalize_text("".join(buf))))
        buf.clear()

    for line in doc.text.splitlines(keepends=True):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
        if not in_fence:
            m = HEADING_RE.match(line)
            if m:
                flush()
                level = len(m.group(1))
                title = m.group(2).strip()
                if level == 1:
                    heading_stack = [title]
                elif level == 2:
                    heading_stack = heading_stack[:1] + [title]
                else:
                    heading_stack = heading_stack[:2] + [title]
                buf.append(line)
                continue
        buf.append(line)

    flush()
    return sections


def _split_paragraphs(text: str) -> list[str]:
    parts = [p.strip() for p in re.split(r"\\n\\s*\\n", text) if p.strip()]
    return parts or [text]


def _apply_overlap(prev: str, overlap_tokens: int) -> str:
    if overlap_tokens <= 0:
        return ""
    words = WORD_OR_PUNCT_RE.findall(prev)
    if not words:
        return ""
    tail = words[-overlap_tokens:]
    return "".join(
        [
            (" " if i and re.match(r"\\w", token) and re.match(r"\\w", tail[i - 1]) else "")
            + token
            for i, token in enumerate(tail)
        ]
    ).strip()


def chunk_markdown(
    doc: MarkdownDocument,
    max_tokens: int,
    overlap_tokens: int,
    min_tokens: int,
) -> list[Chunk]:
    sections = _split_sections(doc)
    chunks: list[Chunk] = []
    chunk_index = 0

    for heading_path, section_text in sections:
        if not section_text:
            continue
        paragraphs = _split_paragraphs(section_text)
        current: list[str] = []
        current_tokens = 0
        for para in paragraphs:
            para_tokens = _estimate_tokens(para)
            if current_tokens + para_tokens > max_tokens and current:
                text = _normalize_text("\n\n".join(current))
                if _estimate_tokens(text) >= min_tokens:
                    chunk_id = f"{doc.path.as_posix()}::{chunk_index}"
                    chunks.append(
                        Chunk(
                            doc_path=doc.path.as_posix(),
                            chunk_id=chunk_id,
                            text=text,
                            title=heading_path.split(" / ")[0] if heading_path else "",
                            heading_path=heading_path,
                        )
                    )
                    chunk_index += 1
                overlap = _apply_overlap(text, overlap_tokens)
                current = [overlap] if overlap else []
                current_tokens = _estimate_tokens(overlap)
            current.append(para)
            current_tokens += para_tokens

        if current:
            text = _normalize_text("\n\n".join(current))
            if _estimate_tokens(text) >= min_tokens:
                chunk_id = f"{doc.path.as_posix()}::{chunk_index}"
                chunks.append(
                    Chunk(
                        doc_path=doc.path.as_posix(),
                        chunk_id=chunk_id,
                        text=text,
                        title=heading_path.split(" / ")[0] if heading_path else "",
                        heading_path=heading_path,
                    )
                )
                chunk_index += 1

    return chunks
