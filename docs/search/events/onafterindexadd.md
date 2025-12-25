# OnAfterIndexAdd


### Описание и параметры


```
void
функция-обработчик(
	int ID,
	array arFields
);
```

Событие "OnAfterIndexAdd" вызывается после добавления новых данных в поисковый индекс.


#### Параметры


| Параметр | Описание |
| --- | --- |
| ID | Уникальный идентификатор записи в поисковом индексе. |
| arFields | Поля поискового индекса. |


#### Смотрите также


- **Обработка событий**

---
### Пример функции-обработчика


```
<?
// регистрируем обработчик события "OnAfterIndexAdd" модуля "search"
RegisterModuleDependences("search", "OnAfterIndexAdd", "my_module", "CMyModule", "AddSearchExtData");
// создаем в модуле my_module в классе CMyModule функцию-метод AddSearchExtData
public static function AddSearchExtData($ID, $arFields)
{
	global $DB;
	if($arFields["MODULE_ID"]=="my_module")
		$DB->Add("my_search_ext_data", array("SEARCH_CONTENT_ID"=>$ID, "EXT_DATA"=>time()));
}
?>
```

---
