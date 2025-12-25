# GetPropertyValues


### Описание и параметры


```
CIBlockElement::GetPropertyValues(
	$IBLOCK_ID,
	$arElementFilter,
	$extMode = false,
	$propertyFilter = array()
);
```

Метод позволяет получить значения свойств для элементов одного информационного блока, отобранных по фильтру


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| IBLOCK_ID | ID инфоблока (ЕДИНИЧНОЕ значение). |
| arElementFilter | Фильтр [CIBlockElement::GetList](getlist.md) для отбора элементов. Ключ IBLOCK_ID указывать нет необходимости - он будет добавлен внутри метода. |
| *extMode* | Признак возврата расширенного числа полей. Необязательный. |
| *propertyFilter* | Фильтр возвращаемых свойств. необязательный. Может иметь только 1 ключ - ID. Это массив ID возвращаемых свойств. Если пуст - будут возвращены значения всех свойств инфоблока, включая неактивные. |

---
### Возвращаемое значение

Возвращаемое значение - объект типа `CIBlockPropertyResult`.

Если **$extMode = false**, то возвратятся следующие ключи для каждого значения свойства:

IBLOCK_ELEMENT_ID - ID элемента,
IBLOCK_PROPERTY_ID - ID свойства,
VALUE - строковое значение свойства,
VALUE_NUM - цифровое значение свойства (имеет смысл для свойств типа число, список, привязка к элементам, разделам, файловым и производным от них). Если **$extMode = true**, то дополнительно вернутся ключи:

PROPERTY_VALUE_ID - ID записи значения свойства в базе,
DESCRIPTION - описание значения свойства (если есть). Результат отсортирован по полю IBLOCK_ELEMENT_ID

---
### Примеры использования

Получить все значения свойств с кодами 10 и 14 активных элементов инфоблока 5


```
$iterator = CIBlockElement::GetPropertyValues(5, array('ACTIVE' => 'Y'), true, array('ID' => array(10, 14)));
while ($row = $iterator->Fetch())
{
	print_r($row);
}
```

---




| ![image](../images/7dd82aba60.gif) 0 **Sherzod Najmiddinov**27.04.2023 12:41:36 |  |  |
| --- | --- | --- |
| \| Код \| \| --- \| \| ``` if (CModule::IncludeModule("iblock")){ $res = CIBlockElement::GetList([], ['IBLOCK_ID'=>IBLOCK_ID], false, [], []); while ($el = $res->GetNextElement()) { $fields = $el->getFields(); $fields['PROPERTIES'] = $el->getProperties(); $arData['ELEMENTS'][] = $fields; } } ``` \| | Код | ``` if (CModule::IncludeModule("iblock")){ $res = CIBlockElement::GetList([], ['IBLOCK_ID'=>IBLOCK_ID], false, [], []); while ($el = $res->GetNextElement()) { $fields = $el->getFields(); $fields['PROPERTIES'] = $el->getProperties(); $arData['ELEMENTS'][] = $fields; } } ``` |
| Код |  |  |
| ``` if (CModule::IncludeModule("iblock")){ $res = CIBlockElement::GetList([], ['IBLOCK_ID'=>IBLOCK_ID], false, [], []); while ($el = $res->GetNextElement()) { $fields = $el->getFields(); $fields['PROPERTIES'] = $el->getProperties(); $arData['ELEMENTS'][] = $fields; } } ``` |  |  |
|  |  |  |


| ![](../images/119669411b.jpg) 0 **Константин Зыков**25.05.2020 15:32:39 |  |  |
| --- | --- | --- |
| В propertyFilter можно указать CODE: | Код | ``` $propertyFilter = ['CODE' => 'SOME_PROPERTY_CODE'] ``` |
| Код |  |  |
| ``` $propertyFilter = ['CODE' => 'SOME_PROPERTY_CODE'] ``` |  |  |
|  |  |  |


