#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vault maintenance utilities for this repo (VS Code / Obsidian).

What it does:
1) Generates `docs/INDEX.md` (section map for the vault).
2) Converts `/api_help/...` links to local relative links using `url_mapping.json`
   (only where the target file exists; otherwise removes the link, keeping text).
3) Converts other root-relative site links like `/learning/...` to full URLs on
   `https://dev.1c-bitrix.ru/...` so they don't look like broken local files.
4) Ensures folder navigation blocks exist on `index.md` / `index.php.md` pages
   that otherwise have no obvious way to reach sibling pages/subfolders.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
MD_LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r"""href=(['"])(.*?)\1""", re.IGNORECASE)

FOLDER_NAV_START = "<!-- vault-nav:start -->"
FOLDER_NAV_END = "<!-- vault-nav:end -->"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_h1(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    m = H1_RE.search(text)
    return m.group(1).strip() if m else None


def normalize_dev_url(raw: str) -> tuple[str, str]:
    raw = raw.strip()
    anchor = ""
    if "#" in raw:
        raw, anchor_part = raw.split("#", 1)
        anchor = f"#{anchor_part}"

    if raw.startswith("/api_help/"):
        raw = "https://dev.1c-bitrix.ru" + raw

    if not raw.startswith("http"):
        return raw, anchor

    parts = urlsplit(raw)
    if "1c-bitrix.ru" not in parts.netloc:
        return raw, anchor

    q = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k != "print"]
    query = urlencode(q) if q else ""
    cleaned = urlunsplit((parts.scheme, parts.netloc, parts.path, query, ""))
    return cleaned.rstrip("?&"), anchor


def is_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def fix_api_help_links(*, docs_dir: Path, mapping: dict[str, str]) -> dict[str, int]:
    exclude_roots = {
        docs_dir / "courses",
        docs_dir / "d7",
        docs_dir / "user_help",
        docs_dir / "bitrix24_api",
    }

    def excluded(p: Path) -> bool:
        return any(is_under(p, ex) for ex in exclude_roots)

    counts = {"changed_files": 0, "fixed_links": 0, "removed_links": 0}

    for md in docs_dir.rglob("*.md"):
        if excluded(md):
            continue

        text = md.read_text(encoding="utf-8", errors="replace")
        original = text

        def repl(m: re.Match[str]) -> str:
            label = m.group(1)
            url = m.group(2)

            normalized, anchor = normalize_dev_url(url)
            if not normalized.startswith(("https://dev.1c-bitrix.ru/api_help/", "http://dev.1c-bitrix.ru/api_help/")):
                return m.group(0)

            candidates = [normalized]
            if normalized.startswith("http://"):
                candidates.append("https://" + normalized[len("http://") :])

            mapped_rel = None
            for c in candidates:
                mapped_rel = mapping.get(c)
                if mapped_rel:
                    break

            if not mapped_rel:
                counts["removed_links"] += 1
                return label

            target = docs_dir / mapped_rel
            if not target.exists():
                counts["removed_links"] += 1
                return label

            rel = os.path.relpath(target, md.parent).replace("\\", "/")
            counts["fixed_links"] += 1
            return f"[{label}]({rel}{anchor})"

        text = MD_LINK_RE.sub(repl, text)

        if text != original:
            md.write_text(text, encoding="utf-8")
            counts["changed_files"] += 1

    return counts


def externalize_root_relative_links(*, docs_dir: Path) -> dict[str, int]:
    counts = {"changed_files": 0, "converted_links": 0}

    for md in docs_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        original = text

        def repl(m: re.Match[str]) -> str:
            label = m.group(1)
            url = m.group(2).strip()
            if not url.startswith("/"):
                return m.group(0)
            if url.startswith("/api_help/"):
                return m.group(0)
            counts["converted_links"] += 1
            return f"[{label}](https://dev.1c-bitrix.ru{url})"

        text = MD_LINK_RE.sub(repl, text)

        if text != original:
            md.write_text(text, encoding="utf-8")
            counts["changed_files"] += 1

    return counts


def _count_links(text: str) -> int:
    return len(MD_LINK_RE.findall(text)) + len(HTML_HREF_RE.findall(text))


