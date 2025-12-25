# getMessengerLink

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/imopenlines/tracker/getmessengerlink.php

```
\Bitrix\ImOpenLines\Tracker::getMessengerLink($lineId, $connectorId, $crmEntities)
```

Метод получения ссылки на Telegram-бота со стартовым параметром, к которому привязаны перечисленные CRM-объекты.
Клиент, перейдя по ссылке, стартует диалог ОЛ на стороне портала. К диалогу будет подключена CRM и будет создано Дело - входящий чат открытой линии.

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
| $crmEntities | array | Массив с кодами CRM-объектов, к которым необходимо привязать диалог. |  |

#### Пример

```
$tracker = \Bitrix\Main\DI\ServiceLocator::getInstance()->get('ImOpenLines.Services.Tracker');

$tracker->getMessengerLink(
	$lineId,
	'telegrambot',
	[
		[
			'ENTITY_TYPE_ID' => \CCrmOwnerType::Deal,
			'ENTITY_ID' => 89,
		],
		[
			'ENTITY_TYPE_ID' => \CCrmOwnerType::Contact,
			'ENTITY_ID' => 83,
		],
		[
			'ENTITY_TYPE_ID' => \CCrmOwnerType::Company,
			'ENTITY_ID' => 83,
		],
		[
			'ENTITY_TYPE_ID' => \CCrmOwnerType::Lead,
			'ENTITY_ID' => 83,
		],
	]
);
```
