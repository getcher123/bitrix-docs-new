# Push and Pull


### Описание

Модуль позволяет организовать транспорт для отправки мгновенных команд. Реализация данного функционала в виде отдельного модуля позволяет любому модулю (в том числе и модулям сторонних разработчиков) используя API отправлять мгновенные нотификации и сообщения клиентам.

Подключение модуля:


```
if (!CModule::IncludeModule('pull'))
	return false;
```

Так же необходимо зарегистрировать зависимость на модуль **Push and Pull**. Регистрация обработчика зависимости:


```
RegisterModuleDependences("pull", "OnGetDependentModule", "your_module", "CYourModulePullSchema", "OnGetDependentModule" );
```

События и push-уведомления они отправляются на серверы рассылки в эпилоге страницы. Если вы отправляете события в ajax-обработчиках, вам необходимо использовать *CMain::FinalActions()* в финале обработчика.

---
### Примеры

**Пример кода класса**


```
class CYourModulePullSchema
{
	public static function OnGetDependentModule()
	{
		return Array(
			'MODULE_ID' => "your_module",
			'USE' => Array("PUBLIC_SECTION")
		);
	}
}
```

Для работы с командами, отправленными из PHP необходимо в вёрстке использовать следующие JS код:

Ловушка для страниц десктопной версии (все события кроме событий online):


```
BX.addCustomEvent("onPullEvent-moduleName", BX.delegate(function(command,params){
	console.log('Events of moduleName', command, params);
}, this));
```

Ловушка для страниц мобильной версии (все события кроме событий online):


```
BX.addCustomEvent("onPull-moduleName", BX.delegate(function(data){
	console.log('Events of moduleName', data.command, data.params);
}, this));
```

**Примечание**: не забывайте сменить в примере "moduleName" на имя вашего модуля.

Пример кода для работы с [PHP классами](classes/index.md) модуля (Pull, Pull Shared, Pull Watch):


```
BX.addCustomEvent("onPullEvent-main", function(module_id,command,params) {
	if (command == 'check')
	{
		console.log('Command from module MAIN - its work!');
	}
});
```

В примере иы подписываемся на событие получение команд (**onPullEvent-moduleName**), moduleName это название вашего модуля, например **main**, в функции получаем command, params которые мы указали при отправке команды из PHP, обрабатываем свои команды с учетом вашей логики.

Если ваша логика требует сбора всех событий, то формат немного отличается: (доступно на любой версии **pull**)

Ловушка для страниц десктопной версии (все события кроме событий online):


```
BX.addCustomEvent("onPullEvent", BX.delegate(function(module_id,command,params){
	console.log(module_id, command, params);
}, this));
```

Ловушка для страниц мобильной версии (все события кроме событий online):


```
BX.addCustomEvent("onPull", BX.delegate(function(data){
	console.log(data.module_id, data.command, data.params);
}, this));
```

Пример кода для работы с [PHP классами](classes/index.md) модуля (Pull, Pull Shared, Pull Watch):


```
BX.addCustomEvent("onPullEvent", function(module_id,command,params) {
	if (module_id == "test" && command == 'check')
	{
		console.log('Work!');
	}
});
```

В примере мы подписываемся на событие получение команд (**onPullEvent**), в функции получаем **module_id**, **command**, **params** которые мы указали при отправке команды из PHP, обрабатываем свои команды с учетом вашей логики.

**Примечания**: - Для получения данных об онлайне используйте событие `onPullOnlineEvent` - Лучше использовать обработчики событий для конкретных модулей, вместо обработчика на все события. Такой формат будет более производителен.

---

<!-- vault-nav:start -->
## В этой папке

<details>
<summary>Показать файлы и папки</summary>

### Папки

- [Классы](classes/index.md)
- [События модуля Push and Pull](events/index.md)

### Файлы

- [Push and Pull в ядре D7](push_pull_d7.md)

</details>

<!-- vault-nav:end -->
