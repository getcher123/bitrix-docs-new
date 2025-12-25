# Телефония

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/index.php

Модуль для работы с облачной телефонией.

```
\Bitrix\Main\Loader::includeModule('voximplant');
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [BlacklistTable](https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/blacklisttable/index.php) | Класс для работы с таблицей **Черный список**. | 15.1.1 |
| [QueueTable](https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/queuetable/index.php) | Класс для работы с таблицей **Очереди звонков**. |  |
| [SipTable](https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/siptable/index.php) | Класс для работы с таблицей **Настройки подключения к sip-серверу**. |  |
| [AddressVerification](https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/addressverification/index.php) | Класс для работы с верификацией адреса. | 16.0.8 |
| [Security](https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/security/index.php) | Классы для управления правами доступа телефонии. | 16.5.1 |
| [Tts](https://dev.1c-bitrix.ru/api_d7/bitrix/voximplant/tts/index.php) | Параметры произнесения речи. | 16.5.0 |

> **Внимание!** Данные классы должны использоваться только для чтения данных из таблиц, а ни в коем случае не должны использоваться для записи данных напрямую в таблицы.

#### Смотрите также

- [Телефония (пользовательская документация)](http://dev.1c-bitrix.ru/user_help/settings/voximplant/index.php)
- [Телефония (API для работы со старой версией ядра)](../../../telephony/index.md)
- [Учебный курс "Телефония в Битрикс24"](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=77)
- [Телефония - Учебный курс "Администратор сервиса Битрикс24 (коробочная версия)"](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=02699)
