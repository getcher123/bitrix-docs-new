# GetDisplayValue


```
array CIBlockFormatProperties::GetDisplayValue(
	array arItem,
	array arProperty,
)
```

Метод помогает компонентам показать значения свойства элемента. Вынесен в модуль для унификации отображения. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| arItem | Массив полей элемента. |
| arProperty | Массив полей свойства (как его возвращает метод [CIBlockElement::GetProperty](../ciblockelement/getproperty.md)). |


#### Возвращаемое значение

Массив полей элемента.

**Примечание:**метод в поле DISPLAY_VALUE выводит только активные по дате элементы (используется фильтр на уровне ядра, поэтому вывести ссылки на неактивные элементы не получится стандартными средствами).






| ![](../images/a93fe0eb87.jpg) 1 **Сергей Куняев**17.07.2015 17:45:21 |  |  |
| --- | --- | --- |
| Если выводимое свойство содержит 1 значение, например, файл, то метод вернет массив файла, если больше, то ассоциативный массив описаний файлов. При выводе в шаблоне следует проверять, делать foreach или нет, если ожидается несколько значений. ************************ Комментарий разработчика: справедливо ен только для файлов, но вообще для всех типов. ************************ Фрагмент кода метода, отвечающий за неоднозначность: \| Код \| \| --- \| \| ``` if ($arProperty["PROPERTY_TYPE"]=="F") { $fileCount = count($arFiles); if ($fileCount == 1) $arProperty["FILE_VALUE"] = $arFiles[0]; elseif ($fileCount > 1) $arProperty["FILE_VALUE"] = $arFiles; else $arProperty["FILE_VALUE"] = false; } ``` \| | Код | ``` if ($arProperty["PROPERTY_TYPE"]=="F") { $fileCount = count($arFiles); if ($fileCount == 1) $arProperty["FILE_VALUE"] = $arFiles[0]; elseif ($fileCount > 1) $arProperty["FILE_VALUE"] = $arFiles; else $arProperty["FILE_VALUE"] = false; } ``` |
| Код |  |  |
| ``` if ($arProperty["PROPERTY_TYPE"]=="F") { $fileCount = count($arFiles); if ($fileCount == 1) $arProperty["FILE_VALUE"] = $arFiles[0]; elseif ($fileCount > 1) $arProperty["FILE_VALUE"] = $arFiles; else $arProperty["FILE_VALUE"] = false; } ``` |  |  |
|  |  |  |
