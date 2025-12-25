# SetPropertyValuesEx


### Описание и параметры


```
CIBlockElement::SetPropertyValuesEx(
	int ELEMENT_ID,
	int IBLOCK_ID,
	array PROPERTY_VALUES,
	array FLAGS = array()
);
```

Метод сохраняет значения всех свойств элемента информационного блока. В отличие от [SetPropertyValues](setpropertyvalues.md) может не содержать полный набор значений. Значения свойств, неуказанных в массиве PROPERTY_VALUES, будут сохранены. Этот метод более экономен в количестве запросов к БД. Метод статический.

Метод возвращает *Null*.

Если необходимо сохранить пустое значение для множественного свойства, то используйте значение *false*, так как просто пустой массив не сохранится.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ELEMENT_ID | Код элемента, значения свойств которого необходимо установить. |
| IBLOCK_ID | Код информационного блока. Может быть не указан. В этом случае будет прочитан из базы данных по коду элемента. |
| PROPERTY_VALUES | Массив значений свойств, в котором коду свойства ставится в соответствие значение свойства. Должен быть вида Array("код свойства1"=>"значения свойства1", ....), где "код свойства" - числовой или символьный код свойства, "значения свойства" - одно или массив всех значений свойства (множественное). **Примечания**: - При добавлении значений свойств типа "Файл" поле DESCRIPTION обязательно. - Если передаётся массив "свойство"=>"значение", то в качестве значения свойств типа "справочник" нужно указывать внешний код элемента справочника. - Для свойства типа **Список** следует передавать идентификатор значения свойства, а не значение. - для свойства типа **Привязка к файлу на сервере**, нужно передавать путь к файлу от корня сайта. |
| FLAGS | Необязательный параметр предоставляет информацию для оптимизации выполнения. Может содержать следующие ключи: - NewElement - можно указать если заведомо известно, что значений свойств у данного элемента нет. Экономит один запрос к БД. - DoNotValidateLists - для свойств типа "список" отключает проверку наличия значений в метаданных свойства. |

---
### Смотрите также


- [CIBlockElement::SetPropertyValues](setpropertyvalues.md)

---
### Примеры использования

Пример 1:


```
<?
$ELEMENT_ID = 18;  // код элемента
$PROPERTY_CODE = "PROP1";  // код свойства
$PROPERTY_VALUE = "Синий";  // значение свойства
// Установим новое значение для данного свойства данного элемента
CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, false, array($PROPERTY_CODE => $PROPERTY_VALUE));
?>
```

Пример 2 (изменение немножественного свойства типа HTML/Text):


```
$el_id = 125;
$iblock_id = 45;
$prop[$prop_code] = array('VALUE'=>array('TYPE'=>'HTML', 'TEXT'=>$prop_value));
CIBlockElement::SetPropertyValuesEx($el_id, $iblock_id, $prop);
```

Пример 3:


```
<input name="MyFile1" type="file" />
<input name="MyFile2" type="file" />

function makeCurentFilesArray($InputFileCode) {
	unset($arFiles, $TMPFILE);
	$arFiles = array();  // Массив всех файлов в свойстве []
	$TMPFILE = array(); // Временный массив для текщего файла
	if(is_array($_FILES[$InputFileCode])) {
		foreach($_FILES[$InputFileCode]['tmp_name'] as $key => $val) {
			if(file_exists($val)) {
				foreach($_FILES[$InputFileCode] as $namekey => $nameval) {
					$TMPFILE[$namekey] = $nameval[$key];
				}
			$arFiles[] = array('VALUE' => $TMPFILE, 'DESCRIPTION' => $TMPFILE['name']);
			}
		}
	}
	return $arFiles;
}

if (!empty($_FILES['MyFile1'])) $PropFileArr['MyFile1'] = makeCurentFilesArray('MyFile1');
if (!empty($_FILES['MyFile2'])) $PropFileArr['MyFile2'] = makeCurentFilesArray('MyFile2');

CIBlockElement::SetPropertyValuesEx($Element_ID, $IBlock_ID, $PropFileArr); // Обновляем массив свойств типа файл
```

---



