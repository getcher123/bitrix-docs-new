# Асинхронные запросы

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/asynchronous_requests.php

За счёт организации очереди асинхронных запросов можно добиться кратного сокращения времени выполнения запросов. Каждый объект клиента создаёт собственную очередь.

Метод добавления асинхронного запроса в очередь возвращает

			промис

**Promise** (промис) – это объект, представляющий результат успешного или неудачного завершения асинхронной операции.

		, не дожидаясь фактического выполнения запроса. Чтобы узнать результат запроса, нужно «подождать» и «развернуть» промис, либо передать ему callback-функции, которые выполнятся при успешном или неуспешном заполнении промиса.

Если стоит простая задача передать серию запросов и обработать их результаты, то можно попросить клиент самостоятельно обработать очередь и вернуть все ответы. Ответы будут отсортированы в порядке времени получения ответа (могут не соответствовать порядку запросов):

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Uri;
use Bitrix\Main\Web\Http\Request;
use Bitrix\Main\Web\Http\Method;
use Bitrix\Main\Web\Http\ClientException;

$http = new HttpClient();

$urls = [
	'http://www.flowersweb.info/images/t/top1.jpg',
	'http://1с-битрикс.рф',
	'https://www.1c-bitrix.ru/',
];

foreach ($urls as $url)
{
	$request = new Request(Method::GET, new Uri($url));

	$http->sendAsyncRequest($request);
}

try
{
	foreach ($http->wait() as $response)
	{
		var_dump($response->getStatusCode());
	}
}
catch (ClientException $e)
{
	var_dump($e->getMessage());
}
```

Если же нужен более точный контроль, в том числе за порядком ответов, то без промисов не обойтись:

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Uri;
use Bitrix\Main\Web\Http\Request;
use Bitrix\Main\Web\Http\Method;
use Bitrix\Main\Web\Http\ClientException;

$http = new HttpClient();

$urls = [
	'http://www.flowersweb.info/images/t/top1.jpg',
	'http://1с-битрикс.рф',
	'https://www.1c-bitrix.ru/',
];

$promises = [];

// добавить запросы в очередь
foreach ($urls as $url)
{
	$request = new Request(Method::GET, new Uri($url));

	$promises[] = $http->sendAsyncRequest($request);
}

// выполнить промисы
foreach ($promises as $promise)
{
	try
	{
		$response = $promise->wait();

		var_dump($promise->getRequest()->getUri()->getHost());
		var_dump($response->getStatusCode());
	}
	catch (ClientException $e)
	{
		var_dump($e->getMessage());
	}
}
```

Также в метод промиса `then` можно передать две callback-функции: на случай успешного заполнения промиса и на случай ошибки. Из callback-функций можно организовать цепочки, последовательно вызывая `then`.

Callback-функция успешного заполнения промиса принимает на вход объект ответа **ResponseInterface** и обязана вернуть объект ответа. Callback-функция ошибки принимает на вход исключение **ClientException** и должна вернуть или выкинуть исключение.

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Uri;
use Bitrix\Main\Web\Http\Request;
use Bitrix\Main\Web\Http\Method;

$http = new HttpClient();

$urls = [
	'http://www.flowersweb.info/images/t/top1.jpg',
	'http://1с-битрикс.рф',
	'https://www.1c-bitrix.ru/',
];

// добавить запросы в очередь
foreach ($urls as $url)
{
	$request = new Request(Method::GET, new Uri($url));

	$promise = $http->sendAsyncRequest($request);

	// callback
	$promise->then(function ($response) use ($promise) {
		var_dump($promise->getRequest()->getUri()->getHost());
		var_dump($response->getStatusCode());

		return $response;
	});
}

// нужно выполнить промисы
$http->wait();
```

Если явно не вызывать обработку очереди (строка `$http->wait();`), то это будет сделано в background jobs ядра. Callback-функции будут вызваны, но увидеть их результат на экране будет невозможно, т.к. фоновые задания выполняются уже после отдачи контента. Это можно использовать, если не нужно показывать результаты обработки запросов – контент отгрузится пользователю быстрее, а запросы выполнятся на фоне (в примере нужно заменить `var_dump()` на `AddMessage2Log()`).
