# GetAdminFilterHTML


### Описание и параметры


```
string
CIBlockProperty*::GetAdminFilterHTML(
	arProperty,
	strHTMLControlName
);
```

Выводит html для фильтра по свойству на административной странице списка элементов инфоблока. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| strHTMLControlName | Имена элементов управления для заполнения значения свойства и его описания. Массив вида: ``` array( "VALUE" => html //безопасное имя для значения, "DESCRIPTION" => html //безопасное имя для описания, "MODE" => //может принимать зачение "FORM_FILL" при вызове из формы редактирования элемента //или "iblock_element_admin" при редактировании в режиме просмотра списка элементов, //а также "EDIT_FORM" при редактировании инфоблока. "FORM_NAME" => //имя формы в которую будет встроен элемент управления. ); ``` |


#### Возвращаемое значение

Возвращаемое значение - html-код.

---
### Примеры использования

Для типа Дата/Время:


```
function GetAdminFilterHTML($arProperty, $strHTMLControlName)
{
	$from_name = $strHTMLControlName["VALUE"].'_from';
	$to_name = $strHTMLControlName["VALUE"].'_to';

	$lAdmin = new CAdminList($strHTMLControlName["TABLE_ID"]);
	$lAdmin->InitFilter(array(
		$from_name,
		$to_name,
	));

	$from = isset($GLOBALS[$from_name])? $GLOBALS[$from_name]: "";
	$to = isset($GLOBALS[$to_name])? $GLOBALS[$to_name]: "";

	return  CAdminCalendar::CalendarPeriod($from_name, $to_name, $from, $to);
}
```

---
