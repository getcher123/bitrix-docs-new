#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Normalizes `*.php.md` pages for a Markdown-vault (VS Code / Obsidian).

Goals:
- Convert leftover HTML fragments to readable Markdown.
- Download external images into `./images/<scope>/...` and rewrite links to local relative paths.

Scopes:
- `docs/d7/**/*.php.md`      -> images in `images/d7/`
- `docs/user_help/**/*.php.md` -> images in `images/user_help/`
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import time
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen


BASE_URL = "https://dev.1c-bitrix.ru"

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
HTML_TOKEN_RE = re.compile(r"</?[a-zA-Z][^>\n]*>")
HTML_CONTENT_TAG_RE = re.compile(
    r"</?(?:p|div|table|thead|tbody|tr|td|th|ul|ol|li|pre|img|h[1-6]|blockquote|section|article|main|header|footer|nav)\b",
    re.I,
)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
BR_TAG_RE = re.compile(r"<br\s*/?>", re.I)

FOLDER_NAV_START = "<!-- vault-nav:start -->"
FOLDER_NAV_END = "<!-- vault-nav:end -->"

MD_IMAGE_RE = re.compile(r"!\[")  # marker only; actual parsing is done manually


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_dev_url(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        return raw
    if raw.startswith("/"):
        return BASE_URL + raw
    if raw.startswith("//"):
        return "https:" + raw
    return raw


def strip_autogen_nav_block(text: str) -> tuple[str, str]:
    if FOLDER_NAV_START not in text or FOLDER_NAV_END not in text:
        return text, ""
    start = text.find(FOLDER_NAV_START)
    end = text.find(FOLDER_NAV_END, start)
    if start == -1 or end == -1:
        return text, ""
    end = end + len(FOLDER_NAV_END)
    nav = text[start:end].strip() + "\n"
    rest = (text[:start] + text[end:]).rstrip() + "\n"
    return rest, nav


def split_header_and_body(text: str) -> tuple[str, str, str]:
    """
    Returns (h1_line, source_line_or_empty, body_text).
    Keeps the original H1 as-is. If there is no H1, uses '# <filename>'.
    """
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    # Find H1.
    h1_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            h1_idx = i
            break

    if h1_idx is None:
        h1 = "# Документация"
        start_idx = 0
    else:
        h1 = lines[h1_idx].rstrip()
        start_idx = h1_idx + 1

    # Find "Источник:" after H1.
    source = ""
    body_start = start_idx
    for i in range(start_idx, min(len(lines), start_idx + 20)):
        if lines[i].startswith("Источник:"):
            source = lines[i].rstrip()
            body_start = i + 1
            break

    # Skip blank lines after header.
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1

    body = "\n".join(lines[body_start:]).strip() + "\n" if body_start < len(lines) else ""
    return h1, source, body


def strip_fenced_code_blocks(text: str) -> str:
    """
    Removes fenced code blocks (```...```) from markdown text.
    Used only for heuristics to avoid treating HTML examples inside code as real HTML.
    """
    out_lines: list[str] = []
    in_fence = False
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out_lines.append(line)
    return "\n".join(out_lines)


def should_convert_html(body: str) -> bool:
    """
    Returns True if the body looks like an unconverted HTML fragment.
    Avoids reconverting already-normalized Markdown that contains HTML-like examples
    inside code fences or inline code.
    """
    probe = strip_fenced_code_blocks(body)
    probe = INLINE_CODE_RE.sub("", probe)
    return bool(HTML_CONTENT_TAG_RE.search(probe))


def normalize_br_runs(text: str) -> str:
    # Collapse repeated <br> runs (often produced by HTML-to-table conversion).
    return re.sub(r"(?:<br\s*/?>\s*){2,}", "<br>", text, flags=re.I)

def escape_html_tokens_outside_code(text: str) -> str:
    """
    Escapes leftover HTML tag tokens in Markdown so they render as text,
    while preserving <br> for table cell line breaks.
    """

    def escape_segment(seg: str) -> str:
        seg = normalize_br_runs(seg)

        def repl(m: re.Match[str]) -> str:
            tok = m.group(0)
            low = tok.lower()
            if low.startswith("<br") or low.startswith("</br"):
                return tok

            inner = tok[1:-1].strip().lower()
            if inner.startswith(("http://", "https://", "mailto:")):
                return tok

            return tok.replace("<", "&lt;").replace(">", "&gt;")

        return HTML_TOKEN_RE.sub(repl, seg)

    out_lines: list[str] = []
    in_fence = False
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence or "`" not in line:
            out_lines.append(escape_segment(line) if not in_fence else line)
            continue

        parts = re.split(r"(`[^`]*`)", line)
        for idx, part in enumerate(parts):
            if idx % 2 == 0:
                parts[idx] = escape_segment(part)
        out_lines.append("".join(parts))

    return "\n".join(out_lines)


@dataclass
class Node:
    tag: str | None
    attrs: dict[str, str]
    children: list["Node"]
    text: str = ""


class _HtmlTreeBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node(tag="root", attrs={}, children=[])
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs_dict = {k.lower(): (v or "") for k, v in attrs}
        node = Node(tag=tag, attrs=attrs_dict, children=[])
        self.stack[-1].children.append(node)

        if tag in {"br", "img", "hr", "meta", "link", "input"}:
            return
        self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                return

    def handle_data(self, data: str) -> None:
        if not data:
            return
        self.stack[-1].children.append(Node(tag=None, attrs={}, children=[], text=data))

    def handle_comment(self, data: str) -> None:
        # Preserve vault nav markers and similar comments; drop noisy separators later.
        self.stack[-1].children.append(Node(tag="comment", attrs={}, children=[], text=data))


def _attrs_class(node: Node) -> set[str]:
    raw = node.attrs.get("class", "")
    return {c for c in re.split(r"\s+", raw.strip()) if c}


def _text_of(node: Node, *, preserve_ws: bool) -> str:
    if node.tag is None:
        return node.text
    if node.tag == "comment":
        return ""
    parts: list[str] = []
    for ch in node.children:
        parts.append(_text_of(ch, preserve_ws=preserve_ws))
    out = "".join(parts)
    if preserve_ws:
        return out
    # HTML-ish whitespace normalization.
    out = out.replace("\xa0", " ")
    out = re.sub(r"\s+", " ", out)
    return out


@dataclass
class RenderContext:
    list_level: int = 0


def _escape_table_cell(text: str) -> str:
    text = text.replace("|", "\\|")
    text = text.replace("\n", "<br>")
    return text.strip()


def _render_children(nodes: list[Node], ctx: RenderContext) -> str:
    return "".join(_render_node(ch, ctx) for ch in nodes)


def _render_inline(node: Node, ctx: RenderContext) -> str:
    rendered = _render_node(node, ctx)
    rendered = rendered.replace("\xa0", " ")
    rendered = re.sub(r"\s+", " ", rendered)
    return rendered.strip()


def _render_list(node: Node, ctx: RenderContext, *, ordered: bool) -> str:
    items = [ch for ch in node.children if ch.tag == "li"]
    if not items:
        return ""

    out_lines: list[str] = []
    index = 1
    indent = "  " * ctx.list_level

    for li in items:
        # Split li children into inline + nested lists.
        nested_lists = [c for c in li.children if c.tag in {"ul", "ol"}]
        inline_nodes = [c for c in li.children if c.tag not in {"ul", "ol"}]

        inline_text = _render_children(inline_nodes, ctx).strip()
        inline_text = re.sub(r"\n{2,}", "\n", inline_text).strip()
        inline_text = re.sub(r"\s+\n", "\n", inline_text)

        prefix = f"{index}. " if ordered else "- "
        first = inline_text.splitlines()[0] if inline_text else ""
        out_lines.append(f"{indent}{prefix}{first}".rstrip())

        # Continuation lines of the same list item.
        for cont in inline_text.splitlines()[1:]:
            out_lines.append(f"{indent}  {cont}".rstrip())

        # Nested lists (increase indentation).
        for nl in nested_lists:
            out_lines.append(_render_node(nl, RenderContext(list_level=ctx.list_level + 1)).rstrip())

        index += 1

    return "\n".join(out_lines).rstrip() + "\n"


def _render_table_learning_spoiler(node: Node, ctx: RenderContext) -> str:
    # Header (year) lives in thead/div.
    year = ""
    theads = [c for c in node.children if c.tag == "thead"]
    if theads:
        year = _text_of(theads[0], preserve_ws=False).strip()
    year = year or "Раздел"

    tbodies = [c for c in node.children if c.tag == "tbody"]
    body_md = ""
    if tbodies:
        body_md = _render_children(tbodies[0].children, ctx).strip()

    if not body_md:
        return ""

    return f"\n\n## {year}\n\n{body_md}\n\n"


def _render_table(node: Node, ctx: RenderContext) -> str:
    classes = _attrs_class(node)
    if "learning-spoiler" in classes:
        return _render_table_learning_spoiler(node, ctx)

    # Collect rows.
    rows: list[list[str]] = []
    header_row: list[str] | None = None

    def iter_tr(n: Node) -> Iterable[Node]:
        for ch in n.children:
            if ch.tag == "tr":
                yield ch
            else:
                yield from iter_tr(ch)

    for tr in iter_tr(node):
        cells = [c for c in tr.children if c.tag in {"td", "th"}]
        if not cells:
            continue
        row: list[str] = []
        has_th = any(c.tag == "th" for c in cells)
        for c in cells:
            cell_txt = _render_children(c.children, ctx).strip()
            cell_txt = re.sub(r"\n{3,}", "\n\n", cell_txt)
            cell_txt = _escape_table_cell(cell_txt)
            row.append(cell_txt)
        if header_row is None and has_th:
            header_row = row
        else:
            rows.append(row)

    if header_row is None and rows:
        header_row, rows = rows[0], rows[1:]

    if not header_row:
        return ""

    col_count = max(len(header_row), *(len(r) for r in rows)) if rows else len(header_row)
    header_row = header_row + [""] * (col_count - len(header_row))
    rows = [r + [""] * (col_count - len(r)) for r in rows]

    out: list[str] = []
    out.append("| " + " | ".join(header_row) + " |")
    out.append("| " + " | ".join(["---"] * col_count) + " |")
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    out.append("")
    return "\n".join(out)


def _render_node(node: Node, ctx: RenderContext) -> str:
    if node.tag is None:
        text = node.text.replace("\xa0", " ")
        # Do not emit raw tag-looking tokens into Markdown (prevents accidental HTML).
        text = text.replace("<", "&lt;").replace(">", "&gt;")
        return text

    if node.tag == "comment":
        # Keep meaningful comments; drop obvious separators like <!------->.
        raw = node.text.strip()
        if not raw or set(raw) == {"-"}:
            return ""
        return f"<!-- {raw} -->\n"

    tag = node.tag
    classes = _attrs_class(node)

    # Drop non-content tags.
    if tag in {"script", "style", "noscript"}:
        return ""

    if tag == "br":
        return "\n"

    if tag == "hr":
        return "\n\n---\n\n"

    if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(tag[1])
        # Avoid generating a second H1; demote to H2.
        if level == 1:
            level = 2
        text = _text_of(node, preserve_ws=False).strip()
        if not text:
            return ""
        return f"\n\n{'#' * level} {text}\n\n"

    if tag in {"b", "strong"}:
        inner = _render_children(node.children, ctx).strip()
        return f"**{inner}**" if inner else ""

    if tag in {"i", "em"}:
        inner = _render_children(node.children, ctx).strip()
        return f"*{inner}*" if inner else ""

    if tag == "code":
        inner = _text_of(node, preserve_ws=True)
        inner = inner.replace("\xa0", " ").strip()
        if not inner:
            return ""
        inner = inner.replace("`", "\\`")
        return f"`{inner}`"

    if tag == "pre":
        inner = _text_of(node, preserve_ws=True)
        inner = inner.replace("\xa0", " ").strip("\n")
        if not inner.strip():
            return ""
        return f"\n\n```\n{inner}\n```\n\n"

    if tag == "a":
        href = node.attrs.get("href", "").strip()
        text = _render_children(node.children, ctx)
        text = re.sub(r"\s+", " ", text).strip()
        if not text and href:
            text = href
        if not text:
            return ""
        if not href or href.startswith(("javascript:", "mailto:")):
            return text
        return f"[{text}]({href})"

    if tag == "img":
        src = node.attrs.get("src", "").strip()
        alt = node.attrs.get("alt", "").strip()
        if not src:
            return ""
        return f"![{alt}]({src})"

    if tag == "ul":
        return "\n" + _render_list(node, ctx, ordered=False) + "\n"

    if tag == "ol":
        return "\n" + _render_list(node, ctx, ordered=True) + "\n"

    if tag == "li":
        # Handled by parent list.
        return _render_children(node.children, ctx)

    if tag == "table":
        return "\n\n" + _render_table(node, ctx) + "\n"

    if tag in {"thead", "tbody", "tr", "td", "th"}:
        return _render_children(node.children, ctx)

    # Notes from Bitrix docs.
    if "note" in classes:
        inner = _render_children(node.children, ctx).strip()
        if not inner:
            return ""
        lines = ["> " + l if l.strip() else ">" for l in inner.splitlines()]
        return "\n\n" + "\n".join(lines).rstrip() + "\n\n"

    # Generic containers: treat block tags as paragraphs.
    block_tags = {
        "p",
        "div",
        "section",
        "article",
        "main",
        "header",
        "footer",
        "nav",
        "blockquote",
    }
    inner = _render_children(node.children, ctx)

    if tag in block_tags:
        inner = inner.strip()
        if not inner:
            return ""
        return "\n\n" + inner + "\n\n"

    # Inline / unknown tags: keep content.
    return inner


def html_fragment_to_markdown(fragment: str) -> str:
    builder = _HtmlTreeBuilder()
    # Wrap as a div to make fragments parse as a single tree.
    builder.feed("<div>" + fragment + "</div>")
    md = _render_children(builder.root.children, RenderContext())

    # Normalize excessive whitespace.
    md = md.replace("\xa0", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip() + "\n"
    return md


def rewrite_markdown_images(text: str, *, repl) -> str:
    """
    Rewrites markdown image URLs robustly (URLs may contain parentheses).
    Supports: ![alt](url) and ![alt](url "title").
    """
    i = 0
    out: list[str] = []
    n = len(text)

    while True:
        start = text.find("![", i)
        if start == -1:
            out.append(text[i:])
            break

        mid = text.find("](", start + 2)
        if mid == -1:
            out.append(text[i:])
            break

        out.append(text[i:start])
        alt = text[start + 2 : mid]

        # Parse (...) with balanced parentheses in URL.
        j = mid + 2
        depth = 0
        while j < n:
            ch = text[j]
            if ch == "\\":
                j += 2
                continue
            if ch == "(":
                depth += 1
                j += 1
                continue
            if ch == ")":
                if depth == 0:
                    break
                depth -= 1
                j += 1
                continue
            j += 1

        if j >= n:
            out.append(text[start:])
            break

        inside = text[mid + 2 : j].strip()

        # Support angle-bracket wrapped URLs.
        if inside.startswith("<") and ">" in inside:
            close = inside.find(">")
            url_part = inside[1:close].strip()
            rest = inside[close + 1 :].strip()
        else:
            parts = inside.split(None, 1)
            url_part = parts[0] if parts else ""
            rest = parts[1] if len(parts) > 1 else ""

        new_url_part = repl(alt, url_part, rest)
        if rest and not rest.startswith(("\"", "'")):
            # Keep any unknown suffix verbatim.
            new_inside = f"{new_url_part} {rest}".strip()
        else:
            new_inside = f"{new_url_part}{(' ' + rest) if rest else ''}".strip()

        out.append(f"![{alt}]({new_inside})")
        i = j + 1

    return "".join(out)


def _safe_segment(seg: str) -> str:
    seg = seg.strip().strip(".")
    seg = re.sub(r"[^0-9A-Za-zА-Яа-я._-]+", "_", seg)
    seg = re.sub(r"_+", "_", seg)
    return seg[:200] or "_"


def _guess_ext_from_content_type(ct: str) -> str:
    ct = (ct or "").split(";", 1)[0].strip().lower()
    return {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/gif": ".gif",
        "image/svg+xml": ".svg",
        "image/webp": ".webp",
    }.get(ct, "")


@dataclass
class ImageResult:
    url: str
    local_path: Path | None
    error: str | None = None


def download_image(url: str, *, scope: str, images_root: Path, sleep_sec: float, timeout_sec: float) -> ImageResult:
    url = normalize_dev_url(url)
    if not url.startswith(("http://", "https://")):
        return ImageResult(url=url, local_path=None, error="not_http_url")

    parts = urlsplit(url)
    netloc = _safe_segment(parts.netloc)
    path = parts.path or ""
    path_parts = [p for p in path.split("/") if p]
    if not path_parts:
        path_parts = ["image"]

    filename = _safe_segment(path_parts[-1])
    ext = Path(filename).suffix
    stem = filename[: -len(ext)] if ext else filename

    # If query exists, add a hash suffix to avoid collisions.
    if parts.query:
        digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
        filename = f"{stem}_{digest}{ext}" if ext else f"{stem}_{digest}"

    rel_dir = Path(scope) / netloc / Path(*[_safe_segment(p) for p in path_parts[:-1]])
    dest = images_root / rel_dir / filename

    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        return ImageResult(url=url, local_path=dest)

    req = Request(
        urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, "")),
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
            "Accept-Language": "ru,en;q=0.8",
        },
    )
    try:
        with urlopen(req, timeout=timeout_sec) as resp:
            data = resp.read()
            content_type = resp.headers.get("Content-Type", "")

        if not ext:
            guessed = _guess_ext_from_content_type(content_type)
            if guessed:
                dest = dest.with_suffix(guessed)

        dest.write_bytes(data)
        if sleep_sec:
            time.sleep(sleep_sec)
        return ImageResult(url=url, local_path=dest)
    except Exception as e:
        return ImageResult(url=url, local_path=None, error=str(e))


