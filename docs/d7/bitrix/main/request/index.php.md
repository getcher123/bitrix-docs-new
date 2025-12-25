# Request

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/request/index.php

### Описание и методы

**Request** - абстрактный класс. Объект запроса позволяет получить данные о текущем запросе: метод и протокол, запрошенный URL, переданные параметры и т.п. Расширение класса [\Bitrix\Main\Type\ParameterDictionary](https://dev.1c-bitrix.ru/api_d7/bitrix/main/type/parameterdictionary/index.php).

Обращается к пространству имён:

- [\Main\Type](../type/index.php.md);
- [\Main\IO](../io/index.php.md)
- [\Main\Text](../text/index.php.md);

| Метод | Описание | С версии |
| --- | --- | --- |
| [isAjaxRequest](https://dev.1c-bitrix.ru/api_d7/bitrix/main/request/isajaxrequest.php) | Метод возвращает true если текущий запрос - AJAX. | 15.5.0 |

### Примеры

```
$request = $context->getRequest();
// Или более краткая форма:
$request = Context::getCurrent()->getRequest();
```

Параметры запроса:

```
$value = $request->get("param");       // получение параметра GET или POST
$value = $request["param"];            // получение параметра GET или POST
$value = $request->getQuery("param");  // получение GET-параметра
$values = $request->getQueryList();    // получение списка GET-параметров
$value = $request->getPost("param");   // получение POST-параметра
$values = $request->getPostList();     // получение списка POST-параметров
$value = $request->getFile("param");   // получение загруженного файла
$values = $request->getFileList();     // получение списка загруженных файлов
$value = $request->getCookie("param"); // получение значения кука
$values = $request->getCookieList();   // получение списка кукисов
```

Данные о запросе:

```
$method = $request->getRequestMethod(); // получение метода запроса
$flag = $request->isPost();             // true - POST-запрос, иначе false
$flag = $request->isAjaxRequest();      // true - AJAX-запрос, иначе false
$flag = $request->isHttps();            // true - HTTPS-запрос, иначе false
```

Данные о запрошенной странице:

```
$flag = $request->isAdminSection();            // true - находимся в админке, иначе false
$requestUri = $request->getRequestUri();       // Запрошенный адрес (напр. "/catalog/category/?param=value")
$requestPage = $request->getRequestedPage();   // Запрошенная страница (напр. "/catalog/category/index.php")
$rDir  = $request->getRequestedPageDirectory();// Директория запрошенной страницы (напр. "/catalog/category")
```
