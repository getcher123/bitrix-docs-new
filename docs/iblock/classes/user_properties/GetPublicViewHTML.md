# GetPublicViewHTML


### Описание и параметры


```
string
CIBlockProperty*::GetPublicViewHTML(
	array arProperty,
	array value,
	array strHTMLControlName
);
```

Метод должна вернуть безопасный HTML отображения значения свойства в публичной части сайта. Если она вернет пустое значение, то значение отображаться не будет. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

**Примечание:**вызывается из метода CIBlockFormatProperties::GetDisplayValue, которая используется компонентами модуля информационных блоков для форматирования значений свойств.


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
	function GetPublicViewHTML($arProperty, $value, $strHTMLControlName)
	{
		if(strlen($value["VALUE"])>0)
			return str_replace(" ", "&nbsp;", htmlspecialcharsex($value["VALUE"]));
		else
			return '';
	}
}
?>
```

---
