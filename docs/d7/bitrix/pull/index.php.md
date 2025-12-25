# Push and Pull

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/pull/index.php

**Push and Pull** - модуль для обеспечения работы интерактивных приложений.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('pull');
```

> **Внимание!** Данные классы должны использоваться только для чтения данных из таблиц, а ни в коем случае не должны использоваться для записи данных напрямую в таблицы.

| Класс | Описание | С версии |
| --- | --- | --- |
| [PushTable](https://dev.1c-bitrix.ru/api_d7/bitrix/pull/pushtable/index.php) | Таблица, содержащая описание мобильных устройств, для дальнейшей отправки по ней push-уведомлений. |  |

#### Смотрите также:

- [Push and Pull (учебный курс)](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2033)
- [Push and Pull (API для старой версии ядра)](../../../push_pull/index.md)
