from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Iterable

from rank_bm25 import BM25Okapi

from ..ingest.pipeline import ChunkRecord


TOKEN_RE = re.compile(r"[A-Za-zА-Яа-я0-9_]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text)]


@dataclass
class Bm25Index:
    doc_ids: list[str]
    tokens: list[list[str]]
    bm25: BM25Okapi

    @classmethod
    def build(cls, records: Iterable[ChunkRecord]) -> "Bm25Index":
        doc_ids: list[str] = []
        tokens: list[list[str]] = []
        for record in records:
            doc_ids.append(record.chunk.chunk_id)
            tokens.append(tokenize(record.chunk.text))
        bm25 = BM25Okapi(tokens)
        return cls(doc_ids=doc_ids, tokens=tokens, bm25=bm25)

    def save(self, path: Path) -> None:
        payload = {"doc_ids": self.doc_ids, "tokens": self.tokens}
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Bm25Index":
        data = json.loads(path.read_text(encoding="utf-8"))
        doc_ids = data["doc_ids"]
        tokens = data["tokens"]
        bm25 = BM25Okapi(tokens)
        return cls(doc_ids=doc_ids, tokens=tokens, bm25=bm25)

    def query(self, text: str, top_k: int) -> list[tuple[str, float]]:
        scores = self.bm25.get_scores(tokenize(text))
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]
        return [(self.doc_ids[idx], float(score)) for idx, score in ranked]
