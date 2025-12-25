# Работа с языковыми файлами

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2916 — Файл init.php](lesson_2916.md)
- [Следующий: 4861 — Гаджеты и их создание →](lesson_4861.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=4789

### Языковые файлы

Для каждого языка существует свой набор языковых файлов, хранящихся в подкаталогах `/lang/` (подробнее смотрите на страницах документации [структура файлов системы](http://dev.1c-bitrix.ru/api_help/main/general/structure.php), [структура файлов модуля](http://dev.1c-bitrix.ru/api_help/main/general/modules/structure.php)).

Языковые файлы, как правило, используются в [административных скриптах](http://dev.1c-bitrix.ru/api_help/main/general/modules/admin.php) модулей или в [компонентах](http://dev.1c-bitrix.ru/api_help/main/general/terms.php#component) и в зависимости от этого подключаются одной из следующих функций:

- [IncludeModuleLangFile](http://dev.1c-bitrix.ru/api_help/main/functions/localization/includemodulelangfile.php) - в административных скриптах;
- [IncludeTemplateLangFile](http://dev.1c-bitrix.ru/api_help/main/functions/localization/includetemplatelangfile.php) - в компонентах;

Для удобства поиска и дальнейшей модификации языковых фраз можно пользоваться параметром страницы [show_lang_files](http://dev.1c-bitrix.ru/api_help/main/general/magic_vars.php#show_lang_files)=Y, позволяющим быстро найти и исправить ту или иную языковую фразу в модуле **Перевод**.

### Файлы в собственных компонентах

При создании собственного компонента языковой путь должен выглядеть следующим образом:



```
/bitrix/templates/[шаблон_сайта|.default]/components/[пространство_имен]/[имя_компонента]/[имя_шаблона_компонента]/lang/[код_языка]/template.php
```

Где код языка, к примеру **= ru**.

В таком случае языковые файлы подключатся автоматически.

Для подключения из компонента языковых сообщений другого компонента можно использовать следующую функцию:

```

function IncludeComponentLangFile ($abs_path, $lang = false)
{
if ($lang === false) $lang = LANGUAGE_ID;

global $BX_DOC_ROOT;

$filepath = rtrim (preg_replace ("'[\\\\/]+'", "/", $abs_path), "/ ");

if (strpos ($filepath, $BX_DOC_ROOT) !== 0)
{
return;
}

$relative_path = substr ($filepath, strlen ($BX_DOC_ROOT));

if (preg_match ("~^/bitrix/components/([-a-zA-Z0-9_\.%]+)/([-a-zA-Z0-9\._%]+)/templates/([-a-zA-Z0-9\._%]+)/(.*)$~", $relative_path, $matches))
{
$lang_path = $BX_DOC_ROOT."/bitrix/components/$matches[1]/$matches[2]/templates/$matches[3]/lang/$lang/$matches[4]";
__IncludeLang ($lang_path);
return;
}

if (preg_match ("~^/bitrix/components/([-a-zA-Z0-9_\.%]+)/([-a-zA-Z0-9\._%]+)/(.*)$~", $relative_path, $matches))
{
$lang_path = $BX_DOC_ROOT."/bitrix/components/$matches[1]/$matches[2]/lang/$lang/$matches[3]";
__IncludeLang ($lang_path);
return;
}
}
```

### Замена фраз в продукте

Иногда при разработке требуется заменить какие-то слова или фразы в компонентах или модулях.

Коснемся этой технологии, суть которой в том, что после подключения языкового файла фразы продукта заменяются на определенные разработчиком.

Путь к файлу замен:

`/bitrix/php_interface/user_lang/<код языка>/lang.php`

**Примечание**: если в **php_interface** нет нужных папок, их следует создать.

Возможно использование папки `/local/php_interface/user_lang/<код языка>/lang.php`.



В файле должны определяться элементы массива `$MESS` в виде `$MESS['языковой файл']['код фразы'] = 'новая фраза'`, например:

```

<?
$MESS["/bitrix/components/bitrix/system.auth.form/templates/.default/lang/ru/template.php"]["AUTH_PROFILE"] = "Мой любимый профиль";
$MESS["/bitrix/modules/main/lang/ru/public/top_panel.php"]['top_panel_tab_view'] = "Смотрим";
$MESS["/bitrix/modules/main/lang/ru/interface/index.php"]['admin_index_sec'] = "Проактивка";
?>
```

Первая строка меняет текст ссылки в компоненте формы авторизации; вторая строка меняет название вкладки публичной панели; третья меняет строку для индексной страницы панели управления.

**Важно!**Возможны проблемы сопровождения этого файла при изменении кода фразы или расположения языкового файла.

### Языковые фразы в D7

По умолчанию подстановка языковых фраз не работает в файле **component_epilog.php** шаблона компонента. Поэтому в нем языковые фразы подключаются следующим образом:

```

use \Bitrix\Main\Localization\Loc;
Loc::loadLanguageFile(__FILE__);
echo Loc::getMessage("SOMETHING_LANGUAGE_CONSTANT");
```

Сами языковые фразы, например, для русского языка должны быть заданы в файле `lang/ru/component_epilog.php`. Кроме того, при таком подключении языковые фразы будут работать как в кеше, так и "мимо" кеша.
