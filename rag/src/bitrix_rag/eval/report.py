from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from statistics import mean
import csv

from ..retrieval.rag import RagService
from .test_set import TestCase


@dataclass(frozen=True)
class EvalRow:
    id: str
    question: str
    expected: list[str]
    top_paths: list[str]
    hit: int
    rank: int | None


@dataclass(frozen=True)
class EvalMetrics:
    recall: float
    mrr: float


def evaluate_search(
    service: RagService, cases: list[TestCase], top_k: int
) -> tuple[list[EvalRow], EvalMetrics]:
    results: list[EvalRow] = []
    recalls: list[int] = []
    mrrs: list[float] = []

    for case in cases:
        hits = service.search(case.question)[:top_k]
        paths = [doc.path for doc in hits]
        rank = None
        for idx, path in enumerate(paths, start=1):
            if path in case.expected:
                rank = idx
                break
        hit = 1 if rank is not None else 0
        mrr = 1 / rank if rank else 0
        recalls.append(hit)
        mrrs.append(mrr)
        results.append(
            EvalRow(
                id=case.id,
                question=case.question,
                expected=case.expected,
                top_paths=paths,
                hit=hit,
                rank=rank,
            )
        )

    metrics = EvalMetrics(
        recall=mean(recalls) if recalls else 0.0,
        mrr=mean(mrrs) if mrrs else 0.0,
    )
    return results, metrics


def write_csv(path: Path, rows: list[EvalRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "question", "expected", "top_paths", "hit", "rank"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "id": row.id,
                    "question": row.question,
                    "expected": ";".join(row.expected),
                    "top_paths": ";".join(row.top_paths),
                    "hit": row.hit,
                    "rank": row.rank or "",
                }
            )
