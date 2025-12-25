# SetPropertyValueCode


### Описание и параметры


```
bool
CIBlockElement::SetPropertyValueCode(
	int ELEMENT_ID,
	string PROPERTY_CODE,
	string PROPERTY_VALUE
);
```

Метод изменяет значение свойства элемента информационного блока. Выполняет один дополнительный запрос к БД для определения кода информационного блока элемента. Если код инфоблока известен, то лучше воспользоваться функцией [SetPropertyValues](setpropertyvalues.md), задав ей 4-й параметр. Статический метод. **Внимание!** Удалять и обновлять несколько значений файлового свойства можно только ОДНИМ вызовом, а не несколькими, так как меняются ID значений свойств.

Отличие метода от SetPropertyValuesEx в том, что он не перезаписывает множественное свойства типа Файл, а дополняет.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ELEMENT_ID | Код элемента, значение свойства которого изменяется. |
| PROPERTY_CODE | Символьный или числовой код свойства, которое изменяется. Если передан неверный PROPERTY_CODE метод все равно вернет *true*. |
| PROPERTY_VALUE | Значение свойства (одиночное или множественное в виде массива значений). Если для свойства типа **список**, **привязка к элементам или разделам** (и их клонам) будет установлено равным переданному значению PROPERTY_VALUE, без проверки, метод вернет *true*. (Если передавать значение, а не его ENUM_ID, то в БД будет записано само значение, привязки к значению не будет.) |


#### Возвращаемое значение

При успешном изменении вернет *true*, иначе - *false*.

---
### Смотрите также


- [CIBlockElement::Update](update.md)
- [CIBlockElement::SetPropertyValues](setpropertyvalues.md)

---
### Примеры использования

**Пример 1:**


```
<?$arFile = CFile::MakeFileArray($_SERVER["DOCUMENT_ROOT"]."/images/add_basket.gif");CIBlockElement::SetPropertyValueCode($ELEMENT_ID, "picture", $arFile);?>
```

При добавлении/изменении значений свойства можно одновременно установить и описание, если после вызова *MakeFileArray* добавить "description".

**Пример 2:**

Для обновления значения поля типа html/текст значение TYPE должно быть либо HTML, либо TEXT:


```
CIBlockElement::SetPropertyValueCode(ELEMENT_ID, NAME_PROPERTY, array(array("TYPE"=>"TEXT", "TEXT"=>"мой текст")));
```

---




