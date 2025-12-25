# GetProperties


### Описание и параметры


```
CDBResult CIBlock::GetProperties(
	int iblock_id,
	array arOrder=Array(),
	array arFilter=Array()
);
```

Возвращает свойства информационного блока *iblock_id*с возможностью сортировки и дополнительной фильтрации. Нестатический метод.
**Примечание:**по умолчанию метод учитывает права доступа к информационному блоку. Для отключения проверки необходимо в параметре arFilter передать ключ "CHECK_PERMISSIONS" со значением "N".



#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| iblock_id | Код информационного блока. |
| arOrder | Массив для сортировки результата. Содержит пары "поле сортировки"=>"направление сортировки". Поля сортировки см. [CIBlockProperty](../ciblockproperty/index.md)::[GetList()](../ciblockproperty/getlist.md). |
| arFilter | Массив вида array("фильтруемое поле"=>"значение фильтра" [, ...]). Фильтруемые поля и их значения смотрите в [CIBlockProperty](../ciblockproperty/index.md)::[GetList()](../ciblockproperty/getlist.md). |


#### Возвращаемое значение

Возвращается объект [CDBResult](../../../main/reference/cdbresult/index.md)---
### Смотрите также


- [Поля свойств](../../fields.md#fproperty)
- [CIBlockProperty](../ciblockproperty/index.md)::[GetList()](../ciblockproperty/getlist.md)

---
### Примеры использования


```
<?
$res = CIBlock::GetProperties($IBLOCK_ID, Array(), Array("CODE"=>"SRC"));
if($res_arr = $res->Fetch())
	$SrcPropID = $res_arr["ID"];
else
{
	$arFields = Array(
		"NAME" 			=> "Источник импорта",
		"ACTIVE" 		=> "Y",
		"SORT" 			=> "1000",
		"DEFAULT_VALUE" => "",
		"CODE" 			=> "SRC",
		"ROW_COUNT" 	=> "1",
		"COL_COUNT" 	=> "10",
		"MULTIPLE"	 	=> "N",
		"MULTIPLE_CNT" 	=> "",
		"PROPERTY_TYPE"	=> "S",
		"LIST_TYPE" 	=> "L",
		"IBLOCK_ID" 	=> $IBLOCK_ID
		);
	$ibp = new CIBlockProperty;
	$SrcPropID = $ibp->Add($arFields);
	if(IntVal($SrcPropID)<=0)
		$strWarning .= $ibp->LAST_ERROR."<br>";
}
?>
```

---
