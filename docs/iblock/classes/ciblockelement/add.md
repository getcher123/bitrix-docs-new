# Add


### Описание


```
int CIBlockElement::Add(
	array arFields,
	bool bWorkFlow = false,
	bool bUpdateSearch = true,
	bool bResizePictures = false
);
```

Метод добавляет новый элемент информационного блока. Перед добавлением элемента вызываются обработчики события [OnBeforeIBlockElementAdd](../../events/onbeforeiblockelementadd.md), из которых можно изменить значения полей или отменить добавление элемента вернув сообщение об ошибке. После добавления элемента вызывается событие [OnAfterIBlockElementAdd](../../events/onafteriblockelementadd.md). Нестатический метод.
#### Смотрите также


- [CIBlockElement::Update](update.md)
- [CIBlockElement](index.md)::[SetPropertyValues()](setpropertyvalues.md)
- [CIBlockElement](index.md)::[SetPropertyValueCode()](setpropertyvaluecode.md)
- [OnBeforeIBlockElementAdd](../../events/onbeforeiblockelementadd.md)
- [OnAfterIBlockElementAdd](../../events/onafteriblockelementadd.md)


**Примечание:**если при добавлении свойств в PROPERTY_VALUES при сохранении элемента инфоблока методом CIBlockElement::Add, происходит подобная ошибка: ``` MySQL Query Error: INS ERT INTO b_iblock_element_property (IBLOCK_ELEMENT_ID, IBLOCK_PROPERTY_ID, VALUE, VALUE_NUM) SEL ECT 323 ,P.ID ,'28' ,28,0000 FR OM b_iblock_property P WHERE ID=42[Column count doesn't match val ue count at row 1] ``` попробуйте выставить пустое значение в *setlocale( LC_NUMERIC, '' );*, чтобы PHP использовал точку при форматировании числа, а не запятую.


---
### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arFields | Массив вида Array("поле"=>"значение", ...), содержащий значения [полей элемента](../../fields.md#felement) инфоблоков и дополнительно может содержать поле "PROPERTY_VALUES" - массив со всеми значениями свойств элемента в виде массива Array("код свойства"=>"значение свойства"). Где "код свойства" - числовой или символьный код свойства, "значение свойства" - одиночное значение, либо массив значений если свойство множественное. Дополнительно для сохранения значения свойств см: [CIBlockElement](index.md)::[SetPropertyValues()](setpropertyvalues.md), [CIBlockElement](index.md)::[SetPropertyValueCode()](setpropertyvaluecode.md). **Примечание:**поля с датами задаются в формате сайта. |  |
| bWorkFlow | Вставка в режиме документооборота. Если true и модуль документооборота установлен, то данное добавление будет учтено в журнале изменения элемента. Не обязательный параметр, по умолчанию вставка в режиме документооборота отключена. | 3.1.3 |
| bUpdateSearch | Индексировать элемент для поиска. Для повышения производительности можно отключать этот параметр во время серии добавлений элементов, а после вставки переиндексировать поиск. Не обязательный параметр, по умолчанию элемент после добавления будет проиндексирован в поиске. | 3.2.1 |
| bResizePictures | Использовать настройки инфоблока для обработки изображений. По умоляанию настройки не применяются. Если этот параметр имеет значение true, то к полям PREVIEW_PICTURE и DETAIL_PICTURE будут применены правила генерации и масштабирования в соответствии с настройками информационного блока. | 8.0.10 |


#### Возвращаемое значение

Метод возвращает ID добавленного элемента инфоблока, если добавление прошло успешно. При возникновении ошибки метод вернет false, а в свойстве объекта LAST_ERROR будет содержаться текст ошибки. ---
### Примеры использования

Пример 1:


```
<?
$el = new CIBlockElement;
$PROP = array();
$PROP[12] = "Белый";  // свойству с кодом 12 присваиваем значение "Белый"
$PROP[3] = 38;        // свойству с кодом 3 присваиваем значение 38
$arLoadProductArray = Array(
	"MODIFIED_BY"    => $USER->GetID(), // элемент изменен текущим пользователем
	"IBLOCK_SECTION_ID" => false,          // элемент лежит в корне раздела
	"IBLOCK_ID"      => 18,
	"PROPERTY_VALUES"=> $PROP,
	"NAME"           => "Элемент",
	"ACTIVE"         => "Y",            // активен
	"PREVIEW_TEXT"   => "текст для списка элементов",
	"DETAIL_TEXT"    => "текст для детального просмотра",
	"DETAIL_PICTURE" => CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/image.gif")
);
if($PRODUCT_ID = $el->Add($arLoadProductArray))
	echo "New ID: ".$PRODUCT_ID;
else
	echo "Error: ".$el->LAST_ERROR;
?>
```

