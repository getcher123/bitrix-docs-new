# GetList


### Описание


```
CDBResult CIBlock::GetList(
	array arOrder = Array("SORT"=>"ASC"),
	array arFilter = Array(),
	bool bIncCnt = false
);
```

Возвращает список информационных блоков по фильтру *arFilter* отсортированный в порядке *arOrder*. Метод статический.


#### Возвращаемое значение

Возвращается объект [CDBResult.](../../../main/reference/cdbresult/index.md)
#### Смотрите также


- [CDBResult](../../../main/reference/cdbresult/index.md)
- [Поля CIBlock](../../fields.md#fiblock)

---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arOrder | Массив для сортировки результата. Содержит пары "*поле сортировки*"=>"*направление сортировки*". Поле для сортировки может принимать значения: - **id** - код инфоблока; - **iblock_type** - тип инфоблоков; - **name** - название инфоблока; - **active** - активность; - **code** - символьный код; - **sort** - индекс сортировки; - **element_cnt** - количество элементов (только если *bIncCnt* = true); - **timestamp_x** - дата последнего изменения. |  |
| arFilter | Массив вида *array("фильтруемое поле"=>"значение фильтра" [, ...])*. Фильтруемое поле может принимать значения: - *ACTIVE* - фильтр по активности (Y\|N); - *NAME* - по названию (можно искать по шаблону [%_]); - *EXTERNAL_ID*, *XML_ID* - по внешнему коду (можно искать по шаблону [%_]); - *SITE_ID* - по сайту; - *TYPE* - по типу инфоблоков (можно искать по шаблону [%_]); - *CODE* - по символьному коду (можно искать по шаблону [%_]); - *ID* - по коду; - *VERSION* - по флагу хранения значений свойств элементов инфоблока; - *SOCNET_GROUP_ID* - по идентификатору группы социальной сети в которой используется инфоблок; - *CNT_ACTIVE* - только если *bIncCnt* = true. Если значение Y, то при подсчете элементов будут учитываться только активные элементы, при любом другом значении все элементы; - *CNT_ALL* - только если *bIncCnt* = true. Если значение Y, то при подсчете элементов будут учитываться и те элементы, которые ещё не были опубликованы. При любом другом значении все элементы; - *MIN_PERMISSION* - фильтр по правам доступа, по умолчанию принимает *R* (уровень доступа *Чтение*). - *CHECK_PERMISSIONS* - если "N", то права на доступ не проверяются. Если проверка прав не нужна, то для ускорения запроса следует указывать значение "N". Кроме того, если не указать данный параметр в фильтре или при создании инфоблока не изменить параметр по умолчанию "нет доступа", то результат выдачи обычному пользователю будет пустым. - *PERMISSIONS_BY* - фильтрация по правам произвольного пользователя. Значение - ID пользователя или 0 (неавторизованный). Перед названием фильтруемого поля можно указать тип фильтрации: - "!" - не равно - "<" - меньше - "<=" - меньше либо равно - ">" - больше - ">=" - больше либо равно Все фильтруемые поля кроме (CHECK_PERMISSIONS, MIN_PERMISSION, CNT_ALL и CNT_ACTIVE) могут содержать перед названием **тип проверки фильтра**. "*значения фильтра*" - одиночное значение или массив. Необязательное. По умолчанию записи не фильтруются. |  |
| bIncCnt | Возвращать ли количество элементов в информационном блоке в поле *ELEMENT_CNT*. Необязательный параметр, по умолчанию равен false. | 3.0.6 |

---
### Примеры использования

**Примечание:** при копировании кода в свой проект рекомендуется убрать необязательный параметр bIncCnt (если он не используется), чтобы избежать проблем с производительностью.


```
<?
// выберем все активные информационные блоки для текущего сайта типа catalog
// у которых символьный код не my_products, со счетчиком активных элементов.
$res = CIBlock::GetList(
	Array(),
	Array(
		'TYPE'=>'catalog',
		'SITE_ID'=>SITE_ID,
		'ACTIVE'=>'Y',
		"CNT_ACTIVE"=>"Y",
		"!CODE"=>'my_products'
	), true
);
while($ar_res = $res->Fetch())
{
	echo $ar_res['NAME'].': '.$ar_res['ELEMENT_CNT'];
}
?>
```

---




| ![](../images/3ade78de6e.jpg) 0 **Олег Постоев**04.07.2023 19:33:13 |  |  |
| --- | --- | --- |
| Сделать виз. редактор по умолчанию во всех инфоблоках: \| Код \| \| --- \| \| ``` \Bitrix\Main\Loader::includeModule('iblock'); $iblocks = []; $rsIblocks = \CIBlock::GetList(); while($arIblock = $rsIblocks->GetNext()) { $iblocks[] = $arIblock; } $arFields = []; $arFields['PREVIEW_TEXT_TYPE']['DEFAULT_VALUE'] = 'html'; $arFields['DETAIL_TEXT_TYPE']['DEFAULT_VALUE'] = 'html'; foreach($iblocks as $iblock) { \CIBlock::setFields((int)$iblock['ID'], $arFields); } ``` \| | Код | ``` \Bitrix\Main\Loader::includeModule('iblock'); $iblocks = []; $rsIblocks = \CIBlock::GetList(); while($arIblock = $rsIblocks->GetNext()) { $iblocks[] = $arIblock; } $arFields = []; $arFields['PREVIEW_TEXT_TYPE']['DEFAULT_VALUE'] = 'html'; $arFields['DETAIL_TEXT_TYPE']['DEFAULT_VALUE'] = 'html'; foreach($iblocks as $iblock) { \CIBlock::setFields((int)$iblock['ID'], $arFields); } ``` |
| Код |  |  |
| ``` \Bitrix\Main\Loader::includeModule('iblock'); $iblocks = []; $rsIblocks = \CIBlock::GetList(); while($arIblock = $rsIblocks->GetNext()) { $iblocks[] = $arIblock; } $arFields = []; $arFields['PREVIEW_TEXT_TYPE']['DEFAULT_VALUE'] = 'html'; $arFields['DETAIL_TEXT_TYPE']['DEFAULT_VALUE'] = 'html'; foreach($iblocks as $iblock) { \CIBlock::setFields((int)$iblock['ID'], $arFields); } ``` |  |  |
|  |  |  |


| ![](../images/11e5e0f336.jpeg) 8 **Dmitry Ipatov**30.01.2015 12:24:16 |  |  |
| --- | --- | --- |
| Если у Вас не выбирается инфоблок в методе CIBlock::GetList, то возможно в правах доступа к инфоблоку для всех выбрано нет доступа, в таком случае можно игнорировать проверку прав, используя параметр "CHECK_PERMISSIONS" => "N": \| Код \| \| --- \| \| ``` $ib_list = CIBlock::GetList( Array(), Array( "CODE" => $ib_code, "TYPE" => "sliders", "IBLOCK_TYPE_ID" => $iblocktype, "CHECK_PERMISSIONS" => "N" ) ); ``` \| | Код | ``` $ib_list = CIBlock::GetList( Array(), Array( "CODE" => $ib_code, "TYPE" => "sliders", "IBLOCK_TYPE_ID" => $iblocktype, "CHECK_PERMISSIONS" => "N" ) ); ``` |
| Код |  |  |
| ``` $ib_list = CIBlock::GetList( Array(), Array( "CODE" => $ib_code, "TYPE" => "sliders", "IBLOCK_TYPE_ID" => $iblocktype, "CHECK_PERMISSIONS" => "N" ) ); ``` |  |  |
|  |  |  |


| ![](../images/73c151367a.jpg) 1 **Анатолий Кирсанов**11.02.2014 05:50:32 |
| --- |
| Поиск по мнемоническому коду по маске тоже работает. |
|  |
