# OnAfterIBlockSectionUpdate


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockSectionUpdate" вызывается после попытки изменения раздела информационного блока методом [CIBlockSection::Update](../classes/ciblocksection/update.md).
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#fsection) изменяемого раздела информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlockSection::Update](../classes/ciblocksection/update.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

---
### Смотрите также


- [Событие "OnBeforeIBlockSectionUpdate"](onbeforeiblocksectionupdate.md) [CIBlockSection::Update](../classes/ciblocksection/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockSectionUpdate", Array("MyClass", "OnAfterIBlockSectionUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockSectionUpdate"
	public static function OnAfterIBlockSectionUpdateHandler(&$arFields)
	{
		if($arFields["RESULT"])
			AddMessage2Log("Запись с кодом ".$arFields["ID"]." изменена.");
		else
			AddMessage2Log("Ошибка изменения записи ".$arFields["ID"]." (".$arFields["RESULT_MESSAGE"].").");
	}
}
?>
```

---



| ![image](../images/7dd82aba60.gif) 0 **Александр Кузнецов**24.06.2015 09:48:44 |  |  |
| --- | --- | --- |
| Имейте в виду, что массив $arFields содержит не все поля раздела. Вот результат json_encode($arFields) для одного из разделов: \| Код \| \| --- \| \| ``` {"ACTIVE":"N","SEARCHABLE_CONTENT":null,"MODIFIED_BY":1,"IBLOCK_ID":"11","ID":7862,"RESULT":true} ``` \| | Код | ``` {"ACTIVE":"N","SEARCHABLE_CONTENT":null,"MODIFIED_BY":1,"IBLOCK_ID":"11","ID":7862,"RESULT":true} ``` |
| Код |  |  |
| ``` {"ACTIVE":"N","SEARCHABLE_CONTENT":null,"MODIFIED_BY":1,"IBLOCK_ID":"11","ID":7862,"RESULT":true} ``` |  |  |
|  |  |  |
