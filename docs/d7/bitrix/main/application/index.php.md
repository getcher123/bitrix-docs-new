# Application

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/index.php

### Описание и примеры

**Application** - абстрактный класс для любых приложений. Любой конкретный класс приложения является наследником этого абстрактного класса.

> Приложение является базовой точкой входа (маршрутизатором) для обращения к глобальным сущностям ядра: соединение с источниками данных, управляемый кеш и т.п. Также приложение содержит глобальные данные, которые относятся к самому сайту и не зависят от конкретного хита. То есть, приложение является неизменяемой частью, не зависящей от конкретного хита.

Обращается к пространству имён

- [\Main\Data](../data/index.php.md);
- [\Main\Diag](../diag/index.php.md);
- [\Main\IO](../io/index.php.md)

Дополнительно о [приложениях](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3511).

#### Примеры

Объект приложения можно получить так:

```
$application = Application::getInstance();
```

Из класса приложения можно получить, например, соединение с БД и **document_root**:

```
$docRoot = Application::getDocumentRoot()
$connection = Application::getConnection();
```

### Методы класса

| Метод | Описание | С версии |
| --- | --- | --- |
| [addBackgroundJob](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/addbackgroundjob.php) | Метод добавляет фоновое задание, выполняющееся после отдачи контента браузеру. | 20.5.0 |
| [getCache](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getcache.php) | Возвращает новый экземпляр объекта кеша |  |
| [getConnection](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getconnection.php) | Возвращает соединение с базой данных указанного имени | 14.0.0 |
| [getConnectionPool](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getconnectionpool.php) | Возвращает объект пула соединений базы данных. | 14.0.0 |
| [getContext](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getcontext.php) | Возвращает содержание текущего соединения. |  |
| [getDocumentRoot](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getdocumentroot.php) | Возвращает document root сервера. |  |
| [getInstance](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getinstance.php) | Возвращает текущий экземпляр приложения. |  |
| [getManagedCache](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getmanagedcache.php) | Возвращает управление управляемым кешем. |  |
| [getPersonalRoot](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/getpersonalroot.php) | Возвращает путь к персональной директории. |  |
| [getTaggedCache](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/gettaggedcache.php) | Метод управляет тегированным кешем. | 14.0.18 |
| [initializeBasicKernel](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/initializebasickernel.php) | Метод производит первичную инициализацию ядра. |  |
| [initializeExtendedKernel](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/initializeextendedkernel.php) | Метод производит полную инициализацию ядра. |  |
| [isUtfMode](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/isutfmode.php) | Метод вернёт true если сервер работает в utf-8 |  |
| [resetAccelerator](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/resetaccelerator.php) | Метод производит перезапуск акселлератора. |  |
| [setContext](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/setcontext.php) | Метод изменяет содержание текущего запроса. |  |
| [start](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/start.php) | Метод запускает выполнение запроса. |  |
