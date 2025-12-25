# Быстрый справочник 1C-Bitrix API

Решения типовых задач с примерами кода и ссылками на документацию.

---

## 📋 Содержание

- [Информационные блоки](#информационные-блоки)
- [Интернет-магазин](#интернет-магазин)
- [Пользователи](#пользователи)
- [Файлы и изображения](#файлы-и-изображения)
- [События](#события)
- [База данных](#база-данных)
- [Кэширование](#кэширование)
- [Bitrix24 REST API](#bitrix24-rest-api)

---

## Информационные блоки

### Получить список элементов

**Класс:** `CIBlockElement`  
**Метод:** `GetList`  
**Документация:** [iblock/classes/ciblockelement/getlist.md](./iblock/classes/ciblockelement/getlist.md)

```php
<?php
CModule::IncludeModule("iblock");

$arSelect = ["ID", "NAME", "PROPERTY_PRICE"];
$arFilter = ["IBLOCK_ID" => 1, "ACTIVE" => "Y"];
$arSort = ["SORT" => "ASC"];

$res = CIBlockElement::GetList($arSort, $arFilter, false, false, $arSelect);
while($ob = $res->GetNextElement()) {
    $arFields = $ob->GetFields();
    $arProps = $ob->GetProperties();
}
?>
```

---

### Добавить элемент

**Класс:** `CIBlockElement`  
**Метод:** `Add`  
**Документация:** [iblock/classes/ciblockelement/add.md](./iblock/classes/ciblockelement/add.md)

```php
<?php
$el = new CIBlockElement;

$arFields = [
    "IBLOCK_ID" => 1,
    "NAME" => "Название элемента",
    "ACTIVE" => "Y",
    "PROPERTY_VALUES" => [
        "PRICE" => 1000,
        "ARTICLE" => "ART-001"
    ]
];

if($ID = $el->Add($arFields)) {
    echo "Элемент добавлен с ID: " . $ID;
} else {
    echo "Ошибка: " . $el->LAST_ERROR;
}
?>
```

---

### Обновить элемент

**Класс:** `CIBlockElement`  
**Метод:** `Update`  
**Документация:** [iblock/classes/ciblockelement/update.md](./iblock/classes/ciblockelement/update.md)

```php
<?php
$el = new CIBlockElement;

$arFields = [
    "NAME" => "Новое название",
    "ACTIVE" => "N"
];

if($el->Update($ELEMENT_ID, $arFields)) {
    echo "Элемент обновлен";
} else {
    echo "Ошибка: " . $el->LAST_ERROR;
}
?>
```

---

### Удалить элемент

**Класс:** `CIBlockElement`  
**Метод:** `Delete`  
**Документация:** [iblock/classes/ciblockelement/delete.md](./iblock/classes/ciblockelement/delete.md)

```php
<?php
if(CIBlockElement::Delete($ELEMENT_ID)) {
    echo "Элемент удален";
}
?>
```

---

### Получить свойства элемента

**Класс:** `CIBlockElement`  
**Метод:** `GetProperty`  
**Документация:** [iblock/classes/ciblockelement/getproperty.md](./iblock/classes/ciblockelement/getproperty.md)

```php
<?php
$res = CIBlockElement::GetProperty($IBLOCK_ID, $ELEMENT_ID, "sort", "asc");
while($ob = $res->GetNext()) {
    echo $ob["CODE"] . ": " . $ob["VALUE"];
}
?>
```

---

### Получить список разделов

**Класс:** `CIBlockSection`  
**Метод:** `GetList`  
**Документация:** [iblock/classes/ciblocksection/getlist.md](./iblock/classes/ciblocksection/getlist.md)

```php
<?php
$arFilter = ["IBLOCK_ID" => 1, "ACTIVE" => "Y"];
$res = CIBlockSection::GetList(["SORT" => "ASC"], $arFilter);
while($arSection = $res->GetNext()) {
    echo $arSection["NAME"];
}
?>
```

---

## Интернет-магазин

### Добавить товар в корзину

**Класс:** `CSaleBasket`  
**Метод:** `Add`  
**Документация:** [sale/classes](./sale/classes/index.md)

```php
<?php
CModule::IncludeModule("sale");
CModule::IncludeModule("catalog");

$arFields = [
    "PRODUCT_ID" => $PRODUCT_ID,
    "QUANTITY" => 1,
    "PRICE" => 1000,
    "CURRENCY" => "RUB",
    "LID" => SITE_ID,
    "NAME" => "Название товара"
];

CSaleBasket::Add($arFields);
?>
```

---

### Получить корзину

**Класс:** `CSaleBasket`  
**Метод:** `GetList`  
**Документация:** [sale/classes](./sale/classes/index.md)

```php
<?php
$arFilter = ["FUSER_ID" => CSaleBasket::GetBasketUserID(), "LID" => SITE_ID];
$res = CSaleBasket::GetList([], $arFilter);
while($arItem = $res->Fetch()) {
    echo $arItem["NAME"] . " - " . $arItem["PRICE"];
}
?>
```

---

### Создать заказ

**Класс:** `CSaleOrder`  
**Метод:** `Add`  
**Документация:** [sale/classes](./sale/classes/index.md)

```php
<?php
$arFields = [
    "LID" => SITE_ID,
    "PERSON_TYPE_ID" => 1,
    "USER_ID" => $USER->GetID(),
    "CURRENCY" => "RUB",
    "PRICE" => 1000
];

$ORDER_ID = CSaleOrder::Add($arFields);
?>
```

---

### Получить заказ

**Класс:** `CSaleOrder`  
**Метод:** `GetByID`  
**Документация:** [sale/classes](./sale/classes/index.md)

```php
<?php
$arOrder = CSaleOrder::GetByID($ORDER_ID);
echo "Заказ №" . $arOrder["ID"] . " на сумму " . $arOrder["PRICE"];
?>
```

---

### Изменить статус заказа

**Класс:** `CSaleOrder`  
**Метод:** `StatusOrder`  
**Документация:** [sale/classes](./sale/classes/index.md)

```php
<?php
CSaleOrder::StatusOrder($ORDER_ID, "F"); // F - выполнен
?>
```

---

## Пользователи

### Авторизация пользователя

**Класс:** `CUser`  
**Метод:** `Login`  
**Документация:** [main/reference/cuser](./main/reference/cuser/index.md)

```php
<?php
global $USER;

$arAuthResult = $USER->Login($login, $password, "Y");
if($arAuthResult === true) {
    echo "Авторизация успешна";
} else {
    echo $arAuthResult["MESSAGE"];
}
?>
```

---

### Регистрация пользователя

**Класс:** `CUser`  
**Метод:** `Register`  
**Документация:** [main/reference/cuser](./main/reference/cuser/index.md)

```php
<?php
$user = new CUser;

$arFields = [
    "LOGIN" => "user@example.com",
    "EMAIL" => "user@example.com",
    "PASSWORD" => "password",
    "CONFIRM_PASSWORD" => "password",
    "NAME" => "Имя",
    "LAST_NAME" => "Фамилия"
];

$ID = $user->Register($arFields);
if($ID > 0) {
    echo "Пользователь зарегистрирован";
} else {
    echo $user->LAST_ERROR;
}
?>
```

---

### Получить пользователя

**Класс:** `CUser`  
**Метод:** `GetByID`  
**Документация:** [main/reference/cuser](./main/reference/cuser/index.md)

```php
<?php
$rsUser = CUser::GetByID($USER_ID);
$arUser = $rsUser->Fetch();
echo $arUser["NAME"] . " " . $arUser["LAST_NAME"];
?>
```

---

### Проверить авторизацию

**Класс:** `CUser`  
**Метод:** `IsAuthorized`  
**Документация:** [main/reference/cuser](./main/reference/cuser/index.md)

```php
<?php
global $USER;

if($USER->IsAuthorized()) {
    echo "Пользователь авторизован";
} else {
    echo "Гость";
}
?>
```

---

### Обновить пользователя

**Класс:** `CUser`  
**Метод:** `Update`  
**Документация:** [main/reference/cuser](./main/reference/cuser/index.md)

```php
<?php
$user = new CUser;

$arFields = [
    "NAME" => "Новое имя",
    "PERSONAL_PHONE" => "+7 (999) 123-45-67"
];

$user->Update($USER_ID, $arFields);
?>
```

---

## Файлы и изображения

### Загрузить файл

**Класс:** `CFile`  
**Метод:** `SaveFile`  
**Документация:** [main/reference/cfile](./main/reference/cfile/index.md)

```php
<?php
$arFile = $_FILES["FILE"];
$FILE_ID = CFile::SaveFile($arFile, "upload");
?>
```

---

### Получить путь к файлу

**Класс:** `CFile`  
**Метод:** `GetPath`  
**Документация:** [main/reference/cfile](./main/reference/cfile/index.md)

```php
<?php
$filePath = CFile::GetPath($FILE_ID);
echo '<img src="' . $filePath . '">';
?>
```

---

### Изменить размер изображения

**Класс:** `CFile`  
**Метод:** `ResizeImageGet`  
**Документация:** [main/reference/cfile](./main/reference/cfile/index.md)

```php
<?php
$arResizeImage = CFile::ResizeImageGet(
    $FILE_ID,
    ["width" => 300, "height" => 200],
    BX_RESIZE_IMAGE_PROPORTIONAL
);

echo '<img src="' . $arResizeImage["src"] . '">';
?>
```

---

### Удалить файл

**Класс:** `CFile`  
**Метод:** `Delete`  
**Документация:** [main/reference/cfile](./main/reference/cfile/index.md)

```php
<?php
CFile::Delete($FILE_ID);
?>
```

---

## События

### Добавить обработчик события

**Класс:** `EventManager`  
**Метод:** `addEventHandler`  
**Документация:** [Bitrix\\Main\\EventManager](./d7/bitrix/main/EventManager/index.php.md)

```php
<?php
$eventManager = \Bitrix\Main\EventManager::getInstance();

$eventManager->addEventHandler(
    "iblock",
    "OnAfterIBlockElementAdd",
    ["MyClass", "OnAfterIBlockElementAddHandler"]
);
?>
```

---

### Вызвать событие

**Класс:** `EventManager`  
**Метод:** `send`  
**Документация:** [Bitrix\\Main\\EventManager](./d7/bitrix/main/EventManager/index.php.md)

```php
<?php
$event = new \Bitrix\Main\Event("mymodule", "OnCustomEvent", ["param" => "value"]);
$event->send();
?>
```

---

## База данных

### Выполнить запрос

**Класс:** `CDatabase`  
**Метод:** `Query`  
**Документация:** [main/reference](./main/reference/index.md)

```php
<?php
global $DB;

$strSql = "SELECT * FROM b_user WHERE ID = " . intval($ID);
$res = $DB->Query($strSql);
while($arUser = $res->Fetch()) {
    echo $arUser["LOGIN"];
}
?>
```

---

### Подготовленный запрос

**Класс:** `Connection`  
**Метод:** `query`  
**Документация:** [Bitrix\\Main\\DB](./d7/bitrix/main/db/index.php.md)

```php
<?php
use Bitrix\Main\Application;

$connection = Application::getConnection();
$sql = "SELECT * FROM b_user WHERE ID = ?";
$result = $connection->query($sql, [$ID]);

while($row = $result->fetch()) {
    echo $row["LOGIN"];
}
?>
```

---

## Кэширование

---

## Bitrix24 REST API

**Точка входа:** [bitrix24_api/index.md](./bitrix24_api/index.md)

Быстрее всего искать по полному имени метода:

```bash
rg -n \"\\bcrm\\.lead\\.add\\b\" docs/bitrix24_api/
rg -n \"\\btasks\\.task\\.add\\b\" docs/bitrix24_api/
```

### Использовать кэш

**Класс:** `CPHPCache`  
**Метод:** `InitCache`, `StartDataCache`, `EndDataCache`  
**Документация:** [main/reference](./main/reference/index.md)

```php
<?php
$cache = new CPHPCache;
$cache_time = 3600;
$cache_id = "my_cache_id";
$cache_path = "/my_cache/";

if($cache->InitCache($cache_time, $cache_id, $cache_path)) {
    $arResult = $cache->GetVars();
} else {
    $cache->StartDataCache();
    
    // Получение данных
    $arResult = ["data" => "value"];
    
    $cache->EndDataCache($arResult);
}
?>
```

---

### Очистить кэш

**Класс:** `CPHPCache`  
**Метод:** `CleanDir`  
**Документация:** [main/reference](./main/reference/index.md)

```php
<?php
$cache = new CPHPCache;
$cache->CleanDir("/my_cache/");
?>
```

---

## 🔗 Дополнительные ресурсы

- **Полный индекс:** [INDEX.md](./INDEX.md)
- **Описание модулей:** [MODULES.md](./MODULES.md)
- **Гайдлайны для AI:** [AGENT.md](./AGENT.md)
- **Главная страница:** [api_documentation.md](./api_documentation.md)

---

**Версия:** 4.0  
**Дата:** 23.12.2025  
**Примеров:** 30+
