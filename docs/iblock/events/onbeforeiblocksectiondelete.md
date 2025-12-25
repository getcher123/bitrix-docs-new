# OnBeforeIBlockSectionDelete


### Описание и параметры


```
bool
функция-обработчик(
	int ID
);
```

Событие "OnBeforeIBlockSectionDelete" вызывается перед удалением раздела методом [CIBlockSection::Delete](../classes/ciblocksection/delete.md). Как правило задачи обработчика данного события - разрешить или запретить удаление.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *ID* | ID удаляемого раздела. |


#### Возвращаемое значение

Для отмены удаления раздела и прекращении выполнения метода [CIBlockSection::Delete](../classes/ciblocksection/delete.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*. ---
### Смотрите также


- [CIBlockSection::Delete](../classes/ciblocksection/delete.md) **Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockSectionDelete", Array("MyClass", "OnBeforeIBlockSectionDeleteHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockSectionDelete"
	public static function OnBeforeIBlockSectionDeleteHandler($ID)
	{
		if($ID==1)
		{
			global $APPLICATION;
			$APPLICATION->throwException("раздел с ID=1 нельзя удалить.");
			return false;
		}
	}
}
?>
```

---



| ![](../images/f605d0ae60.jpg) 1 **Александр Чепурнов**29.04.2020 15:45:02 |  |  |
| --- | --- | --- |
| Событие OnAfterIBlockSectionDelete тоже есть, только не добавлено в данную документацию. У события один параметр - массив полей удаленного раздела. \| Код \| \| --- \| \| ``` AddEventHandler("iblock", "OnAfterIBlockSectionDelete", "OnAfterIBlockSectionDelete"); function OnAfterIBlockSectionDelete($arFields){ if($arFields['ID']==1){ echo 'Удален раздел '.$arFields['ID']; } } ``` \| | Код | ``` AddEventHandler("iblock", "OnAfterIBlockSectionDelete", "OnAfterIBlockSectionDelete"); function OnAfterIBlockSectionDelete($arFields){ if($arFields['ID']==1){ echo 'Удален раздел '.$arFields['ID']; } } ``` |
| Код |  |  |
| ``` AddEventHandler("iblock", "OnAfterIBlockSectionDelete", "OnAfterIBlockSectionDelete"); function OnAfterIBlockSectionDelete($arFields){ if($arFields['ID']==1){ echo 'Удален раздел '.$arFields['ID']; } } ``` |  |  |
|  |  |  |
