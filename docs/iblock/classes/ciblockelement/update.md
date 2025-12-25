# Update


### Описание


```
bool
CIBlockElement::Update(
	int ID,
	array arFields,
	bool bWorkFlow = false,
	bool bUpdateSearch = true,
	bool bResizePictures = false,
	bool bCheckDiskQuota = true
);
```

Метод изменяет параметры элемента с кодом *ID*. Перед изменением элемента вызываются обработчики события [OnStartIBlockElementUpdate](../../events/OnStartIBlockElementUpdate.md) из которых можно изменить значения полей или отменить изменение элемента вернув сообщение об ошибке. После изменения элемента вызывается само событие [OnAfterIBlockElementUpdate](../../events/onafteriblockelementupdate.md). Нестатический метод.

Если изменяется свойство типа **файл**, то необходимо сформировать **массив**.


#### Смотрите также


- [CIBlockElement::Add](add.md)
- [OnBeforeIBlockElementUpdate](../../events/onbeforeiblockelementupdate.md)
- [OnAfterIBlockElementUpdate](../../events/onafteriblockelementupdate.md)

---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| ID | ID изменяемой записи. |  |
| arFields | Массив вида Array("поле"=>"значение", ...), содержащий значения [полей элемента](../../fields.md#felement) инфоблоков и дополнительно может содержать поле "PROPERTY_VALUES" - массив со всеми значениями свойств элемента в виде массива Array("код свойства"=>"значение свойства"). Где "код свойства" - числовой или символьный код свойства, "значение свойства" - одиночное значение, либо массив значений (если свойство множественное). Если массив*PROPERTY_VALUES* задан, то он должен содержать полный набор значений свойств для данного элемента, т.е. если в нем будет отсутствовать одно из свойств, то все его значения для данного элемента будут удалены. Это справедливо для всех типов свойств кроме типа **файл**. Файлы надо удалять через массив с параметром "del"=>"Y". Если свойство типа **список**, то в *PROPERTY_VALUES* надо отдавать не название, а ID значения. Дополнительно для сохранения значения свойств см: [CIBlockElement](index.md)::[SetPropertyValues()](setpropertyvalues.md), [CIBlockElement](index.md)::[SetPropertyValueCode().](setpropertyvaluecode.md) |  |
| bWorkFlow | Изменение в режиме документооборота. Если true и модуль документооборота установлен, то данное изменение будет учтено в журнале изменений элемента. Не обязательный параметр, по умолчанию изменение в режиме документооборота отключено. **Примечание:**в режиме документооборота можно передавать значения не всех свойств в PROPERTY_VALUES, а только необходимых. | 3.1.3 |
| bUpdateSearch | Индексировать элемент для поиска. Для повышения производительности можно отключать этот параметр во время серии изменений элементов, а после их окончания переиндексировать поиск. Не обязательный параметр, по умолчанию элемент после изменения будет автоматически проиндексирован в поиске. | 3.2.1 |
| bResizePictures | Использовать настройки инфоблока для обработки изображений. По умолчанию настройки не применяются. Если этот параметр имеет значение true, то к полям PREVIEW_PICTURE и DETAIL_PICTURE будут применены правила генерации и масштабирования в соответствии с настройками информационного блока. | 8.0.10 |
| bCheckDiskQuota | Проверять ограничение по месту занимаемому базой данных и файлами или нет (настройка главного модуля). Необязательный параметр. | 11.0.14 |


#### Возвращаемое значение

Метод возвращает true если изменение прошло успешно, при возникновении ошибки метод вернет false, а в свойстве LAST_ERROR объекта будет содержаться текст ошибки. ---
### Примеры использования


```
<?
$el = new CIBlockElement;
$PROP = array();
$PROP[12] = "Белый";  // свойству с кодом 12 присваиваем значение "Белый"
$PROP[3] = 38;        // свойству с кодом 3 присваиваем значение 38
$arLoadProductArray = Array(
	"MODIFIED_BY"    => $USER->GetID(), // элемент изменен текущим пользователем
	"IBLOCK_SECTION" => false,          // элемент лежит в корне раздела
	"PROPERTY_VALUES"=> $PROP,
	"NAME"           => "Элемент",
	"ACTIVE"         => "Y",            // активен
	"PREVIEW_TEXT"   => "текст для списка элементов",
	"DETAIL_TEXT"    => "текст для детального просмотра",
	"DETAIL_PICTURE" => CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/image.gif")
);
$PRODUCT_ID = 2;  // изменяем элемент с кодом (ID) 2
$res = $el->Update($PRODUCT_ID, $arLoadProductArray);
?>
```

Менять параметр IBLOCK_ID нельзя.

Пример задания нового значения дополнительного свойства:

Для типа HTML/TEXT, при вставке HTML-кода и автоматическом подключении HTML-редактора:
```
$PROP[tables] = array("VALUE" => array("TYPE" =>"HTML","TEXT" => $matches[0]));
```

Для типа HTML/TEXT, при вставке plain text:
```
$PROP[tables] = array("VALUE" => array("TYPE" =>"TEXT","TEXT" => $matches[0]));
```

---




| ![image](../images/7dd82aba60.gif) 1 **Александр Ризель**17.04.2021 03:36:25 |  |  |
| --- | --- | --- |
| Для того чтобы опубликовать последний черновик надо сделать так: \| Код \| \| --- \| \| ``` $el = new CIBlockElement; $el->Update( $ID, // айди элемента [ 'WF_STATUS_ID' => 1, 'ACTIVE' => 'Y' ], true ); ``` \| | Код | ``` $el = new CIBlockElement; $el->Update( $ID, // айди элемента [ 'WF_STATUS_ID' => 1, 'ACTIVE' => 'Y' ], true ); ``` |
| Код |  |  |
| ``` $el = new CIBlockElement; $el->Update( $ID, // айди элемента [ 'WF_STATUS_ID' => 1, 'ACTIVE' => 'Y' ], true ); ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 2 **Дмитрий Грищенко**22.04.2020 07:43:06 |  |  |
| --- | --- | --- |
| Удаление PREVIEW_PICTURE \| Код \| \| --- \| \| ``` $arFields['PREVIEW_PICTURE'] = ['del' => 'Y']; ``` \| | Код | ``` $arFields['PREVIEW_PICTURE'] = ['del' => 'Y']; ``` |
| Код |  |  |
| ``` $arFields['PREVIEW_PICTURE'] = ['del' => 'Y']; ``` |  |  |
|  |  |  |


| ![](../images/505bdd5535.png) 12 **Антон Царук**24.04.2017 14:16:36 |  |  |
| --- | --- | --- |
| Тонкий момент. Если в init.php задан обработчик OnBeforeIBlockElementUpdate, в котором происходит манипуляция с массивом $arFields[PROPERTY_VALUES] (изменение его значений), а где-то в коде сайта вызывается функция CIBlockElement::Update без задания массива PROPERTY_VALUES, то результатом ее выполнения может стать очистка значений свойств элемента (так как в обработчик массив PROPERTY_VALUES не поступит, что, в общем-то, логично). Поэтому обязательно в OnBeforeIBlockElementUpdate проверяем, есть ли вообще что-то в массиве PROPERTY_VALUES: \| Код \| \| --- \| \| ``` if(count($arFields[PROPERTY_VALUES]))... ``` \| | Код | ``` if(count($arFields[PROPERTY_VALUES]))... ``` |
| Код |  |  |
| ``` if(count($arFields[PROPERTY_VALUES]))... ``` |  |  |
|  |  |  |


| ![](../images/505bdd5535.png) 2 **Антон Царук**13.12.2016 16:45:57 |
| --- |
| Для установки дат DATE_ACTIVE_FROM и DATE_ACTIVE_TO используется формат сайта: d.m.Y. Передавать даты в формате БД - не получается... |
|  |


| ![](../images/ee42e7da8d.jpg) 16 **Сергей Талызенков**18.04.2016 17:27:48 |
| --- |
| IBLOCK_SECTION_ID основной раздел элемента IBLOCK_SECTION - массив разделов к которым привязан элемент |
|  |


| ![](../images/1c5bfe3846.png) 4 **Роман Егоров**26.01.2016 14:49:10 |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ВНИМАНИЕ!**Проблема актуальна на последней текущей версии 15.5.10. Такая запись не пройдет и будет ошибка Fatal error: Call to undefined method CBitrixComponent::CheckFields() in /bitrix/modules/iblock/classes/general/iblocksection.php on line ... **КодCIBlockElement::Update(int ID,int ID, array arFields, bool bWorkFlow = false, bool bUpdateSearch = true, bool bResizePictures = false, bool bCheckDiskQuota = true)** Требуется обязательно использовать конструктор такого вида: **Код$el = new CIBlockElement; $res = $el->Update($PRODUCT_ID, $arLoadProductArray);** | Код | ``` CIBlockElement::Update(int ID,int ID, array arFields, bool bWorkFlow = false, bool bUpdateSearch = true, bool bResizePictures = false, bool bCheckDiskQuota = true) ``` | Код | ``` $el = new CIBlockElement; $res = $el->Update($PRODUCT_ID, $arLoadProductArray); ``` |
| Код |  |  |  |  |
| ``` CIBlockElement::Update(int ID,int ID, array arFields, bool bWorkFlow = false, bool bUpdateSearch = true, bool bResizePictures = false, bool bCheckDiskQuota = true) ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` $el = new CIBlockElement; $res = $el->Update($PRODUCT_ID, $arLoadProductArray); ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/505bdd5535.png) 6 **Антон Царук**26.11.2015 11:12:12 |  |  |
| --- | --- | --- |
| Помимо "PROPERTY_VALUES" в массиве полей может быть еще и сверхсекретный массив с ключом "RIGHTS" - с его помощью можно настроить расширенный доступ к элементу инфоблока. Например, передавая в качестве $arFields вот такой массив \| Код \| \| --- \| \| ``` 'RIGHTS'=>array("n0" => array("GROUP_CODE" => "U777", "DO_CLEAN" => "N", "TASK_ID" => 34) ``` \| можно установить доступ к элементу для определенного пользователя c ID=777. 34 - это ID права доступа "Изменение" в модуле "Инфоблоки" (ID от проекта к проекту может быть разное, надо смотреть в "Правах доступа" правильное значение) | Код | ``` 'RIGHTS'=>array("n0" => array("GROUP_CODE" => "U777", "DO_CLEAN" => "N", "TASK_ID" => 34) ``` |
| Код |  |  |
| ``` 'RIGHTS'=>array("n0" => array("GROUP_CODE" => "U777", "DO_CLEAN" => "N", "TASK_ID" => 34) ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 5 **Карпов Сергей**24.07.2015 12:51:16 |  |  |
| --- | --- | --- |
| Задача: изменить тип анонсного текста с текстового на html Проблема: из документации не очевидно, что следует писать "PREVIEW_TEXT_TYPE" =>"html" и "html" - маленькими буквами Решение: \| Код \| \| --- \| \| ``` $text= "пример текста <br> для html"; $el = new CIBlockElement; $arLoadProductArray = Array( "MODIFIED_BY" => $USER->GetID(), // элемент изменен текущим пользователем "PREVIEW_TEXT_TYPE" =>"html", "PREVIEW_TEXT_TEXT" => html_entity_decode($text), ); $res = $el->Update($id, $arLoadProductArray); ``` \| | Код | ``` $text= "пример текста <br> для html"; $el = new CIBlockElement; $arLoadProductArray = Array( "MODIFIED_BY" => $USER->GetID(), // элемент изменен текущим пользователем "PREVIEW_TEXT_TYPE" =>"html", "PREVIEW_TEXT_TEXT" => html_entity_decode($text), ); $res = $el->Update($id, $arLoadProductArray); ``` |
| Код |  |  |
| ``` $text= "пример текста <br> для html"; $el = new CIBlockElement; $arLoadProductArray = Array( "MODIFIED_BY" => $USER->GetID(), // элемент изменен текущим пользователем "PREVIEW_TEXT_TYPE" =>"html", "PREVIEW_TEXT_TEXT" => html_entity_decode($text), ); $res = $el->Update($id, $arLoadProductArray); ``` |  |  |
|  |  |  |
