# GetPropertyValuesArray


```
CIBlockElement::GetPropertyValuesArray(
	&$result,
	$iblockID,
	$filter,
	$propertyFilter = array(),
	$options = array()
);
```

Получение значений свойств элементов одного инфоблока для компонента. Строго рекомендуется как замена кода вида ``` $iterator = CIBlockElement::GetList(); while ($obj = $iterator->GetNextElement()) { $properties = $obj->GetProperties(); } ``` в целях улучшения производительности.


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| result | Массив результатов, в качестве ключей должен содержать ID элементов. Передается по ссылке. Для каждого элемента вернет массив значений свойств. |
| iblockID | ID инфоблока (ЕДИНИЧНОЕ значение) |
| filter | Фильтр [CIBlockElement::GetList](getlist.md) для отбора элементов. Ключ IBLOCK_ID указывать нет необходимости - он будет добавлен внутри метода. |
| *propertyFilter* | Фильтр для отбора свойств. необязательный. Может содержать 3 ключа. либо ID - массив ID возвращаемых свойств. либо CODE - массив символьных кодов свойств. При указании обоих ключей учитывается только ID. Третий ключ - фильтр по активности свойств. Если не указать - будут выведены только активные свойства |
| *options* | Дополнительные настройки. Необязательный. Возможные ключи: USE_PROPERTY_ID = Y - ключами массива значений для каждого элемента использовать ID свойств. Иначе - символьные коды. PROPERTY_FIELDS - массив полей СВОЙСТВА, возвращаемых в результате. GET_RAW_DATA => Y - в этом случае в возвращаемых данных не будет ключей с ~ в начале, а оставшиеся не будут приведены к html-безопасному виду. |


#### Возвращаемое значение

Возвращаемое значение - нет.






| ![](../images/2974a14dd4.jpg) 16 **Дмитрий Крюков**02.09.2019 01:23:05 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Получение свойств методом GetPropertyValuesArray() для любого количества элементов обходятся статичным количеством запросов, за исключением получения значений списочных свойств, запросы на получение которых выполняются в цикле для каждого значения свойства. | Код | ``` $elements = []; $order = ['SORT' => 'ASC']; $filter = ['IBLOCK_ID' => 1]; $rows = CIBlockElement::GetList($order, $filter); while ($row = $rows->fetch()) { $row['PROPERTIES'] = []; $elements[$row['ID']] =& $row; unset($row); } CIBlockElement::GetPropertyValuesArray($elements, $filter['IBLOCK_ID'], $filter); unset($rows, $filter, $order); ``` | Цитата | Строго рекомендуется как замена кода вида ... GetNextElement() ... GetProperties() |
| Код |  |  |  |  |
| ``` $elements = []; $order = ['SORT' => 'ASC']; $filter = ['IBLOCK_ID' => 1]; $rows = CIBlockElement::GetList($order, $filter); while ($row = $rows->fetch()) { $row['PROPERTIES'] = []; $elements[$row['ID']] =& $row; unset($row); } CIBlockElement::GetPropertyValuesArray($elements, $filter['IBLOCK_ID'], $filter); unset($rows, $filter, $order); ``` |  |  |  |  |
| Цитата |  |  |  |  |
| Строго рекомендуется как замена кода вида ... GetNextElement() ... GetProperties() |  |  |  |  |
|  |  |  |  |  |
