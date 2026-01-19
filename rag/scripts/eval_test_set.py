#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from dotenv import load_dotenv

from bitrix_rag.config import load_config
from bitrix_rag.retrieval.rag import RagService
from bitrix_rag.eval import evaluate_search, parse_test_set, write_csv


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
    rows, metrics = evaluate_search(service, test_set, top_k=args.top_k)

    out_path = Path(args.out)
    write_csv(out_path, rows)

    print(f"Recall@{args.top_k}: {metrics.recall:.3f}")
    print(f"MRR@{args.top_k}: {metrics.mrr:.3f}")
    print(f"Report: {out_path}")


if __name__ == "__main__":
    main()
