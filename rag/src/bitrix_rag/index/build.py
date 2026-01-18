from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess

from ..clients.bge import BgeClient
from ..config import AppConfig
from ..ingest.pipeline import ChunkRecord, iter_chunks
from .incremental import build_incremental_records, build_manifest, save_manifest
from .bm25 import Bm25Index
from .qdrant_store import QdrantStore
from .vector_index import build_vector_index


CHUNKS_FILE = "chunks.jsonl"
BM25_FILE = "bm25.json"
EMBED_CACHE_FILE = "embedding_cache.jsonl"
MANIFEST_FILE = "index_manifest.json"
VERSION_FILE = "index_version.json"


def build_indexes(cfg: AppConfig, incremental: bool = False, strategy: str = "auto") -> None:
    cfg.rag_data_dir.mkdir(parents=True, exist_ok=True)

    if incremental:
        records, manifest, changed = build_incremental_records(
            vault_root=cfg.vault_root,
            chunks_path=cfg.rag_data_dir / CHUNKS_FILE,
            manifest_path=cfg.rag_data_dir / MANIFEST_FILE,
            chunk_size=cfg.indexing.chunk_size,
            chunk_overlap=cfg.indexing.chunk_overlap,
            min_chunk=cfg.indexing.min_chunk,
            strategy=strategy,
            repo_root=cfg.vault_root.parent,
        )
        if not changed:
            print("No changes detected; indexes are up to date.")
            return
        save_manifest(cfg.rag_data_dir / MANIFEST_FILE, manifest)
    else:
        records = iter_chunks(
            cfg.vault_root,
            chunk_size=cfg.indexing.chunk_size,
            chunk_overlap=cfg.indexing.chunk_overlap,
            min_chunk=cfg.indexing.min_chunk,
        )
        save_manifest(cfg.rag_data_dir / MANIFEST_FILE, build_manifest(cfg.vault_root))

    _write_chunks(cfg.rag_data_dir / CHUNKS_FILE, records)

    bm25 = Bm25Index.build(records)
    bm25.save(cfg.rag_data_dir / BM25_FILE)

    try:
        store = QdrantStore.connect(
            url=cfg.qdrant.url,
            collection=cfg.qdrant.collection,
            vector_size=1024,
        )
        if incremental:
            store.recreate(vector_size=1024)
        bge = BgeClient(cfg.bge)
        build_vector_index(
            records,
            store=store,
            bge=bge,
            cache_path=cfg.rag_data_dir / EMBED_CACHE_FILE,
            batch_size=cfg.indexing.embed_batch_size,
            max_text_chars=cfg.indexing.max_rerank_chars,
        )
    except Exception as exc:
        print(f"Vector index skipped (qdrant unavailable): {exc}")

    _write_version(cfg.rag_data_dir / VERSION_FILE, cfg.vault_root.parent, incremental)


def _write_chunks(path: Path, records: list[ChunkRecord]) -> None:
    lines = []
    for record in records:
        lines.append(
            json.dumps(
                {
                    "id": record.chunk.chunk_id,
                    "text": record.chunk.text,
                    "path": record.metadata.path,
                    "section": record.metadata.section,
                    "module": record.metadata.module,
                    "title": record.metadata.title,
                    "heading_path": record.metadata.heading_path,
                    "course_id": record.metadata.course_id,
                    "lesson_id": record.metadata.lesson_id,
                    "hash": record.content_hash,
                },
                ensure_ascii=False,
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_version(path: Path, repo_root: Path, incremental: bool) -> None:
    commit = ""
    try:
        commit = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = ""
    payload = {
        "git_commit": commit,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "incremental": incremental,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
