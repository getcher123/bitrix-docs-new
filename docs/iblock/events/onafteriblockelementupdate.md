# OnAfterIBlockElementUpdate


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockElementUpdate" вызывается после попытки изменения элемента информационного блока методом [CIBlockElement::Update](../classes/ciblockelement/update.md). Работает вне зависимости от того были ли созданы/изменены элементы непосредственно, то есть срабатывает даже после неудавшегося обновления. Поэтому необходимо дополнительно проверять параметр: RESULT_MESSAGE.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#felement) изменяемого элемента информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlockElement::Update](../classes/ciblockelement/update.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. Массив полей элемента передается по ссылке. Любые манипуляции с этим массивом в рамках обработчика не изменят информацию об элементе инфоблока, сохраненную в БД. Однако, если в системе будет несколько обработчиков события, каждый последующий получит массив с изменениями. |

---
### Смотрите также


- [Событие "OnBeforeIBlockElementUpdate"](onbeforeiblockelementupdate.md) [CIBlockElement::Update](../classes/ciblockelement/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockElementUpdate", Array("MyClass", "OnAfterIBlockElementUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockElementUpdate"
	public static function OnAfterIBlockElementUpdateHandler(&$arFields)
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



| ![image](../images/7dd82aba60.gif) 2 **Максим Мандрик**08.07.2017 19:58:29 |
| --- |
| В массиве $arFields нет ключа IBLOCK_SECTION_ID, а есть ключ IBLOCK_SECTION. |
|  |
