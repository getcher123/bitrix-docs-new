# OnBeforeIBlockPropertyDelete


### Описание и параметры


```
bool
функция-обработчик(
	int ID
);
```

Событие "OnBeforeIBlockPropertyDelete" вызывается перед удалением свойства методом [CIBlockProperty::Delete](../classes/ciblockproperty/delete.md). Как правило задачи обработчика данного события - разрешить или запретить удаление.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *ID* | ID удаляемого свойства. |


#### Возвращаемое значение

Для отмены удаления свойства и прекращении выполнения метода [CIBlockProperty::Delete](../classes/ciblockproperty/delete.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*. ---
### Смотрите также


- [CIBlockProperty::Delete](../classes/ciblockproperty/delete.md) **Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockPropertyDelete", Array("MyClass", "OnBeforeIBlockPropertyDeleteHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockPropertyDelete"
	public static function OnBeforeIBlockPropertyDeleteHandler($ID)
	{
		if($ID==1)
		{
			global $APPLICATION;
			$APPLICATION->throwException("Свойство с ID=1 нельзя удалить.");
			return false;
		}
	}
}
?>
```

---
