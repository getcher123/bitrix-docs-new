# CheckFields


### Описание и параметры


```
array
CIBlockProperty*::CheckFields(
	array arProperty,
	array value
);
```

Метод должен проверить корректность значения свойства и вернуть массив. Пустой, если ошибок нет, и с сообщениями об ошибках, если есть. Метод статический.

**Примечание**: вызывается перед добавлением или изменением элемента.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| value | Значение свойства. Массив вида: ``` array( "VALUE" => значение, ); ``` |


#### Возвращаемое значение

Массив сообщений об ошибках или пустой массив.

---
### Смотрите также


- [Свойства элементов инфоблока](../../fields.md#fproperty)
- [GetUserTypeDescription](GetUserTypeDescription.md)

---
### Примеры использования


```
<?
class CIBlockPropertyMyDateTime
{
	function CheckFields($arProperty, $value)
	{
		$arResult = array();
		if(strlen($value["VALUE"])>0 && !CheckDateTime($value["VALUE"]))
			$arResult[] = GetMessage("IBLOCK_PROP_DATETIME_ERROR");
		return $arResult;
	}
}
?>
```

---