Страницы: 1 2След.
| ![image](../images/7dd82aba60.gif) 1 **Андрей Сенин**14.07.2021 09:43:15 |  |  |
| --- | --- | --- |
| \| Цитата \| \| --- \| \| [Ивайло Тихолов](https://dev.1c-bitrix.ru/community/webdev/user/281446/) пишет: [CODE] *Wrong* $PROPERTY_VALUE = array (); CIBlockElement::SetPropertyValuesEx( $ELEMENT_ID , $IBLOCK_ID , array ( $PROPERTY_CODE => $PROPERTY_VALUE )); [/CODE] Для удаления всех значений множественного свойства, пустой массив не поможет. [CODE] *Correct* $PROPERTY_VALUE = array ( 0 => array ( "VALUE" => "" , "DESCRIPTION" => "" ) ); CIBlockElement::SetPropertyValuesEx( $ELEMENT_ID , $IBLOCK_ID , array ( $PROPERTY_CODE => $PROPERTY_VALUE )); [/CODE] Ключи VALUE и DESCRIPTION должны присутствовать. \| Можно указать вместо $PROPERTY_VALUE = array (0 => array ( "VALUE" => "" , "DESCRIPTION" => "" )); $PROPERTY_VALUE = false; | Цитата | [Ивайло Тихолов](https://dev.1c-bitrix.ru/community/webdev/user/281446/) пишет: [CODE] *Wrong* $PROPERTY_VALUE = array (); CIBlockElement::SetPropertyValuesEx( $ELEMENT_ID , $IBLOCK_ID , array ( $PROPERTY_CODE => $PROPERTY_VALUE )); [/CODE] Для удаления всех значений множественного свойства, пустой массив не поможет. [CODE] *Correct* $PROPERTY_VALUE = array ( 0 => array ( "VALUE" => "" , "DESCRIPTION" => "" ) ); CIBlockElement::SetPropertyValuesEx( $ELEMENT_ID , $IBLOCK_ID , array ( $PROPERTY_CODE => $PROPERTY_VALUE )); [/CODE] Ключи VALUE и DESCRIPTION должны присутствовать. |
| Цитата |  |  |
| [Ивайло Тихолов](https://dev.1c-bitrix.ru/community/webdev/user/281446/) пишет: [CODE] *Wrong* $PROPERTY_VALUE = array (); CIBlockElement::SetPropertyValuesEx( $ELEMENT_ID , $IBLOCK_ID , array ( $PROPERTY_CODE => $PROPERTY_VALUE )); [/CODE] Для удаления всех значений множественного свойства, пустой массив не поможет. [CODE] *Correct* $PROPERTY_VALUE = array ( 0 => array ( "VALUE" => "" , "DESCRIPTION" => "" ) ); CIBlockElement::SetPropertyValuesEx( $ELEMENT_ID , $IBLOCK_ID , array ( $PROPERTY_CODE => $PROPERTY_VALUE )); [/CODE] Ключи VALUE и DESCRIPTION должны присутствовать. |  |  |
|  |  |  |


| ![](../images/250dd951eb.jpg) 2 **Ивайло Тихолов**08.04.2021 14:29:40 |  |  |  |  |
| --- | --- | --- | --- | --- |
| \| Код \| \| --- \| \| ``` *Wrong* $PROPERTY_VALUE = array(); CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE)); ``` \| Для удаления всех значений множественного свойства, пустой массив не поможет. \| Код \| \| --- \| \| ``` *Correct* $PROPERTY_VALUE = array( 0 => array("VALUE"=>"","DESCRIPTION"=>"") ); CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE)); ``` \| Ключи VALUE и DESCRIPTION должны присутствовать. | Код | ``` *Wrong* $PROPERTY_VALUE = array(); CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE)); ``` | Код | ``` *Correct* $PROPERTY_VALUE = array( 0 => array("VALUE"=>"","DESCRIPTION"=>"") ); CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE)); ``` |
| Код |  |  |  |  |
| ``` *Wrong* $PROPERTY_VALUE = array(); CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE)); ``` |  |  |  |  |
| Код |  |  |  |  |
| ``` *Correct* $PROPERTY_VALUE = array( 0 => array("VALUE"=>"","DESCRIPTION"=>"") ); CIBlockElement::SetPropertyValuesEx($ELEMENT_ID, $IBLOCK_ID, array($PROPERTY_CODE => $PROPERTY_VALUE)); ``` |  |  |  |  |
|  |  |  |  |  |


| ![](../images/6c4da9849f.jpg) 2 **Анастасия Слимак**28.07.2020 16:49:47 |  |  |
| --- | --- | --- |
| Пример добавления свойства типа **Список.** \| Код \| \| --- \| \| ``` $IBLOCK_ID = 26; $res = CIblockElement::GetList([], ["IBLOCK_ID" => $IBLOCK_ID, "NAME" => "%Huawei%"], false, false, ["ID"]); while ($ob = $res->GetNext()) { CIblockElement::SetPropertyValuesEx($ob["ID"], $IBLOCK_ID, ["MANUFACTURER" => 113]); } ``` \| В примере для всех товаров, которые содержат слово "Huawei" проставляем значение свойства "Производитель" | Код | ``` $IBLOCK_ID = 26; $res = CIblockElement::GetList([], ["IBLOCK_ID" => $IBLOCK_ID, "NAME" => "%Huawei%"], false, false, ["ID"]); while ($ob = $res->GetNext()) { CIblockElement::SetPropertyValuesEx($ob["ID"], $IBLOCK_ID, ["MANUFACTURER" => 113]); } ``` |
| Код |  |  |
| ``` $IBLOCK_ID = 26; $res = CIblockElement::GetList([], ["IBLOCK_ID" => $IBLOCK_ID, "NAME" => "%Huawei%"], false, false, ["ID"]); while ($ob = $res->GetNext()) { CIblockElement::SetPropertyValuesEx($ob["ID"], $IBLOCK_ID, ["MANUFACTURER" => 113]); } ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 13 **Иван Новиков**14.11.2019 14:21:56 |  |  |
| --- | --- | --- |
| Метод не очищает кеш. Для очистки кеша следует вызвать: \| Код \| \| --- \| \| ``` CIBlock::clearIblockTagCache(IBLOCK_ID); ``` \| | Код | ``` CIBlock::clearIblockTagCache(IBLOCK_ID); ``` |
| Код |  |  |
| ``` CIBlock::clearIblockTagCache(IBLOCK_ID); ``` |  |  |
|  |  |  |


| ![](../images/eeabf0f50b.jpg) 1 **Евгений Черешнев**01.11.2019 20:20:00 |  |  |
| --- | --- | --- |
| Пример загрузки input[type="file"] multiple \| Код \| \| --- \| \| ``` /** @var $obRequest \Bitrix\Main\HttpRequest */if (!empty($obRequest->getFile('ATTACHMENT'))) { $arFiles = $obRequest->getFile('ATTACHMENT'); ksort($arFiles); foreach ($arFiles['error'] as $k => $v) { if( $v < 1 ) { $arPhopFiles[] = ['VALUE' => array_combine(array_keys($arFiles), array_column($arFiles, $k)), 'DESCRIPTION' => '']; } } \CIBlockElement::SetPropertyValuesEx(ELEM_ID, IBLOCK_ID, ['ATTACHMENT' => $arPhopFiles]); } ``` \| | Код | ``` /** @var $obRequest \Bitrix\Main\HttpRequest */if (!empty($obRequest->getFile('ATTACHMENT'))) { $arFiles = $obRequest->getFile('ATTACHMENT'); ksort($arFiles); foreach ($arFiles['error'] as $k => $v) { if( $v < 1 ) { $arPhopFiles[] = ['VALUE' => array_combine(array_keys($arFiles), array_column($arFiles, $k)), 'DESCRIPTION' => '']; } } \CIBlockElement::SetPropertyValuesEx(ELEM_ID, IBLOCK_ID, ['ATTACHMENT' => $arPhopFiles]); } ``` |
| Код |  |  |
| ``` /** @var $obRequest \Bitrix\Main\HttpRequest */if (!empty($obRequest->getFile('ATTACHMENT'))) { $arFiles = $obRequest->getFile('ATTACHMENT'); ksort($arFiles); foreach ($arFiles['error'] as $k => $v) { if( $v < 1 ) { $arPhopFiles[] = ['VALUE' => array_combine(array_keys($arFiles), array_column($arFiles, $k)), 'DESCRIPTION' => '']; } } \CIBlockElement::SetPropertyValuesEx(ELEM_ID, IBLOCK_ID, ['ATTACHMENT' => $arPhopFiles]); } ``` |  |  |
|  |  |  |


| ![](../images/3ade78de6e.jpg) 3 **Олег Постоев**25.10.2019 17:08:52 |
| --- |
| При попытке обновить множественное свойство запрос будет проигнорирован, если в массиве те же элементы что и были. Даже, если они в другом порядке. То есть сортировку/порядок значений в свойстве этим методом не изменить. Есть варианта решения разной степени кошмарности: 1. Добавить в массив значений пустышку, а вторым запросом без неё. 2. Добавить рандомный description. Вариант подойдет, если это поле не используется |
|  |


| ![image](../images/7dd82aba60.gif) 11 **Адель Юсупов**03.04.2017 11:17:12 |  |  |
| --- | --- | --- |
| При файсетном индексе необходимо вызвать после вызова CIBlockElement::SetPropertyValuesEx \| Код \| \| --- \| \| ``` \Bitrix\Iblock\PropertyIndex\Manager::updateElementIndex(инфоблок, элемент); ``` \| | Код | ``` \Bitrix\Iblock\PropertyIndex\Manager::updateElementIndex(инфоблок, элемент); ``` |
| Код |  |  |
| ``` \Bitrix\Iblock\PropertyIndex\Manager::updateElementIndex(инфоблок, элемент); ``` |  |  |
|  |  |  |


| ![](../images/73c7a923c3.jpg) 14 **karpulix**28.04.2016 10:42:58 |
| --- |
| Свойство должно быть активным, иначе изменить его не получится. Это конечно может кому-то показаться логичным, но не всегда явным. |
|  |


| ![image](../images/7dd82aba60.gif) 1 **Александр Аваков**27.04.2016 18:04:40 |  |  |
| --- | --- | --- |
| Стоит быть внимательным с регистром кодов свойств! Хоть в битриксе и принято заводить свойства только в UPPERCASE, возможность создать свойство в camelCase тоже присутствует. Если мы используем метод GetList, то регистр будет игнорироваться. При работе с этим методом, регистр не игнорируется. \| Код \| \| --- \| \| ``` // Здесь регистр игнорируется CIBlockElement::GetList([], ['PROPERTY_ORDERID' => 10], false, false, ['ID']); // А здесь нет CIBlockElement::SetPropertyValuesEx(5996, 9, [ 'orderID' => 123 ]); ``` \| | Код | ``` // Здесь регистр игнорируется CIBlockElement::GetList([], ['PROPERTY_ORDERID' => 10], false, false, ['ID']); // А здесь нет CIBlockElement::SetPropertyValuesEx(5996, 9, [ 'orderID' => 123 ]); ``` |
| Код |  |  |
| ``` // Здесь регистр игнорируется CIBlockElement::GetList([], ['PROPERTY_ORDERID' => 10], false, false, ['ID']); // А здесь нет CIBlockElement::SetPropertyValuesEx(5996, 9, [ 'orderID' => 123 ]); ``` |  |  |
|  |  |  |


| ![](../images/599e64eab3.JPG) 11 **xolegator**10.11.2015 16:35:22 |  |  |
| --- | --- | --- |
| **Установить значение свойства типа Справочник (highload блок)** \| Код \| \| --- \| \| ``` CIBlockElement::SetPropertyValuesEx( $elementId, $blockId, array('LINK_TO_MY_HIGHLOAD_BLOCK' => $newValue['UF_XML_ID']) ); ``` \| LINK_TO_MY_HIGHLOAD_BLOCK - код свойства элемента инфоблока типа Справочник. Значение $newValue['UF_XML_ID'] должно возвращать значение 'UF_XML_ID' одного из элементов highload блока, которое требуется установить свойству элемента инфоблока. | Код | ``` CIBlockElement::SetPropertyValuesEx( $elementId, $blockId, array('LINK_TO_MY_HIGHLOAD_BLOCK' => $newValue['UF_XML_ID']) ); ``` |
| Код |  |  |
| ``` CIBlockElement::SetPropertyValuesEx( $elementId, $blockId, array('LINK_TO_MY_HIGHLOAD_BLOCK' => $newValue['UF_XML_ID']) ); ``` |  |  |
|  |  |  |

Страницы: 1 2След.
