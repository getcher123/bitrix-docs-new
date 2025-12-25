# GetByID


### Описание и параметры


```
CIBlockResult CIBlockElement::GetByID(
	int ID
);
```

Возвращается объект [CIBlockResult](../ciblockresult/index.md) с [полями элемента информационного блока](../../fields.md#felement). Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | ID элемента. |

**Примечание:**метод не проверяет, чтобы элемент с кодом *ID*был опубликован и не являлся записью из истории. Для выборки только опубликованных элементов воспользуйтесь методом [CIBlockElement](../ciblockresult/index.md):: [GetList()](getlist.md).


#### Смотрите также


- [CDBResult](../../../main/reference/cdbresult/index.md)
- [CIBlockResult](../ciblockresult/index.md)
- [Поля элемента информационного блока](../../fields.md#felement)
- [CIBlockElement](index.md)::[GetList()](getlist.md)

---
### Примеры использования


```
if(!CModule::IncludeModule("iblock"))
return;
<?
$res = CIBlockElement::GetByID($_GET["PID"]);
if($ar_res = $res->GetNext())
	echo $ar_res['NAME'];
?>
```

---