Пример 2 (примеры массивов для свойств):


```
//описание массива для свойства типа "Html/Text"
$arrProp = Array();
$arrProp[ID или CODE][0] = Array("VALUE" => Array ("TEXT" => "значение", "TYPE" => "html или text"));

//описание массива для свойства типа "Список"
$arrProp = Array();
$arrProp[ID или CODE] = Array("VALUE" => $ENUM_ID ); //ENUM_ID - это ID значения в списке, его можно получить при помощи: CIBlockPropertyEnum::GetList

//описание массива для свойства типа "Список" множественного выбора
$arrProp = Array();
$arrProp[ID или CODE] = array( $ENUM_ID1, $ENUM_ID2, $ENUM_ID3, $ENUM_ID4);

//пример массива для вставки видео
$PROP["561"] = Array (
	"n0" => Array(
		"VALUE" => Array ("PATH" => "/upload/single_2.flv", "WIDTH" => 400, "HEIGHT" => 300, "TITLE" => "Заголовок видео", "DURATION" => "00:30", "AUTHOR" => "Автор видео", "DATE" => "01.02.2011")
	)
);
//При добавлении нового значения/значений множественного свойство типа "Файл" необходимо использовать ключи вида n0,n1,n2 ... nN .
```

Пример 3:


```
//детальная картинка загружается непосредственно из формы
<?
$el = new CIBlockElement;
$PROP = array();
$PROP[12] = 'Белый';  // свойству с кодом 12 присваиваем значение "Белый"
$PROP[3] = 38; // свойству с кодом 3 присваиваем значение 38
$arLoadProductArray = Array(
	'MODIFIED_BY' => $GLOBALS['USER']->GetID(), // элемент изменен текущим пользователем
	'IBLOCK_SECTION_ID' => false, // элемент лежит в корне раздела
	'IBLOCK_ID' => 18,
	'PROPERTY_VALUES' => $PROP,
	'NAME' => 'Элемент',
	'ACTIVE' => 'Y', // активен
	'PREVIEW_TEXT' => 'текст для списка элементов',
	'DETAIL_TEXT' => 'текст для детального просмотра',
	'DETAIL_PICTURE' => $_FILES['DETAIL_PICTURE'] // картинка, загружаемая из файлового поля веб-формы с именем DETAIL_PICTURE
);

if($PRODUCT_ID = $el->Add($arLoadProductArray)) {
	echo 'New ID: '.$PRODUCT_ID;
} else {
	echo 'Error: '.$el->LAST_ERROR;
}
?>
```

Пример 4:


```
//добавления элемента с установкой для его свойства пары "значение" и "описание"
$el = new CIBlockElement;

$PROP = array();
$PROP[id_property] =  Array(
	"n0" => Array(
		"VALUE" => "value",
		"DESCRIPTION" => "description")
	);

$arLoadProductArray = Array(
	"IBLOCK_SECTION" => false,
	"IBLOCK_ID" => iblock_id,
	"PROPERTY_VALUES" => $PROP,
	"NAME" => "Элемент",
);

$PRODUCT_ID = id_element;
$res = $el->Update($PRODUCT_ID, $arLoadProductArray);
```

Пример 5:


```
//получить следующий ID для свойства типа "Счётчик" можно методом CIBlockSequence::GetNext и указать его в методе CIBlockElement:Add

CModule::IncludeModule('iblock');
$IBLOCK_ID = 21;
$PROPERTY_ID = 1223;
$seq = new CIBlockSequence($IBLOCK_ID, $PROPERTY_ID);
$el = new CIBlockElement;
$ID = $el->Add(array(
	"IBLOCK_ID" => $IBLOCK_ID,
	"NAME" => "test element",
	"PROPERTY_VALUES" => array($PROPERTY_ID => $seq->GetNext())
));
$rs = CIBlockElement::GetList(array(), array("ID" => $ID), false, false, array("ID", "PROPERTY_ABSTRACT_ID"));
if($ar = $rs->GetNext())
	echo 'PRINT_R:<pre style="font:16px Courier">', print_r($ar, 1), '</pre>';
```

Пример 6:


