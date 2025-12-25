# GetSearchContent


### Описание и параметры


```
string
CIBlockProperty*::GetSearchContent(
	array arProperty,
	array value,
	array strHTMLControlName
);
```

Метод должна вернуть представление значения свойства для модуля поиска. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

**Примечание:**вызывается при индексации элементов инфоблока модулем поиска. Если для свойства не определен этот метод, но есть метод [GetPublicViewHTML](GetPublicViewHTML.md), то будет вызван он. После удаления разметки HTML в поисковый индекс будет занесен его результат.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| value | Значение свойства. Массив вида: ``` array( "VALUE" => значение, ); ``` |
| strHTMLControlName | Пустой массив. |


#### Возвращаемое значение

Строка.

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
	function GetSearchContent($arProperty, $value, $strHTMLControlName)
	{
		if(strlen($value["VALUE"])>0)
			return $value["VALUE"];
		else
			return '';
	}
}
?>
```

---
