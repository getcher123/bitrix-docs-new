# getImMessengerUrl

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/imconnector/connector/getimmessengerurl.php

```
\Bitrix\ImConnector\Connector::getImMessengerUrl($lineId, $connectorId, $additional)
```

Метод получения ссылки на Telegram-бота c/без стартового параметра.

Возвращает  структуру с двумя ссылками

```
array{web: string, mob: string}
```

- для браузера: https://t.me/bot_name?start=xxxx

- для мобильного устройства: tg://resolve?domain=bot_name&start=xxxx

#### Параметры

| Параметр | Формат | Описание | С версии |
| --- | --- | --- | --- |
| $lineId | int | Код линии. |  |
| $connectorId | string | Код линии. |  |
| $additional | array\|string\|null | Стартовый параметр - строка или набор параметров в массиве. |  |

#### Пример

```
\Bitrix\ImConnector\Connector::getImMessengerUrl(1, 'telegrambot', 'xxxx');
```
