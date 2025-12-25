# OnAdminContextMenuShow


### Описание и параметры


```
void
Handler(
	array &items
);
```

Событие OnAdminContextMenuShow вызывается в функции CAdminContextMenu::Show() при выводе в административном разделе панели кнопок. Событие позволяет модифицировать или добавить собственные кнопки на панель.


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| **items** | Ссылка на массив кнопок на панели. Структура массива описана на странице Конструктор CAdminContextMenu. |


#### Возвращаемое значение

Возвращаемое значение не используется.


#### Смотрите также


- События
- Класс CAdminContextMenu

---
### Примеры использования


```
<?
AddEventHandler("main", "OnAdminContextMenuShow", "MyOnAdminContextMenuShow");
public static function MyOnAdminContextMenuShow(&$items)
{
	//add custom button to the index page toolbar
	if($GLOBALS["APPLICATION"]->GetCurPage(true) == "/bitrix/admin/index.php")
		$items[] = array("TEXT"=>"Настройки модулей", "ICON"=>"", "TITLE"=>"Страница настроек модулей", "LINK"=>"settings.php?lang=".LANGUAGE_ID);
}
?>
```

---
