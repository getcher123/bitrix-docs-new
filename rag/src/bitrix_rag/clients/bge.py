from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import httpx

from ..config import BgeEndpointsConfig


@dataclass(frozen=True)
class BgeHealth:
    status: str
    embed_model: str | None = None
    rerank_model: str | None = None
    device: str | None = None


class BgeClient:
    def __init__(self, cfg: BgeEndpointsConfig) -> None:
        if not cfg.base_url:
            raise ValueError("BGE base_url is empty (set BGE_BASE_URL)")
        self._cfg = cfg

    def _headers(self) -> dict[str, str]:
        headers: dict[str, str] = {}
        if self._cfg.api_key:
            headers["X-API-Key"] = self._cfg.api_key
        return headers

    def health(self, timeout_s: int | None = None) -> BgeHealth:
        url = f"{self._cfg.base_url}{self._cfg.health_path}"
        with httpx.Client(timeout=timeout_s or self._cfg.timeout_s) as client:
            r = client.get(url, headers=self._headers())
            r.raise_for_status()
            data = r.json()
        return BgeHealth(
            status=data.get("status", ""),
            embed_model=data.get("embed_model"),
            rerank_model=data.get("rerank_model"),
            device=data.get("device"),
        )

    def embed(self, texts: list[str], timeout_s: int | None = None) -> list[list[float]]:
        url = f"{self._cfg.base_url}{self._cfg.embed_path}"
        payload = {"texts": texts}
        with httpx.Client(timeout=timeout_s or self._cfg.timeout_s) as client:
            r = client.post(url, headers=self._headers(), json=payload)
            r.raise_for_status()
            data = r.json()
        embeddings = data.get("embeddings")
        if not isinstance(embeddings, list):
            raise ValueError("Invalid /embed response: missing 'embeddings'")
        return embeddings

    def rerank(self, query: str, documents: list[str], timeout_s: int | None = None) -> list[float]:
        url = f"{self._cfg.base_url}{self._cfg.rerank_path}"
        payload = {"query": query, "documents": documents}
        with httpx.Client(timeout=timeout_s or self._cfg.timeout_s) as client:
            r = client.post(url, headers=self._headers(), json=payload)
            r.raise_for_status()
            data = r.json()
        scores = data.get("scores")
        if not isinstance(scores, list):
            raise ValueError("Invalid /rerank response: missing 'scores'")
        return scores


def chunked(items: Iterable[str], size: int) -> Iterable[list[str]]:
    buf: list[str] = []
    for item in items:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf
