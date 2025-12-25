# Update


### Описание и параметры


```
bool CIBlock::Update(
	int ID,
	array arFields
);
```

Метод изменяет параметры информационного блока с кодом *ID*. Модифицировать поля, а также отменить изменение параметров можно добавив обработчик события [OnBeforeIBlockUpdate](../../events/onbeforeiblockupdate.md). После успешного добавления инфоблока вызываются обработчики события [OnAfterIBlockUpdate](../../events/onafteriblockupdate.md). Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | ID изменяемого информационного блока. |
| arFields | Массив Array("поле"=>"значение", ...). Содержит значения [всех полей](../../fields.md#fiblock) информационного блока. Дополнительно в поле SITE_ID должен находиться массив идентификаторов сайтов, к которым привязан изменяемый информационный блок. Кроме того, с помощью поля "GROUP_ID", значением которого должен быть массив соответствий кодов групп правам доступа, можно установить права для разных групп на доступ к информационному блоку(см. [CIBlock](index.md)::[SetPermission()](setpermission.md)). Если задано поле "FIELDS", то будут выполнены настройки полей инфоблока (см. [CIBlock::SetFields](SetFields.md)). |


#### Возвращаемое значение

Метод возвращает true если изменение прошло успешно, при возникновении ошибки метод вернет false, а в свойстве LAST_ERROR объекта будет содержаться текст ошибки. ---
### Смотрите также


- [CIBlock::Add](add.md)
- [Поля информационного блока](../../fields.md#fiblock)
- [CIBlock::SetFields](SetFields.md)
- [OnBeforeIBlockUpdate](../../events/onbeforeiblockupdate.md)
- [OnAfterIBlockUpdate](../../events/onafteriblockupdate.md)

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




| ![](../images/2068d63a6f.jpg) 0 **Алексей Попович**16.05.2021 22:57:31 |  |  |
| --- | --- | --- |
| Чтобы программно отключить проверку на уникальность символьного кода разделов инфоблока, необходимо выполнить такой код: \| Код \| \| --- \| \| ``` \Bitrix\Main\Loader::includeModule('iblock'); $arFields = []; $arFields["SECTION_CODE"]["DEFAULT_VALUE"]["UNIQUE"] = "N"; // отключаем проверку на уникальность $arFields["SECTION_CODE"]["IS_REQUIRED"] = "Y"; // оставляем обязательность самого символьного кода \CIBlock::SetFields($IBLOCK_ID,[$arFields]); ``` \| | Код | ``` \Bitrix\Main\Loader::includeModule('iblock'); $arFields = []; $arFields["SECTION_CODE"]["DEFAULT_VALUE"]["UNIQUE"] = "N"; // отключаем проверку на уникальность $arFields["SECTION_CODE"]["IS_REQUIRED"] = "Y"; // оставляем обязательность самого символьного кода \CIBlock::SetFields($IBLOCK_ID,[$arFields]); ``` |
| Код |  |  |
| ``` \Bitrix\Main\Loader::includeModule('iblock'); $arFields = []; $arFields["SECTION_CODE"]["DEFAULT_VALUE"]["UNIQUE"] = "N"; // отключаем проверку на уникальность $arFields["SECTION_CODE"]["IS_REQUIRED"] = "Y"; // оставляем обязательность самого символьного кода \CIBlock::SetFields($IBLOCK_ID,[$arFields]); ``` |  |  |
|  |  |  |
