# GetPublicEditHTML


### Описание и параметры


```
string
CIBlockProperty*::GetPublicEditHTML(
	array arProperty,
	array value,
	array strHTMLControlName
);
```

Метод должен вернуть HTML отображения элемента управления для редактирования значений свойства в публичной части сайта. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.

<p><div class="note"><b>Примечание:</b> вызывается в компонентах во время построения формы редактирования элемента. На данный момент только для компонентов <a class="link" href="http://dev.1c-bitrix.ru/user_help/service/intranet/components_2/tasks/intranet_tasks_create.php" target="_blank">intranet.tasks.create</a> и <a class="link" href="http://dev.1c-bitrix.ru/user_help/service/intranet/components_2/tasks/intranet_tasks_create_view.php" target="_blank">intranet.tasks.create_view</a>.</div></p>
#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arProperty | Метаданные свойства. См. [Свойства элементов инфоблока](../../fields.md#fproperty) |
| value | Значение свойства. Массив вида: array( "VALUE" => значение, "DESCRIPTION" => описание, ); |
| strHTMLControlName | Имена элементов управления для заполнения значения свойства и его описания. Массив вида: array( "VALUE" => html безопасное имя для значения, "DESCRIPTION" => html безопасное имя для описания, "FORM_NAME" => имя формы в которую будет встроен элемент управления. ); |


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
	//Показываем компонент календаря.
	function GetPublicEditHTML($arProperty, $value, $strHTMLControlName)
	{
		$s = '<input type="text" name="'.htmlspecialchars($strHTMLControlName["VALUE"]).'" size="25" value="'.htmlspecialchars($value["VALUE"]).'" />';
		ob_start();
		$GLOBALS["APPLICATION"]->IncludeComponent(
			'bitrix:main.calendar',
			'',
			array(
				'FORM_NAME' => $strHTMLControlName["FORM_NAME"],
				'INPUT_NAME' => $strHTMLControlName["VALUE"],
				'INPUT_VALUE' => $value["VALUE"],
			),
			null,
			array('HIDE_ICONS' => 'Y')
		);
		$s .= ob_get_contents();
		ob_end_clean();
		return  $s;
	}
}
?>
```

---
