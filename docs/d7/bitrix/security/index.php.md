# Проактивная защита

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/security/index.php

**Проактивная защита** – это комплекс технических и организационных мер, которые объединены общей концепцией безопасности и позволяют значительно расширить понятие защищенности и реакции веб-приложений на угрозы.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('security');
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [Codec](https://dev.1c-bitrix.ru/api_d7/bitrix/security/codec/index.php) | Класс для работы с набором кодеков. | 14.5.5 |
| [Filter](https://dev.1c-bitrix.ru/api_d7/bitrix/security/filter/index.php) | Класс для работы с фильтрами. |  |
| [HostRestriction](https://dev.1c-bitrix.ru/api_d7/bitrix/security/hostrestriction/index.php) | Класс, реализующий проверку и ограничение хостов/доменов. | 14.0.6 |
| [LogicException](https://dev.1c-bitrix.ru/api_d7/bitrix/security/logicexception/index.php) | Исключение возникающее при логических ошибках входящих данных. | 14.0.6 |
| [Mfa](https://dev.1c-bitrix.ru/api_d7/bitrix/security/mfa/index.php) | Класс, реализующий многофакторную аутентификацию. | 14.5.5 |
| [SessionTable](https://dev.1c-bitrix.ru/api_d7/bitrix/security/sessiontable/index.php) | Класс для работы с данными сессий посетителей сайта. | 16.0.0 |

#### Смотрите также:

- [Проактивная защита (учебный курс)](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&CHAPTER_ID=04547)
- [Проактивная защита (пользовательская документация)](http://dev.1c-bitrix.ru/user_help/settings/security/index.php)
