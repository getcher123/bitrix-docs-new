# GetTreeList


```
CDBResult
CIBlockSection::GetTreeList(
	array arFilter=Array(),
	array arSelect=Array()
);
```

Метод возвращает список разделов, отсортированный в порядке "полного развернутого дерева". Метод статический. По сути является оберткой метода [CIBlockSection](index.md)::[GetList](getlist.md)() с предустановленным параметром сортировки:


```
CIBlockSection::GetList(Array("left_margin"=>"asc"), $arFilter);
```


#### Смотрите также


- [CIBlockSection](index.md)::[GetList](getlist.md)






| ![image](../images/7dd82aba60.gif) 3 **Андрей Огибин**16.05.2016 10:15:06 |  |  |
| --- | --- | --- |
| При использовании Fetch урлы разделов получаются неправильные. Лучше использовать GetNext \| Код \| \| --- \| \| ``` $tree = CIBlockSection::GetTreeList( $arFilter=Array('IBLOCK_ID' => $iblock['ID']), $arSelect=Array() ); while($section = $tree->GetNext()) { } ``` \| | Код | ``` $tree = CIBlockSection::GetTreeList( $arFilter=Array('IBLOCK_ID' => $iblock['ID']), $arSelect=Array() ); while($section = $tree->GetNext()) { } ``` |
| Код |  |  |
| ``` $tree = CIBlockSection::GetTreeList( $arFilter=Array('IBLOCK_ID' => $iblock['ID']), $arSelect=Array() ); while($section = $tree->GetNext()) { } ``` |  |  |
|  |  |  |


| ![image](../images/7dd82aba60.gif) 1 **Никита Кургалин**10.08.2015 10:44:59 |  |  |
| --- | --- | --- |
| Пример использования: \| Код \| \| --- \| \| ``` $arFilter = array('IBLOCK_ID' => $IBLOCK_ID, 'ACTIVE' => 'Y'); $arSelect = array('ID', 'NAME'); $rsSection = CIBlockSection::GetTreeList($arFilter, $arSelect); while($arSection = $rsSection->Fetch()) { echo ' - '.$arSection['NAME'].'<br>'; } ``` \| | Код | ``` $arFilter = array('IBLOCK_ID' => $IBLOCK_ID, 'ACTIVE' => 'Y'); $arSelect = array('ID', 'NAME'); $rsSection = CIBlockSection::GetTreeList($arFilter, $arSelect); while($arSection = $rsSection->Fetch()) { echo ' - '.$arSection['NAME'].'<br>'; } ``` |
| Код |  |  |
| ``` $arFilter = array('IBLOCK_ID' => $IBLOCK_ID, 'ACTIVE' => 'Y'); $arSelect = array('ID', 'NAME'); $rsSection = CIBlockSection::GetTreeList($arFilter, $arSelect); while($arSection = $rsSection->Fetch()) { echo ' - '.$arSection['NAME'].'<br>'; } ``` |  |  |
|  |  |  |
