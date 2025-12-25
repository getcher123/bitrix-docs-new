# Loader

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/index.php

**Loader** - класс для загрузки необходимых файлов, классов и модулей. Это единственный класс, который включается непосредственно. Используется для подключения всех модулей, кроме **main** и **fileman**.

Аналог старого [CModule](../../../../main/reference/cmodule/index.md).

| Метод | Описание | С версии |
| --- | --- | --- |
| [autoLoad](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/autoload.php) | Метод производит загрузку зарегистрированных для автозагрузки методов |  |
| [getDocumentRoot](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/getdocumentroot.php) | Метод возвращает document root. | 14.0.0 |
| [getLocal](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/getlocal.php) | Метод проверяет существование файла в /local или /bitrix директориях. |  |
| [getPersonal](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/getpersonal.php) | Метод проверяет существование файла в персональной директории. |  |
| [includeModule](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/includemodule.php) | Метод подключает модуль по его имени. |  |
| [includeSharewareModule](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/includesharewaremodule.php) | Метод подключает партнёрский модуль по его имени. | 14.0.2 |
| [registerAutoLoadClasses](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/registerautoloadclasses.php) | Метод регистрирует классы для автозагрузки. |  |
| [registerNamespace](https://dev.1c-bitrix.ru/api_d7/bitrix/main/loader/registernamespace.php) | Метод регистрирует пространство имен. |  |

#### Примеры

```
// D7
use Bitrix\Main\Loader;
Loader::includeModule("iblock");
Loader::includeSharewareModule("eeeeee.tips");
```
