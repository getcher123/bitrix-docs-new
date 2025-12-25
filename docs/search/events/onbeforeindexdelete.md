# OnBeforeIndexDelete


```
void
функция-обработчик(
	string strWhere
);
```

Событие "OnBeforeIndexDelete" вызывается перед удалением части поискового индекса.


#### Параметры


| Параметр | Описание |
| --- | --- |
| strWhere | SQL условие для удаления. Представляет собой фильтр по полю SEARCH_CONTENT_ID. |


#### Смотрите также


- **Обработка событий**


#### Пример функции-обработчика:


```
<?
// регистрируем обработчик события "OnBeforeIndexDelete" модуля "search"
RegisterModuleDependences("search", "OnBeforeIndexDelete", "my_module", "CMyModule", "DeleteSearchExtData");
// создаем в модуле my_module в классе CMyModule функцию-метод TruncateTables
public static function DeleteSearchExData($strWhere)
{
	global $DB;
	$DB->Query("delete from my_search_ext_data where ".$strWhere);
}
?>
```
