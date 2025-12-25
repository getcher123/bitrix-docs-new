# HttpResponse

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/index.php

Класс `\Bitrix\Main\HttpResponse` - это базовый класс для всех типов http-ответа. Он является контейнером для:

- Http-заголовков [\Bitrix\Main\Web\HttpHeaders](../web/httpheaders/index.php.md)

  - ```
    \Bitrix\Main\HttpResponse::addHeader(
    	$name,
    	$value
    )
    ```
  - ```
    \Bitrix\Main\HttpResponse::setHeaders(
    	Web\HttpHeaders $headers
    )
    ```
  - ```
    \Bitrix\Main\HttpResponse::getHeaders(
    )
    ```
- Cookies [\Bitrix\Main\Web\Cookie](../web/cookie/index.php.md)

  - ```
    \Bitrix\Main\HttpResponse::addCookie(
    	Web\Cookie $cookie,
    	$replace,
    	$checkExpires)
    ```
  - ```
    \Bitrix\Main\HttpResponse::getCookies(
    )
    ```
- Контента, тела ответа `\Bitrix\Main\HttpResponse::$content`

  - ```
    \Bitrix\Main\HttpResponse::setContent(
    	$content
    )
    ```
  - ```
    \Bitrix\Main\HttpResponse::getContent(
    )
    ```

С помощью `\Bitrix\Main\HttpResponse` можно формировать ответы приложения любого необходимого типа и содержания.

Примеры использования:

```
$response = new \Bitrix\Main\HttpResponse();
$response->addHeader('Content-Type', 'text/plain');
$response->addCookie(new \Bitrix\Main\Web\Cookie('Biscuits', 'Yubileynoye'));
$response->setContent('Hello, world!');
```
