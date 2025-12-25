# Группы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 13766 — Маршруты](lesson_13766.md)
- [Следующий: 13770 — Генерация ссылок →](lesson_13770.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=13768

### Объединение в группы

При схожих признаках у нескольких маршрутов рекомендуется объединять их в группы:

```
$routes->group(function (RoutingConfigurator $routes) {
        $routes->get('/path1, function () {});
        $routes->get('/path2, function () {});
        $routes->get('/path3, function () {});
});
```

Само по себе объединение не влияет на поведение системы и имеет смысл именно при наличии общих признаков: параметры, prefix или name, которые будут рассмотрены ниже.

### Параметры группы

Если у нескольких маршрутов есть общий параметр, то имеет смысл вынести его на уровень группы. Это позволит не описывать параметр отдельно для каждого маршрута:

```
$routes
        ->where('serviceCode', '[a-z0-9]+')
        ->group(function (RoutingConfigurator $routes) {
        $routes->get('/{serviceCode}/info', [ServicesController::class, 'info']);
        $routes->get('/{serviceCode}/stats', [ServicesController::class, 'stats']);
});
```

### prefix группы

Если у маршрутов совпадает начало адреса, то вынесите его общим для группы:

```
$routes->prefix('about')->group(function (RoutingConfigurator $routes) {
        $routes->get('company', function () {});
        $routes->get('personal', function () {});
        $routes->get('contact', function () {});
});
```

В примере выше адреса маршрутов будут восприняты как /about/company, /about/personal и /about/contact, таким образом не придется дублировать общую часть.

### name группы

Похожим на **prefix** образом работает формирование общей части в имени роутов:

```
$routes
     ->prefix('about')
     ->name('about_')
     ->group(function (RoutingConfigurator $routes) {
        $routes->name('company')->get('company', function () {});
        $routes->name('personal')->get('personal', function () {});
        $routes->name('contact')->get('contact', function () {});
    })
;
```

В примере выше будут установлены имена маршрутов *about_company*, *about_personal* и *about_contact*.