def _count_local_links(text: str) -> int:
    """
    Counts links that look like *local* vault paths (relative, non-URL).
    Used to decide whether an index page already provides navigable local paths
    to its siblings/subfolders.
    """

    def is_local(url: str) -> bool:
        url = url.strip()
        if not url:
            return False
        if url.startswith(("#", "mailto:", "javascript:")):
            return False
        if url.startswith(("http://", "https://")):
            return False
        # Root-relative links are site paths, not local files.
        if url.startswith("/"):
            return False
        return True

    local = 0
    for _label, url in MD_LINK_RE.findall(text):
        if is_local(url):
            local += 1
    for _quote, url in HTML_HREF_RE.findall(text):
        if is_local(url):
            local += 1
    return local


def _nonempty_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())


def _folder_nav_children(index_path: Path) -> tuple[list[tuple[str, Path]], list[tuple[str, Path]]]:
    """
    Returns (subfolders, files) relative to index_path.parent.
    subfolders: list of (label, rel_target_path)
    files: list of (label, rel_target_path)
    """
    base = index_path.parent

    # Files in the same folder (exclude both index.md and index.php.md).
    files: list[tuple[str, Path]] = []
    for p in sorted(base.glob("*.md")):
        if p.name in {"index.md", "index.php.md"}:
            continue
        label = read_h1(p) or p.name
        files.append((label, Path("./") / p.name))

    # Subfolders that have an index file.
    subfolders: list[tuple[str, Path]] = []
    for d in sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: p.name):
        idx = d / "index.md"
        if not idx.exists():
            idx = d / "index.php.md"
        if not idx.exists():
            continue
        label = read_h1(idx) or d.name
        subfolders.append((label, Path("./") / d.name / idx.name))

    return subfolders, files


def _render_folder_nav(index_path: Path) -> str:
    subfolders, files = _folder_nav_children(index_path)
    if not subfolders and not files:
        return ""

    lines: list[str] = []
    lines.append(FOLDER_NAV_START)
    lines.append("## В этой папке")
    lines.append("")
    lines.append("<details>")
    lines.append("<summary>Показать файлы и папки</summary>")
    lines.append("")

    if subfolders:
        lines.append("### Папки")
        lines.append("")
        for label, rel in subfolders:
            rel_str = str(rel).replace("\\", "/").replace(" ", "%20")
            lines.append(f"- [{label}]({rel_str})")
        lines.append("")

    if files:
        lines.append("### Файлы")
        lines.append("")
        for label, rel in files:
            rel_str = str(rel).replace("\\", "/").replace(" ", "%20")
            lines.append(f"- [{label}]({rel_str})")
        lines.append("")

    lines.append("</details>")
    lines.append("")
    lines.append(FOLDER_NAV_END)
    lines.append("")
    return "\n".join(lines)


def ensure_folder_nav(*, docs_dir: Path) -> dict[str, int]:
    """
    Adds/replaces an autogenerated folder navigation block on index pages that
    are hard to navigate (few links / very short).
    """
    counts = {"changed_files": 0, "processed_indexes": 0}

    for idx in list(docs_dir.rglob("index.md")) + list(docs_dir.rglob("index.php.md")):
        # Course lessons have huge sibling counts; keep them curated.
        if is_under(idx, docs_dir / "courses"):
            continue

        text = idx.read_text(encoding="utf-8", errors="replace")
        counts["processed_indexes"] += 1

        subfolders, files = _folder_nav_children(idx)
        if not subfolders and not files:
            continue

        # Heuristics: if the page is already navigable, don't force a block.
        links = _count_links(text)
        local_links = _count_local_links(text)
        lines = _nonempty_lines(text)
        has_block = FOLDER_NAV_START in text and FOLDER_NAV_END in text
        # If the page already contains enough links AND at least some local
        # links, it is likely navigable without an autogenerated block.
        # External-only link lists are common in scraped Bitrix index pages and
        # are not helpful for offline navigation in the vault.
        if not has_block and local_links > 0 and links >= 3 and lines > 5:
            continue

        block = _render_folder_nav(idx)
        if not block:
            continue

        if has_block:
            start = text.find(FOLDER_NAV_START)
            end = text.find(FOLDER_NAV_END, start)
            if start == -1 or end == -1:
                continue
            end = end + len(FOLDER_NAV_END)
            new_text = text[:start].rstrip() + "\n\n" + block + text[end:].lstrip()
        else:
            new_text = text.rstrip() + "\n\n" + block

        if new_text != text:
            idx.write_text(new_text, encoding="utf-8")
            counts["changed_files"] += 1

    return counts


