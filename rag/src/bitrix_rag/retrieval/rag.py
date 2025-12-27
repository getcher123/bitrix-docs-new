from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable
import time

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
        self._qdrant = None
        try:
            self._qdrant = QdrantStore.connect(
                url=cfg.qdrant.url,
                collection=cfg.qdrant.collection,
                vector_size=1024,
            )
        except Exception:
            self._qdrant = None
        self._bge = BgeClient(cfg.bge)
        self._openai = OpenAIClient(cfg.openai) if cfg.openai.api_key else None

    def search(
        self,
        query: str,
        timings: dict[str, float] | None = None,
        started: float | None = None,
        budget_s: int | None = None,
        sections_override: list[str] | None = None,
    ) -> list[Chunk]:
        search_started = time.monotonic()
        sections = sections_override or route_sections(query)
        filter_ = _sections_filter(sections) if sections else None

        bm25_started = time.monotonic()
        bm25_results = self._bm25.query(query, top_k=self._cfg.retrieval.bm25_k)
        if sections:
            bm25_results = [
                item
                for item in bm25_results
                if (chunk := self._chunks.get(item[0])) and chunk.section in sections
            ]
        if timings is not None:
            timings["bm25_ms"] = (time.monotonic() - bm25_started) * 1000

        vector_results: list[tuple[str, float]] = []
        if self._qdrant and not _skip_vector(sections, self._cfg.retrieval.fast_rest):
            try:
                if started is not None and budget_s is not None:
                    if _time_left(started, budget_s) < 5:
                        raise RuntimeError("Time budget exceeded before embed")
                embed_started = time.monotonic()
                embed_timeout = _cap_timeout(self._cfg.bge.timeout_s, started, budget_s, floor_s=2)
                vector = self._bge.embed([query], timeout_s=embed_timeout)[0]
                if timings is not None:
                    timings["embed_ms"] = (time.monotonic() - embed_started) * 1000
                qdrant_started = time.monotonic()
                vector_results = self._qdrant.search(
                    vector=vector,
                    top_k=self._cfg.retrieval.vector_k,
                    filter_=filter_,
                )
                if timings is not None:
                    timings["qdrant_ms"] = (time.monotonic() - qdrant_started) * 1000
            except Exception as exc:
                print(f"Vector search skipped (reason: {exc})")

        fused = rrf_fuse(bm25_results, vector_results, k=self._cfg.retrieval.rrf_k)
        top_ids = [item.doc_id for item in fused[: self._cfg.retrieval.rerank_k]]

        docs = [self._chunks.get(doc_id) for doc_id in top_ids]
        results = [doc for doc in docs if doc]
        if timings is not None:
            timings["search_ms"] = (time.monotonic() - search_started) * 1000
        return results

    def answer(self, query: str) -> dict:
        started = time.monotonic()
        timings: dict[str, float] = {}
        sections = route_sections(query)
        candidates = self.search(
            query,
            timings=timings,
            started=started,
            budget_s=self._cfg.retrieval.max_latency_s,
            sections_override=sections,
        )
        if not candidates:
            timings["total_ms"] = (time.monotonic() - started) * 1000
            return {
                "answer": "Не найдено в локальном индексе. Попробуйте уточнить запрос.",
                "sources": [],
                "mode": "fallback",
                "timings_ms": timings,
            }

        top = candidates
        try:
            if _skip_rerank(sections, self._cfg.retrieval.fast_rest):
                raise RuntimeError("Rerank skipped for REST fast mode")
            if _time_left(started, self._cfg.retrieval.max_latency_s) < 5:
                raise RuntimeError("Time budget exceeded before rerank")
            rerank_started = time.monotonic()
            docs_text = [doc.text[: self._cfg.indexing.max_rerank_chars] for doc in candidates]
            rerank_timeout = _cap_timeout(
                self._cfg.bge.timeout_s,
                started,
                self._cfg.retrieval.max_latency_s,
                floor_s=2,
            )
            scores = self._bge.rerank(query=query, documents=docs_text, timeout_s=rerank_timeout)
            reranked = sorted(zip(candidates, scores), key=lambda item: item[1], reverse=True)
            top = [doc for doc, _ in reranked[: self._cfg.retrieval.rerank_k]]
            timings["rerank_ms"] = (time.monotonic() - rerank_started) * 1000
        except Exception as exc:
            print(f"Rerank skipped (reason: {exc})")

        sources = [f"docs/{doc.path}" for doc in top][:4]
        context = _build_context(top, max_chars=6000)

        if not self._openai or _skip_llm(sections, self._cfg.retrieval.fast_rest):
            timings["total_ms"] = (time.monotonic() - started) * 1000
            return {
                "answer": _attach_sources(_extractive_answer(query, top), sources),
                "sources": sources,
                "mode": "extractive",
                "timings_ms": timings,
            }

        prompt = _build_prompt(query, context, sources)
        try:
            if _time_left(started, self._cfg.retrieval.max_latency_s) < 5:
                raise RuntimeError("Time budget exceeded before LLM")
            llm_started = time.monotonic()
            llm_timeout = _cap_timeout(
                self._cfg.openai.timeout_s,
                started,
                self._cfg.retrieval.max_latency_s,
                floor_s=2,
            )
            answer = self._openai.complete(prompt, timeout_s=llm_timeout)
            answer = _attach_sources(answer, sources)
            timings["llm_ms"] = (time.monotonic() - llm_started) * 1000
            timings["total_ms"] = (time.monotonic() - started) * 1000
            return {"answer": answer, "sources": sources, "mode": "llm", "timings_ms": timings}
        except Exception as exc:
            print(f"LLM fallback (reason: {exc})")
            timings["total_ms"] = (time.monotonic() - started) * 1000
            return {
                "answer": _attach_sources(_extractive_answer(query, top), sources),
                "sources": sources,
                "mode": "extractive",
                "timings_ms": timings,
            }


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


