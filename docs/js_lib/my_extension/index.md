# Регистрация своих расширений


### Описание и параметры


```
CJSCore::RegisterExt(
	"my_extension",
	array(
		"js" => "/path/to/js/my_ext.js",
		"css" => "/path/to/css/my_ext.css",
		"lang" => "/path/to/lang/".LANGUAGE_ID. "/lang.php",
		"rel" => Array("ajax", "popup", "ls"),
		"skip_core" => false | true,
	)
);
```

Функция регистрирует собственные расширения.


#### Параметры функции


| Параметр | Описание |
| --- | --- |
| my_extension | имя расширения |
| Array | Массив параметров расширения: - **js** - Путь до файла расширения; - **css** - Путь до файла css расширения; - **lang** - Путь до языкового файла расширения; - **rel** - Список "зависимостей". При подключении собственного расширения зависимости будут подключены автоматически. - **skip_core** - При подключении расширения не требуется подключение **core.js**. |

---
### Примеры использования


```
<?
require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
$APPLICATION->SetTitle("Свои расширения");

	CJSCore::RegisterExt("db_js_demo", Array(
		"js" =>    "/script_demo.js",
		"lang" =>   "/lang_js.php",
		"rel" =>   array('jquery')
	));
	CJSCore::Init(array("db_js_demo"));
?>
<div id="hideBlock" style="display:none;">
	<h1>Hello</h1>
	<p>text</p>
</div>
<script>
	window.BXDEBUG = true;
BX.ready(function(){
	BX.PREFIXName('HELLO');
	//BX.PREFIXName.testJQ('#demo');
});
</script>
<p id="demo">click Me</p>
<?require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");?>
```

---




| ![image](../images/7dd82aba60.gif) 4 **Евгений Семашко**05.11.2015 19:51:14 |
| --- |
| Можно передать в качестве параметра также ключ "use" с возможными значениями CJSCore::USE_PUBLIC CJSCore::USE_ADMIN для подключения ТОЛЬКО в админке и ТОЛЬКО в публичке соответственно. |
|  |


| ![](../images/6335e722d9.jpg) 10 **Алексей Шкарупа**14.08.2013 09:21:37 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Не используйте в названиях своих библиотек символы не подходящие под регулярное выражение /[^a-z0-9_]/i (например дефис). \| Код \| \| --- \| \| ``` CJSCore::RegisterExt('mylib-any', array( 'js' => 'any.js' )); var_dump(CJSCore::IsExtRegistered('mylib-any')); В результате будет выведено false ``` \| Функция RegisterExt добавляет библиотеку с тем именем которое ей передали. А все функции которые используется внутри CJSCore::Init проводят обработку имени библиотеки с помощью регулярного выражения /[^a-z0-9_]/i *************************** Комментарий от разработчика: \| Цитата \| \| --- \| \| mylib-any является не валидным именем \| | Код | ``` CJSCore::RegisterExt('mylib-any', array( 'js' => 'any.js' )); var_dump(CJSCore::IsExtRegistered('mylib-any')); В результате будет выведено false ``` | Цитата | mylib-any является не валидным именем |
| Код |  |  |  |  |
| ``` CJSCore::RegisterExt('mylib-any', array( 'js' => 'any.js' )); var_dump(CJSCore::IsExtRegistered('mylib-any')); В результате будет выведено false ``` |  |  |  |  |
| Цитата |  |  |  |  |
| mylib-any является не валидным именем |  |  |  |  |
|  |  |  |  |  |
