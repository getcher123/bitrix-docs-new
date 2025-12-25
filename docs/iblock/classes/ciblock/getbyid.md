# GetByID


```
CDBResult
CIBlock::GetByID(
	int ID
);
```

Возвращает информационный блок по его коду *ID*. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код информационного блока. |


#### Возвращаемое значение

Возвращается объект [CDBResult](../../../main/reference/cdbresult/index.md).
#### Смотрите также


- [CDBResult](../../../main/reference/cdbresult/index.md) [Поля результата](../../fields.md#fiblock)


#### Примеры использования


```
<?
$res = CIBlock::GetByID($_GET["BID"]);
if($ar_res = $res->GetNext())
	echo $ar_res['NAME'];
?>
```
