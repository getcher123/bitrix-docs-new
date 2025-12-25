# GetPublicEditHTMLMulty


### Описание и параметры


```
string
CIBlockProperty*::GetPublicEditHTMLMulty(
	array arProperty,
	array value,
	array strHTMLControlName
);
```

Аналог [GetPublicEditHTML](GetPublicEditHTML.md), но работает с множественными свойствами. Метод должен вернуть HTML отображения элемента управления для редактирования значений свойства в публичной части сайта. Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.


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

<a class="link" name="examples"></a>
<h4>Примеры использования</h4>

<pre id="xmpE7D24E70" class="syntax">&lt;?<br />class CIBlockPropertyMyDateTime<br />{<br />	//Показываем компонент календаря.<br />	function GetPublicEditHTML($arProperty, $value, $strHTMLControlName)<br />	{<br />		$s = '&lt;input type=&quot;text&quot; name=&quot;'.htmlspecialchars($strHTMLControlName[&quot;VALUE&quot;]).'&quot; size=&quot;25&quot; value=&quot;'.htmlspecialchars($value[&quot;VALUE&quot;]).'&quot; /&gt;';<br />		ob_start();<br />		$GLOBALS[&quot;APPLICATION&quot;]-&gt;IncludeComponent(<br />			'bitrix:main.calendar',<br />			'',<br />			array(<br />				'FORM_NAME' =&gt; $strHTMLControlName[&quot;FORM_NAME&quot;],<br />				'INPUT_NAME' =&gt; $strHTMLControlName[&quot;VALUE&quot;],<br />				'INPUT_VALUE' =&gt; $value[&quot;VALUE&quot;],<br />			),<br />			null,<br />			array('HIDE_ICONS' =&gt; 'Y')<br />		);<br />		$s .= ob_get_contents();<br />		ob_end_clean();<br />		return  $s;<br />	}<br />}<br />?&gt;</pre> ---
