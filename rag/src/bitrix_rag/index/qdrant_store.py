from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels


@dataclass(frozen=True)
class QdrantStore:
    client: QdrantClient
    collection: str

    @classmethod
    def connect(cls, url: str, collection: str, vector_size: int) -> "QdrantStore":
        client = QdrantClient(url=url)
        existing = client.get_collections().collections
        if not any(c.name == collection for c in existing):
            client.create_collection(
                collection_name=collection,
                vectors_config=qmodels.VectorParams(
                    size=vector_size,
                    distance=qmodels.Distance.COSINE,
                ),
            )
        return cls(client=client, collection=collection)

    def upsert(
        self,
        ids: list[str],
        vectors: list[list[float]],
        payloads: list[dict],
    ) -> None:
        points = [
            qmodels.PointStruct(id=doc_id, vector=vector, payload=payload)
            for doc_id, vector, payload in zip(ids, vectors, payloads)
        ]
        self.client.upsert(collection_name=self.collection, points=points)

    def search(
        self,
        vector: list[float],
        top_k: int,
        filter_: qmodels.Filter | None = None,
    ) -> list[tuple[str, float]]:
        results = self.client.search(
            collection_name=self.collection,
            query_vector=vector,
            limit=top_k,
            query_filter=filter_,
        )
        return [(str(hit.id), float(hit.score)) for hit in results]
