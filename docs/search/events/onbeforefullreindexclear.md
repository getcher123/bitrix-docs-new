# OnBeforeFullReindexClear


```
void
функция-обработчик();
```

Событие "OnBeforeFullReindexClear" вызывается во время полной переиндексации. В начале первого шага, непосредственно перед удалением всех данных поискового индекса.


#### Смотрите также


- **Обработка событий**


#### Пример функции-обработчика:


```
<?
// регистрируем обработчик события "OnBeforeFullReindexClear" модуля "search"
RegisterModuleDependences("search", "OnBeforeFullReindexClear", "my_module", "CMyModule", "TruncateTables");
// создаем в модуле my_module в классе CMyModule функцию-метод TruncateTables
public static function TruncateTables()
{
	global $DB;
	$DB->Query("truncate table my_search_ext_data");
}
?>
```