```
//Если при добавлении элемента надо обязательно заполнять символьный код элемента, то можно не писать свою функцию, а воспользоваться системным методом:

$params = Array(
	"max_len" => "100", // обрезает символьный код до 100 символов
	"change_case" => "L", // буквы преобразуются к нижнему регистру
	"replace_space" => "_", // меняем пробелы на нижнее подчеркивание
	"replace_other" => "_", // меняем левые символы на нижнее подчеркивание
	"delete_repeat_replace" => "true", // удаляем повторяющиеся нижние подчеркивания
	"use_google" => "false", // отключаем использование google
);


"CODE" => CUtil::translit("здесь переменная названия элемента", "ru" , $params);
```

Пример 7:


```
//пример с символьными кодами свойств в массиве PROPERTY_VALUES:

$arFields = array(
	"ACTIVE" => "Y",
	"IBLOCK_ID" => 123,
	"IBLOCK_SECTION_ID" => 456,
	"NAME" => "Название элемента",
	"CODE" => "nazvanie-elementa",
	"DETAIL_TEXT" => "Описание элемента",
	"PROPERTY_VALUES" => array(
		"MANUFACTURER" =>"Имя производителя", //Производитель - свойство
		"ARTNUMBER" =>"Артикул товара", //Артикул производителя - свойство
		"MATERIAL" =>"Материал товара" //Материал - свойство
	)
);
$oElement = new CIBlockElement();
$idElement = $oElement->Add($arFields, false, false, true);

//Необходимо помнить, что если вы указали не все свойства в массиве PROPERTY_VALUES, то остальные свойства могут быть удалены.
//Для обновления элемента гораздо безопаснее использовать CIBlockElement::SetPropertyValueCode.
```

Пример 8 (как получить значение свойства):


```
//например, можно получить значение счетчика и записать его в базу

//$iblockId - ID инфоблока
//$propertyId - ID свойства

$seq = new CIBlockSequence($iblockId, $propertyId);
$current_value = $seq->GetNext();

//в $current_value - новое значение, которое можно писать в базу
```

---




| ![image](../images/7dd82aba60.gif) 2 **novikov_citgk**08.08.2021 23:45:48 |  |  |
| --- | --- | --- |
| Не хватает в примерах: вставки изображения в PREVIEW_PICTURE (или DETAIL_PICTURE) со стороннего сайта: \| Код \| \| --- \| \| ``` $fields = [ ... "PREVIEW_PICTURE" => CFile::MakeFileArray(http://example.net/image.jpg), ... ]; ``` \| | Код | ``` $fields = [ ... "PREVIEW_PICTURE" => CFile::MakeFileArray(http://example.net/image.jpg), ... ]; ``` |
| Код |  |  |
| ``` $fields = [ ... "PREVIEW_PICTURE" => CFile::MakeFileArray(http://example.net/image.jpg), ... ]; ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 3 **Anton Lytko**21.07.2020 16:51:07 |  |  |
| --- | --- | --- |
| \| Код \| \| --- \| \| ``` // добавление свойства типа Справочник (дополнение к Примеру 2) $arrProp = Array(); $arrProp[ID или CODE]['VALUE'] = $UF_XML_ID; ``` \| | Код | ``` // добавление свойства типа Справочник (дополнение к Примеру 2) $arrProp = Array(); $arrProp[ID или CODE]['VALUE'] = $UF_XML_ID; ``` |
| Код |  |  |
| ``` // добавление свойства типа Справочник (дополнение к Примеру 2) $arrProp = Array(); $arrProp[ID или CODE]['VALUE'] = $UF_XML_ID; ``` |  |  |
|  |  |  |


| ![](../images/227b4c4d52.jpg) 2 **Михаил Базаров**15.04.2020 19:32:28 |  |  |
| --- | --- | --- |
| \| Код \| \| --- \| \| ``` $arMorePhoto["VALUE"]; $i = 0; foreach ($_POST["MORE_PHOTO"] as $morePhoto) { $arMorePhoto['n'.$i] = array("VALUE"=>CFile::MakeFileArray($morePhoto)); $i++; } ``` \| | Код | ``` $arMorePhoto["VALUE"]; $i = 0; foreach ($_POST["MORE_PHOTO"] as $morePhoto) { $arMorePhoto['n'.$i] = array("VALUE"=>CFile::MakeFileArray($morePhoto)); $i++; } ``` |
| Код |  |  |
| ``` $arMorePhoto["VALUE"]; $i = 0; foreach ($_POST["MORE_PHOTO"] as $morePhoto) { $arMorePhoto['n'.$i] = array("VALUE"=>CFile::MakeFileArray($morePhoto)); $i++; } ``` |  |  |
|  |  |  |


