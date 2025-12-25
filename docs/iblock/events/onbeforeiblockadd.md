# OnBeforeIBlockAdd


### Описание и параметры


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlock::Add](../classes/ciblock/add.md)до вставки информационного блока,
и может быть использовано для отмены вставки или переопределения некоторых полей.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#fiblock) нового информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.


#### Возвращаемое значение

Для отмены добавления и прекращении выполнения метода [CIBlock::Add](../classes/ciblock/add.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*.
---
### Смотрите также


- [Событие "OnAfterIBlockAdd"](onafteriblockadd.md) [CIBlock::Add](../classes/ciblock/add.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockAdd", Array("MyClass", "OnBeforeIBlockAddHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockAdd"
	public static function OnBeforeIBlockAddHandler(&$arFields)
	{
		if(strlen($arFields["CODE"])<=0)
		{
			global $APPLICATION;
			$APPLICATION->throwException("Введите символьный код.");
			return false;
		}
	}
}
?>
```

---
