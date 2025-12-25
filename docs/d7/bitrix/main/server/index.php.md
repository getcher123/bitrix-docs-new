# Server

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/index.php

### Описание и методы

**Server** - объект сервера позволяет получить информацию из массива $_SERVER, а также некоторую другую информацию. Расширение класса [Main\Type\ParameterDictionary](https://dev.1c-bitrix.ru/api_d7/bitrix/main/type/parameterdictionary/index.php).

Обращается к пространству имён:

- [Bitrix\Main\Type\ParameterDictionary](https://dev.1c-bitrix.ru/api_d7/bitrix/main/type/parameterdictionary/index.php);

| Метод | Описание | С версии |
| --- | --- | --- |
| [Конструктор](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/__construct.php) | Метод создаёт новый объект сервера. |  |
| [getServerPort](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getserverport.php) | Метод возвращает порт сервера. |  |
| [getServerName](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getservername.php) | Метод возвращает имя сервера. |  |
| [getServerAddr](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getserveraddr.php) | Метод возвращает адрес сервера. |  |
| [getScriptName](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getscriptname.php) | Метод возвращает SCRIPT_NAME. |  |
| [getRequestUri](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getrequesturi.php) | Метод возвращает запрошенный uri |  |
| [getRequestMethod](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getrequestmethod.php) | Метод возвращает запрошенный метод. |  |
| [getPhpSelf](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getphpself.php) | Метод возвращает PHP_SELF. |  |
| [getPersonalRoot](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getpersonalroot.php) | Метод возвращает установленную папку `root` |  |
| [getHttpHost](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/gethttphost.php) | Метод возвращает http хост сервера |  |
| [getDocumentRoot](https://dev.1c-bitrix.ru/api_d7/bitrix/main/server/getdocumentroot.php) | Метод возвращает DOCUMENT_ROOT сервера. |  |

### Пример

```
$server = $context->getServer();
// Или более краткая форма:
$server = Context::getCurrent()->getServer();
```

```
$server->getDocumentRoot(); // DOCUMENT_ROOT
$server->getPersonalRoot(); // BX_PERSONAL_ROOT ("/bitrix")
$server->getHttpHost();     // HTTP_HOST
$server->getServerName();   // SERVER_NAME
$server->getServerAddr();   // SERVER_ADDR
$server->getServerPort();   // SERVER_PORT
$server->getRequestUri();   // REQUEST_URI
$server->getRequestMethod();// REQUEST_METHOD
$server->getPhpSelf();      // PHP_SELF
$server->getScriptName();   // SCRIPT_NAME
$server->get('HTTP_ACCEPT');// Любое значение из $_SERVER
```
