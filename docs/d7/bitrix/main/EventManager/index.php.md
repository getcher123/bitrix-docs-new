# EventManager

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/EventManager/index.php

**EventManager** - класс кратко- и долгосрочной регистрации обработчиков событий.  Класс реализует паттерн **Singleton** (Одиночка), обращаться к нему нужно через *getInstance()*.

> В обработчики, зарегистрированные с помощью *\Bitrix\Main\EventManager::AddEventHandler*, в качестве аргумента будет передан объект события (*Bitrix\Main\Event*). Если хотите, чтобы передавались старые аргументы, нужно использовать *\Bitrix\Main\EventManager::addEventHandlerCompatible*. Аналогично с *\Bitrix\Main\EventManager::registerEventHandler* и *\Bitrix\Main\EventManager::registerEventHandlerCompatible*.

Аналогами класса в старом ядре являются функции:

[RegisterModuleDependences](http://dev.1c-bitrix.ru/api_help/main/functions/module/registermoduledependences.php),

[UnRegisterModuleDependences](http://dev.1c-bitrix.ru/api_help/main/functions/module/unregistermoduledependences.php),

[AddEventHandler](../../../../main/functions/module/addeventhandler.md),

[RemoveEventHandler](http://dev.1c-bitrix.ru/api_help/main/functions/module/removeeventhandler.php),

[GetModuleEvents](http://dev.1c-bitrix.ru/api_help/main/functions/module/getmoduleevents.php).

#### Примеры

```
//версия 1
$eventManager = \Bitrix\Main\EventManager::getInstance();
$eventManager->registerEventHandlerCompatible("module","event","module2","class","function");
```

```
//версия 2 для событий в DataManager например
$eventManager = \Bitrix\Main\EventManager::getInstance();
$eventManager->registerEventHandler("module","event","module2","class","function");
```

Свои обработчики в своих модулях

```
$arMacros["PRODUCTS"]  = "";
$basketId = "10";
```

```
$event = new \Bitrix\Main\Event("mymodule", "OnMacrosProductCreate",array($basketId));
	$event->send();
	if ($event->getResults()){
		foreach($event->getResults() as $evenResult){
			if($evenResult->getResultType() == \Bitrix\Main\EventResult::SUCCESS){
			$arMacros["PRODUCTS"] = $evenResult->getParameters();
			}
		}
}
```

```
$eventManager = \Bitrix\Main\EventManager::getInstance();
$eventManager->addEventHandler("mymodule", "OnMacrosProductCreate", "OnMacrosProductCreate");

function OnMacrosProductCreate(\Bitrix\Main\Event $event){
	$arParam = $event->getParameters();
	$basketId = $arParam[0];
	$result = new \Bitrix\Main\EventResult(1,$basketId);
	return $result;
}
```

```
use Bitrix\Main\EventManager;

$handler = EventManager::getInstance()->addEventHandler(
	"main",
	"OnUserLoginExternal",
	array(
		"Intervolga\\Test\\EventHandlers\\Main",
		"onUserLoginExternal"
	)
);
EventManager::getInstance()->removeEventHandler(
	"main",
	"OnUserLoginExternal",
	$handler
);
EventManager::getInstance()->registerEventHandler(
	"main",
	"OnProlog",
	$this->MODULE_ID,
	"Intervolga\\Test\\EventHandlers",
	"onProlog"
);
EventManager::getInstance()->unRegisterEventHandler(
	"main",
	"OnProlog",
	$this->MODULE_ID,
	"Intervolga\\Test\\EventHandlers",
	"onProlog"
);
$handlers = EventManager::getInstance()->findEventHandlers("main", "OnProlog");
```
