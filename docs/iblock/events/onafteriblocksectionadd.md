# OnAfterIBlockSectionAdd


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockSectionAdd" вызывается после попытки добавления нового раздела информационного блока методом [CIBlockSection::Add](../classes/ciblocksection/add.md).
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#fsection) нового раздела информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlockSection::Add](../classes/ciblocksection/add.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

---
### Смотрите также


- [Событие "OnBeforeIBlockSectionAdd"](onbeforeiblocksectionadd.md) [CIBlockSection::Add](../classes/ciblocksection/add.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockSectionAdd", Array("MyClass", "OnAfterIBlockSectionAddHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockSectionAdd"
	public static function OnAfterIBlockSectionAddHandler(&$arFields)
	{
		if($arFields["ID"]>0)
			AddMessage2Log("Запись с кодом ".$arFields["ID"]." добавлена.");
		else
			AddMessage2Log("Ошибка добавления записи (".$arFields["RESULT_MESSAGE"].").");
	}
}
?>
```

---
