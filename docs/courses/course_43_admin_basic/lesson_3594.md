# Оптимизация запросов к БД

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5101 — Выборка и хранение в кеше только нужных данных](lesson_5101.md)
- [Следующий: 5750 — Как сделать сайт быстрым →](lesson_5750.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3594

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/performance/query-optimization.html#primer-zaprosa-dlya-tovarov). В ней улучшена структура, описание, примеры.

### Пример оптимизации запроса

Всегда минимизируйте запросы. Например, если в цикле идет запрос к элементу ИБ, то уже необходимо задуматься над минимизацией. Да, это займет больше времени, но вам скажут спасибо клиенты.

Нельзя:

```
foreach($arResult["ORDERS"] as $key => $val)
{
	foreach($val["BASKET_ITEMS"] as $vvval)
	{
		$rsEls = CIBlockElement::GetByID();
	}
}
```

Следует:

```

$arIDs = array();
foreach($arResult["ORDERS"] as $key => $val)
	{
		foreach($val["BASKET_ITEMS"] as $vvval)
		{
			$arIDs[] = $vvval["PRODUCT_ID"];
		}
	}
if(!empty($arIDs))
{
	$rsEls = CIBlockElement::GetList(array(), array("ID" => $arIDs));
	...
}

foreach($arResult["ORDERS"] as $key => $val)
{
	foreach($val["BASKET_ITEMS"] as $vvval)
	{
		//наполняем данные, налаживая соответствие ID-ков
	}
}
```

Фактически, вы сводите порой десятки, если не сотни, запросов к одному.

### Специальные методы

Если для какого-либо изменения в БД предусмотрен специальный метод, то следует использовать именно его, а не более общий метод изменения БД.

Хороший пример - модуль интернет-магазина и работа с заказом: можно изменить флаг оплаты заказа путем [CSaleOrder::Update](https://dev.1c-bitrix.ru/api_help/sale/classes/index.php), а можно путем [CSaleOrder::PayOrder](https://dev.1c-bitrix.ru/api_help/sale/classes/index.php). Так вот, следует применять именно *PayOrder*, потому что в нем произойдет вызов соответствующих обработчиков.

Даже если вам надо изменить множество полей (того же заказа) и флаг оплаты, то произведите изменение через *PayOrder*, а затем уже апдейт остальных полей.
