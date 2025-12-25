# GetPublicFilterHTML


### Описание и параметры


```
string
CIBlockProperty*::GetPublicFilterHTML(
	arProperty,
	strHTMLControlName
);
```

Выводит html для фильтра по свойству на публичной странице списка элементов инфоблока. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| strHTMLControlName | Имена элементов управления для заполнения значения свойства и его описания. Массив вида: ``` array( "VALUE" => html //безопасное имя для значения, "DESCRIPTION" => html //безопасное имя для описания, "MODE" => //может принимать значение "FORM_FILL" при вызове из формы редактирования элемента //или "iblock_element_admin" при редактировании в режиме просмотра списка элементов, //а также "EDIT_FORM" при редактировании инфоблока. "FORM_NAME" => //имя формы в которую будет встроен элемент управления. ); ``` |


#### Возвращаемое значение

Возвращаемое значение - html-код.

---
### Примеры использования


```
function GetPublicFilterHTML($arProperty, $strHTMLControlName)
{
	$from_name = $strHTMLControlName["VALUE"].'_from';
	$to_name = $strHTMLControlName["VALUE"].'_to';
	$from = isset($_REQUEST[$from_name])? $_REQUEST[$from_name]: "";
	$to = isset($_REQUEST[$to_name])? $_REQUEST[$to_name]: "";

	return '
		<input name="'.htmlspecialcharsbx($from_name).'" value="'.htmlspecialcharsbx($from).'" size="8" type="text"> ...
		<input name="'.htmlspecialcharsbx($to_name).'" value="'.htmlspecialcharsbx($to).'" size="8" type="text">
	';
}
```

---
