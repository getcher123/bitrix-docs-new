# OnSearchGetTag


### Описание и параметры


```
stringфункция-обработчик(	string tag);
```

Событие "OnSearchGetTag" вызывается при разборе строки тегов из функции [Tags_prepare](../functions/tags_prepare.md).


#### Параметры


| Параметр | Описание |
| --- | --- |
| tag | Тег. |


#### Возвращаемое значение

Функция-обработчик может отфильтровать недопустимые символы или значения тега. И должна его вернуть даже если форматирование не было применено.

---
### Смотрите также


- [Tags_prepare](../functions/tags_prepare.md)
- **Обработка событий**

---
### Пример функции-обработчика


```
<?//init.php// регистрируем обработчик события "OnSearchGetTag" модуля "search"AddEventHandler("search", "OnSearchGetTag", array("CMyClass", "OnSearchGetTag"));class CMyClass{	public static function OnSearchGetTag($tag)	{		static $stop = array(			"АХ" => true,			"ФУ" => true,		);		$tag = ToUpper($tag);		if(array_key_exists($tag, $stop))			return "";		else			return $tag;	}}?>
```

---
