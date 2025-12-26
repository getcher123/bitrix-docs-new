from __future__ import annotations

import re


def route_sections(query: str) -> list[str] | None:
    q = query.lower()
    if "bitrix\\" in query:
        return ["D7"]
    if re.search(r"\\b(crm|tasks|im)\\.", q):
        return ["REST"]
    if "урок" in q or "курс" in q:
        return ["courses"]
    if "настройк" in q or "интерфейс" in q:
        return ["user_help"]
    return None
