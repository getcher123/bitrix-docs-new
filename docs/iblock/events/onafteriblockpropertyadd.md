# OnAfterIBlockPropertyAdd


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockPropertyAdd" вызывается после попытки добавления нового свойства информационного блока методом [CIBlockProperty::Add](../classes/ciblockproperty/add.md).
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#fproperty) нового свойства информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlockProperty::Add](../classes/ciblockproperty/add.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

---
### Смотрите также


- [Событие "OnBeforeIBlockPropertyAdd"](onbeforeiblockpropertyadd.md) [CIBlockProperty::Add](../classes/ciblockproperty/add.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockPropertyAdd", Array("MyClass", "OnAfterIBlockPropertyAddHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockPropertyAdd"
	public static function OnAfterIBlockPropertyAddHandler(&$arFields)
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
