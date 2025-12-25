# setCompress

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/setcompress.php

```
void public
\Bitrix\Main\Web\HttpClient::setCompress(
	boolean $value
);
```

Нестатический метод устанавливает опции компрессии.

> Примите во внимание, что не нужно использовать опции сжатия с выходным потоком, если контент может быть большим. Учтите что сжатый ответ обрабатывается в любом случае, если установлено поле заголовка Content-Encoding.

#### Параметры

| Параметр | Описание | Версия |
| --- | --- | --- |
| $value | Если *true*, будет послан **Accept-Encoding: gzip**. |  |

#### Примеры
