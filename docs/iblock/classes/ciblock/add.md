# Add


### Описание и параметры


```
int
	CIBlock::Add(
	array arFields
);
```

Метод добавляет новый информационный блок. Модифицировать поля, а также отменить создание инфоблока можно добавив обработчик события [OnBeforeIBlockAdd](../../events/onbeforeiblockadd.md). После успешного добавления инфоблока вызываются обработчики события [OnAfterIBlockAdd](../../events/onafteriblockadd.md). Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arFields | Массив Array("поле"=>"значение", ...). Содержит значения [всех полей](../../fields.md#fiblock) информационного блока. Дополнительно в поле SITE_ID должен находиться массив идентификаторов сайтов, к которым привязан добавляемый информационный блок. Кроме того, с помощью поля "GROUP_ID", значением которого должен быть массив соответствий кодов групп правам доступа, можно установить права для разных групп на доступ к информационному блоку(см. [CIBlock](index.md)::[SetPermission()](setpermission.md)). Если задано поле "FIELDS", то будут выполнены настройки полей инфоблока (см. [CIBlock::SetFields](SetFields.md)). Кроме того, предусмотрено поле "VERSION", определяющее способ хранения значений свойств элементов инфоблока (1 - в общей таблице \| 2 - в отдельной). По умолчанию принимает значение **1**. Если необходимо добавить инфоблок с поддержкой бизнес-процессов, то следует указать два дополнительных поля: *BIZPROC*, принимающее значение **Y**, и *WORKFLOW*, принимающее значение **N**. |


#### Возвращаемое значение

Метод возвращает код добавленного информационного блока, если добавление прошло успешно, при возникновении ошибки метод вернет false, а в свойстве объекта LAST_ERROR будет содержаться текст ошибки. ---
### Смотрите также


- [CIBlock::Update](update.md)
- [Поля информационного блока](../../fields.md#fiblock)
- [OnBeforeIBlockAdd](../../events/onbeforeiblockadd.md)
- [OnAfterIBlockAdd](../../events/onafteriblockadd.md)
- [CIBlock::SetFields](SetFields.md)

---
### Примеры использования


```
<?
$arPICTURE = $_FILES["PICTURE"];
$ib = new CIBlock;
$arFields = Array(
	"ACTIVE" => $ACTIVE,
	"NAME" => $NAME,
	"CODE" => $CODE,
	"LIST_PAGE_URL" => $LIST_PAGE_URL,
	"DETAIL_PAGE_URL" => $DETAIL_PAGE_URL,
	"IBLOCK_TYPE_ID" => $type,
	"SITE_ID" => Array("en", "de"),
	"SORT" => $SORT,
	"PICTURE" => $arPICTURE,
	"DESCRIPTION" => $DESCRIPTION,
	"DESCRIPTION_TYPE" => $DESCRIPTION_TYPE,
	"GROUP_ID" => Array("2"=>"D", "3"=>"R")
);
if ($ID > 0)
	$res = $ib->Update($ID, $arFields);
else
{
	$ID = $ib->Add($arFields);
	$res = ($ID>0);
}
?>
```

---
