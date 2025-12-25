# Пользовательские ограничения

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7350 — Пользовательские типы свойств заказа](lesson_7350.md)
- [Следующий: 8517 — Пользовательские правила компаний →](lesson_8517.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7352

С переходом магазина на новую [схему](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=7291) работы было введено понятие ограничений. Ограничения можно добавлять для [служб доставок](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=7330), [платежных систем](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&CHAPTER_ID=03076#restr), [касс](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&CHAPTER_ID=09373) и [компаний](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=7280) (для компаний ограничения являются правилами).

Таким образом, например, службу доставки можно настроить так, что она будет работать только для некоторого местоположения, только для заказов такой-то стоимости,веса или выбрать другие ограничения из стандартных ограничений.

Вы можете дополнить стандартный набор ограничений своими собственными ограничениями. Для этого следует в зависимости от ваших нужд использовать события инициализации ограничений:

- для служб доставок *onSaleDeliveryRestrictionsClassNamesBuildList*:
  ```
  Bitrix\Main\EventManager::getInstance()->addEventHandler(
  	'sale',
  	'onSaleDeliveryRestrictionsClassNamesBuildList',
  	'myDeliveryFunction'
  );
  ```
- для платежных систем *onSalePaySystemRestrictionsClassNamesBuildList*:
  ```
  Bitrix\Main\EventManager::getInstance()->addEventHandler(
  	'sale',
  	'onSalePaySystemRestrictionsClassNamesBuildList',
  	'myPayFunction'
  );
  ```
- для касс *onSaleCashboxRestrictionsClassNamesBuildList*:
  ```
  Bitrix\Main\EventManager::getInstance()->addEventHandler(
  	'sale',
  	'onSaleCashboxRestrictionsClassNamesBuildList',
  	'myCashboxFunction'
  );
  ```
- для компаний *onSaleCompanyRulesClassNamesBuildList*:
  ```
  Bitrix\Main\EventManager::getInstance()->addEventHandler(
  	'sale',
  	'onSaleCompanyRulesClassNamesBuildList',
  	'myCompanyFunction'
  );
  ```

В обработчиках событий соответственно следует возвращать ваш класс ограничений:

- для служб доставок:
  ```
  function myDeliveryFunction()
  {
  	return new \Bitrix\Main\EventResult(
  		\Bitrix\Main\EventResult::SUCCESS,
  		array(
  			'\MyDeliveryRestriction' => '/bitrix/php_interface/include/mydelrestriction.php',
  			)
  	);
  }
  ```
- для платежных систем:
  ```
  function myPayFunction()
  {
  	return new \Bitrix\Main\EventResult(
  		\Bitrix\Main\EventResult::SUCCESS,
  		array(
  			'\MyPayRestriction' => '/bitrix/php_interface/include/mypayrestriction.php',
  		)
  	);
  }
  ```
- для касс:
  ```
  function myCashboxFunction()
  {
  	return new \Bitrix\Main\EventResult(
  		\Bitrix\Main\EventResult::SUCCESS,
  		array(
  			'\MyCashboxRestriction' => '/bitrix/php_interface/include/mycashboxrestriction.php',
  		)
  	);
  }
  ```
- для компаний:
  ```
  function myCompanyFunction()
  {
  	return new \Bitrix\Main\EventResult(
  		\Bitrix\Main\EventResult::SUCCESS,
  		array(
  			'\MyCompanyRestriction' => '/bitrix/php_interface/include/mycompanyrestriction.php',
  		)
  	);
  }
  ```

Далее, описывая ограничение, вы можете вводить какие-то собственные правила. Например, в примере ниже приведено ограничение доступности службы доставки по лунным суткам:

```
use Bitrix\Sale\Delivery\Restrictions;
use Bitrix\Sale\Internals\Entity;

class MyDeliveryRestriction extends Restrictions\Base
{
	public static function getClassTitle()
	{
		return 'по лунным суткам';
	}

	public static function getClassDescription()
	{
		return 'доставка будет выводится только в указанном диапазоне лунных суток';
	}

public static function check($moonday, array $restrictionParams, $deliveryId = 0)
{
	if ($moonday < $restrictionParams['MIN_MOONDAY'] || $moonday > $restrictionParams['MAX_MOONDAY'])
		return false;

	return true;
}
protected static function extractParams(Entity $shipment)
{
	$json = file_get_contents('http://moon-today.com/api/index.php?get=moonday');
	$res = json_decode($json, true);
	return !empty($res['moonday']) ? intval($res['moonday']) : 0;
}
public static function getParamsStructure($entityId = 0)
	{
		return array(
			"MIN_MOONDAY" => array(
				'TYPE' => 'NUMBER',
				'DEFAULT' => "1",
				'LABEL' => 'Минимальные сутки'
			),
			"MAX_MOONDAY" => array(
				'TYPE' => 'NUMBER',
				'DEFAULT' => "30",
				'LABEL' => 'Максимальные сутки'
			)
		);
	}
}
```
