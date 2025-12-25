#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Refetches and fills empty/near-empty `*.php.md` pages in this vault.

Why this exists:
- Many `docs/d7/**/*.php.md` and `docs/user_help/**/*.php.md` files were created
  with only an H1 (placeholders), while the source pages on dev.1c-bitrix.ru
  contain full content.
- This script re-downloads only the missing content and injects it into the
  existing markdown files (keeps the vault format; no site generator needed).

What it does:
- For each target `*.php.md` file that is effectively empty, downloads the
  corresponding HTML page from dev.1c-bitrix.ru.
- Extracts the main documentation block (`div#js-lesson-content-cnt`).
- Writes `# <title>` + extracted HTML into the local markdown file.
- Rewrites internal links to local files when they exist; otherwise keeps them
  as absolute URLs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen


BASE_URL = "https://dev.1c-bitrix.ru"

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
DOC_NAME_RE = re.compile(r'<h1[^>]*class="document-name"[^>]*>(.*?)</h1>', re.I | re.S)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
HREF_RE = re.compile(r"""href=(['"])(.*?)\1""", re.I)
SRC_RE = re.compile(r"""src=(['"])(.*?)\1""", re.I)
DIV_CLASS_RE = re.compile(r"""<div\b[^>]*\bclass=(['"])([^'"]*)\1""", re.I)

FOLDER_NAV_START = "<!-- vault-nav:start -->"
FOLDER_NAV_END = "<!-- vault-nav:end -->"
STUB_LINE = "Эта страница выгружена как индекс‑заглушка."


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_dev_url(raw: str) -> tuple[str, str]:
    raw = raw.strip()
    anchor = ""
    if "#" in raw:
        raw, anchor_part = raw.split("#", 1)
        anchor = f"#{anchor_part}"

    if raw.startswith("/"):
        raw = BASE_URL + raw

    if not raw.startswith("http"):
        return raw, anchor

    parts = urlsplit(raw)
    if "1c-bitrix.ru" not in parts.netloc:
        return raw, anchor

    q = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k != "print"]
    query = urlencode(q) if q else ""
    cleaned = urlunsplit((parts.scheme, parts.netloc, parts.path, query, ""))
    return cleaned.rstrip("?&"), anchor


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html)


def extract_div_inner_by_id(html: str, *, element_id: str) -> str | None:
    # Search for id="..."
    marker_1 = f'id="{element_id}"'
    marker_2 = f"id='{element_id}'"
    idx = html.find(marker_1)
    if idx == -1:
        idx = html.find(marker_2)
    if idx == -1:
        return None

    open_start = html.rfind("<div", 0, idx)
    if open_start == -1:
        return None
    open_end = html.find(">", open_start)
    if open_end == -1:
        return None

    depth = 1
    pos = open_end + 1
    close_start = -1

    while depth > 0 and pos < len(html):
        next_open = html.find("<div", pos)
        next_close = html.find("</div", pos)
        if next_close == -1:
            return None

        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
            continue

        depth -= 1
        close_start = next_close
        pos = next_close + 5

    if close_start == -1:
        return None

    return html[open_end + 1 : close_start].strip()


def extract_div_inner_by_class(html: str, *, class_name: str) -> str | None:
    marker_1 = f'class="{class_name}"'
    marker_2 = f"class='{class_name}'"
    idx = html.find(marker_1)
    if idx == -1:
        idx = html.find(marker_2)
    if idx == -1:
        # class may include multiple names; try a regex match
        m = re.search(rf"""<div\b[^>]*\bclass=(['"])[^'"]*\b{re.escape(class_name)}\b[^'"]*\1""", html, re.I)
        if not m:
            return None
        idx = m.start()

    open_start = html.rfind("<div", 0, idx)
    if open_start == -1:
        return None
    open_end = html.find(">", open_start)
    if open_end == -1:
        return None

    depth = 1
    pos = open_end + 1
    close_start = -1

    while depth > 0 and pos < len(html):
        next_open = html.find("<div", pos)
        next_close = html.find("</div", pos)
        if next_close == -1:
            return None

        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
            continue

        depth -= 1
        close_start = next_close
        pos = next_close + 5

    if close_start == -1:
        return None

    return html[open_end + 1 : close_start].strip()


