# OnSearch


### Описание и параметры


```
string
функция-обработчик(
	string strQuery
);
```

Событие "OnSearch" вызывается перед выполнением поисковых запросов методом CSearch::Search.


#### Параметры


| Параметр | Описание |
| --- | --- |
| strQuery | Поисковая фраза. Если используется поиск по тегам, то в начале добавляется "tags:". |


#### Возвращаемое значение

Функция обработчик может вернуть строку вида "параметр=значение" которая будет добавлена к ссылкам на найденные элементы. Используется модулем статистики для учета поисковых фраз внутреннего поисковика.

---
### Смотрите также


- CSearch::Search
- **Обработка событий**

---
### Примеры использования


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("search", "OnSearch", Array("MyClass", "OnSearchHandler"));
class MyClass
{
	// создаем обработчик события "BeforeIndex"
	public static function OnSearchHandler($strQuery)
	{
		if(strpos($strQuery, "tags:")!==false)
			return "tags_search=Y";
		else
			return "";
	}
}
?>
```

---