def relpath(from_file: Path, to_path: Path) -> str:
    rel = os.path.relpath(to_path, from_file.parent).replace("\\", "/")
    return rel.replace(" ", "%20")


@dataclass
class Stats:
    processed: int = 0
    changed_files: int = 0
    converted_files: int = 0
    downloaded_images: int = 0
    rewritten_image_links: int = 0
    failed_images: int = 0


def iter_php_md_files(docs_dir: Path, *, scopes: set[str]) -> Iterable[tuple[str, Path]]:
    if "d7" in scopes:
        for p in sorted((docs_dir / "d7").rglob("*.php.md")):
            yield "d7", p
    if "user_help" in scopes:
        for p in sorted((docs_dir / "user_help").rglob("*.php.md")):
            yield "user_help", p


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scopes", default="d7,user_help", help="Comma-separated scopes: d7,user_help")
    parser.add_argument(
        "--only",
        default="",
        help="Optional substring filter (process only paths containing this string).",
    )
    parser.add_argument("--max-files", type=int, default=0, help="Limit processed files (0 = no limit).")
    parser.add_argument("--sleep", type=float, default=0.05, help="Sleep seconds between image downloads.")
    parser.add_argument("--timeout", type=float, default=40.0, help="HTTP timeout per image, seconds.")
    args = parser.parse_args()

    root = repo_root()
    docs_dir = root / "docs"
    images_root = root / "images"

    scopes = {s.strip() for s in args.scopes.split(",") if s.strip()}
    stats = Stats()

    img_cache: dict[str, Path] = {}

    files = list(iter_php_md_files(docs_dir, scopes=scopes))
    if args.only:
        needle = args.only.replace("\\", "/")
        files = [(s, p) for s, p in files if needle in p.as_posix()]
    if args.max_files and args.max_files > 0:
        files = files[: args.max_files]

    for scope, path in files:
        stats.processed += 1
        original = path.read_text(encoding="utf-8", errors="replace")
        text = original.replace("\r\n", "\n").replace("\r", "\n")

        # Keep vault-nav block intact.
        text_wo_nav, nav_block = strip_autogen_nav_block(text)

        h1, source, body = split_header_and_body(text_wo_nav)
        body_md = body

        converted = False
        if body and should_convert_html(body):
            body_md = html_fragment_to_markdown(body)
            converted = True
        if body_md:
            body_md = escape_html_tokens_outside_code(body_md)

        # Reassemble.
        out_parts: list[str] = [h1.strip(), ""]
        if source:
            out_parts.append(source.strip())
            out_parts.append("")
        if body_md.strip():
            out_parts.append(body_md.strip())
            out_parts.append("")
        if nav_block.strip():
            out_parts.append(nav_block.strip())
            out_parts.append("")

        out = "\n".join(out_parts).rstrip() + "\n"

        # Download and rewrite images.
        def img_repl(alt: str, url_part: str, rest: str) -> str:
            normalized = normalize_dev_url(url_part)
            if not normalized.startswith(("http://", "https://")):
                return url_part

            cached = img_cache.get(normalized)
            if cached and cached.exists():
                stats.rewritten_image_links += 1
                return relpath(path, cached)

            res = download_image(
                normalized,
                scope=scope,
                images_root=images_root,
                sleep_sec=args.sleep,
                timeout_sec=args.timeout,
            )
            if not res.local_path:
                stats.failed_images += 1
                return url_part

            img_cache[normalized] = res.local_path
            stats.downloaded_images += 1
            stats.rewritten_image_links += 1
            return relpath(path, res.local_path)

        out2 = out
        if MD_IMAGE_RE.search(out):
            out2 = rewrite_markdown_images(out, repl=img_repl)

        if out2 != original:
            path.write_text(out2, encoding="utf-8")
            stats.changed_files += 1
            if converted:
                stats.converted_files += 1

    print(
        "[normalize-php-md] "
        f"processed={stats.processed} changed_files={stats.changed_files} converted_files={stats.converted_files} "
        f"downloaded_images={stats.downloaded_images} rewritten_image_links={stats.rewritten_image_links} "
        f"failed_images={stats.failed_images}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
