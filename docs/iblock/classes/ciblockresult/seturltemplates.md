# SetUrlTemplates


### Описание и параметры


```
void
CIBlockResult::SetUrlTemplates(
	strDetailUrl = "",
	strSectionUrl = "",
	strListUrl = ""
);
```

Устанавливает шаблоны путей для элементов, разделов и списка элементов вместо тех которые указаны в настройках информационного блока. Шаблоны будут использованы методом [CIBlockResult::GetNext](getnext.md). Нестатический метод.

**Примечание**: используется в компонентах для корректного формирования путей, если соответствующие параметры указаны.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| *DetailUrl* | Шаблон для пути к элементу. Если не задан, то путь будет взят из настроек инфоблока. |
| *SectionUrl* | Шаблон для пути к разделу. Если не задан, то путь будет взят из настроек инфоблока. |
| *ListUrl* | Шаблон для пути к списку элементов. Если не задан, то путь будет взят из настроек инфоблока. |


#### Возвращаемое значение

Ничего.

---
### Смотрите также


- [CIBlockResult::GetNext](getnext.md)
- [CIBlockResult::SetSectionContext](setsectioncontext.md)

---
### Примеры использования


```
<?
$rsElements = CIBlockElement::GetList(array(), array("ID" => $ID), false, false, array("ID", "NAME", "DETAIL_PAGE_URL"));
$rsElements->SetUrlTemplates("/catalog/#SECTION_CODE#/#ELEMENT_CODE#.php");
$arElement = $rsElements->GetNext();
?>
```

---
