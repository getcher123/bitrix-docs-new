# XMLDate2Dec


### Описание и параметры


```
string
CIBlockRSS::XMLDate2Dec(
	string dateXML,
	string dateFormat= "DD.MM.YYYY"
);
```

Преобразует дату из rss формата в формат "DD.MM.YYYY". Нестатический метод.

**Примечание**: под rss форматом даты понимается формат, описанный в rfc 822.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| dateXML | rss дата/время. |  |
| dateFormat | Формат даты. Необязательный параметр. По умолчанию используется формат "DD.MM.YYYY". | 11.0.7 |


#### Возвращаемое значение

строка.

---
### Смотрите также


- [http://www.w3.org/Protocols/rfc822/](http://www.w3.org/Protocols/rfc822/)
- [CIBlockRSS](index.md)::[GetNewsEx](getnewsex.md)
- [CIBlockRSS](index.md)::[FormatArray](formatarray.md)

---
### Примеры использования


```
<?
$arXML = CIBlockRSS::GetNewsEx('www.1c-bitrix.ru', '80', '/bitrix/rss.php', 'ID=news_sm&LANG=ru&TYPE=news&LIMIT=5');
if(count($arXML) > 0)
{
	$arRSS = CIBlockRSS::FormatArray($arXML);
	foreach($arRSS["item"] as $arItem)
	{
		echo $arItem["title"].":".CIBlockRSS::XMLDate2Dec($arItem["pubDate"]);
	}
}
?>
```

---
