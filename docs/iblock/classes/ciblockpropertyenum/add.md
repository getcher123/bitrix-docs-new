# Add


### Описание и параметры


```
int CIBlockPropertyEnum::Add(
	array fields
);
```

Метод добавляет новый вариант значения свойства типа "список". Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| fields | Массив Array("поле"=>"значение", ...). Содержит значения [всех полей](../../fields.md#fpropertyenum) варианта значения свойства. |


#### Возвращаемое значение

Метод возвращает код добавленного свойства, если добавление прошло успешно, при возникновении ошибки метод вернет false.

---
### Смотрите также


- [CIBlockPropertyEnum::Update](update.md) [Поля вариантов значения свойств типа "список"](../../fields.md#fpropertyenum)

---
### Примеры использования


```
<?
$ibpenum = new CIBlockPropertyEnum;
if($PropID = $ibpenum->Add(Array('PROPERTY_ID'=>$PROPERTY_ID, 'VALUE'=>'New Enum 1')))
	echo 'New ID:'.$PropID;
?>
```

---




| ![image](../images/7dd82aba60.gif) 0 **Атем Прозоров**16.10.2019 15:52:53 |  |  |
| --- | --- | --- |
| Пример добавления значения: \| Код \| \| --- \| \| ``` \Bitrix\Main\Loader::includeModule('iblock'); $property = \CIBlockProperty::GetList( [], [ 'IBLOCK_ID' => $iblockId, 'CODE' => $code' ] )->Fetch(); $ibpenum = new \CIBlockPropertyEnum(); $valueId = $ibpenum->Add([ 'PROPERTY_ID' => $property['ID'], 'VALUE' => $newValueText, 'XML_ID' => $newValueXmlId, ]); if ((int) $valueId < 0) { throw new \Exception('Unable to add a value'); } ``` \| | Код | ``` \Bitrix\Main\Loader::includeModule('iblock'); $property = \CIBlockProperty::GetList( [], [ 'IBLOCK_ID' => $iblockId, 'CODE' => $code' ] )->Fetch(); $ibpenum = new \CIBlockPropertyEnum(); $valueId = $ibpenum->Add([ 'PROPERTY_ID' => $property['ID'], 'VALUE' => $newValueText, 'XML_ID' => $newValueXmlId, ]); if ((int) $valueId < 0) { throw new \Exception('Unable to add a value'); } ``` |
| Код |  |  |
| ``` \Bitrix\Main\Loader::includeModule('iblock'); $property = \CIBlockProperty::GetList( [], [ 'IBLOCK_ID' => $iblockId, 'CODE' => $code' ] )->Fetch(); $ibpenum = new \CIBlockPropertyEnum(); $valueId = $ibpenum->Add([ 'PROPERTY_ID' => $property['ID'], 'VALUE' => $newValueText, 'XML_ID' => $newValueXmlId, ]); if ((int) $valueId < 0) { throw new \Exception('Unable to add a value'); } ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 1 **Влад Красовский**07.09.2016 18:20:37 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| \| Цитата \| \| \| \| --- \| --- \| --- \| \| [Евгений Полянский](https://dev.1c-bitrix.ru/community/webdev/user/24866/) пишет: Сначала нужно получить ID свойства: \\| Код \\| \\| --- \\| \\| ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` \\| \| Код \| ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` \| \| Код \| \| \| \| ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` \| \| \| Можно короче \| Код \| \| --- \| \| ``` $property = CIBlockProperty::GetByID($PROPERTY_CODE, $IBLOCK_ID)->GetNext(); $PROPERTY_ID = $property['ID']; ``` \| | Цитата | [Евгений Полянский](https://dev.1c-bitrix.ru/community/webdev/user/24866/) пишет: Сначала нужно получить ID свойства: \| Код \| \| --- \| \| ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` \| | Код | ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` | Код | ``` $property = CIBlockProperty::GetByID($PROPERTY_CODE, $IBLOCK_ID)->GetNext(); $PROPERTY_ID = $property['ID']; ``` |
| Цитата |  |  |  |  |  |  |
| [Евгений Полянский](https://dev.1c-bitrix.ru/community/webdev/user/24866/) пишет: Сначала нужно получить ID свойства: \| Код \| \| --- \| \| ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` \| | Код | ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` |  |  |  |  |
| Код |  |  |  |  |  |  |
| ``` $PROPERTY_CODE = 'MY_PROPERTY' ; $properties = CIBlockProperty::GetList( Array ( "sort" => "asc" , "name" => "asc" , Array ( "ACTIVE" => "Y" , "IBLOCK_ID" => $IBLOCK_ID , "CODE" => $PROPERTY_CODE )); while ( $prop_fields = $properties ->GetNext()) { $PROPERTY_ID = $prop_fields [ "ID" ]; } ``` |  |  |  |  |  |  |
| Код |  |  |  |  |  |  |
| ``` $property = CIBlockProperty::GetByID($PROPERTY_CODE, $IBLOCK_ID)->GetNext(); $PROPERTY_ID = $property['ID']; ``` |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


| ![](../images/ab4ec99760.gif) 0 **Евгений Полянский**22.12.2015 17:08:54 |  |  |
| --- | --- | --- |
| Сначала нужно получить ID свойства: \| Код \| \| --- \| \| ``` $PROPERTY_CODE = 'MY_PROPERTY'; $properties = CIBlockProperty::GetList(Array("sort"=>"asc", "name"=>"asc" ;) , Array("ACTIVE"=>"Y", "IBLOCK_ID"=>$IBLOCK_ID,"CODE"=>$PROPERTY_CODE)); while ($prop_fields = $properties->GetNext()) { $PROPERTY_ID = $prop_fields["ID"]; } ``` \| | Код | ``` $PROPERTY_CODE = 'MY_PROPERTY'; $properties = CIBlockProperty::GetList(Array("sort"=>"asc", "name"=>"asc" ;) , Array("ACTIVE"=>"Y", "IBLOCK_ID"=>$IBLOCK_ID,"CODE"=>$PROPERTY_CODE)); while ($prop_fields = $properties->GetNext()) { $PROPERTY_ID = $prop_fields["ID"]; } ``` |
| Код |  |  |
| ``` $PROPERTY_CODE = 'MY_PROPERTY'; $properties = CIBlockProperty::GetList(Array("sort"=>"asc", "name"=>"asc" ;) , Array("ACTIVE"=>"Y", "IBLOCK_ID"=>$IBLOCK_ID,"CODE"=>$PROPERTY_CODE)); while ($prop_fields = $properties->GetNext()) { $PROPERTY_ID = $prop_fields["ID"]; } ``` |  |  |
|  |  |  |
