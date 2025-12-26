from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path


def _env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if value is None:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


def _env_int(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value is None:
        return default
    return int(value)


def _resolve_path(value: str, base: Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = (base / path).resolve()
    return path


@dataclass(frozen=True)
class BgeEndpointsConfig:
    base_url: str
    embed_path: str = "/embed"
    rerank_path: str = "/rerank"
    health_path: str = "/health"
    api_key: str = ""
    timeout_s: int = 30
    retries: int = 3


@dataclass(frozen=True)
class QdrantConfig:
    url: str
    collection: str


@dataclass(frozen=True)
class OpenAIConfig:
    api_key: str
    model: str = "gpt-5"


@dataclass(frozen=True)
class IndexingConfig:
    chunk_size: int = 900
    chunk_overlap: int = 150
    min_chunk: int = 200
    max_rerank_chars: int = 2000


@dataclass(frozen=True)
class RetrievalConfig:
    bm25_k: int = 40
    vector_k: int = 40
    rrf_k: int = 60
    rerank_k: int = 10


@dataclass(frozen=True)
class AppConfig:
    vault_root: Path
    rag_data_dir: Path
    qdrant: QdrantConfig
    bge: BgeEndpointsConfig
    openai: OpenAIConfig
    indexing: IndexingConfig
    retrieval: RetrievalConfig


def load_config(repo_root: Path) -> AppConfig:
    vault_root = _resolve_path(_env("VAULT_ROOT", "docs"), repo_root)
    rag_data_dir = _resolve_path(_env("RAG_DATA_DIR", ".rag"), repo_root)

    qdrant = QdrantConfig(
        url=_env("QDRANT_URL", "http://localhost:6333"),
        collection=_env("QDRANT_COLLECTION", "bitrix_docs"),
    )

    bge = BgeEndpointsConfig(
        base_url=_env("BGE_BASE_URL", "").rstrip("/"),
        embed_path=_env("BGE_EMBED_PATH", "/embed"),
        rerank_path=_env("BGE_RERANK_PATH", "/rerank"),
        health_path=_env("BGE_HEALTH_PATH", "/health"),
        api_key=_env("BGE_API_KEY", ""),
        timeout_s=_env_int("BGE_TIMEOUT_S", 30),
        retries=_env_int("BGE_RETRIES", 3),
    )

    openai = OpenAIConfig(
        api_key=_env("OPENAI_API_KEY", ""),
        model=_env("OPENAI_MODEL", "gpt-5"),
    )

    indexing = IndexingConfig(
        chunk_size=_env_int("RAG_CHUNK_SIZE", 900),
        chunk_overlap=_env_int("RAG_CHUNK_OVERLAP", 150),
        min_chunk=_env_int("RAG_MIN_CHUNK", 200),
        max_rerank_chars=_env_int("RAG_MAX_RERANK_CHARS", 2000),
    )

    retrieval = RetrievalConfig(
        bm25_k=_env_int("RAG_BM25_K", 40),
        vector_k=_env_int("RAG_VECTOR_K", 40),
        rrf_k=_env_int("RAG_RRF_K", 60),
        rerank_k=_env_int("RAG_RERANK_K", 10),
    )

    return AppConfig(
        vault_root=vault_root,
        rag_data_dir=rag_data_dir,
        qdrant=qdrant,
        bge=bge,
        openai=openai,
        indexing=indexing,
        retrieval=retrieval,
    )