| ![image](../images/7dd82aba60.gif) 1 **Владимир Шершнев**16.04.2021 11:30:04 |  |  |
| --- | --- | --- |
| **Внимание! Удалять и обновлять несколько значений файлового свойства можно только ОДНИМ вызовом, а не несколькими, так как меняются ID значений свойств.** Подразумевается, что необходимо собрать для 1 свойства типа файл все удаляемые значения (PROPERTY_VALUE_ID каждого файла) в массив. Затем производить удаление. Например: \| Код \| \| --- \| \| ``` <?php $obElement = \CIBlockElement::GetList( [], [ 'ID' => (int)$aElementID, 'IBLOCK_ID' => (int)$iMainIblockId ], false, false, [ 'ID', 'IBLOCK_ID', ]); if ($obFields = $obElement->GetNextElement()) { $arProperties = $obFields->GetProperties(); if (!empty($arProperties)) { /** * Собираем файлы для удаления в массив, * группируя по свойствам */ foreach ($arProperties as $sPropCode => $arPropValues) { /** * $sPropCode - ключ код свойства, в котором мы ищем удаляемый файл без PROPERTY_ и _VALUE, например PHOTO * $arPropValues - PROPERTY_VALUE_ID удаляемого файла * $arFiles["FILE_DELETE"] - массив, содержащий ID удаляемых файлов всех свойств * $sValue - искомое значение ID */ foreach ($arPropValues['VALUE'] as $iKeyValue => $sValue) { if (in_array($sValue, $arFiles["FILE_DELETE"]) && $arPropValues['PROPERTY_VALUE_ID'][$iKeyValue] > 0) { $arDeleteList[$sPropCode][$arPropValues['PROPERTY_VALUE_ID'][$iKeyValue]] = [ 'VALUE' => [ 'del' => 'Y', ] ]; } } } /** * Если массив для удаления файлов не пустой * производим удаление * */ if (!empty($arDeleteList)) { foreach ($arDeleteList as $sPropForDelete => $arDeleteFiles) { CIBlockElement::SetPropertyValueCode( $aElementID, $sPropForDelete, $arDeleteFiles ); } } } } ``` \| | Код | ``` <?php $obElement = \CIBlockElement::GetList( [], [ 'ID' => (int)$aElementID, 'IBLOCK_ID' => (int)$iMainIblockId ], false, false, [ 'ID', 'IBLOCK_ID', ]); if ($obFields = $obElement->GetNextElement()) { $arProperties = $obFields->GetProperties(); if (!empty($arProperties)) { /** * Собираем файлы для удаления в массив, * группируя по свойствам */ foreach ($arProperties as $sPropCode => $arPropValues) { /** * $sPropCode - ключ код свойства, в котором мы ищем удаляемый файл без PROPERTY_ и _VALUE, например PHOTO * $arPropValues - PROPERTY_VALUE_ID удаляемого файла * $arFiles["FILE_DELETE"] - массив, содержащий ID удаляемых файлов всех свойств * $sValue - искомое значение ID */ foreach ($arPropValues['VALUE'] as $iKeyValue => $sValue) { if (in_array($sValue, $arFiles["FILE_DELETE"]) && $arPropValues['PROPERTY_VALUE_ID'][$iKeyValue] > 0) { $arDeleteList[$sPropCode][$arPropValues['PROPERTY_VALUE_ID'][$iKeyValue]] = [ 'VALUE' => [ 'del' => 'Y', ] ]; } } } /** * Если массив для удаления файлов не пустой * производим удаление * */ if (!empty($arDeleteList)) { foreach ($arDeleteList as $sPropForDelete => $arDeleteFiles) { CIBlockElement::SetPropertyValueCode( $aElementID, $sPropForDelete, $arDeleteFiles ); } } } } ``` |
| Код |  |  |
| ``` <?php $obElement = \CIBlockElement::GetList( [], [ 'ID' => (int)$aElementID, 'IBLOCK_ID' => (int)$iMainIblockId ], false, false, [ 'ID', 'IBLOCK_ID', ]); if ($obFields = $obElement->GetNextElement()) { $arProperties = $obFields->GetProperties(); if (!empty($arProperties)) { /** * Собираем файлы для удаления в массив, * группируя по свойствам */ foreach ($arProperties as $sPropCode => $arPropValues) { /** * $sPropCode - ключ код свойства, в котором мы ищем удаляемый файл без PROPERTY_ и _VALUE, например PHOTO * $arPropValues - PROPERTY_VALUE_ID удаляемого файла * $arFiles["FILE_DELETE"] - массив, содержащий ID удаляемых файлов всех свойств * $sValue - искомое значение ID */ foreach ($arPropValues['VALUE'] as $iKeyValue => $sValue) { if (in_array($sValue, $arFiles["FILE_DELETE"]) && $arPropValues['PROPERTY_VALUE_ID'][$iKeyValue] > 0) { $arDeleteList[$sPropCode][$arPropValues['PROPERTY_VALUE_ID'][$iKeyValue]] = [ 'VALUE' => [ 'del' => 'Y', ] ]; } } } /** * Если массив для удаления файлов не пустой * производим удаление * */ if (!empty($arDeleteList)) { foreach ($arDeleteList as $sPropForDelete => $arDeleteFiles) { CIBlockElement::SetPropertyValueCode( $aElementID, $sPropForDelete, $arDeleteFiles ); } } } } ``` |  |  |
|  |  |  |


| ![](../images/505bdd5535.png) 4 **Антон Царук**13.02.2015 23:08:32 |  |  |
| --- | --- | --- |
| Поле типа "Дата-время" заносится в формате сайта (а не в формате БД, как большинство могло подумать!): например, \| Код \| \| --- \| \| ``` date("d.m.Y H:i:s") ``` \| | Код | ``` date("d.m.Y H:i:s") ``` |
| Код |  |  |
| ``` date("d.m.Y H:i:s") ``` |  |  |
|  |  |  |