def remove_div_by_id(html: str, *, element_id: str) -> str:
    marker_1 = f'id="{element_id}"'
    marker_2 = f"id='{element_id}'"
    idx = html.find(marker_1)
    if idx == -1:
        idx = html.find(marker_2)
    if idx == -1:
        return html

    open_start = html.rfind("<div", 0, idx)
    if open_start == -1:
        return html
    open_end = html.find(">", open_start)
    if open_end == -1:
        return html

    depth = 1
    pos = open_end + 1
    close_start = -1

    while depth > 0 and pos < len(html):
        next_open = html.find("<div", pos)
        next_close = html.find("</div", pos)
        if next_close == -1:
            return html

        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
            continue

        depth -= 1
        close_start = next_close
        pos = next_close + 5

    if close_start == -1:
        return html

    close_end = html.find(">", close_start)
    if close_end == -1:
        return html

    return (html[:open_start] + html[close_end + 1 :]).strip()


def extract_title(html: str) -> str | None:
    m = DOC_NAME_RE.search(html)
    if m:
        title_html = m.group(1).strip()
        title = unescape(strip_tags(title_html)).strip()
        return title if title else None
    m = TITLE_RE.search(html)
    if m:
        title = unescape(strip_tags(m.group(1))).strip()
        return title if title else None
    return None


def remove_autogen_nav_block(text: str) -> str:
    if FOLDER_NAV_START not in text or FOLDER_NAV_END not in text:
        return text
    start = text.find(FOLDER_NAV_START)
    end = text.find(FOLDER_NAV_END, start)
    if start == -1 or end == -1:
        return text
    end = end + len(FOLDER_NAV_END)
    return (text[:start] + text[end:]).strip() + "\n"


def is_effectively_empty(text: str) -> bool:
    # Drop autogenerated folder nav block (if any).
    text = remove_autogen_nav_block(text)

    # Remove the H1 line.
    text_wo_h1 = H1_RE.sub("", text, count=1).strip()
    if not text_wo_h1:
        return True

    # If it's only our stub disclaimer (and possibly a couple of links) — treat as empty.
    compact = "\n".join(line.strip() for line in text_wo_h1.splitlines() if line.strip())
    if not compact:
        return True

    if STUB_LINE in compact:
        # Allow only a few lines beyond the stub.
        lines = [l for l in compact.splitlines() if l.strip()]
        if len(lines) <= 12:
            return True

    # Heuristic: very short body => empty.
    return len(compact) < 80


def file_to_source_url(md_path: Path) -> str | None:
    posix = md_path.as_posix()
    if not posix.endswith(".php.md"):
        return None

    if posix.startswith("docs/d7/"):
        rel = md_path.relative_to(Path("docs/d7")).as_posix()
        rel = rel[: -len(".md")]  # keep the .php suffix
        return f"{BASE_URL}/api_d7/{rel}"

    if posix.startswith("docs/user_help/"):
        rel = md_path.relative_to(Path("docs/user_help")).as_posix()
        rel = rel[: -len(".md")]
        return f"{BASE_URL}/user_help/{rel}"

    return None


def read_h1(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    m = H1_RE.search(text)
    return m.group(1).strip() if m else None


@dataclass(frozen=True)
class RewriteContext:
    file_path: Path
    docs_dir: Path
    url_mapping: dict[str, str]
    page_url: str


def _target_for_dev_path(ctx: RewriteContext, abs_url: str) -> Path | None:
    normalized, _anchor = normalize_dev_url(abs_url)
    parts = urlsplit(normalized)
    if "1c-bitrix.ru" not in parts.netloc:
        return None

    if parts.path.startswith("/api_d7/"):
        rel = parts.path[len("/api_d7/") :].lstrip("/")
        # Map to docs/d7/<rel>.md
        return ctx.docs_dir / "d7" / f"{rel}.md"

    if parts.path.startswith("/user_help/"):
        rel = parts.path[len("/user_help/") :].lstrip("/")
        return ctx.docs_dir / "user_help" / f"{rel}.md"

    if parts.path.startswith("/api_help/"):
        # Try mapping where possible.
        mapped = None
        for candidate in (normalized, normalized.replace("http://", "https://", 1)):
            mapped = ctx.url_mapping.get(candidate)
            if mapped:
                break
        if mapped:
            return ctx.docs_dir / mapped
        return None

    return None


def rewrite_href_and_src(fragment: str, *, ctx: RewriteContext) -> str:
    def rewrite_href(m: re.Match[str]) -> str:
        quote = m.group(1)
        href = m.group(2).strip()

        if not href or href.startswith(("#", "javascript:", "mailto:")):
            return m.group(0)

        normalized, anchor = normalize_dev_url(urljoin(ctx.page_url, href))

        target = _target_for_dev_path(ctx, normalized)
        if target and target.exists():
            rel = os.path.relpath(target, ctx.file_path.parent).replace("\\", "/")
            return f'href={quote}{rel}{anchor}{quote}'

        return f'href={quote}{normalized}{anchor}{quote}'

    def rewrite_src(m: re.Match[str]) -> str:
        quote = m.group(1)
        src = m.group(2).strip()

        if not src or src.startswith(("data:", "javascript:")):
            return m.group(0)

        normalized, anchor = normalize_dev_url(urljoin(ctx.page_url, src))
        # For now we keep images as absolute URLs unless they already exist locally.
        # (Downloading images is intentionally out-of-scope for this refetch script.)
        return f'src={quote}{normalized}{anchor}{quote}'

    fragment = HREF_RE.sub(rewrite_href, fragment)
    fragment = SRC_RE.sub(rewrite_src, fragment)
    return fragment


def fetch_html(url: str, *, timeout_sec: float) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
            "Accept-Language": "ru,en;q=0.8",
        },
    )
    with urlopen(req, timeout=timeout_sec) as resp:
        data = resp.read()
    return data.decode("utf-8", errors="replace")


