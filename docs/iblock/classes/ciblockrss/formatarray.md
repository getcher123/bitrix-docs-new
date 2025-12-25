# FormatArray


### Описание и параметры


```
array
CIBlockRSS::FormatArray(
	array arRes,
	array bOutChannel = false
);
```

Метод преобразует результат метода [CIBlockRSS](index.md)::[GetNewsEx](getnewsex.md) в более приемлемое представление. Нестатический метод.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| arRes | Массив описания xml. Результат работы метода [CIBlockRSS](index.md)::[GetNewsEx.](getnewsex.md) |  |
| *bOutChannel* | Параметр должен быть синхронизирован с одноименным метода [CIBlockRSS](index.md)::[GetNewsEx](getnewsex.md). | 3.2.1 |

---
### Возвращаемое значение

Массив следующего вида:


- title - заголовок rss ленты;
- link - ссылка;
- description - описание;
- lastBuildDate - время в rss формате (см. [CIBlockRSS](index.md)::[XMLDate2Dec](xmldate2dec.md));
- ttl - время действия в минутах;
- image - описание картинки:
- item - массив элементами которого являются нововсти:

---
### Смотрите также


- [CIBlockRSS](index.md)::[GetNewsEx](getnewsex.md)
- [CIBlockRSS](index.md)::[XMLDate2Dec](xmldate2dec.md)

---
### Примеры использования


```
<?
$arXML = CIBlockRSS::GetNewsEx('www.1c-bitrix.ru', '80', '/bitrix/rss.php', 'ID=news_sm&LANG=ru&TYPE=news&LIMIT=5');
if(count($arXML) > 0)
{
	$arRSS = CIBlockRSS::FormatArray($arXML);
	print_r($arRSS);
}
?>
```

---
