# OnBeforeIBlockUpdate


### Описание и параметры


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlock::Update](../classes/ciblock/update.md)до изменения информационного блока,
и может быть использовано для отмены изменения или переопределения некоторых полей.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#fiblock) изменяемого информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.


#### Возвращаемое значение

Для отмены изменения и прекращении выполнения метода [CIBlock::Update](../classes/ciblock/update.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*.
---
### Смотрите также


- [Событие "OnAfterIBlockUpdate"](onafteriblockupdate.md) [CIBlock::Update](../classes/ciblock/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockUpdate", Array("MyClass", "OnBeforeIBlockUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockUpdate"
	public static function OnBeforeIBlockUpdateHandler(&$arFields)
	{
		if(strlen($arFields["CODE"])<=0)
		{
			global $APPLICATION;
			$APPLICATION->throwException("Введите символьный код. (ID:".$arFields["ID"].")");
			return false;
		}
	}
}
?>
```

---
