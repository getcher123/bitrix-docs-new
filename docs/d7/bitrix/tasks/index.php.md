# Задачи

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/index.php

Модуль управления задачами.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('tasks');
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [Access](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/access/index.php) | Пространство имён содержит классы для контроля доступа. | 20.6.0 |
| [CTaskCheckListItem](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/CTaskCheckListItem/index.php) | Класс для работы с чек-листами. | 18.0.6 |
| [CTaskCommentItem](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/CTaskCommentItem/index.php) | Класс для работы с комментариями к задачам. | 18.0.6 |
| [Task](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/task/index.php) | Содержит классы *orm* для сущностей, которые являются вспомогательными для сущности **Задача**. | 15.6.0 |
| [TaskTable](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/tasktable/index.php) | Класс *orm* для сущности **Задача**. | 15.6.0 |
| [Template](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/template/index.php) | Cодержит классы *orm* для сущности **Шаблон задачи**. | 14.5.11 |
| [TemplateTable](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/templatetable/index.php) | Класс *orm* для сущности **Шаблон задачи**. | 14.5.11 |
| [Internals](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/internals/index.php) | Пространство имён содержит классы для работы с таблицами модуля **Задачи**. |  |
| [Integration](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/integration/index.php) | Пространство имён содержит классы для интеграции с различными модулями системы. |  |
| [Rest](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/rest/index.php) | Пространство имён для работы с методами Rest. |  |

#### Смотрите также:

- [Задачи (учебный курс)](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=52&CHAPTER_ID=0501)
- [Задачи (пользовательская документация)](http://dev.1c-bitrix.ru/user_help/content/tasks/components_2/tasks_list.php)
- [Задачи (API для старой версии ядра)](../../../tasks/index.md)
