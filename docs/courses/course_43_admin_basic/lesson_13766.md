# Маршруты

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 21162 — Практика. Внедрение зависимостей](lesson_21162.md)
- [Следующий: 13768 — Группы →](lesson_13768.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=13766

### Запросы

Описание маршрутов начинается с определения метода запроса. Поддерживаются 3 комбинации методов:

```
$routes->get('/countries', function () {
    // сработает только на GET запрос
});

$routes->post('/countries', function () {
    // сработает только на POST запрос
});

$routes->any('/countries', function () {
    // сработает на любой тип запроса
});
```

Для указания произвольного набора методов следует использовать метод **methods**:

```
$routes->any('/countries', function () {
    // сработает на любой тип запроса
})->methods(['GET', 'POST', 'OPTIONS']);
```

### Параметры

Для определения параметра в адресе используются фигурные скобки:

```
$routes->get('/countries/{country}', function ($country) {
        return "country {$country} response";
});
```

По умолчанию для параметров используется паттерн `[^/]+`. Для указания своего критерия используется метод маршрута `where`:

```
$routes->get('/countries/{country}', function ($country) {
        return "country {$country} response";
})->where('country', '[a-zA-Z]+');
```

Если значение параметра может содержать /, то следует использовать паттерн `.*`:

```
$routes->get('/search/{search}', function ($search) {
        return "search {$search} response";
})->where('search', '.*');
```

У параметров могут быть значения по умолчанию, в таком случае им необязательно присутствовать в адресе:

```
$routes->get('/countries/{country}', function ($country) {
        return "country {$country} response";
})->default('country', 'Australia');

// маршрут будет выбран при запросе /countries/
// при этом параметр country будет иметь указанное значение
```

Для удобства можно задать и вовсе не участвующие в формировании адреса параметры:

```
$this->routes->get('/countries/hidden', function ($viewMode) {
        return 'countries response {$viewMode}';
})->default('viewMode', 'custom');
```

Доступ к значениям параметров маршрута получается через параметры контроллера или объект текущего маршрута:

```
$routes->get('/countries/{country}', function ($country) {
        return "country {$country} response";
});

...

$app = \Bitrix\Main\Application::getInstance();
$country = $app->getCurrentRoute()->getParameterValue('country');
```

### Имена

Для удобства и систематизации списка маршрутов присвойте маршруту уникальный идентификатор - имя:

```
$routes->get('/path/with/name', function () {
        return 'path with name';
})->name('some_name');
```

В дальнейшем это позволит обращаться к маршруту при [генерации ссылок](lesson_13770.md).

### Контроллеры

В роутинге поддерживается несколько видов контроллеров:

1. Контроллеры [Bitrix\Main\Engine\Controller](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/controller/index.php):
  ```
  $routes->get('/countries', [SomeController::class, 'view']);
       // будет запущено действие SomeController::viewAction()
  ```
2. Отдельные действия контроллеров *Bitrix\Main\Engine\Contract\RoutableAction*:
  ```
  $routes->get('/countries', SomeAction::class);
  ```
3. Замыкания:
  ```
  $routes->get('/countries/', function () {
           return "countries response";
       });
  ```
  В качестве аргументов возможно указать объект запроса [Bitrix\Main\HttpRequest](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httprequest/index.php), объект текущего маршрута *Bitrix\Main\Routing\Route*, а также именованные параметры маршрута в любой комбинации:
  ```
  use Bitrix\Main\HttpRequest;
  use Bitrix\Main\Routing\Route;
  $routes->get('/countries/{country}', function ($country, HttpRequest $request) {
          return "country {$country} response";
  });
  $routes->get('/countries/{country}', function (Route $route) {
          return "country {$route->getParameterValue('country')} response";
  });
  ```
4. Для обратной совместимости с публичными страницами предусмотрен класс *Bitrix\Main\Routing\Controllers\PublicPageController*:
  ```
   $routes->get('/countries/', new PublicPageController('/countries.php'));
  ```
