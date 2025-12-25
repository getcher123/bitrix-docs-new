#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parses Bitrix learning courses from dev.1c-bitrix.ru into this Markdown vault.

Use-cases:
- Fill empty/placeholder lesson pages (e.g. COURSE_ID=48 and 57).
- Parse additional courses into `docs/courses/`.
- Convert lesson HTML to Markdown, download external images into `./images`,
  rewrite links to local images, and rebuild navigation.

Stdlib-only (no requests/bs4/pandoc).
"""

from __future__ import annotations

import argparse
import re
import time
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

from normalize_php_md import (
    BASE_URL,
    download_image,
    escape_html_tokens_outside_code,
    html_fragment_to_markdown,
    normalize_dev_url,
    relpath,
    rewrite_markdown_images,
)
from refetch_empty_php_md import extract_div_inner_by_id


TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
OG_TITLE_RE = re.compile(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', re.I)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
MD_LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r"""href=(['"])(.*?)\1""", re.I)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def fetch_html(url: str, *, timeout_sec: float) -> str:
    last_err: Exception | None = None
    for attempt in range(3):
        try:
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
        except Exception as e:
            last_err = e
            if attempt < 2:
                time.sleep(0.5 * (2**attempt))
                continue
            raise

    # Unreachable, but keeps type-checkers happy.
    raise RuntimeError(str(last_err))


def _strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html)


def extract_page_title(html: str) -> str | None:
    m = OG_TITLE_RE.search(html)
    if m:
        return unescape(m.group(1)).strip() or None
    m = TITLE_RE.search(html)
    if m:
        return unescape(_strip_tags(m.group(1))).strip() or None
    return None


def add_or_replace_query(url: str, **params: str) -> str:
    parts = urlsplit(url)
    q = dict(parse_qsl(parts.query, keep_blank_values=True))
    q.update({k: v for k, v in params.items() if v is not None})
    query = urlencode(q, doseq=True)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


def normalize_learning_url(raw: str, *, base_url: str) -> str:
    raw = raw.strip()
    if not raw:
        return raw
    if raw.startswith("/"):
        return base_url + raw
    if raw.startswith("//"):
        return "https:" + raw
    return raw


def is_effectively_empty_lesson(text: str) -> bool:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Drop H1.
    text_wo_h1 = H1_RE.sub("", text, count=1).strip()
    if not text_wo_h1:
        return True
    compact = "\n".join(line.strip() for line in text_wo_h1.splitlines() if line.strip())
    return len(compact) < 80


def _q(url: str) -> dict[str, str]:
    parts = urlsplit(url)
    return dict(parse_qsl(parts.query, keep_blank_values=True))


def course_id_from_url(url: str) -> str | None:
    return _q(url).get("COURSE_ID") or None


def lesson_id_from_url(url: str) -> str | None:
    return _q(url).get("LESSON_ID") or None


def iter_lesson_urls_from_course_page(html: str, *, course_id: str) -> list[str]:
    """
    Course pages often embed LESSON_IDs outside of <a href="..."> (e.g. in JS).
    We treat any occurrence of `LESSON_ID=<digits>` as a lesson reference.
    """
    out: list[str] = []
    seen: set[str] = set()

    for m in re.finditer(r"LESSON_ID=(\d+)", html):
        lid = m.group(1)
        url = f"{BASE_URL}/learning/course/index.php?COURSE_ID={course_id}&LESSON_ID={lid}"
        if url in seen:
            continue
        seen.add(url)
        out.append(url)

    return out


def slugify_title(title: str) -> str:
    title = title.strip().lower()
    title = re.sub(r"\s+", "_", title)
    title = re.sub(r"[^0-9a-zа-я._-]+", "_", title, flags=re.I)
    title = re.sub(r"_+", "_", title).strip("._")
    return title[:120] or "course"


def find_or_create_course_dir(*, docs_courses_dir: Path, course_id: str, course_title: str) -> Path:
    existing = sorted([p for p in docs_courses_dir.iterdir() if p.is_dir() and p.name.startswith(f"course_{course_id}_")])
    if existing:
        return existing[0]
    return docs_courses_dir / f"course_{course_id}_{slugify_title(course_title)}"


def rewrite_learning_links_to_local(md: str, *, lesson_id_to_file: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        label = m.group(1)
        url = m.group(2).strip()
        if not url or url.startswith(("#", "mailto:", "javascript:")):
            return m.group(0)

        abs_url = normalize_learning_url(url, base_url=BASE_URL)
        if not abs_url.startswith(("http://", "https://")):
            return m.group(0)

        parts = urlsplit(abs_url)
        if "1c-bitrix.ru" not in parts.netloc:
            return m.group(0)

        q = dict(parse_qsl(parts.query, keep_blank_values=True))
        lid = q.get("LESSON_ID")
        if not lid:
            return m.group(0)

        target = lesson_id_to_file.get(str(lid))
        if not target:
            return m.group(0)

        anchor = f"#{parts.fragment}" if parts.fragment else ""
        return f"[{label}]({target}{anchor})"

    return MD_LINK_RE.sub(repl, md)


def render_lesson_nav(
    *,
    prev_id: str | None,
    prev_title: str | None,
    next_id: str | None,
    next_title: str | None,
) -> str:
    lines: list[str] = []
    lines.append("**Навигация**")
    lines.append("- [← Оглавление курса](index.md)")
    if prev_id:
        label = f"{prev_id} — {prev_title}" if prev_title else prev_id
        lines.append(f"- [← Предыдущий: {label}](lesson_{prev_id}.md)")
    if next_id:
        label = f"{next_id} — {next_title}" if next_title else next_id
        lines.append(f"- [Следующий: {label} →](lesson_{next_id}.md)")
    return "\n".join(lines).strip()


def remove_html_comments_outside_fences(text: str) -> str:
    """
    Drops HTML comments like <!-- ... --> outside fenced code blocks.
    Helps to remove parser-noise from Bitrix learning pages.
    """
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    in_fence = False
    in_comment = False

    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        s = line
        while True:
            if in_comment:
                end = s.find("-->")
                if end == -1:
                    s = ""
                    break
                s = s[end + 3 :]
                in_comment = False
                continue

            start = s.find("<!--")
            if start == -1:
                break
            end = s.find("-->", start + 4)
            if end == -1:
                s = s[:start]
                in_comment = True
                break
            s = s[:start] + s[end + 3 :]

        out.append(s)

    # Trim extra blank lines introduced by removals.
    joined = "\n".join(out)
    joined = re.sub(r"\n{3,}", "\n\n", joined)
    return joined


def write_course_index(*, course_dir: Path, course_id: str, course_title: str, lesson_ids: list[str], lesson_titles: dict[str, str]) -> None:
    lessons_count = len(lesson_ids)
    lines: list[str] = []
    lines.append(f"# {course_title}".strip())
    lines.append("")
    lines.append(f"Официальная страница курса: https://dev.1c-bitrix.ru/learning/course/?COURSE_ID={course_id}")
    lines.append("")
    lines.append("Курс выгружен локально в Markdown‑vault. Если какие-то страницы отображаются некорректно — используйте официальный источник.")
    lines.append("")
    lines.append(f"## Оглавление ({lessons_count} уроков)")
    lines.append("")
    lines.append("<details>")
    lines.append("<summary>Показать список уроков</summary>")
    lines.append("")
    for lid in lesson_ids:
        title = lesson_titles.get(lid, f"Урок {lid}")
        lines.append(f"- [{lid} — {title}](lesson_{lid}.md)")
    lines.append("")
    lines.append("</details>")
    lines.append("")
    (course_dir / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def update_lesson_nav_in_file(
    *,
    path: Path,
    nav_md: str,
) -> None:
    text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    if not lines:
        return
    if not lines[0].startswith("# "):
        return

    # Find existing nav block start.
    nav_start = None
    for i in range(1, min(len(lines), 60)):
        if lines[i].strip() == "**Навигация**":
            nav_start = i
            break

    if nav_start is None:
        # Insert after H1 and first blank line.
        out = [lines[0].rstrip(), "", nav_md.strip(), ""] + lines[1:]
        path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
        return

    # Remove old nav block until the first blank line after it.
    j = nav_start
    while j < len(lines) and lines[j].strip():
        j += 1
    # j points to blank line (or EOF). Remove [nav_start:j].
    out = lines[:nav_start] + [nav_md.strip()] + lines[j:]
    path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def parse_lesson_body_md(
    *,
    url: str,
    lesson_id: str,
    images_root: Path,
    image_scope: str,
    timeout_sec: float,
    sleep_image_sec: float,
    img_cache: dict[str, Path],
    course_dir: Path,
    lesson_id_to_file: dict[str, str],
) -> tuple[str, str, int]:
    html = fetch_html(add_or_replace_query(url, print="Y"), timeout_sec=timeout_sec)
    title = extract_page_title(html) or f"Урок {lesson_id}"
    fragment = extract_div_inner_by_id(html, element_id="js-lesson-content-cnt") or ""
    if not fragment.strip():
        fragment = html
    # Some pages contain malformed comment closers (`--!>`), which breaks HTML parsing.
    fragment = fragment.replace("--!>", "-->")

    md = html_fragment_to_markdown(fragment)
    md = escape_html_tokens_outside_code(md)
    md = remove_html_comments_outside_fences(md)

    downloaded = 0

    def img_repl(_alt: str, url_part: str, _rest: str) -> str:
        nonlocal downloaded
        normalized = normalize_dev_url(url_part)
        if not normalized.startswith(("http://", "https://")):
            normalized = normalize_dev_url(urljoin(url, url_part))
        if not normalized.startswith(("http://", "https://")):
            return url_part

        cached = img_cache.get(normalized)
        if cached and cached.exists():
            return relpath(course_dir / f"lesson_{lesson_id}.md", cached)

        res = download_image(
            normalized,
            scope=image_scope,
            images_root=images_root,
            sleep_sec=sleep_image_sec,
            timeout_sec=timeout_sec,
        )
        if not res.local_path:
            return url_part

        img_cache[normalized] = res.local_path
        downloaded += 1
        return relpath(course_dir / f"lesson_{lesson_id}.md", res.local_path)

    md = rewrite_markdown_images(md, repl=img_repl)
    md = rewrite_learning_links_to_local(md, lesson_id_to_file=lesson_id_to_file)
    return title, md.strip(), downloaded


def generate_courses_root_index(*, docs_courses_dir: Path) -> None:
    index_path = docs_courses_dir / "index.md"
    course_dirs = sorted([d for d in docs_courses_dir.iterdir() if d.is_dir() and d.name.startswith("course_")], key=lambda p: p.name)
    lines: list[str] = []
    lines.append("# Учебные курсы 1C‑Bitrix")
    lines.append("")
    lines.append("Этот раздел содержит выгрузку учебных курсов с `dev.1c-bitrix.ru/learning/` в формате Markdown (под просмотр в VS Code/Obsidian).")
    lines.append("")
    lines.append("## Курсы")
    lines.append("")

    for d in course_dirs:
        idx = d / "index.md"
        title = d.name
        if idx.exists():
            m = H1_RE.search(idx.read_text(encoding="utf-8", errors="replace"))
            if m:
                title = m.group(1).strip()
        lines.append(f"- [{title}](./{d.name}/index.md)")

    lines.append("")
    lines.append("## Как пользоваться")
    lines.append("")
    lines.append("- Начните с `index.md` внутри нужного курса.")
    lines.append("- Для поиска по урокам используйте глобальный поиск по vault (`Ctrl+Shift+F` в VS Code).")
    lines.append("")
    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


@dataclass
class Stats:
    processed_courses: int = 0
    processed_lessons: int = 0
    updated_lessons: int = 0
    skipped_lessons: int = 0
    downloaded_images: int = 0
    failed_lessons: int = 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--course-ids",
        default="48,57",
        help="Comma-separated COURSE_IDs to parse (default: 48,57).",
    )
    parser.add_argument(
        "--only-lessons",
        default="",
        help="Optional comma-separated LESSON_ID list; when set, only these lessons are (re)fetched.",
    )
    parser.add_argument("--force", action="store_true", help="Refetch lessons even if they are not empty.")
    parser.add_argument("--max-lessons", type=int, default=0, help="Limit lessons per course (0 = no limit).")
    parser.add_argument("--sleep-page", type=float, default=0.05, help="Sleep seconds between lesson page fetches.")
    parser.add_argument("--sleep-image", type=float, default=0.02, help="Sleep seconds between image downloads.")
    parser.add_argument("--timeout", type=float, default=40.0, help="HTTP timeout per request, seconds.")
    args = parser.parse_args()

    root = repo_root()
    docs_courses_dir = root / "docs" / "courses"
    images_root = root / "images"
    docs_courses_dir.mkdir(parents=True, exist_ok=True)
    (images_root / "courses").mkdir(parents=True, exist_ok=True)

    stats = Stats()
    img_cache: dict[str, Path] = {}

    course_ids = [c.strip() for c in args.course_ids.split(",") if c.strip()]
    only_lessons = {s.strip() for s in args.only_lessons.split(",") if s.strip()} if args.only_lessons else set()

    for cid in course_ids:
        stats.processed_courses += 1
        course_url = f"{BASE_URL}/learning/course/index.php?COURSE_ID={cid}"
        try:
            course_html = fetch_html(course_url, timeout_sec=args.timeout)
        except Exception as e:
            print(f"[fail] course={cid} url={course_url} error={e}")
            continue
        course_title = extract_page_title(course_html) or f"Курс {cid}"

        course_dir = find_or_create_course_dir(docs_courses_dir=docs_courses_dir, course_id=cid, course_title=course_title)
        course_dir.mkdir(parents=True, exist_ok=True)

        lesson_urls = iter_lesson_urls_from_course_page(course_html, course_id=cid)
        if args.max_lessons and args.max_lessons > 0:
            lesson_urls = lesson_urls[: args.max_lessons]

        lesson_ids: list[str] = []
        lesson_titles: dict[str, str] = {}

        lesson_id_to_file = {}
        for u in lesson_urls:
            lid = lesson_id_from_url(u)
            if lid:
                lesson_id_to_file[lid] = f"lesson_{lid}.md"
                lesson_ids.append(lid)

        image_scope = f"courses/{cid}"

        # Preload titles from existing files for stable nav/index (even on partial runs).
        for lid in lesson_ids:
            path = course_dir / f"lesson_{lid}.md"
            if not path.exists():
                continue
            current = path.read_text(encoding="utf-8", errors="replace")
            m = H1_RE.search(current)
            if m:
                lesson_titles[lid] = m.group(1).strip()

        for u in lesson_urls:
            lid = lesson_id_from_url(u) or "unknown"
            path = course_dir / f"lesson_{lid}.md"

            if only_lessons and lid not in only_lessons:
                continue

            if path.exists() and not args.force:
                current = path.read_text(encoding="utf-8", errors="replace")
                if not is_effectively_empty_lesson(current):
                    stats.skipped_lessons += 1
                    m = H1_RE.search(current)
                    lesson_titles[lid] = m.group(1).strip() if m else lesson_titles.get(lid, f"Урок {lid}")
                    continue

            # Fetch and parse.
            try:
                title, body_md, downloaded = parse_lesson_body_md(
                    url=u,
                    lesson_id=lid,
                    images_root=images_root,
                    image_scope=image_scope,
                    timeout_sec=args.timeout,
                    sleep_image_sec=args.sleep_image,
                    img_cache=img_cache,
                    course_dir=course_dir,
                    lesson_id_to_file=lesson_id_to_file,
                )
            except Exception as e:
                stats.failed_lessons += 1
                print(f"[fail] course={cid} lesson={lid} url={u} error={e}")
                continue

            # Write with temporary nav (titles filled in second pass).
            out: list[str] = []
            out.append(f"# {title}".strip())
            out.append("")
            out.append(render_lesson_nav(prev_id=None, prev_title=None, next_id=None, next_title=None))
            out.append("")
            out.append(f"Официальная страница урока: {u}")
            out.append("")
            out.append(body_md)
            out.append("")
            path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

            lesson_titles[lid] = title
            stats.processed_lessons += 1
            stats.updated_lessons += 1
            stats.downloaded_images += downloaded

            if args.sleep_page:
                time.sleep(args.sleep_page)

        # Second pass: stable prev/next nav with titles.
        for idx, lid in enumerate(lesson_ids):
            prev_id = lesson_ids[idx - 1] if idx > 0 else None
            next_id = lesson_ids[idx + 1] if idx + 1 < len(lesson_ids) else None
            nav_md = render_lesson_nav(
                prev_id=prev_id,
                prev_title=lesson_titles.get(prev_id) if prev_id else None,
                next_id=next_id,
                next_title=lesson_titles.get(next_id) if next_id else None,
            )
            update_lesson_nav_in_file(path=course_dir / f"lesson_{lid}.md", nav_md=nav_md)

        write_course_index(
            course_dir=course_dir,
            course_id=cid,
            course_title=course_title,
            lesson_ids=lesson_ids,
            lesson_titles=lesson_titles,
        )

    generate_courses_root_index(docs_courses_dir=docs_courses_dir)

    print(
        "[parse-courses] "
        f"courses={stats.processed_courses} lessons_processed={stats.processed_lessons} "
        f"lessons_updated={stats.updated_lessons} lessons_skipped={stats.skipped_lessons} "
        f"downloaded_images={stats.downloaded_images} failed_lessons={stats.failed_lessons}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
