# Административное меню

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3491 — Административные скрипты](lesson_3491.md)
- [Следующий: 2825 — Взаимодействие модулей →](lesson_2825.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5187

Меню административной части выводится стандартной функцией [CMain::GetMenuHtmlEx](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/getmenuhtmlex.php).

Меню формируется на основе перебора всех файлов `/bitrix/modules/ID модуля/admin/menu.php`. В каждом таком файле содержится определение массива `$aModuleMenuLinks`, содержащего пункты меню соответствующего модуля. Все эти массивы затем будут объединены в стандартный массив `$arMenuSections`, содержащий информацию о всех пунктах меню.

#### Образец структуры меню на примере \bitrix\modules\main\admin\menu.php

```

$aMenu[] = array(
	"parent_menu" => "global_menu_settings",
	"sort" => 1800,
	"text" => GetMessage("MAIN_MENU_TOOLS"),
	"title" => GetMessage("MAIN_MENU_TOOLS_TITLE"),
	"url" => "tools_index.php?lang=".LANGUAGE_ID,
	"icon" => "util_menu_icon",
	"page_icon" => "util_page_icon",
	"items_id" => "menu_util",
	"items" => array(
		array(
			"text" => GetMessage("MAIN_MENU_SITE_CHECKER"),
			"url" => "site_checker.php?lang=".LANGUAGE_ID,
			"more_url" => array(),
			"title" => GetMessage("MAIN_MENU_SITE_CHECKER_ALT"),
		),
	array(
		"text" => GetMessage("MAIN_MENU_FILE_CHECKER"),
		"url" => "file_checker.php?lang=".LANGUAGE_ID,
		"more_url" => array(),
		"title" => GetMessage("MAIN_MENU_FILE_CHECKER_ALT"),
		),
	array(
		"text" => GetMessage("MAIN_MENU_PHPINFO"),
		"url" => "phpinfo.php?test_var1=AAA&test_var2=BBB",
		"more_url" => array("phpinfo.php"),
		"title" => GetMessage("MAIN_MENU_PHPINFO_ALT"),
		),
	array(
		"text" => GetMessage("MAIN_MENU_SQL"),
		"url" => "sql.php?lang=".LANGUAGE_ID."&del_query=Y",
		"more_url" => array("sql.php"),
		"title" => GetMessage("MAIN_MENU_SQL_ALT"),
		),
	array(
		"text" => GetMessage("MAIN_MENU_PHP"),
		"url" => "php_command_line.php?lang=".LANGUAGE_ID."",
		"more_url" => array("php_command_line.php"),
		"title" => GetMessage("MAIN_MENU_PHP_ALT"),
		),
	array(
		"text" => GetMessage("MAIN_MENU_AGENT"),
		"url" => "agent_list.php?lang=".LANGUAGE_ID,
		"more_url" => array("agent_list.php", "agent_edit.php"),
		"title" => GetMessage("MAIN_MENU_AGENT_ALT"),
		),
	array(
		"text" => GetMessage("MAIN_MENU_DUMP"),
		"url" => "dump.php?lang=".LANGUAGE_ID,
		"more_url" => array("dump.php", "restore_export.php"),
		"title" => GetMessage("MAIN_MENU_DUMP_ALT"),
		),
(strtoupper($DBType) == "MYSQL"?
	Array(
		"text" => GetMessage("MAIN_MENU_REPAIR_DB"),
		"url" => "repair_db.php?lang=".LANGUAGE_ID,
		"more_url" => array(),
		"title" => GetMessage("MAIN_MENU_REPAIR_DB_ALT"),
		)
:null
),
($USER->CanDoOperation('view_event_log')?
	Array(
		"text" => GetMessage("MAIN_MENU_EVENT_LOG"),
		"url" => "event_log.php?lang=".LANGUAGE_ID,
		"more_url" => array(),
		"title" => GetMessage("MAIN_MENU_EVENT_LOG_ALT"),
		)
:null
		),
	),
);
```

Пункты административного меню можно добавлять с помощью события [OnBuildGlobalMenu](http://dev.1c-bitrix.ru/api_help/main/events/onbuildglobalmenu.php).

Если вы пишите свой модуль можете использовать `/bitrix/modules/ID_модуля/admin/menu.php` для добавления пунктов административного меню.

## Старый способ формирования меню

Структура массива **$aModuleMenuLinks**:

```

Array
(
	[0] => Array
		(
			[0] => заголовок пункта меню
			[1] => ссылка на пункте меню
			[2] => Array
				(
					[0] => дополнительная ссылка для подсветки пункта меню 1
					[1] => дополнительная ссылка для подсветки пункта меню 2
					...
					[N] =>  дополнительная ссылка для подсветки пункта меню N
				)
			[3] => Array
				(
					[ALT] => текст всплывающей подсказки на пункте меню
					[SECTION_ID] => уникальный идентификатор раздела меню, принимает значение равное ID модуля, либо одно из следующих:
						FAVORITE - раздел "Избранное"
						GENERAL - раздел "Пользователи"
						MAIN - раздел "Настройки системы"

					[SEPARATOR] => "Y" - пункт меню является заголовком раздела меню
					[SORT] => сортировка раздела меню относительно других разделов меню (только если SEPARATOR=Y)
					[ICON] => ссылка на маленькую иконку используемую в заголовке раздела меню (только если SEPARATOR=Y)
					[BIG_ICON] => ссылка на большую иконку для использование на странице "Рабочий стол" (только если SEPARATOR=Y)
					[INDEX_PAGE] => ссылка на иконке BIG_ICON (только если SEPARATOR=Y)
				)

		)
	[1] => Array( -//- )
	[2] => Array( -//- )
	...
	[M] => Array( -//- )
)
```

#### Пример файла /bitrix/modules/support/admin/menu.php определяющего меню модуля "Техподдержка":

```

<?
// подключим языковой файл
IncludeModuleLangFile(__FILE__);

// определим права текущего пользователя
$SUP_RIGHT = $APPLICATION->GetGroupRight("support");

// если доступ не запрещён то
if($SUP_RIGHT>"D")
{
	// добавляем пункты меню в зависимости от прав

	$aModuleMenuLinks[] = Array(
		GetMessage("SUP_M_SUPPORT"),
		"",
		Array(),
		Array(
			"SEPARATOR"  => "Y",
			"SORT"       => 1000,
			"ICON"       => "/bitrix/images/support/mnu_support.gif",
			"BIG_ICON"   => "/bitrix/images/support/support.gif",
			"INDEX_PAGE" => "/bitrix/admin/ticket_desktop.php?lang=".LANGUAGE_ID."&set_default=Y"
			)
		);

	if ($SUP_RIGHT>="T")
	{
		$aModuleMenuLinks[] = Array(
			GetMessage("SUP_M_REPORT_TABLE"),
			"/bitrix/admin/ticket_desktop.php?lang=".LANGUAGE_ID."&set_default=Y",
			Array("/bitrix/admin/ticket_desktop.php"),
			Array("ALT"=>GetMessage("SUP_M_REPORT_TABLE_ALT"))
		);
	}

	$aModuleMenuLinks[] = Array(
		GetMessage("SUP_M_TICKETS"),
		"/bitrix/admin/ticket_list.php?lang=".LANGUAGE_ID."&set_default=Y",
		Array(
			"/bitrix/admin/ticket_list.php",
			"/bitrix/admin/ticket_edit.php",
			"/bitrix/admin/ticket_message_edit.php"
			),
		Array("ALT"=>GetMessage("SUP_M_TICKETS_ALT"))
		);

	if ($SUP_RIGHT>="T")
	{
		$aModuleMenuLinks[] = Array(
		GetMessage("SUP_M_REPORT_GRAPH"),
			"/bitrix/admin/ticket_report_graph.php?lang=".LANGUAGE_ID."&set_default=Y",
			Array("/bitrix/admin/ticket_report_graph.php"),
			Array("ALT"=>GetMessage("SUP_M_REPORT_GRAPH_ALT"))
			);
	}

	if ($SUP_RIGHT>="V")
	{
		$aModuleMenuLinks[] = Array(
			GetMessage("SUP_M_CATEGORY"),
			"/bitrix/admin/ticket_dict_list.php?lang=".LANGUAGE_ID."&find_type=C&set_filter=Y",
			Array(
				"/bitrix/admin/ticket_dict_edit.php?find_type=C",
				"/bitrix/admin/ticket_dict_list.php?find_type=C"
				)
		);
	}
}
?>
```
