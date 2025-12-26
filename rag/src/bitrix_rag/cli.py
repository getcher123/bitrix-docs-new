from __future__ import annotations

import argparse
from pathlib import Path

from dotenv import load_dotenv

from .config import load_config
from .index.build import build_indexes
from .retrieval.rag import RagService


def main() -> None:
    parser = argparse.ArgumentParser(prog="bitrix-rag")
    parser.add_argument("--env-file", default=".env", help="Path to .env (default: .env)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("index", help="Build BM25 + vector indexes")

    search_parser = sub.add_parser("search", help="Search top chunks")
    search_parser.add_argument("query")

    answer_parser = sub.add_parser("answer", help="Generate answer")
    answer_parser.add_argument("query")
    args = parser.parse_args()

    env_path = Path(args.env_file)
    if env_path.exists():
        load_dotenv(env_path)

    repo_root = Path(__file__).resolve().parents[3]
    cfg = load_config(repo_root)

    if args.command == "index":
        build_indexes(cfg)
        print("Indexes built.")
        return

    service = RagService(cfg)
    if args.command == "search":
        results = service.search(args.query)
        for doc in results:
            print(f"- {doc.path} :: {doc.heading_path or doc.title}")
        return

    if args.command == "answer":
        result = service.answer(args.query)
        print(result["answer"])
        if result.get("sources"):
            print("Sources:")
            for src in result["sources"]:
                print(f"- {src}")
