# Context

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/index.php

### Описание

**Context** - методы работы с информацией о текущем запросе: тип, параметры и их значения.

При инициализации приложения создаётся контекст - объект [HttpContext](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpcontext/index.php), который как контейнер хранит в себе информацию о запросе: параметры запроса, серверное окружение, битриксовое окружение (язык, id сайта), ответ на запрос.  То есть это изменяемая часть, зависящая от текущего хита.

Обращается к пространству имён:

- [\Main](../index.php.md);

Чтобы получить контекст текущего хита нужно выполнить:

```
$context = Application::getInstance()->getContext();
// Или более краткая форма:
$context = Context::getCurrent();
```

**Примеры**:

```
$request = $context->getRequest(); // объект Request
$server = $context->getServer();   // объект Server
$siteId = $context->getSite();     // ID текущего сайта ("s1")
$langId = $context->getLanguage(); // ID текущего языка ("ru")
```

Дополнительно о [контексте](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3511).

### Список методов

| Метод | Описание | С версии |
| --- | --- | --- |
| [Конструктор](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/__construct.php) | Метод создаёт новый экземпляр контекста |  |
| [getApplication](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getapplication.php) | Метод возвращает обратную ссылку на приложение |  |
| [getCulture](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getculture.php) | Метод возвращает региональные культурные настройки для контекста. |  |
| [getCurrent](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getcurrent.php) | Метод возвращает текущий экземпляр контекста. |  |
| [getLanguage](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getlanguage.php) | Метод возвращает текущую языковую раскладку. |  |
| [getRequest](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getrequest.php) | Метод возвращает запрошенный объект контекста. |  |
| [getResponse](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getresponse.php) | Метод возвращает объект отклика контекста. |  |
| [getServer](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getserver.php) | Метод возвращает серверный объект контекста. |  |
| [getSite](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/getsite.php) | Метод возвращает текущий сайт. | 14.0.0 |
| [initialize](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/initialize.php) | Метод инициализирует контекст по запросу и отклику объекта. |  |
| [setCulture](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/setculture.php) | Метод устанавливает региональные культурные настройки для контекста. |  |
| [setLanguage](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/setlanguage.php) | Метод устанавливает язык контекста. |  |
| [setSite](https://dev.1c-bitrix.ru/api_d7/bitrix/main/context/setsite.php) | Метод устанавливает сайт для контекста. | 14.0.0 |
