# ConvertToDB


### Описание и параметры


```
array
CIBlockProperty*::ConvertToDB(
	array arProperty,
	array value
);
```

Метод должен преобразовать значение свойства в формат пригодный для сохранения в базе данных. И вернуть массив вида array("VALUE" => "...", "DESCRIPTION" => "..."). Если значение свойства это массив, то разумным будет использование функции serialize. А вот Дата/время преобразуется в ODBC формат "YYYY-MM-DD HH:MI:SS". Это определит возможности сортировки и фильтрации по значениям данного свойства. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

**Примечание:**вызывается перед сохранением значения свойства в БД.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| value | Значение свойства. Массив вида: array( "VALUE" => значение, "DESCRIPTION" => описание, ); |


#### Возвращаемое значение

Строка представление для БД.

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
	function ConvertToDB($arProperty, $value)
	{
		if(strlen($value["VALUE"])>0)
		{
			$value["VALUE"] = CDatabase::FormatDate(
				$value["VALUE"],
				CLang::GetDateFormat("FULL"), "YYYY-MM-DD HH:MI:SS"
			);
		}
		return $value;
	}
}
?>
```

---
