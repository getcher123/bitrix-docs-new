# GetProperty


### Описание


```
CDBResult
	CIBlockElement::GetProperty(
	int iblock_id,
	int element_id,
	array arOrder = Array(),
	array arFilter = Array()
);
```

Метод возвращает значения свойства для элемента *element_id*. Метод статический.


#### Смотрите также


- [CDBResult](../../../main/reference/cdbresult/index.md)
- [Поля свойств](../../fields.md#fproperty)

---
### Параметры вызова


| Параметр | Описание |
| --- | --- |
| iblock_id | Код инфоблока. |
| element_id | Код элемента. |
| arOrder | Массив вида Array(*by1*=>*order1*[, *by2*=>*order2* [, ..]]), где *by* - поле для сортировки, может принимать значения: - **id** - код свойства; - **sort** - индекс сортировки; - **name** - имя свойства; - active - активность свойства; - value_id - код значения свойства; - enum_sort - индекс сортировки варианта списочного свойства; *order* - порядок сортировки, может принимать значения: - **asc** - по возрастанию; - **desc** - по убыванию; Необязательный. По умолчанию равен *Array("sort"=>"asc")* **Примечание:**параметр не должен быть *false*, иначе метод отработает неправильно и результат не будет отобран по заданным критериям. |
| arFilter | Массив вида array("фильтруемое поле"=>"значения фильтра" [, ...]) "фильтруемое поле" может принимать значения: ACTIVE - активность (Y/N), - NAME - название свойства (можно использовать маску %\|_), - ID - код свойства, - ACTIVE - активность (Y\|N), - SEARCHABLE - участвует в поиске или нет (Y\|N), - PROPERTY_TYPE - тип свойства, - CODE - символьный код свойства, - EMPTY - пустота свойства (Y\|N). Не обязательный параметр, по умолчанию равен array(). |

**Примечание**- Существуют ещё параметры, оставленные для сохранения совместимости: **$by**и **$order**.

---
### Возвращаемое значение

Возвращается объект [CDBResult](../../../main/reference/cdbresult/index.md), содержащий [поля свойств](../../fields.md#fproperty) и поля со значениями:


PROPERTY_VALUE_ID - код значения свойства,
VALUE - значение свойства,
DESCRIPTION - описание значения свойства,
VALUE_ENUM - текстовое значение элемента списочного свойства,
VALUE_XML_ID - внешний код значения свойства типа "список". ---
### Примеры использования

Пример 1:


```
<?
$db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, array("sort" => "asc"), Array("CODE"=>"FORUM_TOPIC_ID"));
if($ar_props = $db_props->Fetch())
	$FORUM_TOPIC_ID = IntVal($ar_props["VALUE"]);
else
	$FORUM_TOPIC_ID = false;
?>
```

Пример 2 (получить значения для множественного свойства):


```
$VALUES = array();
$res = CIBlockElement::GetProperty(IKSO_CUSTOM::$IBLOCKS['brands'], $BRAND_ID, "sort", "asc", array("CODE" => "BRAND_CLASS"));
while ($ob = $res->GetNext())
{
	$VALUES[] = $ob['VALUE'];
}
```

Пример 3 (получить значения для немножественного свойства):


```
$res = CIBlockElement::GetProperty(IKSO_CUSTOM::$IBLOCKS['brands'], $BRAND_ID, "sort", "asc", array("CODE" => "BRAND_CLASS"));
	if ($ob = $res->GetNext())
	{
		$VALUE = $ob['VALUE'];
	}
```

Пример 4:

Если значений у свойства нет и в фильтр не передается "EMPTY"=>"N", то метод вернет массив с с пустым ключом VALUE:


```
//используются Инфоблоки 2.0
$db_props = CIBlockElement::GetProperty(30, 14391, "sort", "asc", Array("CODE"=>"XXX")); // XXX - множественное свойства типа "Строка"
if($ar_props = $db_props->Fetch()):
echo "<pre>".print_r($ar_props, true)."<pre>";
endif;
```

Пример 5

Если нужно получить имена значения типа список


```
?
$res = CIBlockElement::GetProperty(ID_BLOKA, ID_ELEMENTA, array("sort" => "asc"), Array("CODE"=>"CATEGORIES"));
	while ($ob = $res->GetNext()) {
		$prop = $ob['VALUE_ENUM'];
		echo $prop. "
";
	}
?
```

---




| ![](../images/8e2ac2aab3.jpg) 0 **Сергей Мостовой**16.02.2022 13:31:55 |  |  |
| --- | --- | --- |
| Вывести Артикул товара, где CML2_ARTICLE код свойства в инфоблоке \| Код \| \| --- \| \| ``` <? if($arElement["PROPERTIES"]["CML2_ARTICLE"]["VALUE"]) { ?> <strong>Артикул:</strong> <?=$arElement["PROPERTIES"]["CML2_ARTICLE"]["VALUE"]?> <? } ?> ``` \| | Код | ``` <? if($arElement["PROPERTIES"]["CML2_ARTICLE"]["VALUE"]) { ?> <strong>Артикул:</strong> <?=$arElement["PROPERTIES"]["CML2_ARTICLE"]["VALUE"]?> <? } ?> ``` |
| Код |  |  |
| ``` <? if($arElement["PROPERTIES"]["CML2_ARTICLE"]["VALUE"]) { ?> <strong>Артикул:</strong> <?=$arElement["PROPERTIES"]["CML2_ARTICLE"]["VALUE"]?> <? } ?> ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 1 **crazydrummer**10.05.2021 21:08:53 |  |  |
| --- | --- | --- |
| **Получаем все поля и свойства в удобном для дальнейшего вывода формате** \| Код \| \| --- \| \| ``` public static function getIblockElement($iblockElementId) { $arOrder = []; $arFilter = ['ID' => $iblockElementId]; $arGroupBy = false; $arNavStartParams = false; $arSelectFields = ['ID', '*']; $dbRes = \CIBlockElement::GetList( $arOrder, $arFilter, $arGroupBy, $arNavStartParams, $arSelectFields ); $element = $dbRes->Fetch(); $propsDbres = \CIBlockElement::GetProperty($element['IBLOCK_ID'], $iblockElementId, "sort", "asc", array(">ID" => 1)); $i = 0; while ($prop = $propsDbres->GetNext()) { $i = !isset($element['PROPS'][$prop['CODE' ]]) ? 0 : $i+1; $element['PROPS'][$prop['CODE']]['NAME'] = $prop['NAME']; $element['PROPS'][$prop['CODE']]['TYPE'] = $prop['PROPERTY_TYPE']; $element['PROPS'][$prop['CODE']]['ACTIVE'] = $prop['ACTIVE']; $element['PROPS'][$prop['CODE']]['VALUES'][$i] = [ 'VALUE' => $prop['VALUE'], 'DESCRIPTION' => $prop['DESCRIPTION'], ]; if ($prop['PROPERTY_TYPE'] == 'F') $element['PROPS'][$prop['CODE']]['VALUE'][$i]['PATH'] = \CFile::GetPath(intval($prop['VALUE'])); } return $element; } ``` \| | Код | ``` public static function getIblockElement($iblockElementId) { $arOrder = []; $arFilter = ['ID' => $iblockElementId]; $arGroupBy = false; $arNavStartParams = false; $arSelectFields = ['ID', '*']; $dbRes = \CIBlockElement::GetList( $arOrder, $arFilter, $arGroupBy, $arNavStartParams, $arSelectFields ); $element = $dbRes->Fetch(); $propsDbres = \CIBlockElement::GetProperty($element['IBLOCK_ID'], $iblockElementId, "sort", "asc", array(">ID" => 1)); $i = 0; while ($prop = $propsDbres->GetNext()) { $i = !isset($element['PROPS'][$prop['CODE' ]]) ? 0 : $i+1; $element['PROPS'][$prop['CODE']]['NAME'] = $prop['NAME']; $element['PROPS'][$prop['CODE']]['TYPE'] = $prop['PROPERTY_TYPE']; $element['PROPS'][$prop['CODE']]['ACTIVE'] = $prop['ACTIVE']; $element['PROPS'][$prop['CODE']]['VALUES'][$i] = [ 'VALUE' => $prop['VALUE'], 'DESCRIPTION' => $prop['DESCRIPTION'], ]; if ($prop['PROPERTY_TYPE'] == 'F') $element['PROPS'][$prop['CODE']]['VALUE'][$i]['PATH'] = \CFile::GetPath(intval($prop['VALUE'])); } return $element; } ``` |
| Код |  |  |
| ``` public static function getIblockElement($iblockElementId) { $arOrder = []; $arFilter = ['ID' => $iblockElementId]; $arGroupBy = false; $arNavStartParams = false; $arSelectFields = ['ID', '*']; $dbRes = \CIBlockElement::GetList( $arOrder, $arFilter, $arGroupBy, $arNavStartParams, $arSelectFields ); $element = $dbRes->Fetch(); $propsDbres = \CIBlockElement::GetProperty($element['IBLOCK_ID'], $iblockElementId, "sort", "asc", array(">ID" => 1)); $i = 0; while ($prop = $propsDbres->GetNext()) { $i = !isset($element['PROPS'][$prop['CODE' ]]) ? 0 : $i+1; $element['PROPS'][$prop['CODE']]['NAME'] = $prop['NAME']; $element['PROPS'][$prop['CODE']]['TYPE'] = $prop['PROPERTY_TYPE']; $element['PROPS'][$prop['CODE']]['ACTIVE'] = $prop['ACTIVE']; $element['PROPS'][$prop['CODE']]['VALUES'][$i] = [ 'VALUE' => $prop['VALUE'], 'DESCRIPTION' => $prop['DESCRIPTION'], ]; if ($prop['PROPERTY_TYPE'] == 'F') $element['PROPS'][$prop['CODE']]['VALUE'][$i]['PATH'] = \CFile::GetPath(intval($prop['VALUE'])); } return $element; } ``` |  |  |
|  |  |  |


| ![](../images/586ec3bc3e.jpg) 6 **stvbox**19.11.2012 13:15:36 |
| --- |
| Третий параметр метода не должен быть false. Не правильно происходит перегрузка функции и результат - все подряд, вместо отобранного по необходимым критериям. |
|  |


| ![](../images/bc5412c00e.jpg) 3 **Сергей Фролов**02.12.2011 17:18:50 |  |  |
| --- | --- | --- |
| Если нужно получить значение типа список \| Код \| \| --- \| \| ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, array("sort" => "asc"), Array("CODE"=>"FORUM_TOPIC_ID")); if($ar_props = $db_props->Fetch()) $property_enums = CIBlockPropertyEnum::GetList(Array("DEF"=>"DESC", "SORT"=>"ASC"), Array("IBLOCK_ID"=>$IBLOCK_ID, "ID"=>$ar_props["VALUE"])); while($enum_fields = $property_enums->GetNext()) { $prop_value = $enum_fields["VALUE"]; } ``` \| | Код | ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, array("sort" => "asc"), Array("CODE"=>"FORUM_TOPIC_ID")); if($ar_props = $db_props->Fetch()) $property_enums = CIBlockPropertyEnum::GetList(Array("DEF"=>"DESC", "SORT"=>"ASC"), Array("IBLOCK_ID"=>$IBLOCK_ID, "ID"=>$ar_props["VALUE"])); while($enum_fields = $property_enums->GetNext()) { $prop_value = $enum_fields["VALUE"]; } ``` |
| Код |  |  |
| ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, array("sort" => "asc"), Array("CODE"=>"FORUM_TOPIC_ID")); if($ar_props = $db_props->Fetch()) $property_enums = CIBlockPropertyEnum::GetList(Array("DEF"=>"DESC", "SORT"=>"ASC"), Array("IBLOCK_ID"=>$IBLOCK_ID, "ID"=>$ar_props["VALUE"])); while($enum_fields = $property_enums->GetNext()) { $prop_value = $enum_fields["VALUE"]; } ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 3 **PetrW**03.02.2009 20:20:24 |  |  |  |  |
| --- | --- | --- | --- | --- |
| \| Код \| \| --- \| \| ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, "sort", "asc", Array("CODE"=>"FORUM_TOPIC_ID")); ``` \| Возможно еще так: \| Код \| \| --- \| \| ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, Array("sort"=>"asc"), Array("CODE"=>"FORUM_TOPIC_ID")); ``` \| | Код | ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, "sort", "asc", Array("CODE"=>"FORUM_TOPIC_ID")); ``` | Код | ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, Array("sort"=>"asc"), Array("CODE"=>"FORUM_TOPIC_ID")); ``` |
| Код |  |  |  |  |
| ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, "sort", "asc", Array("CODE"=>"FORUM_TOPIC_ID")); ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` $db_props = CIBlockElement::GetProperty($PRODUCT_IBLOCK_ID, $PRODUCT_ID, Array("sort"=>"asc"), Array("CODE"=>"FORUM_TOPIC_ID")); ``` |  |  |  |  |
|  |  |  |  |  |
