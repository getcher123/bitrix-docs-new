from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoredDoc:
    doc_id: str
    score: float


def rrf_fuse(
    bm25: list[tuple[str, float]],
    vector: list[tuple[str, float]],
    k: int,
) -> list[ScoredDoc]:
    scores: dict[str, float] = {}
    for rank, (doc_id, _) in enumerate(bm25, start=1):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    for rank, (doc_id, _) in enumerate(vector, start=1):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    fused = [ScoredDoc(doc_id=doc_id, score=score) for doc_id, score in scores.items()]
    return sorted(fused, key=lambda item: item.score, reverse=True)
