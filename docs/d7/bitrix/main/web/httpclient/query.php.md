# query

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/query.php

```
boolean public
\Bitrix\Main\Web\HttpClient::query(
	string $method,
	string $url,
	array|string|resource $entityBody = null
);
```

Нестатический метод выполняет HTTP запрос.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $method | HTTP метод (GET, POST и так далее). **Важно**: должно быть набрано в верхнем регистре. |  |
| $url | Абсолютный URI в виде: `"http://user:pass@host:port/path/?query"`. |  |
| $entityBody | Сущность POST/PUT запроса. Если это - обработчик ресурсов, то данные будут читаться непосредственно из потока. |  |

#### Примеры
