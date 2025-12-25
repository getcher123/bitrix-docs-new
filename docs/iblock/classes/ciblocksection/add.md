# Add


### Описание


```
int
CIBlockSection::Add(
	array arFields,
	bool bResort = true,
	bool bUpdateSearch = true,
	bool bResizePictures = false
);
```

Метод добавляет новый раздел в информационный блок. Перед добавлением раздела вызываются обработчики события [OnBeforeIBlockSectionAdd](../../events/onbeforeiblocksectionadd.md) из которых можно изменить значения полей или отменить добавление раздела вернув сообщение об ошибке. После добавления раздела вызывается событие [OnAfterIBlockSectionAdd](../../events/onafteriblocksectionadd.md). Нестатический метод.


#### Смотрите также


- [CIBlockSection::Update](update.md)
- [OnBeforeIBlockSectionAdd](../../events/onbeforeiblocksectionadd.md)
- [OnAfterIBlockSectionAdd](../../events/onafteriblocksectionadd.md)

---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arFields | Массив вида Array("поле"=>"значение", ...), содержащий значения [полей раздела](../../fields.md#fsection) инфоблоков. Пользовательские свойства UF_XXX можно тоже занести в массив и они будут добавляться. |  |
| bResort | Флаг, указывающий пересчитывать ли правую и левую границы после изменения (поля *LEFT_MARGIN* и *RIGHT_MARGIN*). **Примечание**: настоятельно рекомендуется не устанавливать значение *false*. Установите значение в <i>false</i>, если необходимо выполнить большое количество добавлений при небольшом исходном количестве разделов (например автоматизированное создание дерева разделов &quot;с нуля&quot;), в этом случае для повышения производительности можно установить параметр в <i>false</i>, а после всех изменений вызвать метод <a class="link" href="/api_help/iblock/classes/ciblocksection/index.php">CIBlockSection</a>::<a class="link" href="/api_help/iblock/classes/ciblocksection/resort.php">ReSort</a>() | 3.2.1 |
| bUpdateSearch | Флаг, указывающий, что раздел должен быть проиндексирован для поиска сразу же после сохранения. | 4.0.6 |
| bResizePictures | Использовать настройки инфоблока для обработки изображений. По умолчанию настройки не применяются. Если этот параметр имеет значение true, то к полям PICTURE и DETAIL_PICTURE будут применены правила генерации и масштабирования в соответствии с настройками информационного блока. | 9.0.4 |


#### Возвращаемое значение

Метод возвращает идентификационный код добавленного раздела блока, если добавление прошло успешно. При возникновении ошибки метод вернет false, а в свойстве объекта LAST_ERROR будет содержаться текст ошибки. ---
### Примеры использования


```
<?
$bs = new CIBlockSection;
$arFields = Array(
	"ACTIVE" => $ACTIVE,
	"IBLOCK_SECTION_ID" => $IBLOCK_SECTION_ID,
	"IBLOCK_ID" => $IBLOCK_ID,
	"NAME" => $NAME,
	"SORT" => $SORT,
	"PICTURE" => $_FILES["PICTURE"],
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
if(!$res)
  echo $bs->LAST_ERROR;
?>
```

---




| ![](../images/903baa0e2b.jpeg) 4 **Дмитрий Воеводин**24.08.2016 10:01:09 |  |  |
| --- | --- | --- |
| Если необходимо задать параметры SEO при создании раздела, то в массив $arFields нужно добавить: \| Код \| \| --- \| \| ``` $arFields["IPROPERTY_TEMPLATES"] = array( "SECTION_META_TITLE" => $arLevel["Title"], "SECTION_META_KEYWORDS" => $arLevel["Keywords"], "SECTION_META_DESCRIPTION" => $arLevel["Description"], ); ``` \| | Код | ``` $arFields["IPROPERTY_TEMPLATES"] = array( "SECTION_META_TITLE" => $arLevel["Title"], "SECTION_META_KEYWORDS" => $arLevel["Keywords"], "SECTION_META_DESCRIPTION" => $arLevel["Description"], ); ``` |
| Код |  |  |
| ``` $arFields["IPROPERTY_TEMPLATES"] = array( "SECTION_META_TITLE" => $arLevel["Title"], "SECTION_META_KEYWORDS" => $arLevel["Keywords"], "SECTION_META_DESCRIPTION" => $arLevel["Description"], ); ``` |  |  |
|  |  |  |
