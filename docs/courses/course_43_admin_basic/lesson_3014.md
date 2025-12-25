# Использование постранички для массивов данных

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 14036 — Шифрованные cookies](lesson_14036.md)
- [Следующий: 9221 — Балансировка запросов в кластере →](lesson_9221.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3014

Пример реализации выборки из нескольких инфоблоков с постраничной навигацией и сортировкой.

#### Задача

1. Выбрать список элементов из нескольких инфоблоков в таблицу;
2. Иметь возможность сортировки элементов;
3. Должна работать постраничная навигация

#### Решение

Этот пример можно использовать при небольшом количестве выбираемых элементов (максимум до 100), естественно с кэшированием.

Соберём все данные в ассоциативный массив, например вот такой:

```
[ITEM] => Array
	(
		[0] => Array
			(
				[CITY_NAME] => value
				[CITY_DETAIL_URL] => value
				[OBJECT_NAME] => value
				[OBJECT_ID] => 2487
				[DATE_CREATE] => 02.07.2006
				[STATUS] => Y
				[PAID_STATUS] => Y
				[DETAIL_OBJECT_URL] => value
			)

		[1] => Array
			(
				[CITY_NAME] => value
				[CITY_DETAIL_URL] => value
				[OBJECT_NAME] => value
				[OBJECT_ID] => 2489
				[DATE_CREATE] => 02.07.2006
				[STATUS] => Y
				[PAID_STATUS] => N
				[DETAIL_OBJECT_URL] => value
			)
```

Теперь нужно отсортировать массив `$arResult['ITEM']`, для этого пишем класс:

```
class CCabinet_SortObject {

	function __cmp_ValueOf($a, $b, $name, $order) {
		if(is_set($a[$name]) && is_set($b[$name])) {
			if($order == 'ASC')
				return ($a[$name]<$b[$name])?true:false;
 			elseif($order == 'DESC')
 				return ($b[$name]>$a[$name])?false:true;
		}
	}

	function cmp_STATUS_ASC($a, $b) {
		return CCabinet_SortObject::__cmp_ValueOf($a, $b, "STATUS", "ASC");
	}

	function cmp_STATUS_DESC($a, $b) {
		return CCabinet_SortObject::__cmp_ValueOf($a, $b, "STATUS", "DESC");
	}

	function cmp_NAME_ASC($a, $b) {
		return CCabinet_SortObject::__cmp_ValueOf($a, $b, "OBJECT_NAME", "ASC");
	}

	function cmp_NAME_DESC($a, $b) {
		return CCabinet_SortObject::__cmp_ValueOf($a, $b, "OBJECT_NAME", "DESC");
	}

	function cmp_CITY_ASC($a, $b) {
		return CCabinet_SortObject::__cmp_ValueOf($a, $b, "CITY_NAME", "ASC");
	}

	function cmp_CITY_DESC($a, $b) {
		return CCabinet_SortObject::__cmp_ValueOf($a, $b, "CITY_NAME", "DESC");
	}

	function cmp_DATE_DESC($a, $b) {
		if ($a["DATE_CREATE"] == $b["DATE_CREATE"]) {
        	return 0;
	    }
	    return ($a["DATE_CREATE"] > $b["DATE_CREATE"]) ? -1 : 1;
	}

	function cmp_DATE_ASC($a, $b) {
		if ($a["DATE_CREATE"] == $b["DATE_CREATE"]) {
        	return 0;
	    }
	    return ($a["DATE_CREATE"] < $b["DATE_CREATE"]) ? -1 : 1;
	}

}
```

Вот пример применения класса:

```
usort($arResult['ITEM'], array("CCabinet_SortObject", "cmp_".$arParams['SORT_BY']."_".$arParams['SORT_ORDER']));
```

После чего нам нужно разбить массив постранично используя **API**:

```
$rs_ObjectList = new CDBResult;
$rs_ObjectList->InitFromArray($arResult['ITEM']);
$rs_ObjectList->NavStart(10, false);
$arResult["NAV_STRING"] = $rs_ObjectList->GetPageNavString("", 'komka.cabinet');
$arResult["PAGE_START"] = $rs_ObjectList->SelectedRowsCount() - ($rs_ObjectList->NavPageNomer - 1) * $rs_ObjectList->NavPageSize;
while($ar_Field = $rs_ObjectList->Fetch())
{
$arResult['_ITEM'][] = $ar_Field;
}
```
