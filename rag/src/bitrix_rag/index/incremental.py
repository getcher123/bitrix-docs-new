from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
from typing import Iterable

from ..ingest.chunker import Chunk
from ..ingest.loader import iter_markdown_files
from ..ingest.metadata import DocMetadata
from ..ingest.pipeline import ChunkRecord, chunk_file


@dataclass(frozen=True)
class ManifestEntry:
    mtime: float
    size: int


def load_manifest(path: Path) -> dict[str, ManifestEntry]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    entries: dict[str, ManifestEntry] = {}
    for rel, meta in data.get("files", {}).items():
        entries[rel] = ManifestEntry(mtime=float(meta["mtime"]), size=int(meta["size"]))
    return entries


def save_manifest(path: Path, entries: dict[str, ManifestEntry]) -> None:
    payload = {
        "files": {rel: {"mtime": entry.mtime, "size": entry.size} for rel, entry in entries.items()}
    }
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def build_incremental_records(
    vault_root: Path,
    chunks_path: Path,
    manifest_path: Path,
    chunk_size: int,
    chunk_overlap: int,
    min_chunk: int,
    strategy: str = "auto",
    repo_root: Path | None = None,
) -> tuple[list[ChunkRecord], dict[str, ManifestEntry], bool]:
    if not chunks_path.exists():
        records = _build_full_records(vault_root, chunk_size, chunk_overlap, min_chunk)
        manifest = build_manifest(vault_root)
        return records, manifest, True

    existing = _load_existing_records(chunks_path)
    manifest = load_manifest(manifest_path)

    if strategy == "auto":
        if repo_root and (repo_root / ".git").exists():
            strategy = "git"
        else:
            strategy = "mtime"

    if strategy == "git":
        changed_rel = _git_changed_paths(repo_root or vault_root, vault_root)
        current_files = list(iter_markdown_files(vault_root))
        current_rel = {path.relative_to(vault_root).as_posix() for path in current_files}
        removed_rel = {rel for rel in changed_rel if rel not in current_rel}
        changed_rel = {rel for rel in changed_rel if rel in current_rel}
    else:
        current_files = list(iter_markdown_files(vault_root))
        current_rel = {path.relative_to(vault_root).as_posix() for path in current_files}
        changed_rel = _mtime_changed_paths(vault_root, manifest)
        removed_rel = set(manifest.keys()) - current_rel

    if not changed_rel and not removed_rel:
        return _flatten_records(existing), manifest, False

    records_by_path = {rel: list(items) for rel, items in existing.items()}
    for rel in removed_rel:
        records_by_path.pop(rel, None)

    for path in current_files:
        rel = path.relative_to(vault_root).as_posix()
        if rel not in changed_rel:
            continue
        records_by_path[rel] = chunk_file(
            path=path,
            vault_root=vault_root,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            min_chunk=min_chunk,
        )

    new_manifest = build_manifest(vault_root)
    return _flatten_records(records_by_path), new_manifest, True


def _build_full_records(
    vault_root: Path,
    chunk_size: int,
    chunk_overlap: int,
    min_chunk: int,
) -> list[ChunkRecord]:
    records: list[ChunkRecord] = []
    for path in iter_markdown_files(vault_root):
        records.extend(
            chunk_file(
                path=path,
                vault_root=vault_root,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                min_chunk=min_chunk,
            )
        )
    return records


def build_manifest(vault_root: Path) -> dict[str, ManifestEntry]:
    entries: dict[str, ManifestEntry] = {}
    for path in iter_markdown_files(vault_root):
        stat = path.stat()
        rel = path.relative_to(vault_root).as_posix()
        entries[rel] = ManifestEntry(mtime=stat.st_mtime, size=stat.st_size)
    return entries


def _mtime_changed_paths(
    vault_root: Path, manifest: dict[str, ManifestEntry]
) -> set[str]:
    changed: set[str] = set()
    for path in iter_markdown_files(vault_root):
        rel = path.relative_to(vault_root).as_posix()
        stat = path.stat()
        entry = manifest.get(rel)
        if entry is None or entry.mtime != stat.st_mtime or entry.size != stat.st_size:
            changed.add(rel)
    return changed


def _load_existing_records(chunks_path: Path) -> dict[str, list[ChunkRecord]]:
    records: dict[str, list[ChunkRecord]] = {}
    for line in chunks_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rel_path = row["path"]
        chunk = Chunk(
            doc_path=rel_path,
            chunk_id=row["id"],
            text=row["text"],
            title=row.get("title") or "",
            heading_path=row.get("heading_path") or "",
        )
        metadata = DocMetadata(
            path=rel_path,
            section=row.get("section") or "",
            module=row.get("module") or "",
            title=row.get("title") or "",
            heading_path=row.get("heading_path") or "",
            course_id=row.get("course_id"),
            lesson_id=row.get("lesson_id"),
        )
        record = ChunkRecord(chunk=chunk, metadata=metadata, content_hash=row.get("hash") or "")
        records.setdefault(rel_path, []).append(record)
    return records


def _flatten_records(records_by_path: dict[str, list[ChunkRecord]]) -> list[ChunkRecord]:
    records: list[ChunkRecord] = []
    for rel in sorted(records_by_path.keys()):
        records.extend(records_by_path[rel])
    return records


def _git_changed_paths(repo_root: Path, vault_root: Path) -> set[str]:
    git_dir = repo_root / ".git"
    if not git_dir.exists():
        return set()

    changed: set[str] = set()
    commands = [
        ["git", "-C", str(repo_root), "diff", "--name-only"],
        ["git", "-C", str(repo_root), "ls-files", "--others", "--exclude-standard"],
    ]
    for cmd in commands:
        try:
            output = subprocess.check_output(cmd, text=True)
        except Exception:
            continue
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
            changed.add(line)

    try:
        prefix = vault_root.relative_to(repo_root).as_posix()
    except ValueError:
        prefix = ""

    if not prefix:
        return changed

    prefix = prefix.rstrip("/") + "/"
    filtered: set[str] = set()
    for path in changed:
        if path.startswith(prefix):
            filtered.add(path[len(prefix) :])
    return filtered
