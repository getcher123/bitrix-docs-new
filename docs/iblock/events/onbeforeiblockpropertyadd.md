# OnBeforeIBlockPropertyAdd


### Описание и параметры


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlockProperty::Add](../classes/ciblockproperty/add.md)до вставки свойства в инфоблок,
и может быть использовано для отмены вставки или переопределения некоторых полей.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#fproperty) нового свойства информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.


#### Возвращаемое значение

Для отмены добавления и прекращении выполнения метода [CIBlockProperty::Add](../classes/ciblockproperty/add.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*.
---
### Смотрите также


- [Событие "OnAfterIBlockPropertyAdd"](onafteriblockpropertyadd.md) [CIBlockProperty::Add](../classes/ciblockproperty/add.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockPropertyAdd", Array("MyClass", "OnBeforeIBlockPropertyAddHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockPropertyAdd"
	public static function OnBeforeIBlockPropertyAddHandler(&$arFields)
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
