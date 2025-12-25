# Компонент интеграции визуального редактора

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2894 — Пример создания компонента](lesson_2894.md)
- [Следующий: 3053 — Кеширование в собственных компонентах →](lesson_3053.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2813

Создадим компонент, интегрирующий популярный редактор *TinyMCE* в *Bitrix Framework*.

Загрузите [свежую версию](https://www.tiny.cloud/) редактора с сайта производителя.

В своем пространстве имен в папке `/local` создайте структуру папок и файлов:

- `/bitrix/components/tools/`;

  - `/bitrix/components/tools/editor.tiny.mce/`;

    - `/bitrix/components/tools/editor.tiny.mce/templates/`;

      - `/bitrix/components/tools/editor.tiny.mce/templates/.default/`;
    - `/bitrix/components/tools/editor.tiny.mce/tiny_mce/` - папка для дистрибутива редактора;
    - **component.php** — логика компонента;
    - **.parameters.php** — файл для описания входящих параметров.

Скопируйте скаченный дистрибутив в папку `/tiny_mce`.

В файл **component.php** добавляем код:



```

<? if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();
	$APPLICATION->AddHeadScript($this->__path .'/tiny_mce/tiny_mce.js');

	$sNameTextArea   =  (isset($arParams['TEXTAREA_NAME'])   == false) ? 'content'   : $arParams['TEXTAREA_NAME'];
	$sIdTextArea   	 =  (isset($arParams['TEXTAREA_ID'])     == false) ? '' 		 : $arParams['TEXTAREA_ID'];
		if ('' == trim($sIdTextArea))
		$sIdTextArea = 'content';
	$sEditorID 		 =  (isset($arParams['INIT_ID'])  	     == false) ? 'textareas' : $arParams['INIT_ID'];
	$iTextareaWidth  =  (isset($arParams['TEXTAREA_WIDTH'])  == false) ? '100%'      : $arParams['TEXTAREA_WIDTH'];
	$iTextareaHeight =  (isset($arParams['TEXTAREA_HEIGHT']) == false) ? '300'       : $arParams['TEXTAREA_HEIGHT'];
	$sText 			 =  (isset($arParams['TEXT']) 			 == false) ? ''       	 : $arParams['TEXT'];
	?>

<script type="text/javascript">

<?
if ($arParams['TYPE_EDITOR'] == 'TYPE_1')
{
	?>
	tinyMCE.init(
		{
			language : 'ru',
			mode 	 : "textareas",
			//elements : "<?=$sEditorID?>",
			editor_selector : "<?=$sEditorID?>",
			theme    : "advanced",
			plugins  : "safari, spellchecker, upload.images.komka, wordcount, fullscreen",
			theme_advanced_buttons1 : "formatselect,fontselect,fontsizeselect,bold,italic,underline,link,justifyleft,justifycenter,
                                       justifyright,pasteword,pastetext,images,|,bullist,numlist,|,undo,redo,|,spellchecker,fullscreen",
			theme_advanced_buttons2 : "",
			theme_advanced_buttons3 : "",
			theme_advanced_toolbar_location   : "top",
			theme_advanced_toolbar_align      : "left",
			theme_advanced_statusbar_location : "bottom",
			theme_advanced_resizing           : false,
			content_css                       : "<?=$this->__path?>/example.css",
			height : "<?=$iTextareaHeight?>",
			spellchecker_languages : '+Русский=ru,English=en',
			spellchecker_word_separator_chars : '\\s!\"#$%&()*+,-./:;<=>?@[\]^_{|}'
		}
	);
	<?
}
elseif($arParams['TYPE_EDITOR'] == 'TYPE_2')
{
	?>
		tinyMCE.init({
				language : 'ru',
				mode 	 : "textareas",
				editor_selector : "<?=$sEditorID?>",
				theme    : "advanced",
				plugins : "safari,spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,imagemanager,filemanager",
				theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
				theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
				theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
				theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",
				theme_advanced_toolbar_location : "top",
				theme_advanced_toolbar_align : "left",
				theme_advanced_statusbar_location : "bottom",
				theme_advanced_resizing : true,
				content_css : "<?=$this->__path?>/example.css",
				height : "<?=$iTextareaHeight?>",
				template_external_list_url : "js/template_list.js",
				external_link_list_url : "js/link_list.js",
				external_image_list_url : "js/image_list.js",
				media_external_list_url : "js/media_list.js",
				template_replace_values : {username : "Some User", staffid : "991234"}
			}
		);
	<?
}
?>

</script>
<textarea id="<?=$sIdTextArea?>" class="<?=$sEditorID?>"  name="<?=$sNameTextArea?>" style="width:<?=$iTextareaWidth?>"><?=$sText?></textarea>
<? $this->IncludeComponentTemplate();?>
```

Файл **.parameters.php**

```

<? if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

$arComponentParameters = array(
	"PARAMETERS" => array(
		"TYPE_EDITOR" => Array(
			"PARENT" => "SETTINGS",
			"NAME" => "Режим редактора",
			"TYPE" => "LIST",
			"VALUES" => array('TYPE_1' => 'Упрощенные редактор', 'TYPE_2' => 'Полной редактор'),
		),

		'INIT_ID' => array(
			"PARENT" => "SETTINGS",
			"NAME" => "ID редатора (уникальный)",
			"TYPE" => "STRING",
			"DEFAULT" => '',
		),

		'TEXT' => array(
			"PARENT" => "SETTINGS",
			"NAME" => "Контент который нужно вставить в редактор",
			"TYPE" => "STRING",
			"DEFAULT" => $_POST['content'],
		),

		'TEXTAREA_NAME' => array(
			"PARENT" => "SETTINGS",
			"NAME" => "Имя поля TEXTAREA",
			"TYPE" => "STRING",
			"DEFAULT" => 'content',
		),

		'TEXTAREA_ID' => array(
			"PARENT" => "SETTINGS",
			"NAME" => "ID поля TEXTAREA",
			"TYPE" => "STRING",
			"DEFAULT" => 'content',
		),

		'TEXTAREA_WIDTH' => array(
			"PARENT" => "SETTINGS",
			"NAME" => "Ширина редактора",
			"TYPE" => "STRING",
			"DEFAULT" => '100%',
		),

		'TEXTAREA_HEIGHT' => array(
			"PARENT" => "SETTINGS",
			"NAME" => "Высота редактора",
			"TYPE" => "STRING",
			"DEFAULT" => '300',
		),
	)
);
?>
```

Важные моменты в коде файла **component.php**, которые надо пояснить. Подключение собственно редактора:

```
<?  $APPLICATION->AddHeadScript($this->__path .’/tiny_mce/tiny_mce.js’); ?>
```

Подключение стилей, которые вынесены в папку с компонентом чтобы было удобнее, это настройка уже в js, в коде инициализации:

```
content_css : ‘<?=$this->__path?>/example.css’,
```

**Внимание!** если на странице 2 или более редакторов, то мы идентифицируем их по имени класса editor_selector : `‘<?=$sEditorID?>’`.

Собственно сама область текста для которой это все и делается:

```
<textarea id=’<?=$sIdTextArea?>’  name=’<?=$sNameTextArea?>’ style=’width:<?=$iTextareaWidth?>’><?=$sText?></textarea>
```

#### Как использовать

Подключается вот в таком виде:

```
<? echo $_POST['content'] ?>
<? echo $_POST['content2'] ?>
<form action="" method="post" name="">
<? $APPLICATION->IncludeComponent("tools:editor.tiny.mce", ".default", array(
	"TEXT" => $_POST["content"], // контент из запроса который нужно вставить
	"TEXTAREA_NAME" => "content", // имя поля
	"TEXTAREA_ID" => "content",         // id поля
	"TEXTAREA_WIDTH" => "100%",  // ширина
	"TEXTAREA_HEIGHT" => "300",    // высота
	"INIT_ID" => "ID" // ID самого редактора
),
false
);
?>
<input value="submit" name="sub" type="submit" />
</form>
```
