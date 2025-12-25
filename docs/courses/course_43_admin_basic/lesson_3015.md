# Некоторые ошибки при работе с инфоблоками

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2915 — Практика. Копирование инфоблока](lesson_2915.md)
- [Следующий: 5196 — Практика. Ограничение области поиска разделом →](lesson_5196.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3015

**Ошибка типа**:

`Fatal error: Class 'CIBlockElement' not found in /hosting/site.ru/www/index.php on line XX`

Если используете модуль **Инфоблоки**, его нужно сначала подключить:

 `CModule::IncludeModule("iblock");`

|  |
| --- |

**Ошибка типа**:

`Fatal error: Call to a member function GetNextElement() on a non-object in /hosting/site.ru/www/index.php on line XX`

Скорее всего вы передали неверные параметры какому-то методу. Например, так:

`$res = CIBlockElement::GetList(array(), $arFilter, array(), array(), $arSelect);`

Третий-то параметр должен быть **true/false**, а не **array**. Читайте внимательно описание используемого метода.
