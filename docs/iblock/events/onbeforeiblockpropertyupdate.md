# OnBeforeIBlockPropertyUpdate


### Описание и параметры


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlockProperty::Update](../classes/ciblockproperty/update.md)до изменения свойства информационного блока,
и может быть использовано для отмены изменения или для переопределения некоторых полей.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#fproperty) изменяемого свойства информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.


#### Возвращаемое значение

Для отмены изменения и прекращении выполнения метода [CIBlockProperty::Update](../classes/ciblockproperty/update.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*.
---
### Смотрите также


- [Событие "OnAfterIBlockPropertyUpdate"](onafteriblockpropertyupdate.md) [CIBlockProperty::Update](../classes/ciblockproperty/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockPropertyUpdate", Array("MyClass", "OnBeforeIBlockPropertyUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockPropertyUpdate"
	public static function OnBeforeIBlockPropertyUpdateHandler(&$arFields)
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
