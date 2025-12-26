from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib

from .chunker import Chunk, chunk_markdown
from .loader import MarkdownDocument, iter_markdown_files, load_markdown
from .metadata import DocMetadata, classify_section, extract_title, infer_module, parse_course_ids


@dataclass(frozen=True)
class ChunkRecord:
    chunk: Chunk
    metadata: DocMetadata
    content_hash: str


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def iter_chunks(
    vault_root: Path,
    chunk_size: int,
    chunk_overlap: int,
    min_chunk: int,
) -> list[ChunkRecord]:
    records: list[ChunkRecord] = []
    for path in iter_markdown_files(vault_root):
        doc = load_markdown(path)
        rel_path = path.relative_to(vault_root)
        title = extract_title(doc.text)
        section = classify_section(rel_path)
        module = infer_module(rel_path)
        course_id, lesson_id = parse_course_ids(rel_path)
        chunks = chunk_markdown(doc, chunk_size, chunk_overlap, min_chunk)
        for chunk in chunks:
            content_hash = _hash_text(chunk.text)
            metadata = DocMetadata(
                path=str(rel_path.as_posix()),
                section=section,
                module=module,
                title=title or chunk.title,
                heading_path=chunk.heading_path,
                course_id=course_id,
                lesson_id=lesson_id,
            )
            records.append(ChunkRecord(chunk=chunk, metadata=metadata, content_hash=content_hash))
    return records
