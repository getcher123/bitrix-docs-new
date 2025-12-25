# BeforeIndex


### Описание и параметры


```
функция-обработчик(
	array arFields
);
```

Событие "BeforeIndex" вызывается перед индексацией элемента методом CSearch::Index.


Важно! Функция-обработчик не принимает параметр arFields по ссылке. Не верно: `function BeforeIndexHandler(&$arFields)`. Верно: `function BeforeIndexHandler($arFields)`.


#### Параметры


| Параметр | Описание |
| --- | --- |
| arFields | Массив следующего содержания: - **MODULE_ID** - идентификатор модуля (не изменится); - **ITEM_ID** - идентификатор элемента (не изменится); - **PARAM1** - первый параметр элемента; - **PARAM2** - второй параметр элемента; - **DATE_FROM** - дата начала активности элемента; - **DATE_TO** - дата окончания активности элемента; - **TITLE** - заголовок; - **BODY** - содержание; - **TAGS** - теги элемента; - **SITE_ID** - массив сайтов; - **PERMISSIONS** - массив идентификаторов групп пользователей которым разрешено чтение; - **URL** - адрес относительно корня сайта, по которому доступен данный элемент; |

Данный обработчик может модифицировать поля параметра arFields и должен вернуть его как результат своей работы.

**Важные моменты**


- Если в обработчике проводятся модификации поля *SITE_ID*, то надо помнить,что индексы в массиве должны быть с нуля и по порядку. Иначе массив будет воспринят как ассоциативный и элементы привяжутся к сайтам неверно (вместо *SITE_ID* окажутся числа и элементы пропадут из поиска).
- Чтобы не добавлять запись в индекс (например, если надо какой-то подраздел инфоблока не индексировать), необходимо в функции-обработчике выполнить: ``` unset($arFields["BODY"]); unset($arFields["TITLE"]); ```
- Если выполняются проверки типа: ``` $bTitle = array_key_exists("TITLE", $arFields); $bBody = array_key_exists("BODY", $arFields); if($bTitle && $bBody && strlen($arFields["BODY"])<=0 && strlen($arFields["TITLE"])<=0) ``` то для исключения элемента из индекса как записи следует выполнять: ``` $arFields["BODY"]=''; $arFields["TITLE"]=''; ```

---
### Смотрите также


- CSearch::Index

---
### Примеры


#### Пример функции-обработчика:


```
<?// файл /bitrix/php_interface/init.php// регистрируем обработчикAddEventHandler("search", "BeforeIndex", Array("MyClass", "BeforeIndexHandler"));
class MyClass
{
	// создаем обработчик события "BeforeIndex"
	public static function BeforeIndexHandler($arFields)
	{
		if($arFields["MODULE_ID"] == "iblock" && $arFields["PARAM2"] == 33)
		{
			if(array_key_exists("BODY", $arFields))
			{
				$arFields["BODY"] .= " самые свежие новости";
			}
		}
		return $arFields;
	}
}
?>
```


#### Пример использования функции-обработчика:

Пример использования функции-обработчика, чтобы компонент **search.title** проводил поиск не только по заголовкам, но и некоторому свойству:


```
// регистрируем обработчик
AddEventHandler("search", "BeforeIndex", "BeforeIndexHandler");
 // создаем обработчик события "BeforeIndex"
function BeforeIndexHandler($arFields)
{
	if(!CModule::IncludeModule("iblock")) // подключаем модуль
		return $arFields;
	if($arFields["MODULE_ID"] == "iblock")
	{
		$db_props = CIBlockElement::GetProperty(                        // Запросим свойства индексируемого элемента
			$arFields["PARAM2"],         // BLOCK_ID индексируемого свойства
			$arFields["ITEM_ID"],          // ID индексируемого свойства
			array("sort" => "asc"),       // Сортировка (можно упустить)
			Array("CODE"=>"CML2_ARTICLE")); // CODE свойства (в данном случае артикул)
		if($ar_props = $db_props->Fetch())
			$arFields["TITLE"] .= " ".$ar_props["VALUE"];   // Добавим свойство в конец заголовка индексируемого элемента
	}
	return $arFields; // вернём изменения
}
```

