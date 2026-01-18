#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import time
import os
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://apidocs.bitrix24.ru"
START_URL = "https://apidocs.bitrix24.ru/local-integrations/index.html"
DEFAULT_SCOPE_PREFIX = "local-integrations/"
SLEEP_S = 0.2
TOC_URL = "https://apidocs.bitrix24.ru/toc.js"


def clean_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\\\|?*]', "_", name)
    name = re.sub(r"\\s+", "_", name)
    name = name.strip("._")
    return name[:200] or "index"


def normalize_prefix(prefix: str | None) -> str:
    if not prefix:
        return ""
    prefix = prefix.strip()
    if prefix.startswith("/"):
        prefix = prefix[1:]
    if prefix and not prefix.endswith("/"):
        prefix += "/"
    return prefix


def url_to_rel_md_path(url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return Path("index.md")
    if path.endswith(".html"):
        path = path[: -len(".html")]
    return Path(path + ".md")


def url_to_output_path(url: str, output_dir: Path, strip_prefix: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if strip_prefix and path.startswith(strip_prefix):
        path = path[len(strip_prefix) :]
    if not path:
        return output_dir / "index.md"
    parts = path.split("/")
    filename = parts[-1]
    if filename.endswith(".html"):
        filename = filename[: -len(".html")]
    if not filename:
        filename = "index"
    filename = clean_filename(filename) + ".md"
    return output_dir.joinpath(*parts[:-1], filename)


def download_image(img_url: str, images_dir: Path) -> str | None:
    if img_url.startswith("data:"):
        return None
    if img_url.endswith(".svg"):
        return None
    try:
        resp = requests.get(img_url, timeout=30)
        if resp.status_code != 200:
            return None
        img_name = Path(urlparse(img_url).path).name
        if not img_name:
            img_name = f"image_{abs(hash(img_url))}.png"
        img_name = clean_filename(img_name)
        images_dir.mkdir(parents=True, exist_ok=True)
        img_path = images_dir / img_name
        img_path.write_bytes(resp.content)
        return img_path.name
    except Exception:
        return None


def is_in_scope(path: str, scope_prefix: str) -> bool:
    path = path.lstrip("/")
    if not scope_prefix:
        return True
    if path == scope_prefix.rstrip("/"):
        return True
    return path.startswith(scope_prefix)


def resolve_link(
    href: str,
    base_url: str,
    output_dir: Path,
    current_dir: Path,
    scope_prefix: str,
    strip_prefix: str,
    skip_roots: list[Path],
) -> str:
    if href.startswith("#"):
        return href
    abs_url = urljoin(base_url, href)
    parsed = urlparse(abs_url)
    if parsed.netloc == urlparse(BASE_URL).netloc:
        rel_md = url_to_rel_md_path(abs_url)
        for root in skip_roots:
            target_path = root / rel_md
            if target_path.exists():
                rel_link = os.path.relpath(target_path, current_dir)
                if parsed.fragment:
                    return f"{rel_link}#{parsed.fragment}"
                return rel_link
        if is_in_scope(parsed.path, scope_prefix):
            target_path = url_to_output_path(abs_url, output_dir, strip_prefix)
            rel_link = os.path.relpath(target_path, current_dir)
            if parsed.fragment:
                return f"{rel_link}#{parsed.fragment}"
            return rel_link
    return abs_url


def render_inline(
    elem,
    base_url: str,
    output_dir: Path,
    current_dir: Path,
    scope_prefix: str,
    strip_prefix: str,
    skip_roots: list[Path],
) -> str:
    if elem.name is None:
        return str(elem)
    if elem.name == "a":
        href = elem.get("href", "")
        text = elem.get_text(strip=True)
        if not href:
            return text
        link = resolve_link(href, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots)
        return f"[{text}]({link})" if text else link
    if elem.name == "code":
        return f"`{elem.get_text()}`"
    if elem.name in ["strong", "b"]:
        return f"**{elem.get_text(strip=True)}**"
    if elem.name in ["em", "i"]:
        return f"*{elem.get_text(strip=True)}*"
    if elem.name == "br":
        return "\\n"
    return "".join(
        render_inline(child, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots)
        for child in elem.children
    )


def element_to_md(
    elem,
    base_url: str,
    output_dir: Path,
    current_dir: Path,
    images_dir: Path,
    scope_prefix: str,
    strip_prefix: str,
    skip_roots: list[Path],
) -> str:
    if elem.name is None:
        text = str(elem).strip()
        return text
    if elem.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        level = int(elem.name[1])
        text = elem.get_text(" ", strip=True)
        words = text.split()
        if len(words) % 2 == 0:
            mid = len(words) // 2
            if words[:mid] == words[mid:]:
                text = " ".join(words[:mid])
        return f"{'#' * level} {text}"
    if elem.name == "p":
        return render_inline(elem, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots).strip()
    if elem.name in ["ul", "ol"]:
        items = []
        for idx, li in enumerate(elem.find_all("li", recursive=False)):
            prefix = "-" if elem.name == "ul" else f"{idx + 1}."
            items.append(
                f"{prefix} "
                f"{render_inline(li, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots).strip()}"
            )
        return "\n".join(items)
    if elem.name == "pre":
        code = elem.get_text().rstrip()
        return f"```\\n{code}\\n```"
    if elem.name == "img":
        src = elem.get("src", "")
        alt = elem.get("alt", "image")
        if not src:
            return ""
        abs_url = urljoin(base_url, src)
        name = download_image(abs_url, images_dir)
        if not name:
            return ""
        rel_path = os.path.relpath(images_dir / name, current_dir)
        return f"![{alt}]({rel_path})"
    if elem.name == "table":
        rows = []
        for tr in elem.find_all("tr"):
            cells = [
                render_inline(td, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots).strip()
                for td in tr.find_all(["td", "th"])
            ]
            if cells:
                rows.append("| " + " | ".join(cells) + " |")
        if len(rows) > 1:
            header_sep = "| " + " | ".join(["---"] * len(rows[0].split("|")[1:-1])) + " |"
            rows.insert(1, header_sep)
        return "\n".join(rows)
    if elem.name == "blockquote":
        text = render_inline(elem, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots).strip()
        return "\n".join([f"> {line}" for line in text.splitlines() if line.strip()])
    if elem.name in ["div", "section", "article"]:
        parts = []
        for child in elem.children:
            result = element_to_md(
                child, base_url, output_dir, current_dir, images_dir, scope_prefix, strip_prefix, skip_roots
            )
            if result:
                parts.append(result)
        return "\n\n".join(parts)
    return render_inline(elem, base_url, output_dir, current_dir, scope_prefix, strip_prefix, skip_roots).strip()


def html_to_markdown(
    html: str,
    base_url: str,
    output_dir: Path,
    current_dir: Path,
    images_dir: Path,
    scope_prefix: str,
    strip_prefix: str,
    skip_roots: list[Path],
) -> str:
    soup = BeautifulSoup(html, "html.parser")
    parts = []
    for child in soup.children:
        result = element_to_md(child, base_url, output_dir, current_dir, images_dir, scope_prefix, strip_prefix, skip_roots)
        if result:
            parts.append(result)
    markdown = "\n\n".join(parts)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()


def extract_state(html_text: str) -> dict | None:
    soup = BeautifulSoup(html_text, "html.parser")
    state = soup.find("script", id="diplodoc-state")
    if not state or not state.string:
        return None
    raw = state.string
    raw = raw.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return json.loads(raw)


def load_toc_links(scope_prefix: str) -> list[str]:
    try:
        resp = requests.get(TOC_URL, timeout=30)
        if resp.status_code != 200:
            return []
        text = resp.text
        match = re.search(r"window.__DATA__.data.toc\s*=\s*(\{.*\})\s*;", text)
        if not match:
            return []
        toc = json.loads(match.group(1))
    except Exception:
        return []

    def collect(node: dict, links: set[str]) -> None:
        href = node.get("href")
        if href:
            href = href.lstrip("/")
            if not scope_prefix:
                links.add(href)
            elif href == scope_prefix.rstrip("/") or href.startswith(scope_prefix):
                links.add(href)
        for item in node.get("items", []):
            collect(item, links)

    links: set[str] = set()
    collect(toc, links)
    return sorted(links)


def parse_page(
    url: str,
    output_dir: Path,
    images_dir: Path,
    visited: set[str],
    queue: list[str],
    scope_prefix: str,
    strip_prefix: str,
    skip_roots: list[Path],
    skip_existing_output: bool,
) -> str:
    if url in visited:
        return "skipped_seen"
    visited.add(url)

    rel_md = url_to_rel_md_path(url)
    for root in skip_roots:
        if (root / rel_md).exists():
            return "skipped_existing"

    output_path = url_to_output_path(url, output_dir, strip_prefix)
    if skip_existing_output and output_path.exists():
        return "skipped_output"

    print(f"Parsing: {url}")
    resp = requests.get(url, timeout=30)
    resp.encoding = "utf-8"
    if resp.status_code != 200:
        print(f"HTTP {resp.status_code}: {url}")
        return "failed"

    state = extract_state(resp.text)
    if not state:
        print(f"No state payload: {url}")
        return "failed"

    title = state.get("data", {}).get("title") or "Без названия"
    html = state.get("data", {}).get("html") or ""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    current_dir = output_path.parent
    markdown = html_to_markdown(html, BASE_URL, output_dir, current_dir, images_dir, scope_prefix, strip_prefix, skip_roots)
    output_path.write_text(f"# {title}\n\n{markdown}\n", encoding="utf-8")

    inner = BeautifulSoup(html, "html.parser")
    for a in inner.find_all("a", href=True):
        href = a["href"]
        abs_url = urljoin(BASE_URL, href)
        parsed = urlparse(abs_url)
        if parsed.netloc == urlparse(BASE_URL).netloc and is_in_scope(parsed.path, scope_prefix):
            rel_md = url_to_rel_md_path(abs_url)
            if any((root / rel_md).exists() for root in skip_roots):
                continue
            abs_url = abs_url.split("#")[0]
            if abs_url not in visited:
                queue.append(abs_url)
    return "parsed"


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse apidocs.bitrix24.ru pages into Markdown.")
    parser.add_argument("--scope-prefix", default=DEFAULT_SCOPE_PREFIX, help="URL prefix to include (default: local-integrations/).")
    parser.add_argument("--output-dir", default="", help="Output directory (repo-relative or absolute).")
    parser.add_argument("--images-dir", default="", help="Images directory (repo-relative or absolute).")
    parser.add_argument("--sleep", type=float, default=SLEEP_S)
    parser.add_argument("--skip-existing-root", action="append", default=[], help="Skip if page exists under this root.")
    parser.add_argument("--skip-existing-output", action="store_true", help="Skip if output file already exists.")
    parser.add_argument("--strip-prefix", action="store_true", help="Strip scope prefix from output paths.")
    parser.add_argument("--no-strip-prefix", action="store_true", help="Keep full paths (override default strip behavior).")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    scope_prefix = normalize_prefix(args.scope_prefix)
    if args.no_strip_prefix:
        strip_prefix = ""
    elif args.strip_prefix or scope_prefix == DEFAULT_SCOPE_PREFIX:
        strip_prefix = scope_prefix
    else:
        strip_prefix = ""

    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = repo_root / output_dir
    elif scope_prefix == DEFAULT_SCOPE_PREFIX:
        output_dir = repo_root / "docs" / "bitrix24_api" / "local-integrations"
    else:
        output_dir = repo_root / "docs" / "bitrix24_api" / "apidocs"

    if args.images_dir:
        images_dir = Path(args.images_dir)
        if not images_dir.is_absolute():
            images_dir = repo_root / images_dir
    elif scope_prefix == DEFAULT_SCOPE_PREFIX:
        images_dir = repo_root / "images" / "bitrix24_api" / "local-integrations"
    else:
        images_dir = repo_root / "images" / "bitrix24_api" / "apidocs"

    skip_roots = []
    for root in args.skip_existing_root:
        root_path = Path(root)
        if not root_path.is_absolute():
            root_path = repo_root / root_path
        skip_roots.append(root_path)

    visited: set[str] = set()
    toc_links = load_toc_links(scope_prefix)
    if toc_links:
        queue = [urljoin(BASE_URL + "/", href) for href in toc_links]
    else:
        queue = [START_URL]

    counts = {
        "parsed": 0,
        "skipped_existing": 0,
        "skipped_output": 0,
        "skipped_seen": 0,
        "failed": 0,
    }

    while queue:
        url = queue.pop(0)
        status = parse_page(
            url,
            output_dir,
            images_dir,
            visited,
            queue,
            scope_prefix,
            strip_prefix,
            skip_roots,
            args.skip_existing_output,
        )
        counts[status] = counts.get(status, 0) + 1
        time.sleep(args.sleep)

    print("Done.")
    print(f"Parsed: {counts['parsed']}")
    print(f"Skipped (existing): {counts['skipped_existing']}")
    print(f"Skipped (output): {counts['skipped_output']}")
    print(f"Skipped (seen): {counts['skipped_seen']}")
    print(f"Failed: {counts['failed']}")


if __name__ == "__main__":
    main()
