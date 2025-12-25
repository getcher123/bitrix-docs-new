# waitResponse

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/waitresponse.php

```
void public
\Bitrix\Main\Web\HttpClient::waitResponse(
	boolean $value
);
```

Нестатический метод устанавливает опцию ожидания ответа.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $value | Если *true* - ожидает получения тела ответа.Если *false* - разрывает соединение сразу после чтения заголовков ответа. (По умолчанию *true*). |  |

#### Примеры
