# Кастомизация типов дополнительных услуг

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8517 — Пользовательские правила компаний](lesson_8517.md)
- [Следующий: 5329 — Кастомизация служб доставок →](lesson_5329.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7849

К службам доставки можно добавлять [дополнительные услуги](/learning/course/index.php?COURSE_ID=42&LESSON_ID=7302), оказываемые клиентам при доставке товаров. Так, например, вы можете спросить у клиента нужно ли товар упаковать в подарочную упаковку.

В случае, если вас не устраивают стандартные типы дополнительных услуг, то вы можете добавлять свои собственные типы. Для этого следует использовать событие *onSaleDeliveryExtraServicesClassNamesBuildList*, которое регистрирует пользовательские типы услуг:

```

EventManager::getInstance()->addEventHandler(
	'sale',
	'onSaleDeliveryExtraServicesClassNamesBuildList',
	'myFunction'
);
```

Зарегистрируйте свой класс, который реализует ваш кастомный тип:

```

class MyService extends \Bitrix\Sale\Delivery\ExtraServices\Base
{
	public function getClassTitle()
	{
			return "Моя услуга";
	}
	...
}
```

Обработчик события должен вернуть список ваших классов типов дополнительных услуг и путей к ним:

```

public static function myFunction(Main\Event $event)
{
	return new Main\EventResult(
		Main\EventResult::SUCCESS,
		array(
			'MyService' = > 'folder/myservice.php',
		)
	);
}
```

В результате ваш класс включится в работу и будет реализован интерфейс услуг в соответствии с вашими настройками.

Класс наследуется от базового Base, который размещается в директории: `/bitrix/modules/sale/lib/delivery/extra_services`.

Там же вы сможете найти примеры штатных типов услуг.
