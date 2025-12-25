# Генерация ссылок

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 13768 — Группы](lesson_13768.md)
- [Следующий: 15330 — Логгеры →](lesson_15330.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=13770

### Маршруты с именем

При описании маршрута задайте для него уникальное имя:

```
$routes->get('/countries/{country}', function () {
        return 'some output';
})->name('country_detail');
```

И используйте это имя для генерации ссылки:

```
$router = \Bitrix\Main\Application::getInstance()->getRouter();
$url = $router->route('country_detail', ['country' => 'Australia']);

// $url: /countries/Australia
```

Имена выступают в роли уникальных идентификаторов. Если понадобится поменять формат ссылки, например поменять статическую часть:

```
- $routes->get('/countries/{country}', function () {
+ $routes->get('/страны/{country}', function () {
        return 'some output';
})->name('country_detail');
```

То в этом случае не придется менять все ссылки на данный маршрут, поскольку они используют именно *name* для адресации.

### Маршруты без имени

Если для маршрута не задано уникальное имя, то допустимо в ссылке указывать его адрес вручную. При наличии GET параметров может быть полезен хелпер *\Bitrix\Main\Routing\Router::url()*:

```
$country = 'Australia';
$router = \Bitrix\Main\Application::getInstance()->getRouter();
$url = $router->url("/contries/{$country}", [
        'showMoreDetails' => 1
]);

// $url: /contries/Australia?showMoreDetails=1
```