| ![](../images/505bdd5535.png) 3 **Антон Царук**13.12.2016 16:45:43 |
| --- |
| Для установки дат DATE_ACTIVE_FROM и DATE_ACTIVE_TO используется формат сайта: d.m.Y. Передавать даты в формате БД - не получается... |
|  |


| ![](../images/505bdd5535.png) 7 **Антон Царук**26.11.2015 11:12:52 |  |  |
| --- | --- | --- |
| Помимо "PROPERTY_VALUES" в массиве полей может быть еще и сверхсекретный массив с ключом "RIGHTS" - с его помощью можно настроить расширенный доступ к элементу инфоблока. Например, передавая в качестве $arFields вот такой массив \| Код \| \| --- \| \| ``` 'RIGHTS'=>array("n0" => array("GROUP_CODE" => "U777", "DO_CLEAN" => "N", "TASK_ID" => 34) ``` \| можно установить доступ к элементу для определенного пользователя c ID=777. 34 - это ID права доступа "Изменение" в модуле "Инфоблоки" (ID от проекта к проекту может быть разное, надо смотреть в "Правах доступа" правильное значение) | Код | ``` 'RIGHTS'=>array("n0" => array("GROUP_CODE" => "U777", "DO_CLEAN" => "N", "TASK_ID" => 34) ``` |
| Код |  |  |
| ``` 'RIGHTS'=>array("n0" => array("GROUP_CODE" => "U777", "DO_CLEAN" => "N", "TASK_ID" => 34) ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 3 **Илья Кругляков**04.08.2015 10:31:30 |
| --- |
| Может кому пригодится. Если вы собираетесь добавляемый элемент данным методом далее отправить в корзину, то перед добавлением его в корзину необходимо воспользоваться методом **CCatalogProduct::Add.**Который добавляет параметры товара к элементу каталога. Иначе он не будет добавлен в корзину. |
|  |


| ![image](../images/7dd82aba60.gif) 1 **Илья Карев**21.04.2015 17:24:59 |  |  |  |  |
| --- | --- | --- | --- | --- |
| \| Код \| \| --- \| \| ``` //пример массива для вставки видео $PROP["561"] = Array ( "n0" => Array( "VALUE" => Array ("PATH" => "/upload/single_2.flv", "WIDTH" => 400, "HEIGHT" => 300, "TITLE" => "Заголовок видео", "DURATION" => "00:30", "AUTHOR" => "Автор видео", "DATE" => "01.02.2011") ) ); //При добавлении нового значения/значений множественного свойство типа "Файл" необходимо использовать ключи вида n0,n1,n2 ... nN . ``` \| но для фото надо использовать CFile::MakeFileArray($filename); $filename должен начинаться с $_SERVER['DOCUMENT_ROOT'] \| Код \| \| --- \| \| ``` $PROP["MORE_PHOTO"] = Array ( "n0" => Array( "VALUE" => CFile::MakeFileArray($filename) ) ); ``` \| | Код | ``` //пример массива для вставки видео $PROP["561"] = Array ( "n0" => Array( "VALUE" => Array ("PATH" => "/upload/single_2.flv", "WIDTH" => 400, "HEIGHT" => 300, "TITLE" => "Заголовок видео", "DURATION" => "00:30", "AUTHOR" => "Автор видео", "DATE" => "01.02.2011") ) ); //При добавлении нового значения/значений множественного свойство типа "Файл" необходимо использовать ключи вида n0,n1,n2 ... nN . ``` | Код | ``` $PROP["MORE_PHOTO"] = Array ( "n0" => Array( "VALUE" => CFile::MakeFileArray($filename) ) ); ``` |
| Код |  |  |  |  |
| ``` //пример массива для вставки видео $PROP["561"] = Array ( "n0" => Array( "VALUE" => Array ("PATH" => "/upload/single_2.flv", "WIDTH" => 400, "HEIGHT" => 300, "TITLE" => "Заголовок видео", "DURATION" => "00:30", "AUTHOR" => "Автор видео", "DATE" => "01.02.2011") ) ); //При добавлении нового значения/значений множественного свойство типа "Файл" необходимо использовать ключи вида n0,n1,n2 ... nN . ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` $PROP["MORE_PHOTO"] = Array ( "n0" => Array( "VALUE" => CFile::MakeFileArray($filename) ) ); ``` |  |  |  |  |
|  |  |  |  |  |


| ![image](../images/7dd82aba60.gif) 24 **Владислав Ухов**07.09.2014 19:18:40 |
| --- |
| Для привязки элемента к нескольким разделам инфоблока используйте ключ IBLOCK_SECTION (массив из ID разделов.) вместо IBLOCK_SECTION_ID |
|  |
