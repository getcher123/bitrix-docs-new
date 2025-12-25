# OnAfterIBlockUpdate


### Описание и параметры


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockUpdate" вызывается после попытки изменения информационного блока методом [CIBlock::Update](../classes/ciblock/update.md).
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#fiblock) изменяемого информационного блока. Дополнительно, в элементе массива с индексом "RESULT" содержится результат работы (возвращаемое значение) метода [CIBlock::Update](../classes/ciblock/update.md) и, в случае ошибки, элемент с индексом "RESULT_MESSAGE" будет содержать текст ошибки. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

---
### Смотрите также


- [Событие "OnBeforeIBlockUpdate"](onbeforeiblockupdate.md) [CIBlock::Update](../classes/ciblock/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockUpdate", Array("MyClass", "OnAfterIBlockUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnAfterIBlockUpdate"
	public static function OnAfterIBlockUpdateHandler(&$arFields)
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
