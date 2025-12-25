# SubQuery


### Описание и параметры


```
object
CIBlockElement::SubQuery(
	string strField,
	array arFilter
);
```

Позволяет использовать подзапросы. Метод статический.

**Примечание**: применимо только к полю **ID**элемента основного запроса.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| strField | Название поля, по которому будет осуществляться фильтрация. Возможные значения: - **ID** - по идентификатору элемента - **PROPERTY_<PROPERTY_CODE>** - по значению свойства, где **PROPERTY_CODE** - это ID или символьный код свойства привязки. Свойство должно быть типа "привязка к элементам". |
| arFilter | Фильтр элементов тот же, что и в методе [CIBlockElement::GetList](getlist.md) за исключением того, что с версии 23.0.0 принимается ключ `IBLOCK_ID` либо `=IBLOCK_ID`. Значение - одиночное (ID одного инфоблока) |


#### Возвращаемое значение

Объект подзапроса.

---
### Примеры использования


```
<?
//Выбрать авторов написавших книги в 21-ом веке.
if(CModule::IncludeModule('iblock'))
{
	$rsBooks = CIBlockElement::GetList(
		array("NAME" => "ASC"), //Сортируем по имени
		array(
			"IBLOCK_ID" => $AUTHOR_IBLOCK,
			"ACTIVE" => "Y",
			"ID" => CIBlockElement::SubQuery("PROPERTY_AUTHOR", array(
				"IBLOCK_ID" => $BOOK_IBLOCK,
				">=PROPERTY_PRINT_DATE" => "2000-01-01 00:00:00",
			)),
		),
		false, // Без группировки
		false,  //Без постранички
		array("ID", "IBLOCK_ID", "NAME") // Выбираем только поля необходимые для показа
	);
	while($arBook = $rsBooks->GetNext())
		echo "<li>", $arBook["NAME"],"\n";
}
?>
```

---

#### Смотрите также


- [CIBlockElement::GetList](getlist.md)





| ![image](../images/7dd82aba60.gif) 8 **Дмитрий Чернояров**18.03.2015 11:04:18 |  |  |
| --- | --- | --- |
| Такая схема хорошо работает как исключающий фильтр по множественному свойству, т.к. поддерживается тип проверки фильтра "отрицание" ("!"). \| Код \| \| --- \| \| ``` <? ... $arFilter = array( 'IBLOCK_ID' => $IBLOCK_ID, 'SECTION_ID' => 3, 'PROPERTY_'.PROP_PRODUCT_TYPE_ID => array('542'), '!ID' => CIBlockElement::SubQuery("ID", array( "IBLOCK_ID" => $IBLOCK_ID, 'SECTION_ID' => 3, "PROPERTY_".PROP_PRODUCT_TYPE_ID => array('532'), ) ); ... ?> ``` \| | Код | ``` <? ... $arFilter = array( 'IBLOCK_ID' => $IBLOCK_ID, 'SECTION_ID' => 3, 'PROPERTY_'.PROP_PRODUCT_TYPE_ID => array('542'), '!ID' => CIBlockElement::SubQuery("ID", array( "IBLOCK_ID" => $IBLOCK_ID, 'SECTION_ID' => 3, "PROPERTY_".PROP_PRODUCT_TYPE_ID => array('532'), ) ); ... ?> ``` |
| Код |  |  |
| ``` <? ... $arFilter = array( 'IBLOCK_ID' => $IBLOCK_ID, 'SECTION_ID' => 3, 'PROPERTY_'.PROP_PRODUCT_TYPE_ID => array('542'), '!ID' => CIBlockElement::SubQuery("ID", array( "IBLOCK_ID" => $IBLOCK_ID, 'SECTION_ID' => 3, "PROPERTY_".PROP_PRODUCT_TYPE_ID => array('532'), ) ); ... ?> ``` |  |  |
|  |  |  |
