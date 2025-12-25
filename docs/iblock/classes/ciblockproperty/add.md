# Add


### Описание и параметры


```
int CIBlockProperty::Add(
	array arFields
);
```

Метод добавляет новое свойство. Отменить добавление или изменить поля свойства можно в обработчике события [OnBeforeIBlockPropertyAdd](../../events/onbeforeiblockpropertyadd.md). После добавления нового свойства вызываются обработчики события [OnAfterIBlockPropertyAdd](../../events/onafteriblockpropertyadd.md). Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arFields | Массив Array("поле"=>"значение", ...). Содержит значения [всех полей](../../fields.md#fproperty) свойства. Кроме того, с помощью поля "VALUES", значением которого должен быть массив структуры ``` array( array( "VALUE"=>"значение", "DEF"=>"по умолчанию (Y/N)", "SORT"=>"индекс сортировки" ... ), ) ``` , можно установить варианты выбора для свойств типа "список" (подробнее смотрите метод [CIBlockProperty](index.md)::[UpdateEnum()](updateenum.md)). |


#### Возвращаемое значение

Метод возвращает ID добавленного свойства, если добавление прошло успешно, при возникновении ошибки метод вернет false, а в свойстве объекта LAST_ERROR будет содержаться текст ошибки. ---
### Смотрите также


- [CIBlockProperty::Update](update.md)
- [Поля свойства](../../fields.md#fproperty)
- [OnBeforeIBlockPropertyAdd](../../events/onbeforeiblockpropertyadd.md)
- [OnAfterIBlockPropertyAdd](../../events/onafteriblockpropertyadd.md)

---
### Примеры использования


```
<?
$arFields = Array(
	"NAME" => "Цвет",
	"ACTIVE" => "Y",
	"SORT" => "100",
	"CODE" => "color",
	"PROPERTY_TYPE" => "L",
	"IBLOCK_ID" => 11
);
$arFields["VALUES"][0] = Array(
	"VALUE" => "Красный",
	"DEF" => "N",
	"SORT" => "100"
);
$arFields["VALUES"][1] = Array(
	"VALUE" => "Желтый",
	"DEF" => "N",
	"SORT" => "200"
);
$arFields["VALUES"][2] = Array(
	"VALUE" => "Зеленый",
	"DEF" => "Y",
	"SORT" => "300"
);
$ibp = new CIBlockProperty;
$PropID = $ibp->Add($arFields);
?>
```


```
//добавление свойства типа "HTML"
$arFields = Array(
	"NAME" => "Итог",
	"ACTIVE" => "Y",
	"SORT" => "600",
	"CODE" => "ITOG",
	"PROPERTY_TYPE" => "S",
	"USER_TYPE" => "HTML",
	"IBLOCK_ID" => $arParams["IBLOCK_ID"],
);

$ibp = new CIBlockProperty;
$PropID = $ibp->Add($arFields);


//для добавления свойства типа "Видео" в массиве arFields должно быть указано:
"PROPERTY_TYPE" => "S",
"USER_TYPE" => "video",
```


```
//установка параметра "Выводить поле для описания значения" для свойства инфоблока ("WITH_DESCRIPTION" => "Y")
// доступно только для типов свойств:  S - строка, N - число и F - файл
$arFields = Array(
	"NAME" => "Прочее",
	"ACTIVE" => "Y",
	"SORT" => "1700",
	"CODE" => "F_OTHER",
	"PROPERTY_TYPE" => "S",
	"IBLOCK_ID" => $IBLOCK_ID,
	"WITH_DESCRIPTION" => "Y",
);

$iblockproperty = new CIBlockProperty;
$PropertyID = $iblockproperty->Add($arFields);
```


```
//добавление к инфоблоку свойства типа "Справочник"
$arFields = Array(
	"NAME" => "Производитель",
	"ACTIVE" => "Y",
	"SORT" => "50",
	"CODE" => "PROIZVODITEL",
	"PROPERTY_TYPE" => "S",
	"USER_TYPE" => "directory",
	"IBLOCK_ID" => 888888888888888,//номер вашего инфоблока
	"LIST_TYPE" => "L",
	"MULTIPLE" => "N",
	"USER_TYPE_SETTINGS" => array("size"=>"1", "width"=>"0", "group"=>"N", "multiple"=>"N", "TABLE_NAME"=>"b_producers")
);

$ibp = new CIBlockProperty;
$PropID = $ibp->Add($arFields);


//затем следует в значение свойства вставить значение поля  UF_XML_ID от вашего справочника
CIBlockElement::SetPropertyValuesEx(123188, 888888888888888, array('PROIZVODITEL'=>'000000701'));
```

---



| ![](../images/2068d63a6f.jpg) 5 **Алексей Попович**29.11.2019 21:28:39 |  |  |
| --- | --- | --- |
| Для включения галочки о показе свойства в карточке товара, в список параметров нужно передать массив по ключу "Features" В общем, массив параметра выглядит так: \| Код \| \| --- \| \| ``` $arFields = [ 'NAME' => $arProperty['NAME'], 'ACTIVE' => 'Y', 'SORT' => 500, 'CODE' => $code, 'PROPERTY_TYPE' => 'S', 'IBLOCK_ID' => $this->IBLOCK_ID, 'XML_ID' => $arProperty['XML_ID'], 'FEATURES' => [ [ 'IS_ENABLED'=>'Y', 'MODULE_ID'=>'iblock', 'FEATURE_ID'=>'DETAIL_PAGE_SHOW' ] ] ]; ``` \| | Код | ``` $arFields = [ 'NAME' => $arProperty['NAME'], 'ACTIVE' => 'Y', 'SORT' => 500, 'CODE' => $code, 'PROPERTY_TYPE' => 'S', 'IBLOCK_ID' => $this->IBLOCK_ID, 'XML_ID' => $arProperty['XML_ID'], 'FEATURES' => [ [ 'IS_ENABLED'=>'Y', 'MODULE_ID'=>'iblock', 'FEATURE_ID'=>'DETAIL_PAGE_SHOW' ] ] ]; ``` |
| Код |  |  |
| ``` $arFields = [ 'NAME' => $arProperty['NAME'], 'ACTIVE' => 'Y', 'SORT' => 500, 'CODE' => $code, 'PROPERTY_TYPE' => 'S', 'IBLOCK_ID' => $this->IBLOCK_ID, 'XML_ID' => $arProperty['XML_ID'], 'FEATURES' => [ [ 'IS_ENABLED'=>'Y', 'MODULE_ID'=>'iblock', 'FEATURE_ID'=>'DETAIL_PAGE_SHOW' ] ] ]; ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 0 **Ilya Chumakov**14.06.2019 10:41:09 |
| --- |
| LIST_TYPE в массиве полей отвечает за внешний вид свойства типа список. Если значение = L, то это просто список. Если C - флажки |
|  |


| ![image](../images/7dd82aba60.gif) 5 **ivan trufanov**26.06.2017 02:49:32 |  |  |
| --- | --- | --- |
| Для привязки свойства к элементам инфоблока нужно указать PROPERTY_TYPE => E и LINK_IBLOCK_ID => <нужный iblock> \| Код \| \| --- \| \| ``` $arFields = Array( "NAME" => "Внешний ID элемента", "ACTIVE" => "Y", "SORT" => "600", "CODE" => "ExtElementID", "PROPERTY_TYPE" => "E", "IBLOCK_ID" => 2, "LINK_IBLOCK_ID" => 1 ); $ibp = new CIBlockProperty; $PropID = $ibp->Add($arFields); ``` \| | Код | ``` $arFields = Array( "NAME" => "Внешний ID элемента", "ACTIVE" => "Y", "SORT" => "600", "CODE" => "ExtElementID", "PROPERTY_TYPE" => "E", "IBLOCK_ID" => 2, "LINK_IBLOCK_ID" => 1 ); $ibp = new CIBlockProperty; $PropID = $ibp->Add($arFields); ``` |
| Код |  |  |
| ``` $arFields = Array( "NAME" => "Внешний ID элемента", "ACTIVE" => "Y", "SORT" => "600", "CODE" => "ExtElementID", "PROPERTY_TYPE" => "E", "IBLOCK_ID" => 2, "LINK_IBLOCK_ID" => 1 ); $ibp = new CIBlockProperty; $PropID = $ibp->Add($arFields); ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 9 **Адель Юсупов**24.01.2015 14:37:25 |
| --- |
| //Для прикрепления свойства к разделу необходимо использовать класс **$SECTION_ID = 1; //**- идентификатор раздела, либо 0, если требуется отвязать свойство от инфоблока. **$PROPERTY_ID = 2;**// - идентификатор свойства. **$arLink = array('SMART_FILTER' => 'N');**//- в данный момент может содержать 2 ключа, это IBLOCK_ID и SMART_FILTER. //В свою очередь $arLink = array(‘SMART_FILTER’ => ‘Y’) - включить свойство в умный фильтр, если свойство в умный фильтр включать не требуется, можно просто //не указывать SMART_FILTER, либо $arLink = array(‘SMART_FILTER’ => ‘N’). CIBlockSectionPropertyLink::Add($SECTION_ID, $PROPERTY_ID, $arLink = array()); |
|  |