def _build_prompt(query: str, context: str, sources: list[str]) -> str:
    sources_block = "\n".join(f"- {src}" for src in sources)
    return (
        "Ты помощник по документации Bitrix. Отвечай на русском, кратко и по делу. "
        "В ответе обязательно 2-4 локальные ссылки вида docs/.... Не выдумывай. "
        "Используй только источники из списка ниже и указывай их пути дословно.\n\n"
        f"Вопрос:\n{query}\n\n"
        f"Разрешенные источники:\n{sources_block}\n\n"
        f"Контекст:\n{context}\n\n"
        "Ответ:"
    )


def _extractive_answer(query: str, chunks: list[Chunk]) -> str:
    snippets = []
    for chunk in chunks[:3]:
        text = chunk.text.strip().replace("\n", " ")
        snippets.append(text[:300])
    return " ".join(snippets) or f"Не найдено точного ответа на запрос: {query}"


def _attach_sources(answer: str, sources: list[str]) -> str:
    if not sources:
        return answer
    missing = [src for src in sources if src not in answer]
    if not missing:
        return answer
    tail = "\n\nСсылки:\n" + "\n".join(f"- {src}" for src in sources)
    return answer.rstrip() + tail


def _time_left(started: float, budget_s: int) -> float:
    return budget_s - (time.monotonic() - started)


def _cap_timeout(
    default_s: int,
    started: float | None,
    budget_s: int | None,
    floor_s: int = 2,
) -> int:
    if started is None or budget_s is None:
        return default_s
    remaining = _time_left(started, budget_s)
    return max(floor_s, min(default_s, int(remaining)))


def _skip_vector(sections: list[str] | None, fast_rest: bool) -> bool:
    return bool(fast_rest and sections == ["REST"])


def _skip_rerank(sections: list[str] | None, fast_rest: bool) -> bool:
    return bool(fast_rest and sections == ["REST"])


def _skip_llm(sections: list[str] | None, fast_rest: bool) -> bool:
    return bool(fast_rest and sections == ["REST"])
