# OnHttpClientBuildRequest

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/events/onhttpclientbuildrequest.php

Cобытие вызывается после создания объекта запроса. Оно позволяет донастроить опции клиента и изменить объект запроса (следует учитывать, что объект запроса является неизменяемым, а все изменения делаются через методы `with...`). Объект запроса возвращается в результате события типа `\Bitrix\Main\Web\Http\RequestEventResult`.

#### Пример

```
\Bitrix\Main\EventManager::getInstance()->addEventHandler('main', 'OnHttpClientBuildRequest', 'MyOnHttpClientBuildRequest');
function MyOnHttpClientBuildRequest(\Bitrix\Main\Web\Http\RequestEvent $event)
{
	$client = $event->getClient();
	$client->setProxy('');

	$request = $event->getRequest();
	$request = $request->withHeader('MyHeader', 'MyValue');

	$result = new \Bitrix\Main\Web\Http\RequestEventResult($request);

	$event->addResult($result);
}
```
