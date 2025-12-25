# setProxy

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/setproxy.php

```
void public
\Bitrix\Main\Web\HttpClient::setProxy(
	string $proxyHost,
	null|integer $proxyPort = null,
	null|string $proxyUser = null,
	null|string $proxyPassword = null
);
```

Нестатический метод устанавливает HTTP прокси для запроса.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $proxyHost | Имя или адрес хоста (без *http://*). |  |
| $proxyPort | Номер порта. |  |
| $proxyUser | Имя пользователя. |  |
| $proxyPassword | Пароль пользователя. |  |

#### Примеры
