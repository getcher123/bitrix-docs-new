# Delete


```
bool
CIBlock::Delete(
	int ID
);
```

Метод удаляет информационный блок. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код информационного блока. |


#### Возвращаемое значение

Возвращается true в случае успешного удаления и false - в противном случае. Удаление можно отменить в обработчике события [OnBeforeIBlockDelete](../../events/onbeforeiblockdelete.md).
#### Примеры использования


```
<?
if($USER->IsAdmin())
{
	$DB->StartTransaction();
	if(!CIBlock::Delete($iblock_id))
	{
		$strWarning .= GetMessage("IBLOCK_DELETE_ERROR");
		$DB->Rollback();
	}
	else
		$DB->Commit();
}
?>
```
