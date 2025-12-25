# HttpRequest

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/index.php

### Описание и пример

**HttpRequest** - Класс управляет объектом **Request**, содержащим информацию о текущем запросе - его тип, параметры и их значения: класс "запроса к серверу". Класс позволяет избавиться от глобальных [переменных](http://dev.1c-bitrix.ru/api_help/main/general/magic_vars.php) в коде, используемых в старом ядре.

**Примеры**

Конструировать объект разработчику не нужно, получить его можно через приложение и контекст:

```
use Bitrix\Main\Application;
$request = Application::getInstance()->getContext()->getRequest();

$name = $request->getPost("name");
$email = htmlspecialchars($request->getQuery("email"));
```

### Методы

| Метод | Описание | С версии |
| --- | --- | --- |
| [Конструктор](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/__construct.php) | Метод создаёт новый объект **HttpRequest**. |  |
| [addFilter](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/addfilter.php) | Метод применяет фильтр к данным запроса с сохранением оригинальных значений. | 14.0.0 |
| [getCookie](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getcookie.php) | Метод возвращает параметры COOKIES из текущего запроса. |  |
| [getCookieList](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getcookielist.php) | Метод возвращает список параметров COOKIES текущего запроса. |  |
| [getHttpHost](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/gethttphost.php) | метод возвращает узел переменной сервера без номера порта. |  |
| [getPost](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getpost.php) | метод возвращает POST параметры текущего запроса. |  |
| [getPostList](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getpostlist.php) | Метод возвращает список POST параметров текущего запроса. |  |
| [getQuery](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getquery.php) | Метод возвращает GET параметр текущего запроса. |  |
| [getQueryList](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getquerylist.php) | Метод возвращает список GET параметров текущего запроса. |  |
| [getRequestedPage](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getrequestedpage.php) | Метод возвращает текущую страницу, полученную из запрошенного URI. |  |
| [getScriptFile](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getscriptfile.php) | Метод возвращает файл скрипта при необходимости откорректированный посредством **urlrewrite.php** или файл **virtual_file_system.php**. | 14.9.2 |
| [getSystemParameters](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getsystemparameters.php) | Метод возвращает массив с предопределёнными параметрами запроса. | 15.5.10 |
| [getUserAgent](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getuseragent.php) | Метод возвращает запрошенный заголовок юзер-агента HTTP. |  |
| [getDecodedUri](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getdecodeduri.php) | Метод возвращает расшифрованный URL | 14.9.4 |
| [getFile](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getfile.php) | Метод возвращает параметры FILES текущего запроса. |  |
| [getFileList](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getfilelist.php) | Метод возвращает список параметров FILES текущего запроса. |  |
| [getInput](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/getinput.php) | Метод возвращает первичные запрошенные данные. | 16.5.8 |
