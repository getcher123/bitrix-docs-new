# GetSectionElementsCount


```
int CIBlockSection::GetSectionElementsCount(
	int ID,
	array arFilter = Array()
);
```

Метод считает количество элементов внутри раздела *ID*, учитывая фильтр *arFilter*. Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код раздела. |
| arFilter | Массив вида Array("фильтруемое поле"=>"значение", ...), где фильтруемое поле может принимать значения: *CNT_ACTIVE* - активные элементы (Y\|N),*CNT_ALL* - учитывать ещё не опубликованные элементы (если установлен модуль документооборота), *PROPERTY* - массив для фильтрации элементов по значениям свойств, вида Array("код свойства"=>"значение", ...), |

**Примечание:**метод устарел, для получения количества рекомендуется использовать метод [CIBlockElement::GetList](../ciblockelement/getlist.md)с установленным параметром для группировки. #### Смотрите также - [CIBlockElement::GetList](../ciblockelement/getlist.md)




| ![](../images/8e80c8aebb.jpg) 6 **Егор Солуянов**17.02.2016 21:26:18 |  |  |
| --- | --- | --- |
| Вывести количество активных элементов данного раздела и его подразделов: \| Код \| \| --- \| \| ``` $activeElements = CIBlockSection::GetSectionElementsCount($SECTION_ID, Array("CNT_ACTIVE"=>"Y")); echo $activeElements; ``` \| | Код | ``` $activeElements = CIBlockSection::GetSectionElementsCount($SECTION_ID, Array("CNT_ACTIVE"=>"Y")); echo $activeElements; ``` |
| Код |  |  |
| ``` $activeElements = CIBlockSection::GetSectionElementsCount($SECTION_ID, Array("CNT_ACTIVE"=>"Y")); echo $activeElements; ``` |  |  |
|  |  |  |
