from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable

from qdrant_client.http import models as qmodels

from ..clients.bge import BgeClient
from ..clients.openai_client import OpenAIClient
from ..config import AppConfig
from ..index.bm25 import Bm25Index
from ..index.build import BM25_FILE, CHUNKS_FILE
from ..index.qdrant_store import QdrantStore
from .hybrid import rrf_fuse
from .router import route_sections


@dataclass(frozen=True)
class Chunk:
    doc_id: str
    text: str
    path: str
    title: str
    heading_path: str
    section: str
    module: str


class ChunkStore:
    def __init__(self, chunks_path: Path) -> None:
        self._chunks: dict[str, Chunk] = {}
        for line in chunks_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            self._chunks[row["id"]] = Chunk(
                doc_id=row["id"],
                text=row["text"],
                path=row["path"],
                title=row.get("title") or "",
                heading_path=row.get("heading_path") or "",
                section=row.get("section") or "",
                module=row.get("module") or "",
            )

    def get(self, doc_id: str) -> Chunk | None:
        return self._chunks.get(doc_id)


class RagService:
    def __init__(self, cfg: AppConfig) -> None:
        self._cfg = cfg
        self._chunks = ChunkStore(cfg.rag_data_dir / CHUNKS_FILE)
        self._bm25 = Bm25Index.load(cfg.rag_data_dir / BM25_FILE)
        self._qdrant = QdrantStore.connect(
            url=cfg.qdrant.url,
            collection=cfg.qdrant.collection,
            vector_size=1024,
        )
        self._bge = BgeClient(cfg.bge)
        self._openai = OpenAIClient(cfg.openai) if cfg.openai.api_key else None

    def search(self, query: str) -> list[Chunk]:
        sections = route_sections(query)
        filter_ = _sections_filter(sections) if sections else None

        bm25_results = self._bm25.query(query, top_k=self._cfg.retrieval.bm25_k)

        vector = self._bge.embed([query])[0]
        vector_results = self._qdrant.search(
            vector=vector,
            top_k=self._cfg.retrieval.vector_k,
            filter_=filter_,
        )

        fused = rrf_fuse(bm25_results, vector_results, k=self._cfg.retrieval.rrf_k)
        top_ids = [item.doc_id for item in fused[: self._cfg.retrieval.rerank_k]]

        docs = [self._chunks.get(doc_id) for doc_id in top_ids]
        return [doc for doc in docs if doc]

    def answer(self, query: str) -> dict:
        candidates = self.search(query)
        if not candidates:
            return {
                "answer": "Не найдено в локальном индексе. Попробуйте уточнить запрос.",
                "sources": [],
                "mode": "fallback",
            }

        docs_text = [doc.text[: self._cfg.indexing.max_rerank_chars] for doc in candidates]
        scores = self._bge.rerank(query=query, documents=docs_text)
        reranked = sorted(zip(candidates, scores), key=lambda item: item[1], reverse=True)
        top = [doc for doc, _ in reranked[: self._cfg.retrieval.rerank_k]]

        sources = [doc.path for doc in top][:4]
        context = _build_context(top, max_chars=6000)

        if not self._openai:
            return {
                "answer": _extractive_answer(query, top),
                "sources": sources,
                "mode": "extractive",
            }

        prompt = _build_prompt(query, context)
        answer = self._openai.complete(prompt)
        return {"answer": answer, "sources": sources, "mode": "llm"}


def _sections_filter(sections: list[str] | None) -> qmodels.Filter | None:
    if not sections:
        return None
    return qmodels.Filter(
        must=[
            qmodels.FieldCondition(
                key="section",
                match=qmodels.MatchAny(any=sections),
            )
        ]
    )


def _build_context(chunks: Iterable[Chunk], max_chars: int) -> str:
    parts: list[str] = []
    size = 0
    for chunk in chunks:
        header = f"[{chunk.path}]\n"
        body = chunk.text.strip()
        block = f"{header}{body}\n\n"
        if size + len(block) > max_chars:
            break
        parts.append(block)
        size += len(block)
    return "".join(parts).strip()


def _build_prompt(query: str, context: str) -> str:
    return (
        "Ты помощник по документации Bitrix. Отвечай на русском, кратко и по делу. "
        "В ответе обязательно 2-4 локальные ссылки вида docs/.... Не выдумывай.\n\n"
        f"Вопрос:\n{query}\n\n"
        f"Контекст:\n{context}\n\n"
        "Ответ:"
    )


def _extractive_answer(query: str, chunks: list[Chunk]) -> str:
    snippets = []
    for chunk in chunks[:3]:
        text = chunk.text.strip().replace("\n", " ")
        snippets.append(text[:300])
    return " ".join(snippets) or f"Не найдено точного ответа на запрос: {query}"
