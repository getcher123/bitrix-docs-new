# Основные методы работы

Несколько базовых примеров работы. Примеры даны для лидов, но по аналогии можно работать с другими сущностями CRM.


Добавление лида.


```
if (\Bitrix\Main\Loader::includeModule('crm'))
{
	$entity = new CCrmLead;
	$fields = array(
		'TITLE' => 'Test'
	);
	echo $entity->add($fields);
}
```


Изменение, удаление лида


```
<?php
if (\Bitrix\Main\Loader::includeModule('crm'))
{
	$entity = new CCrmLead(true);//true - проверять права на доступ
	$fields = array(
		'TITLE' => 'Test'
	);
	$entity->update(1, $fields);

	$entity->delete(1);
}
```


Операции выборки. Принципы работы практически аналогичны **выборке в инфоблоках**.


```
<?php
if (\Bitrix\Main\Loader::includeModule('crm'))
{
	CCrmLead::GetListEx(
		$arOrder = array(),
		$arFilter = array(),
		$arGroupBy = false,
		$arNavStartParams = false,
		$arSelectFields = array());
}
```

По умолчанию при выборке проверяются права. Чтобы отменить проверку в фильтре надо передать `CHECK_PERMISSIONS => 'N'`.


Добавление простого товара. Простой товар - это товар, привязанный к сущности в обход каталога товаров. Он не будет сохранён отдельно в базе.


```
<?php
if (\Bitrix\Main\Loader::includeModule('crm'))
{
	$rows = array();
	$rows[] = array(
		'PRODUCT_NAME' => 'Страховка', 'QUANTITY' => 2,   'PRICE' => 300,
		'MEASURE_CODE' => 796
	);
	$rows[] = array(
		'PRODUCT_NAME' => 'Выезд менеджера', 'QUANTITY' => 1,  'PRICE' => 100,
		'MEASURE_CODE' => 796
	);
	CCrmProductRow::SaveRows('D', 10, $rows);//привязываем к сделке
	CCrmProductRow::SaveRows('L', 8, $rows);//к лиду
	CCrmProductRow::SaveRows('Q', 1, $rows);//к предложению
	//для счетов несколько иначе - при обновлении или добавлении  указываем отдельным полем
	CCrmInvoice::add(array(
		'ORDER_TOPIC' => 'Новый счет',
		'PRODUCT_ROWS' => $rows
	));
}
```


Добавление товара в каталог


```
<?php
if (\Bitrix\Main\Loader::includeModule('crm'))
{
	$pid = CCrmProduct::add(array(
		'NAME' => 'Товар в базе',
		'QUANTITY' => 1,
		'PRICE' => 100,
		'MEASURE_CODE' => 796,
		'CURRENCY_ID' => 'RUB',
	));
	if ($pid)
	{
		$rows = array();
		$rows[] = array(
			'PRODUCT_ID' => $pid,
			'QUANTITY' => 1,
		);
		CCrmProductRow::SaveRows('D', 10, $rows);
	}
}
```


Получение CODE измерения.


```
<?php
if (\Bitrix\Main\Loader::includeModule('crm'))
{
	//получение списка измерений
	\Bitrix\Crm\Measure::getMeasures();
	//получение одного измерения по умолчанию
	\Bitrix\Crm\Measure::getDefaultMeasure();
	//вернется массив массивов вида:
	/*
		[ID] => 1
		[CODE] => 6
		[IS_DEFAULT] =>
		[SYMBOL] => м
	*/
}
```


Получение кодов справочных сущностей справочника


```
<?php
if (\Bitrix\Main\Loader::includeModule('crm'))  {
	$fields = array(
		'TYPE_ID' => CCrmActivityType::Call, //тип самого дела, может быть: Meeting, Call, Task, Email (константы класса)
		'OWNER_TYPE_ID' => CCrmOwnerType::Deal, //тип основной сущности, к которой привязывается дело,
                                                //может быть Deal, Lead, Contact, Company (константы класса)
		'OWNER_ID' => 10, //ID основной сущности
		'SUBJECT' => 'Телефонный разговор исходящий',
		'START_TIME' => $date,
		'END_TIME' => $date,
		'COMPLETED' => 'Y', //флаг завершенности дела
		'RESPONSIBLE_ID' => 1, //ответственный
		'PRIORITY' => CCrmActivityPriority::Medium, //приоритет, может быть None, Low, Medium, High (константы класса)
		'DESCRIPTION' => 'Описание',
		'DIRECTION' => CCrmActivityDirection::Outgoing, //актуально для типов дел, где может быть направление
			//(входящий или исходящий - телефон или email),
			//может быть Outgoing, Incoming (константы класса)
		'BINDINGS' => array(
			array(
				'OWNER_TYPE_ID' => CCrmOwnerType::Deal,
				'OWNER_ID' => 666
			)
		), //массив дополнительных связей - например, звонок привязан к сделке (основная привязка),
		// но еще относится к контакту - с КЕМ звонок.

		'ORIGIN_ID' => 'XYZ_1' //некий внешний идентификатор, опционально
	);

	CCrmActivity::Add($fields, true);
}
```