---



| ![](../images/fc43a3698a.jpeg) 5 **Андрей Чурсин**26.05.2021 14:08:58 |
| --- |
| $fields["PARAM1"] - тип ИБ $fields["PARAM2"] - ID ИБ |
|  |


| ![](../images/2068d63a6f.jpg) 2 **Алексей Попович**17.05.2017 06:40:26 |  |  |
| --- | --- | --- |
| Пример обработчика, исключающего элемент инфоблока из поискового индекса по свойству для случая, когда инфоблок привязан к нескольким сайтам: \| Код \| \| --- \| \| ``` AddEventHandler("search", "BeforeIndex", Array("SearchExclude", "BeforeIndexHandler")); class SearchExclude { function BeforeIndexHandler($arFields) { if ($arFields["MODULE_ID"] == "iblock" && $arFields["PARAM2"] == 18) { $db_props = CIBlockElement::GetProperty( // Запросим свойства индексируемого элемента $arFields["PARAM2"], // BLOCK_ID индексируемого свойства $arFields["ITEM_ID"], // ID индексируемого свойства array("sort" => "asc"), // Сортировка (можно упустить) Array("CODE"=>"AKTIVNOST_KAMPFER")); // CODE свойства (в данном случае артикул) if($ar_props = $db_props->Fetch()){ if($ar_props['VALUE_XML_ID']!=='true'){ $tmpAr = array(); foreach ($arFields['SITE_ID'] as $sIndex=>$SID) { if($SID!=='s2') $tmpAr[] = $SID; } $arFields['SITE_ID'] = $tmpAr; } } // } return $arFields; } } ``` \| Если элемент привязан к нескольким сайтам, то нужно убрать по условию ненужный идентификатор сайта | Код | ``` AddEventHandler("search", "BeforeIndex", Array("SearchExclude", "BeforeIndexHandler")); class SearchExclude { function BeforeIndexHandler($arFields) { if ($arFields["MODULE_ID"] == "iblock" && $arFields["PARAM2"] == 18) { $db_props = CIBlockElement::GetProperty( // Запросим свойства индексируемого элемента $arFields["PARAM2"], // BLOCK_ID индексируемого свойства $arFields["ITEM_ID"], // ID индексируемого свойства array("sort" => "asc"), // Сортировка (можно упустить) Array("CODE"=>"AKTIVNOST_KAMPFER")); // CODE свойства (в данном случае артикул) if($ar_props = $db_props->Fetch()){ if($ar_props['VALUE_XML_ID']!=='true'){ $tmpAr = array(); foreach ($arFields['SITE_ID'] as $sIndex=>$SID) { if($SID!=='s2') $tmpAr[] = $SID; } $arFields['SITE_ID'] = $tmpAr; } } // } return $arFields; } } ``` |
| Код |  |  |
| ``` AddEventHandler("search", "BeforeIndex", Array("SearchExclude", "BeforeIndexHandler")); class SearchExclude { function BeforeIndexHandler($arFields) { if ($arFields["MODULE_ID"] == "iblock" && $arFields["PARAM2"] == 18) { $db_props = CIBlockElement::GetProperty( // Запросим свойства индексируемого элемента $arFields["PARAM2"], // BLOCK_ID индексируемого свойства $arFields["ITEM_ID"], // ID индексируемого свойства array("sort" => "asc"), // Сортировка (можно упустить) Array("CODE"=>"AKTIVNOST_KAMPFER")); // CODE свойства (в данном случае артикул) if($ar_props = $db_props->Fetch()){ if($ar_props['VALUE_XML_ID']!=='true'){ $tmpAr = array(); foreach ($arFields['SITE_ID'] as $sIndex=>$SID) { if($SID!=='s2') $tmpAr[] = $SID; } $arFields['SITE_ID'] = $tmpAr; } } // } return $arFields; } } ``` |  |  |
|  |  |  |
