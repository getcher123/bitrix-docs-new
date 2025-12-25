# OnAfterIBlockPropertyUpdate


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockPropertyUpdate" вызывается после попытки изменения свойства информационного блока методом [CIBlockProperty::Update](../classes/ciblockproperty/update.md).
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#fproperty) изменяемого свойства информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlockProperty::Update](../classes/ciblockproperty/update.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

---
### Смотрите также


- [Событие "OnBeforeIBlockPropertyUpdate"](onbeforeiblockpropertyupdate.md) [CIBlockProperty::Update](../classes/ciblockproperty/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockPropertyUpdate", Array("MyClass", "OnAfterIBlockPropertyUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockPropertyUpdate"
	public static function OnAfterIBlockPropertyUpdateHandler(&$arFields)
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
