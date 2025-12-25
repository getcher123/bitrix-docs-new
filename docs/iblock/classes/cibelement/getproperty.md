# GetProperty


### Описание и параметры


```
array
_CIBElement::GetProperty(
	mixed ID
);
```

Метод возвращает параметры свойства *ID* и его значения для текущего элемента информационного блока. Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| *ID* | Числовой или символьный код свойства. |


#### Возвращаемое значение

Метод возвращает массив [полей свойства](../../fields.md#fproperty)и дополнительно поля со значениями свойства:
*VALUE*=> значение свойства или массив значений свойств, если свойство множественное,
*VALUE_ENUM_ID*=> код варианта значения для свойства типа "Список" (массив или единичное значение),
*DESCRIPTION*=> описание значения свойства (массив или единичное значение),
*PROPERTY_VALUE_ID*=> код значения свойства (массив или единичное значение).
**Примечание:**если **GetProperty**применяется к результату работы [CIBlockElement::GetList](../ciblockelement/getlist.md), то в **arSelectFields**необходимо **обязательно**указать *IBLOCK_ID*, иначе результат будет пустым.

---
### Смотрите также


- [CIBlockElement](../ciblockelement/index.md)::[GetProperty()](../ciblockelement/getproperty.md) [_CIBElement](index.md):: [GetProperties()](getproperties.md)

---
### Примеры использования


```
<?
$res = CIBlockElement::GetByID($_GET["PID"]);
if($obRes = $res->GetNextElement())
{
	$ar_res = $obRes->GetProperty("PHOTOS");
	print_r($ar_res);
}
?>
```


```
Вывод примера:

Array
(
	[ID] => 388
	[TIMESTAMP_X] => 20050119162457
	[IBLOCK_ID] => 11
	[NAME] => Photos with description
	[ACTIVE] => Y
	[SORT] => 500
	[CODE] =>
	[DEFAULT_VALUE] =>
	[PROPERTY_TYPE] => F
	[ROW_COUNT] => 1
	[COL_COUNT] => 30
	[LIST_TYPE] => L
	[MULTIPLE] => Y
	[XML_ID] =>
	[FILE_TYPE] =>
	[MULTIPLE_CNT] => 5
	[TMP_ID] =>
	[WITH_DESCRIPTION] => Y
	[LINK_IBLOCK_ID] => 0
	[VALUE_TYPE] => text
	[VALUE_ENUM] =>
	[VALUE] => Array
	(
		[0] => 2311
	)

	[~VALUE] => Array
	(
		[0] => 2311
	)

	[DESCRIPTION] => Array
	(
		[0] => Descr
	)

	[~DESCRIPTION] => Array
	(
		[0] => Descr
	)

	[PROPERTY_VALUE_ID] => Array
	(
		[0] => 53865
	)

	[~NAME] => Photos with description
	[~DEFAULT_VALUE] =>
)
```

---
