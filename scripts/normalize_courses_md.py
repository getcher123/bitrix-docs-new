#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Normalizes course lesson markdown (`docs/courses/**/lesson_*.md`) for vault use:

- Downloads external images referenced in Markdown image syntax.
- Stores them under `images/courses/<COURSE_ID>/...`.
- Rewrites image links to local relative paths.

Stdlib-only (reuses helpers from `scripts/normalize_php_md.py`).
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from normalize_php_md import download_image, relpath, rewrite_markdown_images


MD_IMAGE_MARKER_RE = re.compile(r"!\[")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def course_id_from_path(p: Path) -> str | None:
    for parent in p.parents:
        if parent.name.startswith("course_"):
            m = re.match(r"course_(\d+)_", parent.name)
            if m:
                return m.group(1)
            m = re.match(r"course_(\d+)$", parent.name)
            if m:
                return m.group(1)
            return None
    return None


@dataclass
class Stats:
    processed: int = 0
    changed_files: int = 0
    downloaded_images: int = 0
    rewritten_links: int = 0
    failed_images: int = 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default="", help="Optional substring filter (process only paths containing this string).")
    parser.add_argument("--sleep", type=float, default=0.02, help="Sleep seconds between image downloads.")
    parser.add_argument("--timeout", type=float, default=40.0, help="HTTP timeout per image, seconds.")
    args = parser.parse_args()

    root = repo_root()
    docs_dir = root / "docs"
    images_root = root / "images"

    stats = Stats()
    img_cache: dict[str, Path] = {}

    lessons = sorted((docs_dir / "courses").rglob("lesson_*.md"))
    if args.only:
        needle = args.only.replace("\\", "/")
        lessons = [p for p in lessons if needle in p.as_posix()]

    for path in lessons:
        stats.processed += 1
        original = path.read_text(encoding="utf-8", errors="replace")
        if not MD_IMAGE_MARKER_RE.search(original):
            continue

        cid = course_id_from_path(path)
        if not cid:
            continue

        scope = f"courses/{cid}"

        def img_repl(_alt: str, url_part: str, rest: str) -> str:
            nonlocal stats
            # Only rewrite http(s) URLs (leave local already-local ones).
            if not url_part.startswith(("http://", "https://")):
                return url_part

            cached = img_cache.get(url_part)
            if cached and cached.exists():
                stats.rewritten_links += 1
                return relpath(path, cached)

            res = download_image(
                url_part,
                scope=scope,
                images_root=images_root,
                sleep_sec=args.sleep,
                timeout_sec=args.timeout,
            )
            if not res.local_path:
                stats.failed_images += 1
                return url_part

            img_cache[url_part] = res.local_path
            stats.downloaded_images += 1
            stats.rewritten_links += 1
            return relpath(path, res.local_path)

        out = rewrite_markdown_images(original, repl=img_repl)
        if out != original:
            path.write_text(out, encoding="utf-8")
            stats.changed_files += 1

    print(
        "[normalize-courses] "
        f"processed={stats.processed} changed_files={stats.changed_files} "
        f"downloaded_images={stats.downloaded_images} rewritten_links={stats.rewritten_links} "
        f"failed_images={stats.failed_images}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

