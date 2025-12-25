# Режим legacy

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/legacy.php

При создании объекта http-клиента можно передать в конструктор опции в виде массива (для большинства опций есть также сеттеры):

| Опция | Тип | Описание |
| --- | --- | --- |
| **redirect** * | bool | Следовать переадресации (по умолчанию `true` – редирект). |
| **redirectMax** * | int | Максимальное количество редиректов (по умолчанию `5`). |
| **waitResponse** | bool | Дождаться ответа или отключиться сразу после запроса (по умолчанию `true` – ожидание ответа). |
| **socketTimeout** | int | Таймаут соединения в секундах (по умолчанию `30`). |
| **streamTimeout** | int | Таймаут потока в секундах (по умолчанию `60`). |
| **version** * | string | Версия HTTP (HttpClient::HTTP_1_0, HttpClient::HTTP_1_1) (по умолчанию `"1.0"`). |
| **proxyHost** | string | Имя\адрес прокси сервера. |
| **proxyPort** | int | Порт прокси сервера. |
| **proxyUser** | string | Имя пользователя прокси сервера. |
| **proxyPassword** | string | Пароль прокси сервера. |
| **compress** | bool | Использовать сжатие gzip (по умолчанию `false`). |
| **charset** | string | Кодировка для содержимого POST и PUT запросов. |
| **disableSslVerification** | bool | Если установлено `true`, то верификация ssl-сертификатов производиться не будет. |
| **bodyLengthMax** | int | Максимальная длина запроса. |
| **privateIp** | bool | Включить запросы к частным IP-адресам (по умолчанию `true` – включить). |
| **debugLevel** | int | Уровень отладки с использованием констант `HttpDebug::*`. |
| **cookies** * | array | Массив файлов cookie для HTTP-запроса. |
| **headers** * | array | Массив заголовков для HTTP-запроса. |
| **useCurl** | bool | Включить использование библиотеки CURL (по умолчанию `false`). |
| **curlLogFile** | string | Полный путь к файлу с логами CURL. |

***** – опции, работающие только в legacy-режиме.

Значения опций по умолчанию на конкретном проекте можно установить в **settings.php**:

```
return [
	// ...
	"http_client_options" => [
		"value" => [
			"socketTimeout" => 20,
			"streamTimeout" => 20,
			"useCurl" => true,
		],
	]
	// ...
];
```

Доступные основные методы:

- [get](get.php.md)
- [head](head.php.md)
- [post](post.php.md)
- [query](query.php.md)
- [download](download.php.md)
- [getHeaders](getheaders.php.md)
- [getCookies](getcookies.php.md)
- [getStatus](getstatus.php.md)
- [getResult](getresult.php.md)
- [getError](geterror.php.md)

Простейший пример использования:

```
use Bitrix\Main\Web\HttpClient;

$http = new HttpClient([
	'compress' => true,
	'headers' => [
		'User-Agent' => 'bitrix',
	],
]);

$result = $http->get('https://1c-bitrix.ru/');

if ($result !== false)
{
	var_dump($http->getStatus());
	var_dump($http->getHeaders());
}
else
{
	var_dump($http->getError());
}
```

Клиент сам выполнит редирект и распакует ответ.

В **main 23.300.0** появилась возможность динамически, в отличие от опции **waitResponse**, определять через callback-функцию **shouldFetchBody**, нужно ли выкачивать тело ответа. В параметры callback-функции приходит объект ответа с заголовками и объект запроса:

```
use Bitrix\Main\Web\HttpClient;
use Bitrix\Main\Web\Http\Response;
use Psr\Http\Message\RequestInterface;

$http = new HttpClient();

$http->shouldFetchBody(function (Response $response, RequestInterface $request) {
	var_dump($request->getHeaders());
	return ($response->getHeadersCollection()->getContentType() === 'text/html');
});

$result = $http->get('https://www.1c-bitrix.ru/');
var_dump($result);
```
