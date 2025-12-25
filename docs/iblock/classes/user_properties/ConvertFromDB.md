# ConvertFromDB


### Описание и параметры


```
array
CIBlockProperty*::ConvertFromDB(
	array arProperty,
	array value
);
```

Метод должен преобразовать значение свойства из формата пригодного для сохранения в базе данных в формат обработки. И вернуть массив вида array("VALUE" => "...", "DESCRIPTION" => "..."). Дополняет [ConvertToDB](ConvertToDB.md). Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

**Примечание**: Вызывается в методе [CIBlockResult::Fetch](../ciblockresult/getnext.md). Для корректной работы необходимо в фильтре метода [CIBlockElement::GetList](../ciblockelement/getlist.md)указать "IBLOCK_ID".


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| value | Значение свойства прочитанное из базы данных. Массив вида: array( "VALUE" => значение, "DESCRIPTION" => описание, ); |


#### Возвращаемое значение

Внешнее представление значения свойства.

---
### Смотрите также


- [Свойства элементов инфоблока](../../fields.md#fproperty)
- [GetUserTypeDescription](GetUserTypeDescription.md)
- [ConvertToDB](ConvertToDB.md)

---
### Примеры использования


```
<?
class CIBlockPropertyMyDateTime
{
	function ConvertFromDB($arProperty, $value)
	{
		if(strlen($value["VALUE"])>0)
		{
			$value["VALUE"] = CDatabase::FormatDate(
				$value["VALUE"],
				"YYYY-MM-DD HH:MI:SS",
				CLang::GetDateFormat("FULL")
			);
			//Удалим незначимые нули
			$value["VALUE"] = str_replace(" 00:00:00", "", $value["VALUE"]);
		}
		return $value;
	}
}
?>
```

---
