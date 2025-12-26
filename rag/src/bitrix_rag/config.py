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
class AppConfig:
    vault_root: Path
    qdrant: QdrantConfig
    bge: BgeEndpointsConfig
    openai: OpenAIConfig


def load_config(repo_root: Path) -> AppConfig:
    vault_root = Path(_env("VAULT_ROOT", str((repo_root / ".." / "docs").resolve()))).resolve()

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

    return AppConfig(vault_root=vault_root, qdrant=qdrant, bge=bge, openai=openai)

