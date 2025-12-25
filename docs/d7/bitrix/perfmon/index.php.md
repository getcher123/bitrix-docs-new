# Монитор производительности

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/perfmon/index.php

**Монитор производительности** - модуль мониторинга параметров производительности сайта.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('perfmon');
```

| Пространство имен | Описание | С версии |
| --- | --- | --- |
| [Sql](https://dev.1c-bitrix.ru/api_d7/bitrix/perfmon/sql/index.php) | Набор классов для генерации DDL. |  |
| [Php](https://dev.1c-bitrix.ru/api_d7/bitrix/perfmon/php/index.php) | Класс для генерации php-кода. | 15.5.1 |

#### Смотрите также:

- [Монитор производительности (учебный курс)](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=04643)
- [Монитор производительности (API для старой версии ядра)](../../../perfmon/index.md)
