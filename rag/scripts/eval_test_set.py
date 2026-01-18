#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from statistics import mean

from dotenv import load_dotenv

from bitrix_rag.config import load_config
from bitrix_rag.retrieval.rag import RagService


LINK_RE = re.compile(r"\(([^)]+)\)")


def parse_test_set(path: Path) -> list[tuple[str, str, list[str]]]:
    rows: list[tuple[str, str, list[str]]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| Q"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        qid = parts[0]
        question = parts[1]
        expected_raw = parts[3]
        expected = []
        for link in LINK_RE.findall(expected_raw):
            if link.startswith("http"):
                continue
            expected.append(_normalize_link(link))
        rows.append((qid, question, [e for e in expected if e]))
    return rows


def _normalize_link(link: str) -> str:
    link = link.strip()
    link = link.replace("\\\\", "/")
    while link.startswith("../"):
        link = link[3:]
    if link.startswith("./"):
        link = link[2:]
    if link.startswith("docs/"):
        link = link[5:]
    return link


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", default="rag/.env", help="Path to .env")
    parser.add_argument("--test-set", default="docs/RAG/RAG_TEST_SET.md")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--out", default="docs/RAG/RAG_EVAL_REPORT.csv")
    args = parser.parse_args()

    env_path = Path(args.env_file)
    if env_path.exists():
        load_dotenv(env_path)

    repo_root = Path(__file__).resolve().parents[2]
    cfg = load_config(repo_root)
    service = RagService(cfg)

    test_set = parse_test_set(Path(args.test_set))
    results = []
    recalls = []
    mrrs = []

    for qid, question, expected in test_set:
        hits = service.search(question)[: args.top_k]
        paths = [doc.path for doc in hits]
        rank = None
        for idx, path in enumerate(paths, start=1):
            if path in expected:
                rank = idx
                break
        hit = 1 if rank is not None else 0
        mrr = 1 / rank if rank else 0
        recalls.append(hit)
        mrrs.append(mrr)
        results.append(
            {
                "id": qid,
                "question": question,
                "expected": ";".join(expected),
                "top_paths": ";".join(paths),
                "hit": hit,
                "rank": rank or "",
            }
        )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "question", "expected", "top_paths", "hit", "rank"],
        )
        writer.writeheader()
        writer.writerows(results)

    recall = mean(recalls) if recalls else 0.0
    mrr = mean(mrrs) if mrrs else 0.0
    print(f"Recall@{args.top_k}: {recall:.3f}")
    print(f"MRR@{args.top_k}: {mrr:.3f}")
    print(f"Report: {out_path}")


if __name__ == "__main__":
    main()
