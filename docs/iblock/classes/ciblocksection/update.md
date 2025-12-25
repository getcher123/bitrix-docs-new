# Update


### Описание


```
bool CIBlockSection::Update(
	int ID,
	array arFields,
	bool bResort = true,
	bool bUpdateSearch = true,
	bool bResizePictures = false
);
```

Метод изменяет параметры раздела с кодом *ID*. Перед изменением раздела вызываются обработчики события [OnBeforeIBlockSectionUpdate](../../events/onbeforeiblocksectionupdate.md) из которых можно изменить значения полей или отменить изменение параметров раздела вернув сообщение об ошибке. После изменения раздела вызывается событие [OnAfterIBlockSectionUpdate](../../events/onafteriblocksectionupdate.md). Нестатический метод.

**Примечание**: Изменить значения полей GLOBAL_ACTIVE, DEPTH_LEVEL, LEFT_MARGIN, RIGHT_MARGIN, IBLOCK_ID, DATE_CREATE и CREATED_BY нельзя. Значение первого определяется флагом активности раздела и его родителей. DEPTH_LEVEL, LEFT_MARGIN и RIGHT_MARGIN расчитываются автоматически в зависимости от положения раздела в дереве.


#### Смотрите также


- [CIBlockSection::Add](add.md)
- [OnBeforeIBlockSectionUpdate](../../events/onbeforeiblocksectionupdate.md)
- [OnAfterIBlockSectionUpdate](../../events/onafteriblocksectionupdate.md)

