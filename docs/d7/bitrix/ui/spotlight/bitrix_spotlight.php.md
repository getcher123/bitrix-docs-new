# Компонент bitrix:spotlight

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/spotlight/bitrix_spotlight.php

### Описание и параметры

Компонент выводит подсказку на странице около указанного DOM-элемента. Учитывает и фиксирует факт показа подсказки текущему пользователю. Компонент адаптирован под композит.

#### Параметры

| Параметр | Описание | С версии |
| --- | --- | --- |
| ID | идентификатор подсказки. Обязательный параметр. |  |
| USER_TYPE | Тип пользователя. Допустимые значения:<br><br>- OLD - показ подсказки для старых пользователей.<br>- NEW - показ подсказки для новых пользователей.<br>- ALL - показ подсказки для любых пользователей. |  |
| USER_TIMESPAN | Промежуток времени в секундах для определения нового/старого пользователя. По умолчанию 30 дней. |  |
| LIFETIME | Время жизни подсказки в секундах. По умолчанию 30 дней. |  |
| START_DATE | Дата, с которой начнется показ подсказки. По умолчанию не задана. |  |
| END_DATE | Дата, до которой можно показывать подсказку. По умолчанию не задана. |  |
| JS_OPTIONS | массив опций для конструктора BX.SpotLight. |  |

### Пример вызова

```
<?$APPLICATION->includeComponent("bitrix:spotlight", "", array(
	"ID" => "my-spotlight",
	"JS_OPTIONS" => array(
		"targetElement" => "box",
		"content" => "Текст подсказки",
		"targetVertex" => "middle-center"
	)
));
?>
```

### Пример обработки событий в JavaScript

Пример показывает два варианта обработки событий пульсирующего круга, подключенного с помощью компонента **bitrix:spotlight**:

1. **Статический**. В ключе **events** указывается ссылка на статическую функцию.
2. **Экземплярный**. Компонент bitrix:spotlight создает объект пульсирующего круга с помощью менеджера BX.SpotLight.Manager. Через этот менеджер можно получить ссылку на объект типа BX.SpotLight.

```
<?

$APPLICATION->includeComponent("bitrix:spotlight", "", array(
	"ID" => "my-spotlight3",
	"USER_TYPE" => "OLD",
	"USER_TIMESPAN" => 3600 * 24 * 30,
	"LIFETIME" => 3600 * 24 * 30,
	"START_DATE" => gmmktime(8, 30, 0, 10, 10, 2017), // October 10, 2017 11:30 MSK
	"END_DATE" => gmmktime(8, 30, 0, 12, 10, 2017), // December 10, 2017 11:30 MSK
	"JS_OPTIONS" => array(
		"targetElement" => "box",
		"content" => "Text Text",
		"top" => 100,
		"left" => 100,
		"events" => array(
			"onTargetEnter" => "BX.MyModule.MyComponent.handleTargetEnter" //статический метод
		),
		"targetVertex" => "middle-right"
	)
));

?>

<script>
(function() {

	BX.namespace("BX.MyModule.MyComponent");

	BX.MyModule.MyComponent = function(options)
	{
		//Получаем экземпляр подсказки.
		var spotlight = BX.SpotLight.Manager.get("my-spotlight");
		if (spotlight)
		{
			spotlight.bindEvents({
				onTargetEnter: this.handleTargetEnter.bind(this)
			});
		}
	};

	BX.MyModule.MyComponent.handleTargetEnter = function(spotlight)
	{
		console.log("handleTargetEnter", this, spotlight);
	};

	BX.MyModule.MyComponent.prototype =
	{
		handleTargetEnter: function(spotlight)
		{
			console.log("handleTargetEnter prototype", this, spotlight);
		}
	};

})();

BX.ready(function() {
	new BX.MyModule.MyComponent();
});

</script>
```
