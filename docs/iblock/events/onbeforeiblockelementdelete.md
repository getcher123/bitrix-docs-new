# OnBeforeIBlockElementDelete


### Описание и параметры


```
bool
функция-обработчик(
	int ID
);
```

Событие "OnBeforeIBlockElementDelete" вызывается перед удалением элемента методом [CIBlockElement::Delete](../classes/ciblockelement/delete.md). Как правило задачи обработчика данного события - разрешить или запретить удаление.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *ID* | ID удаляемого элемента. |


#### Возвращаемое значение

Для отмены удаления элемента и прекращении выполнения метода [CIBlockElement::Delete](../classes/ciblockelement/delete.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*. ---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockElementDelete", Array("MyClass", "OnBeforeIBlockElementDeleteHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockElementDelete"
	public static function OnBeforeIBlockElementDeleteHandler($ID)
	{
		if($ID==1)
		{
			global $APPLICATION;
			$APPLICATION->throwException("элемент с ID=1 нельзя удалить.");
			return false;
		}
	}
}
?>
```

---
### Смотрите также


- [CIBlockElement::Delete](../classes/ciblockelement/delete.md) **Обработка событий**

---
