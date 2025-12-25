# Uri

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/index.php

### Описание и примеры

**Uri** - класс для работы со ссылками.

Аналог [CMain::GetCurPageParam](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getcurpageparam.php) и [DeleteParam](http://dev.1c-bitrix.ru/api_help/main/functions/other/deleteparam.php) в старом ядре. Работа с классом `\Bitrix\Main\Web\Uri` несколько сложнее чем в старом ядре: это следствие того, что в этом классе каждый метод отвечает только за один аспект работы класса.

**Примеры**

```
use Bitrix\Main\Application;
use Bitrix\Main\Web\Uri;

$request = Application::getInstance()->getContext()->getRequest();
$uriString = $request->getRequestUri();
$uri = new Uri($uriString);
$uri->deleteParams(array("baz"));
$uri->addParams(array("foo" => "bar"));
$redirect = $uri->getUri();
```

### Методы

| Метод | Описание | С версии |
| --- | --- | --- |
| [addParams](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/addparams.php) | Метод добавляет параметры в запрос или заменяет существующие параметры. | 15.5.10 |
| [deleteParams](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/deleteparams.php) | Метод удаляет параметры из запроса. | 15.5.10 |
| [getFragment](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getfragment.php) | Метод возвращает фрагмент. | 14.0.15 |
| [getHost](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/gethost.php) | Метод возвращает хост. | 14.0.15 |
| [getLocator](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getlocator.php) | Метод возвращает URI без фрагмента. | 15.5.10 |
| [getPass](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getpass.php) | Метод возвращает пароль. | 14.0.15 |
| [getPath](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getpath.php) | Метод возвращает путь. | 14.0.15 |
| [getPathQuery](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getpathquery.php) | Метод возвращает путь с запросом. | 14.0.15 |
| [getPort](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getport.php) | Метод возвращает номер порта. | 14.0.15 |
| [getQuery](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getquery.php) | Метод возвращает запрос | 14.0.15 |
| [getScheme](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getscheme.php) | Метод возвращает схему. | 14.0.15 |
| [getUri](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/geturi.php) | Метод возвращает URI с фрагментом, если он имеется. | 15.5.10 |
| [getUser](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/getuser.php) | Метод возвращает пользователя. | 14.0.15 |
| [setHost](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/sethost.php) | Метод устанавливает хост | 14.0.15 |
| [setPath](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/setpath.php) | Метод устанавливает путь. | 15.5.10 |
| [setUser](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/setuser.php) | Метод устанавливает пользователя. | 16.5.7 |
| [setPass](https://dev.1c-bitrix.ru/api_d7/bitrix/main/web/uri/setpass.php) | Метод устанавливает пароль. | 16.5.7 |
