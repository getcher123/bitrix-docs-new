# OnAdminListDisplay


### Описание и параметры


```
void
Handler(
	object &list
);
```

Событие OnAdminListDisplay вызывается в функции CAdminList::Display() при выводе в административном разделе списка элементов. Событие позволяет модифицировать объект списка, в частности, добавить произвольные групповые действия над элементами списка, добавить команды в меню действий элемента списка и т.п.


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| list | Ссылка на объект класса CAdminList. |


#### Возвращаемое значение

Возвращаемое значение не используется.


#### Смотрите также


- События
- Класс CAdminListRow

---
### Примеры использования


```
<?AddEventHandler("main", "OnAdminListDisplay", "MyOnAdminListDisplay");public static function MyOnAdminListDisplay(&$list){	//add custom group action	if($list->table_id == "tbl_posting")		$list->arActions["status_draft"] = "Статус: Черновик";}//process custom actionAddEventHandler("main", "OnBeforeProlog", "MyOnBeforeProlog");public static function MyOnBeforeProlog(){	if($_SERVER["REQUEST_METHOD"] == "POST" && $_POST["action"] == "status_draft" && is_array($_POST["ID"]) && $GLOBALS["APPLICATION"]->GetCurPage() == "/bitrix/admin/posting_admin.php")	{		if($GLOBALS["APPLICATION"]->GetGroupRight("subscribe") == "W" && check_bitrix_sessid())		{			if(CModule::IncludeModule("subscribe"))			{				$cPosting = new CPosting;				foreach($_POST["ID"] as $ID)					if(($ID = intval($ID)) > 0)						$cPosting->ChangeStatus($ID, "D");			}		}	}}?>
```

---
