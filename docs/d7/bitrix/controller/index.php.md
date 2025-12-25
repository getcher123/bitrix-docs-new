# Контроллер сайтов

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/controller/index.php

**Контроллер сайтов** – модуль, который предназначен для группового централизованного администрирования, обновления, мониторинга большого количества сайтов, расположенных как на этом же сервере, так и на удаленных серверах доступных через Интернет.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'controller'
);
```

| Класс/Пространство имен | Описание | С версии |
| --- | --- | --- |
| [GroupMapTable](https://dev.1c-bitrix.ru/api_d7/bitrix/controller/groupmaptable/index.php) | Таблица соответствий групп пользователей, подключенных сайтов и групп пользователей контроллера. |  |
| [AuthGrantTable](https://dev.1c-bitrix.ru/api_d7/bitrix/controller/authgranttable/index.php) | Таблица выданных разрешений для пользователей для выполнения определённых операций с подключенными сайтами. |  |
| [AuthLogTable](https://dev.1c-bitrix.ru/api_d7/bitrix/controller/authlogtable/index.php) | Таблица журнала действий пользователей. |  |
| [GroupTable](https://dev.1c-bitrix.ru/api_d7/bitrix/controller/grouptable/index.php) | Таблица групп подключенных сайтов. |  |
| [MemberTable](https://dev.1c-bitrix.ru/api_d7/bitrix/controller/membertable/index.php) | Таблица подключенных сайтов. |  |

#### Смотрите также:

- [Контроллер сайтов (учебный курс)](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&CHAPTER_ID=04546)
- [Контроллер сайтов (API для старой версии ядра)](../../../controller/index.md)
