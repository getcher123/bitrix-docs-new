# GetUserTypeDescription


### Описание


```
array
CIBlockProperty*::GetUserTypeDescription(
);
```

Метод возвращает массив описывающий поведение пользовательского свойства. Вызывается по событию [OnIBlockPropertyBuildList](../../events/OnIBlockPropertyBuildList.md). Метод статический при использовании штатных свойств. У свойств, созданных клиентом, обязан быть статическим при использовании php7.


#### Параметры вызова

Отсутствуют.

#### Возвращаемое значение

Массив.

---
### Структура массива


| Поле | Описание |
| --- | --- |
| PROPERTY_TYPE | Обязательное. Указывает модулю какое свойство будет базовым для хранения значений пользовательского свойства, а также для фильтрации и некоторых других действий. Возможные значения: - S - строка - N - число с плавающей точкой - L - список значений - F - файл - G - привязка к разделам - E - привязка к элементам |
| USER_TYPE | Обязательное. Уникальный идентификатор пользовательского свойства. |
| DESCRIPTION | Обязательное. Краткое описание. Будет выведено в списке выбора типа свойства при редактировании информационного блока. |
| [CheckFields](CheckFields.md) | Не обязательное. Значением этого поля должен быть массив из двух элементов. В первом должно быть название класса, а во втором название метода который будет вызван при наступлении соответствующего события. |
| [GetUIFilterProperty](getuifilterproperty.md) | Аналогично. С версии 18.5.0. |
| [GetLength](GetLength.md) | Аналогично. |
| [ConvertToDB](ConvertToDB.md) | Аналогично. |
| [ConvertFromDB](ConvertFromDB.md) | Аналогично. |
| [GetPropertyFieldHtml](GetPropertyFieldHtml.md) | Аналогично. |
| [GetPropertyFieldHtmlMulty](getpropertyfieldhtmlmulty.md) | Необязательный обработчик. Является аналогом [GetPropertyFieldHtml](GetPropertyFieldHtml.md) за исключением того, что в *value* приходят несколько значений.. |
| [GetAdminListViewHTML](GetAdminListViewHTML.md) | Аналогично. |
| [GetPublicViewHTML](GetPublicViewHTML.md) | Аналогично. |
| [GetPublicEditHTML](GetPublicEditHTML.md) | Аналогично. |
| [GetSettingsHTML](GetSettingsHTML.md) | Аналогично. |
| [PrepareSettings](PrepareSettings.md) | Аналогично. |

---
### Смотрите также


- [OnIBlockPropertyBuildList](../../events/OnIBlockPropertyBuildList.md)

---
### Примеры использования


```
<?
class CIBlockPropertyMyDateTime
{
	public static function GetUserTypeDescription()
	{
		return array(
			"PROPERTY_TYPE"		=>"S",
			"USER_TYPE"		=>"MyDateTime",
			"DESCRIPTION"		=>"Дата/Время",
			//optional handlers
			"CheckFields"		=>array("CIBlockPropertyMyDateTime","CheckFields"),
			"GetLength"		=>array("CIBlockPropertyMyDateTime","GetLength"),
			"ConvertToDB"		=>array("CIBlockPropertyMyDateTime","ConvertToDB"),
			"ConvertFromDB"		=>array("CIBlockPropertyMyDateTime","ConvertFromDB"),
			"GetPropertyFieldHtml"	=>array("CIBlockPropertyMyDateTime","GetPropertyFieldHtml"),
			"GetAdminListViewHTML"	=>array("CIBlockPropertyMyDateTime","GetAdminListViewHTML"),
			"GetPublicViewHTML"	=>array("CIBlockPropertyMyDateTime","GetPublicViewHTML"),
			"GetPublicEditHTML"	=>array("CIBlockPropertyMyDateTime","GetPublicEditHTML"),
		);
	}
}
?>
```

---
