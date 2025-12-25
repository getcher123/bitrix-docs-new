# Модификация шаблона или создание result_modifier?

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2993 — Пример. Выборка из Информационного блока](lesson_2993.md)
- [Следующий: 2899 — Пример. Компонент в элементе ИБ →](lesson_2899.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2897

Достаточно часто можно решить одну и ту же задачу разными способами. Выбор конечного варианта в таких задачах остается за разработчиком, который он принимает в зависимости от конкретной задачи. Рассмотрим пример решений задачи, которую можно решить двумя способами.

Как сделать возможность вставки видео при публикации новостей на сайте? На первый взгляд это может показаться сложно. Но фактически все легко реализуемо. Идея состоит в том, чтобы для прикреплённого к новости файла подключать компонент **Медиа проигрыватель** (**bitrix:player**). Для отображения новости будет использоваться компонент **Новость детально** (**bitrix:news.detail**).

Какой бы способ вы не использовали, необходимо [создать свойство](lesson_2831.md) типа **Файл** в инфоблоке новостей.

#### Решение с редактированием шаблона

- Скопируйте шаблон компонента **news.detail** в шаблон сайта. Сам компонент менять не придётся.
- Создайте новую страницу в визуальном редакторе и разместите на ней компонент **Медиа проигрыватель** (**bitrix:player**). Укажите базовые настройки (путь к видео файлу пока не заполняйте). Скопируйте полученный код вызова компонента. Например такой:
  ```
  <?$APPLICATION->IncludeComponent(
  	"bitrix:player",
  	"",
  	Array(
  		"PLAYER_TYPE" => "auto",
  		"USE_PLAYLIST" => "N",
  		"PATH" => "",
  		"WIDTH" => "400",
  		"HEIGHT" => "300",
  		"FULLSCREEN" => "Y",
  		"SKIN_PATH" => "/bitrix/components/bitrix/player/mediaplayer/skins",
  		"SKIN" => "bitrix.swf",
  		"CONTROLBAR" => "bottom",
  		"WMODE" => "transparent",
  		"HIDE_MENU" => "N",
  		"SHOW_CONTROLS" => "Y",
  		"SHOW_STOP" => "N",
  		"SHOW_DIGITS" => "Y",
  		"CONTROLS_BGCOLOR" => "FFFFFF",
  		"CONTROLS_COLOR" => "000000",
  		"CONTROLS_OVER_COLOR" => "000000",
  		"SCREEN_COLOR" => "000000",
  		"AUTOSTART" => "N",
  		"REPEAT" => "N",
  		"VOLUME" => "90",
  		"DISPLAY_CLICK" => "play",
  		"MUTE" => "N",
  		"HIGH_QUALITY" => "Y",
  		"ADVANCED_MODE_SETTINGS" => "N",
  		"BUFFER_LENGTH" => "10",
  		"DOWNLOAD_LINK_TARGET" => "_self"
  	)
  );?>
  ```
- В шаблоне компонента вместо свойства movie настройте подключение медиаплеера. Найдите строки вывода свойств:
  ```
  30	<?foreach($arResult["DISPLAY_PROPERTIES"] as $pid=>$arProperty):?>
   31
   32	<?=$arProperty["NAME"]?>:
   33		<?if(is_array($arProperty["DISPLAY_VALUE"])):?>
   34			<?=implode(" / ", $arProperty["DISPLAY_VALUE"]);?>
   35		<?else:?>
   36			<?=$arProperty["DISPLAY_VALUE"];?>
   37		 <?endif?>
   38		<br />
   39	<?endforeach;?>
  ```
- Вставьте проверку и замену, получается:
  ```
  <?foreach($arResult["DISPLAY_PROPERTIES"] as $pid=>$arProperty):?>
  <?if ($arProperty["CODE"]=='movie' && $arProperty["DISPLAY_VALUE"]) {?>
  <?$APPLICATION->IncludeComponent(
  	"bitrix:player",
  	"",
  	Array(
  		"PLAYER_TYPE" => "auto",
  		"USE_PLAYLIST" => "N",
  		"PATH" => CFile::GetPath($arProperty["VALUE"]),
  		"WIDTH" => "400",
  		"HEIGHT" => "300",
  		"FULLSCREEN" => "Y",
  		"SKIN_PATH" => "/bitrix/components/bitrix/player/mediaplayer/skins",
  		"SKIN" => "bitrix.swf",
  		"CONTROLBAR" => "bottom",
  		"WMODE" => "transparent",
  		"HIDE_MENU" => "N",
  		"SHOW_CONTROLS" => "Y",
  		"SHOW_STOP" => "N",
  		"SHOW_DIGITS" => "Y",
  		"CONTROLS_BGCOLOR" => "FFFFFF",
  		"CONTROLS_COLOR" => "000000",
  		"CONTROLS_OVER_COLOR" => "000000",
  		"SCREEN_COLOR" => "000000",
  		"AUTOSTART" => "N",
  		"REPEAT" => "N",
  		"VOLUME" => "90",
  		"DISPLAY_CLICK" => "play",
  		"MUTE" => "N",
  		"HIGH_QUALITY" => "Y",
  		"ADVANCED_MODE_SETTINGS" => "N",
  		"BUFFER_LENGTH" => "10",
  		"DOWNLOAD_LINK_TARGET" => "_self"
  	),
  	$component
  );?>
  <? } else {?>
  	<?=$arProperty["NAME"]?>:
  	<?if(is_array($arProperty["DISPLAY_VALUE"])):?>
  		<?=implode(" / ", $arProperty["DISPLAY_VALUE"]);?>
  	<?else:?>
  		<?=$arProperty["DISPLAY_VALUE"];?>
  	<?endif?>
  <?}?>
  	<br />
  	<?endforeach;?>
  ```

**Примечание**: Здесь следует обратить внимание на следующие моменты:

- Для получения пути к файлу из ID используется системный вызов [CFile::GetPath](http://dev.1c-bitrix.ru/api_help/main/reference/cfile/getpath.php).
- При подключении компонентов указан четвёртый параметр `$component` для того чтобы из публичной части случайно не изменить его параметры (см. класс [CMain::IncludeComponent](http://dev.1c-bitrix.ru/api_help/main/reference/cmain/includecomponent.php)).

#### Решение с помощью result_modifier.php

Если вы хотите, чтобы решение не было похоже на "костыли", необходимо вынести замену свойства в **result_modifier.php**. Тогда шаблон компонента будет стандартный.

- Создайте файл **result_modifier.php** с кодом:
  ```
  <?
  // передадим значение свойства по ссылке:
  $arProperty = &$arResult['DISPLAY_PROPERTIES'][$arParams['PROPERTY_VIDEO']];
  if ($arProperty['DISPLAY_VALUE']) // проверим, установлено ли свойство
  {
  	global $APPLICATION;
  	ob_start(); // включим буферизацию чтобы отловить вывод компонента
  	$APPLICATION->IncludeComponent(
  	"bitrix:player",
  	"",
  	Array(
  		"PLAYER_TYPE" => "auto",
  		"USE_PLAYLIST" => "N",
  		"PATH" => CFile::GetPath($arProperty["VALUE"]),
  		"WIDTH" => "400",
  		"HEIGHT" => "300",
  		"FULLSCREEN" => "Y",
  		"SKIN_PATH" => "/bitrix/components/bitrix/player/mediaplayer/skins",
  		"SKIN" => "bitrix.swf",
  		"CONTROLBAR" => "bottom",
  		"WMODE" => "transparent",
  		"HIDE_MENU" => "N",
  		"SHOW_CONTROLS" => "Y",
  		"SHOW_STOP" => "N",
  		"SHOW_DIGITS" => "Y",
  		"CONTROLS_BGCOLOR" => "FFFFFF",
  		"CONTROLS_COLOR" => "000000",
  		"CONTROLS_OVER_COLOR" => "000000",
  		"SCREEN_COLOR" => "000000",
  		"AUTOSTART" => "N",
  		"REPEAT" => "N",
  		"VOLUME" => "90",
  		"DISPLAY_CLICK" => "play",
  		"MUTE" => "N",
  		"HIGH_QUALITY" => "Y",
  		"ADVANCED_MODE_SETTINGS" => "N",
  		"BUFFER_LENGTH" => "10",
  		"DOWNLOAD_LINK_TARGET" => "_self"
  		)
  	);
  	$arProperty['DISPLAY_VALUE'] = ob_get_contents(); // подменим $arResult
  	ob_clean(); // очистим наш буфер чтобы плеер не появился дважды
  	ob_end_clean(); // закроем буфер
  }
  ?>
  ```
  Символьный код свойства можно сделать параметром компонента, чтобы не привязываться жёстко к конкретному инфоблоку. Для этого нужно доработать файл **.parameters.php** компонента Новость детально, расположенный в скопированном шаблоне компонента.
- Измените код файла **.parameters.php**:
  ```
  <?
  if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();
  $arProps = array();
  $rs=CIBlockProperty::GetList(array(),array("IBLOCK_ID"=>$arCurrentValues['IBLOCK_ID'],"ACTIVE"=>"Y"));
  while($f = $rs->Fetch())
  	$arProps[$f['CODE']] = $f['NAME'];
  $arTemplateParameters = array(
  	"DISPLAY_DATE" => Array(
  		"NAME" => GetMessage("T_IBLOCK_DESC_NEWS_DATE"),
  		"TYPE" => "CHECKBOX",
  		"DEFAULT" => "Y",
  	),
  	"DISPLAY_NAME" => Array(
  		"NAME" => GetMessage("T_IBLOCK_DESC_NEWS_NAME"),
  		"TYPE" => "CHECKBOX",
  		"DEFAULT" => "Y",
  	),
  	"DISPLAY_PICTURE" => Array(
  		"NAME" => GetMessage("T_IBLOCK_DESC_NEWS_PICTURE"),
  		"TYPE" => "CHECKBOX",
  		"DEFAULT" => "Y",
  	),
  	"DISPLAY_PREVIEW_TEXT" => Array(
  		"NAME" => GetMessage("T_IBLOCK_DESC_NEWS_TEXT"),
  		"TYPE" => "CHECKBOX",
  		"DEFAULT" => "Y",
  	),
  	"PROPERTY_VIDEO" => Array(
  		"NAME" => "Свойство, в котором хранится видео",
  		"TYPE" => "LIST",
  		"VALUES" => $arProps
  	),
  );
  ?>
  ```

В результате в настройках параметра появляется новое поле: **Свойство, в котором хранится видео**.



Не забудьте в параметрах подключения компонента указать свойство, в котором хранится видео, иначе оно выводиться не будет.
