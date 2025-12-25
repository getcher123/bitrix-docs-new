# OnSearchGetURL


### Описание и параметры


```
stringфункция-обработчик(
	array arFields
);
```

Событие "OnSearchGetURL" вызывается при форматировании элемента в результатах поиска из метода CSearch::Fetch и при построении Google Sitemap CSiteMap::Create. На данный момент событие вызывается только для параметризированных URL.


#### Параметры


| Параметр | Описание |
| --- | --- |
| arFields | Массив описывающий элемент поискового индекса. |


#### Возвращаемое значение

Функция-обработчик может применить форматирование к элементу URL. И должна его вернуть даже если форматирование не было применено.

---
### Смотрите также


- CSearch::Fetch
- CSiteMap::Create
- **Обработка событий**

---
### Пример функции-обработчика


```
<?//init.php// регистрируем обработчик события "OnSearchGetURL" модуля "search"AddEventHandler("search", "OnSearchGetURL", array("CMyClass", "OnSearchGetURL"));class CMyClass{	public static function OnSearchGetURL($arFields)	{		$url = str_replace("#MY_SID#", md5(rand()), $arFields["URL"]);		return $url;	}}?>
```

---