def extract_primary_content(html: str) -> str | None:
    """
    Most dev.1c-bitrix.ru doc pages store the actual content inside
    `div#js-lesson-content-cnt`. Some pages (mostly namespace indexes) have
    only `div.content-text` with a list of links.
    """
    detail = extract_div_inner_by_id(html, element_id="js-lesson-content-cnt")
    if detail:
        return detail

    content_text = extract_div_inner_by_class(html, class_name="content-text")
    if not content_text:
        return None

    # Drop breadcrumb banner where present.
    content_text = remove_div_by_id(content_text, element_id="pagetop")
    return content_text.strip()


def iter_php_md_files(docs_dir: Path, *, scopes: set[str]) -> Iterable[Path]:
    if "d7" in scopes:
        yield from sorted((docs_dir / "d7").rglob("*.php.md"))
    if "user_help" in scopes:
        yield from sorted((docs_dir / "user_help").rglob("*.php.md"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scopes",
        default="d7,user_help",
        help="Comma-separated scopes: d7,user_help",
    )
    parser.add_argument(
        "--only",
        default="",
        help="Optional substring filter (process only paths containing this string).",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Limit number of updated files (0 = no limit).",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.2,
        help="Sleep seconds between requests.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout per page, seconds.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Refetch even if the file is not considered empty.",
    )
    args = parser.parse_args()

    scopes = {s.strip() for s in args.scopes.split(",") if s.strip()}
    unknown = scopes - {"d7", "user_help"}
    if unknown:
        print(f"Unknown scopes: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    root = repo_root()
    docs_dir = root / "docs"
    mapping_path = root / "url_mapping.json"
    url_mapping = json.loads(mapping_path.read_text(encoding="utf-8")) if mapping_path.exists() else {}

    candidates = list(iter_php_md_files(docs_dir, scopes=scopes))
    if args.only:
        needle = args.only.replace("\\", "/")
        candidates = [p for p in candidates if needle in p.relative_to(root).as_posix()]
    updated = 0
    skipped = 0
    failed = 0

    for md in candidates:
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            failed += 1
            continue

        if not args.force and not is_effectively_empty(text):
            skipped += 1
            continue

        url = file_to_source_url(md.relative_to(root))
        if not url:
            skipped += 1
            continue

        try:
            html = fetch_html(url, timeout_sec=args.timeout)
        except Exception as e:
            failed += 1
            print(f"[fail] {md}: {url} ({e})")
            continue

        title = extract_title(html) or read_h1(md) or md.stem
        detail = extract_primary_content(html)
        if not detail:
            failed += 1
            print(f"[fail] {md}: cannot extract main content from {url}")
            continue

        ctx = RewriteContext(file_path=md, docs_dir=docs_dir, url_mapping=url_mapping, page_url=url)
        detail = rewrite_href_and_src(detail, ctx=ctx)

        if "404 - Страница не найдена" in detail:
            new_text = f"# {title}\n\n" f"Источник: {url}\n\n" f"Страница не найдена на источнике.\n"
        else:
            new_text = f"# {title}\n\n" f"Источник: {url}\n\n" f"{detail}\n"
        md.write_text(new_text, encoding="utf-8")
        updated += 1

        if args.max_files and updated >= args.max_files:
            break

        if args.sleep:
            time.sleep(args.sleep)

    print(f"[refetch] scopes={','.join(sorted(scopes))} total={len(candidates)} updated={updated} skipped={skipped} failed={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
