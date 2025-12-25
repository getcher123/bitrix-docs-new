# sendStatusDelivery

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/imconnector/customconnectors/sendstatusdelivery.php

```
public static function
\Bitrix\ImConnector\CustomConnectors::sendStatusDelivery(
	$connector,
	$line,
	$data
)
```

Метод подтверждения доставки сообщения от Открытой Линии во внешнюю систему.

#### Параметры

| Параметр | Описание | С версии |
| --- | --- | --- |
| connector | ID коннектора, который был указан при регистрации обработчика. |  |
| line | ID открытой линии |  |
| data | Массив массивов сообщений, где каждое сообщение описывается следующим форматом:<br><br>```<br>array(<br>	'im',//Пересылается элемент 'im' из входящего сообщения ОЛ<br>	'message' => array(<br>		'id'//Массив ID во внешней системе. Именно массив, а не единичное значение, даже если ID один.<br>	),<br>	'chat' => array(<br>		'id'//ID чата во внешней системе.<br>	),<br>);<br>``` |  |
