# AddEventHandler


### Описание и параметры


```
AddEventHandler(
	string from_module_id,
	string MESSAGE_ID,
	mixed callback,
	int sort = 100,
	mixed full_path = false
);
```

Регистрирует произвольный обработчик *callback* события *MESSAGE_ID* модуля *from_module_id*. Если указан полный путь к файлу с обработчиком *full_path*, то он будет автоматически подключен перед вызовом обработчика. Вызывается на каждом хите и работает до момента окончания работы скрипта.


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| *from_module_id* | Идентификатор модуля который будет инициировать событие. |
| *MESSAGE_ID* | Идентификатор события. |
| *callback* | Название функции обработчика. Если это метод класса, то массив вида Array(класс(объект), название метода). |
| *sort* | Очередность (порядок), в котором выполняется данный обработчик (обработчиков данного события может быть больше одного). Необязательный параметр, по умолчанию равен 100. |
| *full_path* | Полный путь к файлу для подключения при возникновении события перед вызовом *callback*. |


#### Примечание

Все зарегистрированные обработчики хранятся в глобальной переменной $MAIN_MODULE_EVENTS.

---
### Аналоги в ядре D7

У функции есть **аналоги в ядре D7**.

Обратите внимание, порядок параметров в них отличается: подключение файла выполняется перед сортировкой.



- `Bitrix\Main\EventManager::addEventHandler` — регистрирует обработчик события. В качестве аргумента передается объект события Bitrix\Main\Event. ``` EventManager::addEventHandler( $fromModuleId, $eventType, $callback, $includeFile = false, $sort = 100 ) ```
- `Bitrix\Main\EventManager::addEventHandlerCompatible` — регистрирует обработчик события со старыми аргументами. ``` EventManager::addEventHandlerCompatible( $fromModuleId, $eventType, $callback, $includeFile = false, $sort = 100 ) ```

---
### Смотрите также


- **Связи и взаимодействие модулей** RegisterModuleDependences

---
### Примеры использования


```
<?
// скрипт в файле /bitrix/php_interface/init.php
AddEventHandler("main", "OnBeforeUserLogin", Array("MyClass", "BeforeLogin"));class MyClass
{
	function BeforeLogin(&$arFields)
	{
		if(strtolower($arFields["LOGIN"])=="guest")
		{
			global $APPLICATION;
			$APPLICATION->throwException("Пользователь с именем входа Guest не может быть авторизован.");
			return false;
		}
	}
}
?>
```

---




| ![image](../images/7dd82aba60.gif) 0 **Андрей Огибин**01.09.2019 18:16:19 |  |  |
| --- | --- | --- |
| Если нужно передать переменную в обработчик (в данном случае мне нужно было добавить в цепочку навигации NAME из arResult) | Код | ``` AddEventHandler("main", "OnEpilog", function() use ($arResult) { global $APPLICATION; $APPLICATION->AddChainItem($arResult['NAME']); }); ``` |
| Код |  |  |
| ``` AddEventHandler("main", "OnEpilog", function() use ($arResult) { global $APPLICATION; $APPLICATION->AddChainItem($arResult['NAME']); }); ``` |  |  |
|  |  |  |


| ![](../images/de0a211802.jpg) 1 **Роберт Басыров**24.12.2009 15:30:27 |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Задача**: Посчитать количество залогиненных пользователей на сайте на данный момент времени и вывести на экран это число. | Код | ``` AddEventHandler("main", "OnBeforeProlog", "MyUserOnline"); function MyUserOnline() { if($GLOBALS["USER"]->IsAuthorized()) CUser::SetLastActivityDate($GLOBALS["USER"]->GetID()); } ``` | Код | ``` //online status $db = CUser::GetList($by, $order, array("LAST_ACTIVITY"=>120)); while($dba = $db->Fetch()) echo $dba['ID']."<br>"; ``` |
| Код |  |  |  |  |
| ``` AddEventHandler("main", "OnBeforeProlog", "MyUserOnline"); function MyUserOnline() { if($GLOBALS["USER"]->IsAuthorized()) CUser::SetLastActivityDate($GLOBALS["USER"]->GetID()); } ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` //online status $db = CUser::GetList($by, $order, array("LAST_ACTIVITY"=>120)); while($dba = $db->Fetch()) echo $dba['ID']."<br>"; ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/de0a211802.jpg) 6 **Роберт Басыров**21.04.2009 15:11:01 |  |  |
| --- | --- | --- |
| Задача: При авторизации сделать проверку наличия действующих сессий с данным логином, и при наличии сбросить их, что бы в один момент времени был авторизован только 1 клиент. Решение: 1. В файл /bitrix/php_interface/init.php дописываем: \| Код \| \| --- \| \| ``` AddEventHandler("main", "OnAfterUserLogin", "MyOnAfterUserLogin"); AddEventHandler("main", "OnBeforeProlog", "MyOnBeforeProlog"); function MyOnAfterUserLogin($arFields) { global $USER; $USER->Update($USER->GetID(),array("UF_USERSESS"=>session_id())); } function MyOnBeforeProlog($arFields) { global $USER; $arUser = $USER->GetByID($USER->GetID())->Fetch(); if (session_id() != $arUser[UF_USERSESS]) $USER->Logout(); } ``` \| 2. В Настройки -> Настройки продукта -> Пользовательские поля создаем новый элемент следующего вида: Тип данных: Строка Объект: USER Код поля: UF_USERSESS Не показывать в списке: Y Размер поля ввода для отображения: 32 | Код | ``` AddEventHandler("main", "OnAfterUserLogin", "MyOnAfterUserLogin"); AddEventHandler("main", "OnBeforeProlog", "MyOnBeforeProlog"); function MyOnAfterUserLogin($arFields) { global $USER; $USER->Update($USER->GetID(),array("UF_USERSESS"=>session_id())); } function MyOnBeforeProlog($arFields) { global $USER; $arUser = $USER->GetByID($USER->GetID())->Fetch(); if (session_id() != $arUser[UF_USERSESS]) $USER->Logout(); } ``` |
| Код |  |  |
| ``` AddEventHandler("main", "OnAfterUserLogin", "MyOnAfterUserLogin"); AddEventHandler("main", "OnBeforeProlog", "MyOnBeforeProlog"); function MyOnAfterUserLogin($arFields) { global $USER; $USER->Update($USER->GetID(),array("UF_USERSESS"=>session_id())); } function MyOnBeforeProlog($arFields) { global $USER; $arUser = $USER->GetByID($USER->GetID())->Fetch(); if (session_id() != $arUser[UF_USERSESS]) $USER->Logout(); } ``` |  |  |
|  |  |  |
