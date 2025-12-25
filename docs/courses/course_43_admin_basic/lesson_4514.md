# Данные до и после update

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 1981 — Совместная работа пары событий](lesson_1981.md)
- [Следующий: 2816 — Дополнительно →](lesson_2816.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=4514

### Описание

Задача выполнения произвольного кода при изменении данных - очень частая задача, например: разнообразные оповещения, синхронизация таблиц, сброс кеша. При наличии событий, вызываемых после успешного обновления, задача решается достаточно тривиально до тех пор пока не требуется выполнить код только тогда, когда данные **действительно** изменились (значения полей элемента таблицы до и после записи различаются).

В обработчиках нет старых данных в силу того, что если будет реализована передача данных штатно, то это минимум в два раза увеличит число запросов на каждое обновление.

Решить задачу в D7 достаточно просто, в случае старого API - несколько сложнее, хотя подход одинаков. На D7 проще в силу того что набор имеющихся событий и место их вызова стандартизированы, равно как и данные, доступные в обработчиках. В старом ядре не всегда есть обработчики либо есть только один (обычно вызываемый после обновления).

### D7

Реальный пример, взятый из API купонов правил корзины. В случае перепривязки купона (смены правила корзины, к которому он относится), необходимо обновить флаг существования купонов как у старого, так и у нового правила. Класс [\Bitrix\Sale\Internals\DiscountCouponTable](http://dev.1c-bitrix.ru/api_d7/bitrix/sale/internals/discountcoupontable/index.php):

```
public static function onUpdate(Main\Entity\Event $event)
{
	if (!self::isCheckedCouponsUse())
		return;
	$data = $event->getParameter('fields');
	if (isset($data['DISCOUNT_ID']))
	{
		$data['DISCOUNT_ID'] = (int)$data['DISCOUNT_ID'];
		$id = $event->getParameter('id');
		$couponIterator = self::getList(array(
			'select' => array('ID', 'DISCOUNT_ID'),
			'filter' => array('=ID' => $id)
	));
	if ($coupon = $couponIterator->fetch())
	{
		$coupon['DISCOUNT_ID'] = (int)$coupon['DISCOUNT_ID'];
		if ($coupon['DISCOUNT_ID'] !== $data['DISCOUNT_ID'])
			{
			self::$discountCheckList[$data['DISCOUNT_ID']] = $data['DISCOUNT_ID'];
			self::$discountCheckList[$coupon['DISCOUNT_ID']] = $coupon['DISCOUNT_ID'];
			}
	}
	unset($coupon, $couponIterator);
	}
}

public static function onAfterUpdate(Main\Entity\Event $event)
{
	self::updateUseCoupons();
}
```

Использованы события **onUpdate** и **onAfterUpdate**. Первое вызывается перед изменением записи в таблице, но уже **после** проверки данных и возможной отмены действия. Поскольку функционал реализован в самом классе, нет необходимости регистрировать обработчики отдельно. Для вмешательства в работу чужого класса регистрацию своих обработчиков придется сделать, используя следующий код:

```
      $eventManager = \Bitrix\Main\EventManager::getInstance();
	$eventManager->registerEventHandler('модуль', 'событие', 'Ваш_модуль', 'Ваш_класс', 'метод_класса');

/* событие - \Bitrix\Main\Entity\DataManager::EVENT_ON_UPDATE или \Bitrix\Main\Entity\DataManager::EVENT_ON_AFTER_UPDATE */
```

Что же делают эти два обработчика? Рассмотрим обработчик **onUpdate**.

1. ```
  if (!self::isCheckedCouponsUse())
  	return;
  ```
  Возможность отключить обработчик. Нужна, например, при деактивации набора купонов либо массовой операции перепривязки (когда использующий API и так знает исходное и новое правило корзины).
2. ```
  $data = $event->getParameter('fields');
  if (isset($data['DISCOUNT_ID'] ) )
  {
  	$data['DISCOUNT_ID'] = (int)$data['DISCOUNT_ID'];
  	$id = $event->getParameter('id');
  	$couponIterator = self::getList(array(
  		'select' => array('ID', 'DISCOUNT_ID'),
  		'filter' => array('=ID' => $id)
  		));
  	if ($coupon = $couponIterator->fetch())
  	{
  		$coupon['DISCOUNT_ID'] = (int)$coupon['DISCOUNT_ID'];
  		if ($coupon['DISCOUNT_ID'] !== $data['DISCOUNT_ID'] )
  		{
  			self::$discountCheckList[$data['DISCOUNT_ID']] = $data['DISCOUNT_ID'];
  			self::$discountCheckList[$coupon['DISCOUNT_ID']] = $coupon['DISCOUNT_ID'];
  		}
  	}
     unset($coupon, $couponIterator);
  }
  ```
  Проверяется наличие интересующего нас поля (DISCOUNT_ID). Если оно есть, получается из базы старое значение, сравнивается, и, в случае несовпадения, - заносятся старое и новое значение в статическую переменную класса.
3. Собственно, остался вызов **onAfterUpdate**, внутри которого проверяется, что переменная с данными не пустая и идет обновление флага существования купонов для старого и нового правил корзины.

**Примечание**: Обязательные условия:

- Оба обработчика должны относится к одному классу.
- Оба обработчика должны быть статические.
- Данные хранятся в статической переменной класса.

Этот подход можно реализовывать и на отдельных функциях и глобальных переменных, но сложность разработки возрастает непропорционально, а легкость понимая такого кода наоборот, снижается.

### Старое ядро

При реализации на API старого ядра задача усложняется - может не оказаться необходимых событий. Единственный выход - либо просить вендора их добавить, либо искать обходные пути. В рамках описываемой задачи предположим, что они есть. Небольшой недостаток есть в том, что в старом ядре может выполниться событие **Before** и не выполниться **After**. Рассмотрим на примере [CCatalogProduct](http://dev.1c-bitrix.ru/api_help/catalog/classes/ccatalogproduct/index.php). У метода [Update](http://dev.1c-bitrix.ru/api_help/catalog/classes/ccatalogproduct/ccatalogproduct__update.bc9a623b.php) есть два события - [OnBeforeProductUpdate](http://dev.1c-bitrix.ru/api_help/catalog/events/onbeforeproductupdate.php) и [OnProductUpdate](http://dev.1c-bitrix.ru/api_help/catalog/events/onproductupdate.php). Создаем класс обработчиков:

```
class MyChanger
{
	protected static $oldWeight = array();

	public static function OnBeforeUpdate($id, &$fields)
	{
		$id = (int)$id;
		if ($id <= 0)
		return true;
		if (isset($fields['WEIGHT'] ) )
			{
			$productRes = CCatalogProduct::GetList(array(), array('ID' => $id), false, false, array('WEIGHT') );
			$product = $productRes->Fetch();
			if (!empty($product))
			{
			if ($product['WEIGHT'] != $fields['WEIGHT'] )
			self::$oldWeight[$id] = $product['WEIGHT'];
			}
		}
		return true;
	}

	public static function OnUpdate($id, $fields)
		{
		if (isset($fields['WEIGHT'] ) && isset(self::$oldWeight[$id] ) )
		{
		/*
		* необходимые действия
		*/

	unset(self::$oldWeight[$id] );
		}
	}
}
```

Этот класс контролирует изменение веса товара. Задача условна, но код содержит все необходимое для подобных действий.

Метод **MyChanger::OnBeforeUpdate** вешается на событие модуля catalog **OnBeforeProductUpdate**. Если в массиве обновляемых данных есть поле WEIGHT - из базы получается старое значение и если оно отличается, то старое заносится в статическую переменную.

Метод **MyChanger::OnUpdate** должен содержать требуемую логику (логирование, отправка писем и так далее). Он должен быть зарегистрирован на событие модуля catalog **OnProductUpdate**.

**Примечание**: перечень параметров обработчика должен соответствовать параметрам, передаваемым в обработчик из метода.

Данный пример стоит рассматривать как учебный, не учитывающий возможность групповых операций (массовый вызов Update). Для массовых операций необходима реализация блокировки обработчиков, получения требуемых данных одним запросом перед пакетом операций и принудительного исполнения своего кода после завершения пакета.
