# Добавление закладки в социальную сеть

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3395 — Как написать обработчик события](lesson_3395.md)
- [Следующий: 2949 — Учет регистрации нового пользователя в статистике →](lesson_2949.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2812

Как добавить произвольную закладку в социальную сеть без изменения стандартных компонентов? Для этого необходимо написать обработчики специальных событий.

Обработчики можно расположить в файле `/bitrix/php_interface/init.php`.

```

// Событие происходит при формировании списка дополнительного
// функционала соц.сети
// В обработчике можно изменить или дополнить список
AddEventHandler("socialnetwork", "OnFillSocNetFeaturesList", "__AddSocNetFeature");

// Событие происходит при формировании списка закладок
// В обработчике можно изменить список закладок
AddEventHandler("socialnetwork", "OnFillSocNetMenu", "__AddSocNetMenu");

// Событие происходит в комплексном компоненте при работе в ЧПУ
// режиме при формировании списка шаблонов адресов страниц
// комплексного компонента
AddEventHandler("socialnetwork", "OnParseSocNetComponentPath", "__OnParseSocNetComponentPath");

// Событие происходит в комплексном компоненте при работе в
// не ЧПУ режиме при формировании списка псевдонимов переменных
AddEventHandler("socialnetwork", "OnInitSocNetComponentVariables", "__OnInitSocNetComponentVariables");

// При формировании списка дополнительного функционала
// добавим дополнительную запись superficha
function __AddSocNetFeature(&$arSocNetFeaturesSettings)
{
	$arSocNetFeaturesSettings["superficha"] = array(
		"allowed" => array(SONET_ENTITY_USER, SONET_ENTITY_GROUP),
		"operations" => array(
			"write" => array(SONET_ENTITY_USER => SONET_RELATIONS_TYPE_NONE, SONET_ENTITY_GROUP => SONET_ROLES_MODERATOR),
			"view" => array(SONET_ENTITY_USER => SONET_RELATIONS_TYPE_ALL, SONET_ENTITY_GROUP => SONET_ROLES_USER),
		),
		"minoperation" => "view",
	);
}

// При формировании списка закладок добавим дополнительную
// закладку для функционала superficha
function __AddSocNetMenu(&$arResult)
{
	// Доступна для показа
	$arResult["CanView"]["superficha"] = true;
	// Ссылка закладки
	$arResult["Urls"]["superficha"] = CComponentEngine::MakePathFromTemplate("/workgroups/group/#group_id#/superficha/", array("group_id" => $arResult["Group"]["ID"]));
	// Название закладки
	$arResult["Title"]["superficha"] = "Моя фича";
}

// При формировании списка шаблонов адресов страниц
// комплексного компонента в режиме ЧПУ добавим шаблон
// для superficha
function __OnParseSocNetComponentPath(&$arUrlTemplates, &$arCustomPagesPath)
{
	// Шаблон адреса страницы
	$arUrlTemplates["superficha"] = "group/#group_id#/superficha/";
	// Путь относительно корня сайта,
		// по которому лежит страница
	$arCustomPagesPath["superficha"] = "/bitrix/php_interface/1/";
}

// Если компонент соц.сети работает в режиме
// ЧПУ, то этот обработчик не нужен
function __OnInitSocNetComponentVariables(&$arVariableAliases, &$arCustomPagesPath)
{
	}
```

По пути `/bitrix/php_interface/1/` должен лежать файл **superficha.php**, который содержит код страницы:

```

<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();?>
<?
$APPLICATION->IncludeComponent(
	"bitrix:socialnetwork.group_menu",
	"",
	Array(
		"GROUP_VAR" => $arResult["ALIASES"]["group_id"],
		"PAGE_VAR" => $arResult["ALIASES"]["page"],
		"PATH_TO_GROUP" => $arResult["PATH_TO_GROUP"],
		"PATH_TO_GROUP_MODS" => $arResult["PATH_TO_GROUP_MODS"],
		"PATH_TO_GROUP_USERS" => $arResult["PATH_TO_GROUP_USERS"],
		"PATH_TO_GROUP_EDIT" => $arResult["PATH_TO_GROUP_EDIT"],
		"PATH_TO_GROUP_REQUEST_SEARCH" => $arResult["PATH_TO_GROUP_REQUEST_SEARCH"],
		"PATH_TO_GROUP_REQUESTS" => $arResult["PATH_TO_GROUP_REQUESTS"],
		"PATH_TO_GROUP_REQUESTS_OUT" => $arResult["PATH_TO_GROUP_REQUESTS_OUT"],
		"PATH_TO_GROUP_BAN" => $arResult["PATH_TO_GROUP_BAN"],
		"PATH_TO_GROUP_BLOG" => $arResult["PATH_TO_GROUP_BLOG"],
		"PATH_TO_GROUP_PHOTO" => $arResult["PATH_TO_GROUP_PHOTO"],
		"PATH_TO_GROUP_FORUM" => $arResult["PATH_TO_GROUP_FORUM"],
		"PATH_TO_GROUP_CALENDAR" => $arResult["PATH_TO_GROUP_CALENDAR"],
		"PATH_TO_GROUP_FILES" => $arResult["PATH_TO_GROUP_FILES"],
		"PATH_TO_GROUP_TASKS" => $arResult["PATH_TO_GROUP_TASKS"],
		"GROUP_ID" => $arResult["VARIABLES"]["group_id"],
		"PAGE_ID" => "group_superficha",
		),
	$component
);
?>

Полезный код страницы...
```
