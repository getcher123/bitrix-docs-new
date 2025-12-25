# OnAfterIBlockAdd


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockAdd" вызывается после попытки добавления нового информационного блока методом [CIBlock::Add](../classes/ciblock/add.md).
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#fiblock) нового информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlock::Add](../classes/ciblock/add.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. |

**Примечание:**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

---
### Смотрите также


- [Событие "OnBeforeIBlockAdd"](onbeforeiblockadd.md) [CIBlock::Add](../classes/ciblock/add.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockAdd", Array("MyClass", "OnAfterIBlockAddHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockAdd"
	public static function OnAfterIBlockAddHandler(&$arFields)
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
