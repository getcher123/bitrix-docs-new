# HttpClient

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/index.php

**HttpClient** – класс для работы с HTTP. Класс работает через сокеты. Класс принимает опции по умолчанию из настроек конфигурации **http_client_options** файла `/bitrix/.settings.php`.

С версии **main 23.0.0** в HttpClient добавлена поддержка [PSR-18](https://www.php-fig.org/psr/psr-18/). Помимо [PSR](psr18.php.md), клиент работает в [legacy-режиме](legacy.php.md), поддерживает очереди [асинхронных запросов](asynchronous_requests.php.md) и [библиотеку CURL](curl.php.md).

| Метод | Описание | С версии |
| --- | --- | --- |
| [disableSslVerification](disablesslverification.php.md) | Метод запрещает верификацию ssl сертификата. | 15.5.9 |
| [download](download.php.md) | Метод скачивает и сохраняет файлы. |  |
| [get](get.php.md) | Метод выполняет GET запрос. |  |
| [getCharset](getcharset.php.md) | Метод возвращает кодировку контента ответа. |  |
| [getContentType](getcontenttype.php.md) | Метод возвращает тип контента ответа. |  |
| [getCookies](getcookies.php.md) | Метод возвращает отпарсенный HTTP ответ cookies |  |
| [getEffectiveUrl](geteffectiveurl.php.md) | Метод возвращает URL последнего редиректа или первначалный URL. |  |
| [getError](geterror.php.md) | Метод возвращает массив ошибок при неудаче |  |
| [getHeaders](getheaders.php.md) | Метод возвращает отпарсенные заголовки HTTP ответов. |  |
| [getResult](getresult.php.md) | Метод возвращает строку сущности HTTP ответа. |  |
| [getStatus](getstatus.php.md) | Метод возвращает код статуса HTTP ответа. |  |
| [head](head.php.md) | Метод выполняет HEAD запрос. |  |
| [post](post.php.md) | Метод выполняет POST запрос. |  |
| [query](query.php.md) | Метод выполняет HTTP запрос. |  |
| [setAuthorization](setauthorization.php.md) | Метод устанавливает поле заголовка запроса аутентификации. |  |
| [setCharset](setcharset.php.md) | Метод устанавливает кодировку для тела объекта |  |
| [setCompress](setcompress.php.md) | Метод устанавливает опции компрессии. |  |
| [setCookies](setcookies.php.md) | Метод устанавливает массив cookies для HTTP запроса |  |
| [setHeader](setheader.php.md) | Метод устанавливает поле заголовка HTTP запроса. |  |
| [setOutputStream](setoutputstream.php.md) | Метод устанавливает вывод ответа в поток вместо строкового результата. |  |
| [setProxy](setproxy.php.md) | Метод устанавливает HTTP прокси для запроса. |  |
| [setRedirect](setredirect.php.md) | Метод устанавливает опции редиректа. |  |
| [setStreamTimeout](setstreamtimeout.php.md) | Метод устанавливает поток сокетов для чтения таймаута. |  |
| [setVersion](setversion.php.md) | Метод устанавливает версию HTTP протокола. |  |
| [waitResponse](waitresponse.php.md) | Метод устанавливает опцию ожидания ответа. |  |
| [destruct](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/__destruct.php) | Метод закрывает соединение при уничтожении объекта. |  |
| [Конструктор](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/httpclient/__construct.php) | Метод создаёт новый объект класса. |  |
| [setTimeout](settimeout.php.md) | Метод устанавливает таймаут соединения. |  |

**Примеры**

Пример настройки:

```
'http_client_options' =>
	array (
		'value' =>
			array (
				'redirect' => true,//делаем редиректы, если требуется
				'redirectMax' => 10,//но не более 10
				'version' => '1.1'//работаем по протоколу http 1.1
			),
		'readonly' => false,
	),
```

Правильность настроек, можно проверить так (должен быть выведен ваш массив):

```
use Bitrix\Main\Config\Configuration;
print_r(Configuration::getValue("http_client_options"));
```

```
use Bitrix\Main\Web\HttpClient;

$httpClient = new HttpClient();
$httpClient->setHeader('Content-Type', 'application/json', true);
$response = $httpClient->post('http://www.example.com', json_encode(array('x' => 1)));
```

```
use Bitrix\Main\Web\HttpClient;

$httpClient = new HttpClient();
$httpClient->download('http://www.example.com/robots.txt', $_SERVER['DOCUMENT_ROOT'].'/upload/my.txt');
```

```
use Bitrix\Main\Web\HttpClient;
$url = "http://www.example.com"; // отсюда возьмется кука
$url2 = "http://www.example.com/form_request"; // адрес, куда посылать запрос
$post = "val1=true&val2=false"; // запрос строкой, либо массивом

$httpClient = new HttpClient();
$httpClient->query("GET", $url);
$cookie = $httpClient->getCookies()->toArray(); // Кука отдаются объектом -> впихнем ее в массив.

echo "<pre>"; print_r($cookie); echo "</pre>";

$httpClient->setHeader('Content-Type','application/x-www-form-urlencoded');
$httpClient->setCookies($cookie); // Аргумент должен быть массивом!
$response = $httpClient->post($url2, $post);

echo "<pre>"; var_dump($response); echo "</pre>";
```
