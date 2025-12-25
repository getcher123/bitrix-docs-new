# GetAdminListViewHTML


### Описание и параметры


```
string
CIBlockProperty*::GetAdminListViewHTML(
	array arProperty,
	array value,
	array strHTMLControlName
);
```

Метод должен вернуть безопасный HTML отображения значения свойства в списке элементов административной части. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

**Примечание:**вызывается во время построения списка элементов.


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
	function GetAdminListViewHTML($arProperty, $value, $strHTMLControlName)
	{
		if(strlen($value["VALUE"])>0)
			return str_replace(" ", "&nbsp;", htmlspecialcharsex($value["VALUE"]));
		else
			return '&nbsp;';
	}
}
?>
```

---
