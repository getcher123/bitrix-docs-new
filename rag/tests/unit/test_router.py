from bitrix_rag.retrieval.router import route_sections


def test_route_sections_d7():
    assert route_sections("Использую D7 ORM") == ["D7"]


def test_route_sections_rest():
    assert route_sections("REST api метод") == ["REST"]


def test_route_sections_courses():
    assert route_sections("Урок 5: настройки") == ["courses"]


def test_route_sections_user_help():
    assert route_sections("Настройка интерфейса админки") == ["user_help"]


def test_route_sections_classic():
    assert route_sections("CIBlockElement::GetList") == ["classic"]


def test_route_sections_unknown():
    assert route_sections("Что такое FooBar?") is None
