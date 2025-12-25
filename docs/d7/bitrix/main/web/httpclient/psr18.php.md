# PSR-18: HTTP Client

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/psr18.php

Интерфейс `\Psr\Http\Client\ClientInterface` содержит всего один метод для отправки HTTP-запроса:

```
interface ClientInterface
{
	public function sendRequest(RequestInterface $request): ResponseInterface;
}
```

PSR требует создать и передать объект запроса типа **RequestInterface** и возвращает объект ответа типа **ResponseInterface** (описаны в [PSR-7](https://www.php-fig.org/psr/psr-7/)). Обработка ошибок реализуется на исключениях. В ядре интерфейсы PSR-7 реализованы в классах:

- `\Bitrix\Main\Web\Uri` – URI;
- `\Bitrix\Main\Web\Http\Request` – запрос;
- `\Bitrix\Main\Web\Http\Response` – ответ;
- `\Bitrix\Main\Web\Http\Stream` – тело запроса/ответа;
- `\Bitrix\Main\Web\Http\ClientException` – исключение верхнего уровня;
- `\Bitrix\Main\Web\Http\RequestException` – ошибка запроса;
- `\Bitrix\Main\Web\Http\NetworkException` – сетевая ошибка.

Особенностью PSR-7 является использование потоков для тела запроса и ответа. Ниже пример отправки формы методом POST:

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Uri;
use Bitrix\Main\Web\Http\Request;
use Bitrix\Main\Web\Http\Method;
use Bitrix\Main\Web\Http\Stream;
//use Bitrix\Main\Web\Http\FormStream;
use Bitrix\Main\Web\Http\ClientException;

$http = new HttpClient([
	'compress' => true,
]);

$data = [
	"k1" => "v1",
	"k2" => "v2",
];

$uri = new Uri('http://vm.vad/test.php');

// подготовка тела запроса
$body = new Stream('php://temp', 'r+');
$body->write(http_build_query($data, '', '&'));

// ИЛИ более простой способ (main 23.300.0)
// $body = new FormStream($data);

$request = new Request(Method::POST, $uri, [], $body);

try
{
	$response = $http->sendRequest($request);

	var_dump($response->getStatusCode());
	var_dump($response->getHeaders());
	var_dump((string)$response->getBody());
}
catch (ClientException $e)
{
	var_dump($e->getMessage());
}
```

Рассмотрим более сложный пример, когда нужно передать файл методом POST:

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Uri;
use Bitrix\Main\Web\Http\Request;
use Bitrix\Main\Web\Http\Method;
use Bitrix\Main\Web\Http\MultipartStream;
use Bitrix\Main\Web\Http\ClientException;

$http = new HttpClient([
	'compress' => true,
]);

$res = fopen("/home/bitrix/www/20190807_120929.jpg", 'r');

$data = [
	"k1" => "v1",
	"k2" => "v2",
	"k3" => [
		'resource' => $res,
		'filename' => "pic.jpg",
	],
];

$uri = new Uri('http://vm.vad/test.php');

$body = new MultipartStream($data);

$headers = [
	'User-Agent' => 'bitrix',
	'Content-type' => 'multipart/form-data; boundary=' . $body->getBoundary(),
];

$request = new Request(Method::POST, $uri, $headers, $body);

fclose($res);

try
{
	$response = $http->sendRequest($request);

	var_dump($response->getStatusCode());
	var_dump($response->getHeaders());
	var_dump((string)$response->getBody());
}
catch (ClientException $e)
{
	var_dump($e->getMessage());
}
```

Обратите внимание, что ответ с редиректом будет возвращён как есть, без перехода по заголовку **Location**. PSR-18 считает, что ответы с кодом **30x** ничем не отличаются от всех остальных. Пример обработки редиректа может выглядеть так:

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Uri;
use Bitrix\Main\Web\Http\Request;
use Bitrix\Main\Web\Http\Method;
use Bitrix\Main\Web\Http\ClientException;

$http = new HttpClient([
	'compress' => true,
	'disableSslVerification' => true,
]);

$uri = new Uri('http://1с-битрикс.рф/');

$request = new Request(Method::GET, $uri);

try
{
	do
	{
		$response = $http->sendRequest($request);

		if ($response->hasHeader('Location'))
		{
			$location = $response->getHeader('Location')[0];
			var_dump($location);

			$request = $request->withUri(new Uri($location));
		}
	}
	while ($response->hasHeader('Location'));

//	var_dump((string)$response->getBody());
}
catch (ClientException $e)
{
	var_dump($e->getMessage());
}

/*
Распечатает:
string(37) "https://xn--1--clc2aam4begg.xn--p1ai/"
string(25) "https://www.1c-bitrix.ru/"
*/
```

Вместо вышеуказанного можно использовать старый способ:

```
use Bitrix\Main\Web\HttpClient;

$http = (new HttpClient())->disableSslVerification();

var_dump($http->get('http://1с-битрикс.рф/'));
```
