# OnBeforeIBlockSectionUpdate


### Описание и параметры


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlockSection::Update](../classes/ciblocksection/update.md)до изменения раздела информационного блока,
и может быть использовано для отмены изменения или для переопределения некоторых полей.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#fsection) изменяемого раздела информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.


#### Возвращаемое значение

Для отмены изменения и прекращении выполнения метода [CIBlockSection::Update](../classes/ciblocksection/update.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*.
---
### Смотрите также


- [Событие "OnAfterIBlockSectionUpdate"](onafteriblocksectionupdate.md) [CIBlockSection::Update](../classes/ciblocksection/update.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockSectionUpdate", Array("MyClass", "OnBeforeIBlockSectionUpdateHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockSectionUpdate"
	public static function OnBeforeIBlockSectionUpdateHandler(&$arFields)
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
