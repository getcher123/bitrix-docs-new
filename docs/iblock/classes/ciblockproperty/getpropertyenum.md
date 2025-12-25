# GetPropertyEnum


### Описание и параметры


```
CDBResult CIBlockProperty::GetPropertyEnum(
	mixed PROP_ID,
	array arOrder = Array("SORT"=>"asc"),
	array arFilter = Array()
)
```

Возвращает варианты для значения свойства *PROP_ID*типа "список" отсортированные в порядке *arOrder* и отфильтрованные по *arFilter*. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| PROP_ID | Числовой или символьный код свойства. |
| arOrder | Массив для сортировки, имеющий вид *by1*=>*order1*[, *by2*=>*order2* [, ..]], где *by* - поле сортировки, может принимать значения: *id* - код; *value* - значение, *sort* - поле сортировки*,* *external_id* - внешний код, *order* - порядок сортировки, может принимать значения: *asc* - по возрастанию; *desc* - по убыванию; |
| arFilter | Массив вида array("фильтруемое поле"=>"значение" [, ...]) "фильтруемое поле" может принимать значения: *VALUE* - по значению варианта свойства (можно искать по шаблону [%_]); *EXTERNAL_ID* - по значению внешнего кода варианта свойства (можно искать по шаблону [%_]); *IBLOCK_ID* - по коду информационного блока, которому принадлежит свойство; *ID* - по коду значения варианта свойства; Необязательное. По умолчанию записи не фильтруются. |


#### Возвращаемое значение

Возвращается объект [CDBResult](../../../main/reference/cdbresult/index.md), содержащий записи [полей вариантов свойства](../../fields.md#fiblockpropertyenum). ---
### Смотрите также


- [Поля вариантов свойства](../../fields.md#fiblockpropertyenum)
- [CIBlockPropertyEnum](../ciblockpropertyenum/index.md)::[GetList()](../ciblockpropertyenum/getlist.md)

---
### Примеры использования


```
<?
$db_enum_list = CIBlockProperty::GetPropertyEnum("IMPORTANT_NEWS", Array(), Array("IBLOCK_ID"=>$BID, "VALUE"=>"Yes"));
if($ar_enum_list = $db_enum_list->GetNext())
{
	$db_important_news = CIBlockElement::GetList(Array(), Array("IBLOCK_ID"=>$BID, "PROPERTY"=>array("IMPORTANT_NEWS"=>$ar_enum_list["ID"])));
}
?>
```

---