---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| ID | Код изменяемой записи. |  |
| arFields | Массив вида Array("поле"=>"значение", ...), содержащий значения [полей раздела](../../fields.md#fsection) инфоблоков. |  |
| bResort | Флаг, указывающий пересчитывать ли правую и левую границы после изменения (поля *LEFT_MARGIN* и *RIGHT_MARGIN*). **Примечание**: настоятельно рекомендуется не устанавливать значение *false*. Если в перечне обновляемых полей имеются ключи IBLOCK_SECTION_ID, NAME, SORT, ACTIVE, то параметр bResort обязательно должен быть установлен в *true*. В противном случае необходимо вызывать после серии операций метод [CIBlockSection](index.md)::[ReSort](resort.md). Установите значение в <i>false</i>, в случае если поля которые влияют на значения границ не изменяются или необходимо выполнить серию изменений приводящих к полной перестройке дерева разделов, в последнем случае для повышения производительности можно установить параметр в <i>false</i>, а после всех изменений вызвать метод <a class="link" href="/api_help/iblock/classes/ciblocksection/index.php">CIBlockSection</a>::<a class="link" href="/api_help/iblock/classes/ciblocksection/resort.php">ReSort</a>() |  |
| bUpdateSearch | Флаг, указывающий, что раздел должен быть проиндексирован для поиска сразу же после сохранения. | 4.0.6 |
| bResizePictures | Использовать настройки инфоблока для обработки изображений. По умолчанию настройки не применяются. Если этот параметр имеет значение true, то к полям PICTURE и DETAIL_PICTURE будут применены правила генерации и масштабирования в соответствии с настройками информационного блока. | 9.0.4 |


#### Возвращаемое значение

Метод возвращает true если изменение прошло успешно, при возникновении ошибки метод вернет false, а в свойстве LAST_ERROR объекта будет содержаться текст ошибки. ---
### Примеры использования


```
<?
$bs = new CIBlockSection;
$arPICTURE = $_FILES["PICTURE"];
$arPICTURE["MODULE_ID"] = "iblock";
$arFields = Array(
	"ACTIVE" => $ACTIVE,
	"IBLOCK_SECTION_ID" => $IBLOCK_SECTION_ID,
	"IBLOCK_ID" => $IBLOCK_ID,
	"NAME" => $NAME,
	"SORT" => $SORT,
	"PICTURE" => $arPICTURE,
	"DESCRIPTION" => $DESCRIPTION,
	"DESCRIPTION_TYPE" => $DESCRIPTION_TYPE
);
if($ID > 0)
{
	$res = $bs->Update($ID, $arFields);
}
else
{
	$ID = $bs->Add($arFields);
	$res = ($ID>0);
}
?>
```

---




| ![image](../images/7dd82aba60.gif) 1 **Константин Фокин**17.09.2016 14:37:33 |  |  |
| --- | --- | --- |
| Нигде не нашёл этой информации - для того, чтобы задать разделу родительским "верхний уровень", нужно \| Код \| \| --- \| \| ``` $arFields = Array( "IBLOCK_SECTION_ID" => 0 ); ``` \| | Код | ``` $arFields = Array( "IBLOCK_SECTION_ID" => 0 ); ``` |
| Код |  |  |
| ``` $arFields = Array( "IBLOCK_SECTION_ID" => 0 ); ``` |  |  |
|  |  |  |


| ![](../images/ebfc93e621.jpg) 6 **Вадим Подовалов**05.03.2015 15:05:00 |  |  |
| --- | --- | --- |
| Если необходимо обновить SEO-данные секции, добавляем ключ ["IPROPERTY_TEMPLATES"] в $arFields : \| Код \| \| --- \| \| ``` $arFields["IPROPERTY_TEMPLATES"] = array( "SECTION_META_TITLE" => "", "SECTION_META_KEYWORDS" => "", "SECTION_META_DESCRIPTION" =>"", "SECTION_PAGE_TITLE" =>"", "ELEMENT_META_TITLE" =>"", "ELEMENT_META_KEYWORDS" =>"", "ELEMENT_META_DESCRIPTION" =>"", "ELEMENT_PAGE_TITLE" =>"", "SECTION_PICTURE_FILE_ALT" => "", "SECTION_PICTURE_FILE_TITLE" =>"", "SECTION_PICTURE_FILE_NAME" => "", "SECTION_DETAIL_PICTURE_FILE_ALT" => "", "SECTION_DETAIL_PICTURE_FILE_TITLE" =>"", "SECTION_DETAIL_PICTURE_FILE_NAME" => "", "ELEMENT_PREVIEW_PICTURE_FILE_ALT" => "", "ELEMENT_PREVIEW_PICTURE_FILE_TITLE" =>"", "ELEMENT_PREVIEW_PICTURE_FILE_NAME" =>"", "ELEMENT_DETAIL_PICTURE_FILE_ALT" =>"", "ELEMENT_DETAIL_PICTURE_FILE_TITLE" =>"", "ELEMENT_DETAIL_PICTURE_FILE_NAME" =>"" ); ``` \| | Код | ``` $arFields["IPROPERTY_TEMPLATES"] = array( "SECTION_META_TITLE" => "", "SECTION_META_KEYWORDS" => "", "SECTION_META_DESCRIPTION" =>"", "SECTION_PAGE_TITLE" =>"", "ELEMENT_META_TITLE" =>"", "ELEMENT_META_KEYWORDS" =>"", "ELEMENT_META_DESCRIPTION" =>"", "ELEMENT_PAGE_TITLE" =>"", "SECTION_PICTURE_FILE_ALT" => "", "SECTION_PICTURE_FILE_TITLE" =>"", "SECTION_PICTURE_FILE_NAME" => "", "SECTION_DETAIL_PICTURE_FILE_ALT" => "", "SECTION_DETAIL_PICTURE_FILE_TITLE" =>"", "SECTION_DETAIL_PICTURE_FILE_NAME" => "", "ELEMENT_PREVIEW_PICTURE_FILE_ALT" => "", "ELEMENT_PREVIEW_PICTURE_FILE_TITLE" =>"", "ELEMENT_PREVIEW_PICTURE_FILE_NAME" =>"", "ELEMENT_DETAIL_PICTURE_FILE_ALT" =>"", "ELEMENT_DETAIL_PICTURE_FILE_TITLE" =>"", "ELEMENT_DETAIL_PICTURE_FILE_NAME" =>"" ); ``` |
| Код |  |  |
| ``` $arFields["IPROPERTY_TEMPLATES"] = array( "SECTION_META_TITLE" => "", "SECTION_META_KEYWORDS" => "", "SECTION_META_DESCRIPTION" =>"", "SECTION_PAGE_TITLE" =>"", "ELEMENT_META_TITLE" =>"", "ELEMENT_META_KEYWORDS" =>"", "ELEMENT_META_DESCRIPTION" =>"", "ELEMENT_PAGE_TITLE" =>"", "SECTION_PICTURE_FILE_ALT" => "", "SECTION_PICTURE_FILE_TITLE" =>"", "SECTION_PICTURE_FILE_NAME" => "", "SECTION_DETAIL_PICTURE_FILE_ALT" => "", "SECTION_DETAIL_PICTURE_FILE_TITLE" =>"", "SECTION_DETAIL_PICTURE_FILE_NAME" => "", "ELEMENT_PREVIEW_PICTURE_FILE_ALT" => "", "ELEMENT_PREVIEW_PICTURE_FILE_TITLE" =>"", "ELEMENT_PREVIEW_PICTURE_FILE_NAME" =>"", "ELEMENT_DETAIL_PICTURE_FILE_ALT" =>"", "ELEMENT_DETAIL_PICTURE_FILE_TITLE" =>"", "ELEMENT_DETAIL_PICTURE_FILE_NAME" =>"" ); ``` |  |  |
|  |  |  |


| ![](../images/00420f9a83.png) 13 **Александр Пятницин**16.12.2014 17:46:58 |  |  |
| --- | --- | --- |
| Пользовательские поля, если они нужны, указываем тут же: \| Код \| \| --- \| \| ``` $bs = new CIBlockSection; $arFields = Array( "ACTIVE" => $ACTIVE, "IBLOCK_SECTION_ID" => False, "IBLOCK_ID" => $IBLOCK_ID, "NAME" => $data["title"], "UF_DESCRIPTION" => $data["description"], "UF_KEYWORDS" => $data["keywords"], "UF_TITLE" => $data["head_title"] ); $bs->Update($data["id"], $arFields); ``` \| | Код | ``` $bs = new CIBlockSection; $arFields = Array( "ACTIVE" => $ACTIVE, "IBLOCK_SECTION_ID" => False, "IBLOCK_ID" => $IBLOCK_ID, "NAME" => $data["title"], "UF_DESCRIPTION" => $data["description"], "UF_KEYWORDS" => $data["keywords"], "UF_TITLE" => $data["head_title"] ); $bs->Update($data["id"], $arFields); ``` |
| Код |  |  |
| ``` $bs = new CIBlockSection; $arFields = Array( "ACTIVE" => $ACTIVE, "IBLOCK_SECTION_ID" => False, "IBLOCK_ID" => $IBLOCK_ID, "NAME" => $data["title"], "UF_DESCRIPTION" => $data["description"], "UF_KEYWORDS" => $data["keywords"], "UF_TITLE" => $data["head_title"] ); $bs->Update($data["id"], $arFields); ``` |  |  |
|  |  |  |
