from __future__ import annotations

import re


def route_sections(query: str) -> list[str] | None:
    q = query.lower()
    if "bitrix\\" in query or " d7" in q or "orm" in q:
        return ["D7"]
    if re.search(r"\\b(crm|tasks|im|sale)\\.", q) or "rest" in q:
        return ["REST"]
    if "урок" in q or "курс" in q:
        return ["courses"]
    if "настройк" in q or "интерфейс" in 