def generate_index(*, docs_dir: Path) -> None:
    exclude_top_dirs = {"courses", "d7", "user_help", "bitrix24_api"}

    entry_files = [
        docs_dir / "MAIN_INDEX.md",
        docs_dir / "api_documentation.md",
        docs_dir / "QUICK_REFERENCE.md",
        docs_dir / "MODULES.md",
        docs_dir / "courses" / "index.md",
        docs_dir / "d7" / "index.md",
        docs_dir / "user_help" / "index.md",
        docs_dir / "bitrix24_api" / "index.md",
    ]

    classic_modules: list[tuple[str, str, int]] = []
    for p in sorted([d for d in docs_dir.iterdir() if d.is_dir() and d.name not in exclude_top_dirs]):
        idx = p / "index.md"
        if not idx.exists():
            continue
        title = read_h1(idx) or p.name
        count = len(list(p.rglob("*.md")))
        classic_modules.append((p.name, title, count))

    d7_modules: list[tuple[str, str, int]] = []
    bitrix_d7 = docs_dir / "d7" / "bitrix"
    if bitrix_d7.exists():
        for p in sorted([d for d in bitrix_d7.iterdir() if d.is_dir()]):
            idx = p / "index.php.md"
            if not idx.exists():
                continue
            title = read_h1(idx) or p.name
            count = len(list(p.rglob("*.md")))
            d7_modules.append((p.name, title, count))

    user_help_sections: list[tuple[str, str, int]] = []
    user_help = docs_dir / "user_help"
    if user_help.exists():
        for p in sorted([d for d in user_help.iterdir() if d.is_dir()]):
            idx = p / "index.php.md"
            if not idx.exists():
                continue
            title = read_h1(idx) or p.name
            count = len(list(p.rglob("*.md")))
            user_help_sections.append((p.name, title, count))

    courses: list[tuple[str, str, int]] = []
    courses_dir = docs_dir / "courses"
    if courses_dir.exists():
        for p in sorted([d for d in courses_dir.iterdir() if d.is_dir() and d.name.startswith("course_")]):
            idx = p / "index.md"
            if not idx.exists():
                continue
            title = read_h1(idx) or p.name
            lessons = len(list(p.glob("lesson_*.md")))
            courses.append((p.name, title, lessons))

    bitrix24_sections: list[tuple[str, str, int]] = []
    b24_repo_root = docs_dir / "bitrix24_api" / "b24-rest-docs"
    if b24_repo_root.exists():
        for p in sorted([d for d in b24_repo_root.iterdir() if d.is_dir()]):
            idx = p / "index.md"
            if not idx.exists():
                continue
            title = read_h1(idx) or p.name
            count = len(list(p.rglob("*.md")))
            bitrix24_sections.append((p.name, title, count))

    out: list[str] = []
    out.append("# Индекс разделов (справочно)")
    out.append("")
    out.append(
        "Этот файл — справочная «карта» разделов/модулей. Начинайте с **[MAIN_INDEX.md](./MAIN_INDEX.md)** — это единая навигационная страница (роли/задачи)."
    )
    out.append("")
    out.append("> Примечание: индекс генерируется скриптом `scripts/vault_maintenance.py`.")
    out.append("")
    out.append("## Старт")
    out.append("")
    out.append("- [MAIN_INDEX.md — единая точка входа](./MAIN_INDEX.md)")
    out.append("")
    out.append("## Справочные страницы")
    out.append("")
    for f in entry_files:
        if f.name == "MAIN_INDEX.md":
            continue
        if not f.exists():
            continue
        title = read_h1(f) or f.stem
        rel = f.relative_to(docs_dir)
        rel_str = str(rel).replace("\\", "/")
        out.append(f"- [{title}](./{rel_str})")

    out.append("")
    out.append("## Классическое API (modules)")
    out.append("")
    for name, title, count in classic_modules:
        out.append(f"- [{title}](./{name}/index.md) — {count} стр.")

    out.append("")
    out.append("## API D7 (namespaces)")
    out.append("")
    d7_total = len(list((docs_dir / 'd7').rglob('*.md')))
    out.append(f"- [API D7 (современное)](./d7/index.md) — {d7_total} стр.")
    out.append("")
    out.append("<details>")
    out.append("<summary>Модули D7 (Bitrix\\\\*)</summary>")
    out.append("")
    for name, title, count in d7_modules:
        out.append(f"- [{title}](./d7/bitrix/{name}/index.php.md) — {count} стр.")
    out.append("")
    out.append("</details>")

    out.append("")
    out.append("## Пользовательская документация")
    out.append("")
    user_help_total = len(list((docs_dir / 'user_help').rglob('*.md')))
    out.append(f"- [Пользовательская документация](./user_help/index.md) — {user_help_total} стр.")
    out.append("")
    out.append("<details>")
    out.append("<summary>Разделы user_help</summary>")
    out.append("")
    for name, title, count in user_help_sections:
        out.append(f"- [{title}](./user_help/{name}/index.php.md) — {count} стр.")
    out.append("")
    out.append("</details>")

    out.append("")
    out.append("## Учебные курсы")
    out.append("")
    courses_total = len(list((docs_dir / 'courses').rglob('*.md')))
    out.append(f"- [Учебные курсы](./courses/index.md) — {courses_total} файлов")
    out.append("")
    for name, title, lessons in courses:
        out.append(f"- [{title}](./courses/{name}/index.md) — {lessons} уроков")

    out.append("")
    out.append("## Bitrix24 REST API")
    out.append("")
    bitrix24_total = len(list((docs_dir / "bitrix24_api").rglob("*.md")))
    out.append(f"- [Bitrix24 REST API](./bitrix24_api/index.md) — {bitrix24_total} стр.")

    if (docs_dir / "bitrix24_api" / "b24-rest-docs" / "index.md").exists():
        out.append("")
        out.append("<details>")
        out.append("<summary>Разделы Bitrix24 REST (b24-rest-docs)</summary>")
        out.append("")
        out.append("- [Оглавление](./bitrix24_api/b24-rest-docs/index.md)")
        for name, title, count in bitrix24_sections:
            out.append(f"- [{title}](./bitrix24_api/b24-rest-docs/{name}/index.md) — {count} стр.")
        out.append("")
        out.append("</details>")

    out.append("")
    out.append("---")
    out.append("")
    total = len(list(docs_dir.rglob('*.md')))
    out.append(f"Сгенерировано автоматически. Всего Markdown‑файлов в `docs/`: **{total}**.")
    out.append("")

    (docs_dir / "INDEX.md").write_text("\n".join(out), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index-only", action="store_true", help="Only regenerate docs/INDEX.md")
    parser.add_argument("--links-only", action="store_true", help="Only fix/externalize links")
    parser.add_argument("--nav-only", action="store_true", help="Only (re)build folder navigation blocks on index pages")
    args = parser.parse_args()

    root = repo_root()
    docs_dir = root / "docs"

    mapping_path = root / "url_mapping.json"
    mapping = json.loads(mapping_path.read_text(encoding="utf-8")) if mapping_path.exists() else {}

    if args.nav_only:
        stats = ensure_folder_nav(docs_dir=docs_dir)
        print(f"[folder-nav] processed_indexes={stats['processed_indexes']} changed_files={stats['changed_files']}")
        return 0

    if not args.index_only:
        if mapping:
            stats = fix_api_help_links(docs_dir=docs_dir, mapping=mapping)
            print(f"[api_help] changed_files={stats['changed_files']} fixed_links={stats['fixed_links']} removed_links={stats['removed_links']}")
        stats = externalize_root_relative_links(docs_dir=docs_dir)
        print(f"[root-links] changed_files={stats['changed_files']} converted_links={stats['converted_links']}")
        stats = ensure_folder_nav(docs_dir=docs_dir)
        print(f"[folder-nav] processed_indexes={stats['processed_indexes']} changed_files={stats['changed_files']}")

    if not args.links_only:
        generate_index(docs_dir=docs_dir)
        print("[index] wrote docs/INDEX.md")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
