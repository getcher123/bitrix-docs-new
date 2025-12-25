# OnAfterIBlockElementDelete


```
функция-обработчик(
	array &arFields
);
```

Событие "OnAfterIBlockElementDelete" вызывается после того, как элемент и вся связанная с ним информация были удалены из базы данных.


#### Параметры функции-обработчика


| Параметр | Описание |
| --- | --- |
| *arFields* | [Массив полей](../fields.md#felement) элемента информационного блока. |


#### Возвращаемое значение

Отсутствует.


#### Пример использования


```
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnAfterIBlockElementDelete", Array("MyClass", "OnAfterIBlockElementDeleteHandler"));

class MyClass
{
	// создаем обработчик события "OnAfterIBlockElementDelete"
	public static function OnAfterIBlockElementDeleteHandler($arFields)
	{
		// Выполняем какие-либо действия
	}
}
```
