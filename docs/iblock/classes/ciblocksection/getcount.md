# GetCount


### Описание и параметры


```
int
CIBlockSection::GetCount(
	array arFilter = Array()
);
```

Возвращает количество разделов, удовлетворяющих фильтру *arFilter*. Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arFilter | Массив вида array("фильтруемое поле"=>"значение" [, ...]) "фильтруемое поле" может принимать значения: *ACTIVE* - фильтр по активности (Y\|N); *GLOBAL_ACTIVE* - фильтр по активности, учитывая активность вышележащих разделов (Y\|N); *NAME* - по названию (можно искать по шаблону [%_]); *CODE* - по символьному коду (по шаблону [%_]); *EXTERNAL_ID* - по внешнему коду (по шаблону [%_]); *SECTION_ID* - по коду раздела-родителя; *DEPTH_LEVEL* - по уровню вложенности; *LEFT_BORDER, RIGHT_BORDER* - по левой и правой границе (поля *LEFT_MARGIN* и *RIGHT_MARGIN*, см. примечание); *ID* - по коду раздела; *IBLOCK_ID* - по коду родительского информационного блока; *IBLOCK_ACTIVE* - по активности родительского информационного блока; *IBLOCK_NAME* - по названию информационного блока (по шаблону [%_]); *IBLOCK_TYPE* - по типу информационного блока; *IBLOCK_CODE -*по символьному коду информационного блока (по шаблону [%_]); *IBLOCK_EXTERNAL_ID* - по внешнему коду информационного блока (по шаблону [%_]); Перед названием фильтруемого поля можно указать тип фильтрации: "!" - не равно "<" - меньше "<=" - меньше либо равно ">" - больше ">=" - больше либо равно "значения фильтра" одиночное значение или массив. Необязательное. По умолчанию записи не фильтруются. |


#### Возвращаемое значение

Число - количество разделов. ---
### Смотрите также


- [CIBlockSection](index.md)::[GetList()](getlist.md)

---
### Примеры использования


```
<?
$arFilter = Array(
	"IBLOCK_ID"=>$IBLOCK_ID,
	"SECTION_ID"=>$f_ID
);

echo CIBlockSection::GetCount($arFilter);
?>
```

---



| ![](../images/629082c923.jpg) 2 **Роман Клёпов**27.05.2014 11:18:54 |  |  |
| --- | --- | --- |
| Для рекурсивного подсчета подразделов (любого уровня вложенности) можно воспользоваться следующим кодом: | Код | ``` <?php $arFilSecCount = Array( "ACTIVE" => "Y", "IBLOCK_ID"=>$iBlockId, ">LEFT_BORDER" => $arSecLeftMargin, "<RIGHT_BORDER" => $arSecRightMargin, ); $subSecCount = CIBlockSection::GetCount($arFilSecCount); echo $subSecCount; ?> ``` |
| Код |  |  |
| ``` <?php $arFilSecCount = Array( "ACTIVE" => "Y", "IBLOCK_ID"=>$iBlockId, ">LEFT_BORDER" => $arSecLeftMargin, "<RIGHT_BORDER" => $arSecRightMargin, ); $subSecCount = CIBlockSection::GetCount($arFilSecCount); echo $subSecCount; ?> ``` |  |  |
|  |  |  |
