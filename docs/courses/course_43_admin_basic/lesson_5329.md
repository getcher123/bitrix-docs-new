# Кастомизация служб доставок

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7849 — Кастомизация типов дополнительных услуг](lesson_7849.md)
- [Следующий: 7847 — Кастомизация платежных систем →](lesson_7847.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5329

### Кастомизация

Средства системы позволяют кастомизировать и добавлять свои собственные службы доставки, причем в магазине на ядре D7 они представляют из себя классы. Следовательно, можно использовать механизм наследования. Для создания собственной службы доставки необходимо создать класс - наследник базового [\Bitrix\Sale\Delivery\Services\Base](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/classes/delivery/services/base/index.php).

Пример наследования для служб доставок:

```

class SimpleHandler extends \Bitrix\Sale\Delivery\Services\Base
{
	protected static $isCalculatePriceImmediately = true;
		protected static $whetherAdminExtraServiceShow = true;

	/**
	* @param array $initParams
	* @throws \Bitrix\Main\ArgumentTypeException
	*/

	public function __construct(array $initParams)
	{
		parent::__construct($initParams);
	}
}

```

Система будет искать обработчик в следующих директориях:

```

self::$handlersDirectories = array(
	'LOCAL' = > '/local/php_interface/include/sale_delivery',
	'CUSTOM' = > '/bitrix/php_interface/include/sale_delivery',
	'SYSTEM' = > '/bitrix/modules/sale/handlers/delivery'
)
```

Вы можете ограничить использование службы доставки по каким-либо параметрам. Например, по максимальному весу или размеру.
Для этого применяйте [стандартные ограничения](/learning/course/?COURSE_ID=42&LESSON_ID=7330). Если же необходимо что-то особенное, то создайте [собственные типы ограничений](lesson_7352.md).

Также для служб доставок можно задать дополнительные услуги как [стандартные](/learning/course/?COURSE_ID=42&LESSON_ID=7302), так и [собственно созданные](lesson_7849.md).

Дополнительно стоит отметить, что для служб доставок имеется событие *onSaleDeliveryServiceCalculate*, которое позволяет вмешаться в расчеты стоимости доставки (например, вы можете увеличить стоимость доставки на 100 единиц):

```

EventManager::getInstance()->addEventHandler(
	'sale',
	'onSaleDeliveryServiceCalculate',
	'myCalc'
);

function myCalc(\Bitrix\Main\Event $event)
{
	/** @var Delivery\CalculationResult $baseResult */
	$baseResult = $event->getParameter('RESULT');
	$shipment = $event->getParameter('SHIPMENT');

	$price = $baseResult->getDeliveryPrice() + 100;
	$baseResult->setDeliveryPrice($price);

	$event->addResult(
		new EventResult(
			EventResult::SUCCESS, array('RESULT' => $baseResult)
		)
	);
}
```

**Важно!** При создании службы доставки учитывайте тот факт, что сайт может быть как в кодировке utf-8, так и в кодировке cp-1251. Если производится обмен данными со службой доставки, то необходимо правильно менять кодировку при отправлении и получении данных. Здесь вам поможет метод *\Bitrix\Main\Text\Encoding::convertEncoding()*.

**Примечание**: о работе с REST служб доставки читайте

			в отдельной главе


В данной главе рассмотрим принципы работы с REST служб доставки:

- Настройка обработчика службы доставки;
- Настройка службы доставки;
- Настройка дополнительных услуг для службы доставки;
- Работа со свойствами отгрузки;
- Типовой сценарий работы REST служб доставки: работа с доставкой в центре продаж.
  Стартовой точкой для менеджера может являться функционал принятия оплаты ("Принять
  оплату в сделке") или создание дела на доставку.

[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=013084&LESSON_PATH=3913.3516.4776.7351.13084)...

		.

### Примеры служб доставок

В качестве примера служб доставок лучше всего подходят следующие:

- *\Sale\Handlers\Delivery\SimpleHandler* (`/bitrix/modules/sale/handlers/delivery/simple/handler.php`)  - простейший пример обработчика.
- *\Sale\Handlers\Delivery\SpsrHandler* (`/bitrix/modules/sale/handlers/delivery/spsr/handler.php`)  - вариант посложнее с использованием всех возможностей текущей архитектуры.

Для служб доставок существует механизм автоматического отслеживания идентификаторов отправления (трэкинг-номеров) (пример, как это реализовано для службы доставки **СПСР**: *\Sale\Handlers\Delivery\SpsrTracking*).

### Рекомендации

Для запросов к сервису службы доставки рекомендуется использовать встроенный класс *\Bitrix\Main\Web\HttpClient* вместо сторонних расширений. Оптимальный формат обмена - json, так как возможно использовать встроенный класс *\Bitrix\Main\Web\Json*.

При обмене информацией с сервисами служб доставок зачастую необходимо передавать идентификаторы местоположений.  Сопоставление идентификаторов местоположений интернет-магазина с идентификаторами местоположений служб доставок - задача нетривиальная. Как пример, используйте *\Sale\Handlers\Delivery\Spsr\Location::mapStepless()*.

Чтобы не порождать лишних запросов к службе доставки и не замедлять работу сайта, желательно при возможности кешировать полученную от сервисов служб доставок информацию. Однако, делать это надо аккуратно во избежание побочных эффектов. Используйте *\Sale\Handlers\Delivery\Spsr\Cache*.

В случае возникновения ошибок и для отладки желательно записывать события, связанные с получением информации от служб доставок в системный журнал. Для этих целей используйте класс *\CEventLog*.
