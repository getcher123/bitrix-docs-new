# OnReIndex


### Описание и параметры


```
boolфункция-обработчик(
	array NS,
	string oCallback,
	string callback_method
);
```

Событие "OnReindex" вызывается во время переиндексации данных модуля методами CSearch::ReindexModule или CSearch::ReIndexAll.


#### Параметры


| Параметр | Описание |
| --- | --- |
| NS | Массив в котором передается информация о начале текущего шага. - **MODULE** - идентификатор модуля; - **ID** - идентификатор элемента; - **SITE_ID** - массив сайтов; |
| oCallback | Объект модуля поиска для вызова метода индексации элемента. |
| callback_method | Метод объекта модуля поиска для индексации элемента. |

---
### Смотрите также


- CSearch::ReindexModule
- CSearch::ReIndexAll
- **Обработка событий**

---
### Примеры использования


```
<?// регистрируем обработчик события "OnReindex" модуля "search"RegisterModuleDependences("search", "OnReindex", "my_module", "CMyModule", "OnReindex");// создаем в модуле my_module в классе CMyModule функцию-метод OnReindexpublic static function OnReindex($NS, $oCallback, $callback_method){	global $DB;	$NS["ID"] = intval($NS["ID"]);	if($NS["MODULE"]=="my_module" && $NS["ID"] > 0)		$strWhere = "WHERE ID > ".$NS["ID"];	else		$strWhere = "";	$strSql =		"SELECT FT.ID, FT.TITLE, FT.MESSAGE, ".		"  DATE_FORMAT(FT.POST_DATE, '%d.%m.%Y %H:%i:%s') as POST_DATE, FT.LID ".		"FROM b_my_table FT ".		$strWhere.		" ORDER BY FT.ID";	$db_res = $DB->Query($strSql);	while ($res = $db_res->Fetch())	{		$Result = array(			"ID" => $res["ID"],			"SITE_ID" => array("s1"),			"DATE_CHANGE" => $res["POST_DATE"],			"URL" => "/my_module/index.php?ID=".$res["ID"],			"PERMISSIONS" => array(2),			"TITLE" => $res["TITLE"],			"BODY" => $res["MESSAGE"],		);		$index_res = call_user_func(array($oCallback, $callback_method), $Result);		if(!$index_res)			return $Result["ID"];	}	return false;}// вызываем переиндексацию модуляCSearch::ReIndexModule("my_module");?>
```

---
