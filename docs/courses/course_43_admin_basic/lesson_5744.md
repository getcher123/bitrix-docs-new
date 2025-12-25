# Копирование значений полей элементов в свойства

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5534 — Примеры работы с множественными свойствами](lesson_5534.md)
- [Следующий: 5761 — Получение суммы значений полей связанных инфоблоков →](lesson_5761.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5744

Рассмотрим пример функции, которая копирует значения полей элементов инфоблока (`$_FROM_FIELD_NAMES`) в свойства элементов инфоблока (`$TO_PROPERTY_NAMES`).



Копироваться будут поля **Начало активности (DATE_ACTIVE_FROM)** и **Окончание активности (DATE_ACTIVE_TO)** в свойства **DATE_BEGIN** и **DATE_END** элементов инфоблока с ID = 22:



```
function copy_from_fields_to_propertys_values( $IBLOCK_ID, $_FROM_FIELD_NAMES, $TO_PROPERTY_NAMES ){
/* *
* $_FROM_FIELD_NAMES = array(DATE_ACTIVE_FROM, DATE_ACTIVE_TO);
* $TO_PROPERTY_NAMES = array(DATE_BEGIN, DATE_END);
* copy_from_fields_to_propertys_values(22, array("DATE_ACTIVE_FROM","DATE_ACTIVE_TO"), array("DATE_BEGIN","DATE_END"));
* */
	if ( CModule::IncludeModule ( "iblock" ) ){
		$arOrder = array(
			"sort" => "ASC",
		);

		$arFilter = array(
			"IBLOCK_ID" => $IBLOCK_ID,
		);

		foreach ( $TO_PROPERTY_NAMES as $property_name ) {
			$TO_PROPERTY_NAMES_with_prop[] = 'PROPERTY_' . $property_name;
		}

		$arSelect = array(
			"NAME",
			"ID"
		);

		$arSelect = array_merge ( $arSelect, $_FROM_FIELD_NAMES, $TO_PROPERTY_NAMES_with_prop );

		$db_elemens = CIBlockElement::GetList ( $arOrder, $arFilter, false, false, $arSelect );

		while ( $arElement = $db_elemens->Fetch () ) {
			$PRODUCT_ID = $arElement["ID"];

		foreach ( $TO_PROPERTY_NAMES as $key => $property_name ) {
			CIBlockElement::SetPropertyValues ( $PRODUCT_ID, $IBLOCK_ID, $arElement[$_FROM_FIELD_NAMES[$key]], $property_name );
 			}
		}

		}
		else
		{
			die( "Модуль iblock не установлен" );
		}
	}
```

#### Дополнительная информация

- Документация по методу [CIBlockElement::SetPropertyValues](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/setpropertyvalues.php)
