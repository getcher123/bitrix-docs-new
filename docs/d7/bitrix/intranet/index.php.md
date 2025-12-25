# Intranet

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/index.php

`\Bitrix\Intranet` – пространство имен модуля **Intranet**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'intranet'
);
```

| Класс, пространство имен | Описание |
| --- | --- |
| [Composite](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/composite/index.php)Пространство имён содержит классы для работы по композитным технологиям. |  |
| [Integration](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/integration/index.php)Пространство имён содержит классы интегрирования интранета с Б24. |  |
| [Internals](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/internals/index.php)Пространство имён, содержащее классы для работы с таблицами модуля. Отключён с версии 20.5.400 |  |
| [OutlookApplication](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/outlookapplication/index.php)Класс для работы с приложением Outlook. |  |
| [UserAbsence](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/userabsence/index.php)Класс методов для получения данных о текущем графике отсутствий. |  |
| [UserTable](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/usertable/index.php)Класс для работы с таблицей пользователей. |  |
| [UStat](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/ustat/index.php)Пространство имён содержит классы для работы со статистикой по пользователям. |  |
| [Util](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/util/index.php)Класс вспомогательных методов. |  |

#### Смотрите также:

- [Модуль Интранет в старом ядре](../../../intranet/index.md).