| ![](../images/2068d63a6f.jpg) 3 **Алексей Попович**20.06.2019 17:27:36 |  |  |
| --- | --- | --- |
| пример получения списка товаров вместе с получением свойств \| Код \| \| --- \| \| ``` $rsItems = \CIBlockElement::GetList($arSort, $arFilter, $groupParams, $pageParams, $arSelect); $arElementLink = array(); $elementsID = array(); while ($arElement = $rsItems->GetNext()) { $result[] = $arElement; } if (!empty($result)) { foreach ($result as $key=>$item){ $result[$key]["PROPERTIES"] = array(); $arElementLink[$item["ID"]] = &$result[$key]; $elementsID[$key] = $item["ID"]; } $arPropFilter = array( 'ID' => $elementsID, 'IBLOCK_ID' => $arFilter['IBLOCK_ID'], ); \CIBlockElement::GetPropertyValuesArray($arElementLink, $arFilter['IBLOCK_ID'], $arPropFilter, []); foreach ($result as $key => $arItem) { if (!empty($arItem['PROPERTIES'])) { $arProperties = []; foreach ($arItem['PROPERTIES'] as $pCode => $arProperty) { if ( (is_array($arProperty['VALUE']) && !empty($arProperty['VALUE'])) \\|\\| (!is_array($arProperty['VALUE']) && strlen($arProperty['VALUE']) > 0)) { $arProperties[$pCode] = \CIBlockFormatProperties::GetDisplayValue( array('ID' => $arItem['ID'], 'NAME' => $arItem['NAME']), $arProperty, ''); } } if (!empty($arProperties)) { $result[$key]['PROPERTIES'] = $arProperties; } } } } ``` \| | Код | ``` $rsItems = \CIBlockElement::GetList($arSort, $arFilter, $groupParams, $pageParams, $arSelect); $arElementLink = array(); $elementsID = array(); while ($arElement = $rsItems->GetNext()) { $result[] = $arElement; } if (!empty($result)) { foreach ($result as $key=>$item){ $result[$key]["PROPERTIES"] = array(); $arElementLink[$item["ID"]] = &$result[$key]; $elementsID[$key] = $item["ID"]; } $arPropFilter = array( 'ID' => $elementsID, 'IBLOCK_ID' => $arFilter['IBLOCK_ID'], ); \CIBlockElement::GetPropertyValuesArray($arElementLink, $arFilter['IBLOCK_ID'], $arPropFilter, []); foreach ($result as $key => $arItem) { if (!empty($arItem['PROPERTIES'])) { $arProperties = []; foreach ($arItem['PROPERTIES'] as $pCode => $arProperty) { if ( (is_array($arProperty['VALUE']) && !empty($arProperty['VALUE'])) \|\| (!is_array($arProperty['VALUE']) && strlen($arProperty['VALUE']) > 0)) { $arProperties[$pCode] = \CIBlockFormatProperties::GetDisplayValue( array('ID' => $arItem['ID'], 'NAME' => $arItem['NAME']), $arProperty, ''); } } if (!empty($arProperties)) { $result[$key]['PROPERTIES'] = $arProperties; } } } } ``` |
| Код |  |  |
| ``` $rsItems = \CIBlockElement::GetList($arSort, $arFilter, $groupParams, $pageParams, $arSelect); $arElementLink = array(); $elementsID = array(); while ($arElement = $rsItems->GetNext()) { $result[] = $arElement; } if (!empty($result)) { foreach ($result as $key=>$item){ $result[$key]["PROPERTIES"] = array(); $arElementLink[$item["ID"]] = &$result[$key]; $elementsID[$key] = $item["ID"]; } $arPropFilter = array( 'ID' => $elementsID, 'IBLOCK_ID' => $arFilter['IBLOCK_ID'], ); \CIBlockElement::GetPropertyValuesArray($arElementLink, $arFilter['IBLOCK_ID'], $arPropFilter, []); foreach ($result as $key => $arItem) { if (!empty($arItem['PROPERTIES'])) { $arProperties = []; foreach ($arItem['PROPERTIES'] as $pCode => $arProperty) { if ( (is_array($arProperty['VALUE']) && !empty($arProperty['VALUE'])) \|\| (!is_array($arProperty['VALUE']) && strlen($arProperty['VALUE']) > 0)) { $arProperties[$pCode] = \CIBlockFormatProperties::GetDisplayValue( array('ID' => $arItem['ID'], 'NAME' => $arItem['NAME']), $arProperty, ''); } } if (!empty($arProperties)) { $result[$key]['PROPERTIES'] = $arProperties; } } } } ``` |  |  |
|  |  |  |
