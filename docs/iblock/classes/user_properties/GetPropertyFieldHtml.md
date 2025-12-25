# GetPropertyFieldHtml


### Описание и параметры


```
string
CIBlockProperty*::GetPropertyFieldHtml(
	array arProperty,
	array value,
	array strHTMLControlName
);
```

Метод должен вернуть HTML отображения элемента управления для редактирования значений свойства в административной части. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

**Примечание:**вызывается во время построения формы редактирования элемента.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| value | Значение свойства. Массив вида: array( "VALUE" => значение, "DESCRIPTION" => описание, ); |
| strHTMLControlName | Имена элементов управления для заполнения значения свойства и его описания. Массив вида: array( "VALUE" => html безопасное имя для значения, "DESCRIPTION" => html безопасное имя для описания, "MODE" => может принимать зачение "FORM_FILL" при вызове из формы редактирования элемента или "iblock_element_admin" при редактировании в режиме просмотра списка элементов, а также "EDIT_FORM" при редактировании инфоблока. "FORM_NAME" => имя формы в которую будет встроен элемент управления. ); |


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
	function GetPropertyFieldHtml($arProperty, $value, $strHTMLControlName)
	{
		return  CAdminCalendar::CalendarDate($strHTMLControlName["VALUE"], $value["VALUE"], 20).
			($arProperty["WITH_DESCRIPTION"]=="Y"?
				' <input type="text" size="20" name="'.$strHTMLControlName["DESCRIPTION"].'" value="'.htmlspecialchars($value["DESCRIPTION"]).'">'
				:''
			);
	}
}
?>
```

---
