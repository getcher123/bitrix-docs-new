# Пользовательские движки шаблонизации

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3008 — Переопределение входящих переменных](lesson_3008.md)
- [Следующий: 3031 — Разработка верстки шаблона компонента →](lesson_3031.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2822

### Шаблонизация

Компоненты могут работать с любыми движками шаблонизации, которые могут быть подключены из PHP. Чтобы добавить новый движок шаблонизации на сайт необходимо определить (или дополнить) глобальную переменную `$arCustomTemplateEngines` в файле `/bitrix/php_interface/init.php`. В этой переменной содержится ассоциативный массив, каждый элемент которого имеет вид:

```
"код_шаблонизатора" => array(
	"templateExt" => array("расширение1"[, "расширение2"...]),
	"function" => "имя_функции_подключения_движка"
)
```

где:



- `код_шаблонизатора` - произвольное уникальное в рамках сайта слово,
- `расширениеN` - расширение файла, который должен обрабатываться этим движком шаблонизации,
- `имя_функции_подключения_движка` - имя функции, которая будет вызываться, если шаблон компонента имеет указанное расширение. Функцию можно разместить в этом же файле `/bitrix/php_interface/init.php`.

Например, если на сайте кроме стандартного движка шаблонизации (PHP) требуется использовать **Smarty**, то в файл `/bitrix/php_interface/init.php` необходимо добавить следующий код:

```
global $arCustomTemplateEngines;
	$arCustomTemplateEngines = array(
		"smarty" => array(
			"templateExt" => array("tpl"),
			"function" => "SmartyEngine"
		),
);
```

Тогда при подключении шаблона с расширением **tpl** будет запускаться не стандартный движок PHP, а функция *SmartyEngine*, которая должна подключить движок Smarty.

Синтаксис функций подключения движков следующий:

```
   function имя_функции_подключения_движка($templateFile, $arResult, $arParams, $arLangMessages, $templateFolder, $parentTemplateFolder, $template)
```

где:

- `$templateFile` – путь к файлу шаблона относительно корня сайта,
- `$arResult` – массив результатов работы компонента,
- `$arParams` – массив входных параметров компонента,
- `$arLangMessages` – массив языковых сообщений (переводов) шаблона,
- `$templateFolder` – путь к папке шаблона относительно корня сайта (если шаблон лежит не в
  папке, то эта переменная пуста),
- `$parentTemplateFolder` - путь относительно корня сайта к папке шаблона комплексного
  компонента, в составе которого подключается данный компонент (если компонент
  подключается самостоятельно, то эта переменная пуста),
- `$template` – объект шаблона.

Код функции подключения движка шаблонизации зависит от подключаемого движка.

### Подключение Smarty

Полный пример подключения движка **Smarty**

В файл `/bitrix/php_interface/init.php` необходимо добавить код:

```
global $arCustomTemplateEngines;
$arCustomTemplateEngines = array(
	"smarty" => array(
		"templateExt" => array("tpl"),
		"function" => "SmartyEngine"
	)
);

function SmartyEngine($templateFile, $arResult, $arParams, $arLangMessages, $templateFolder, $parentTemplateFolder, $template)
{
	if (!defined("SMARTY_DIR"))
		define("SMARTY_DIR", "<абсолютный путь к движку Smarty>/libs/");

	require_once('<абсолютный путь к движку Smarty>/libs/Smarty.class.php');

	$smarty = new Smarty;

	$smarty->compile_dir = "<абсолютный путь к движку Smarty>/templates_c/";
	$smarty->config_dir = "<абсолютный путь к движку Smarty>/configs/";
	$smarty->template_dir = "<абсолютный путь к движку Smarty>/templates/";
	$smarty->cache_dir = "<абсолютный путь к движку Smarty>/cache/";

	$smarty->compile_check = true;
	$smarty->debugging = false;

	$smarty->assign("arResult", $arResult);
	$smarty->assign("arParams", $arParams);
	$smarty->assign("MESS", $arLangMessages);
	$smarty->assign("templateFolder", $templateFolder);
	$smarty->assign("parentTemplateFolder", $parentTemplateFolder);

	$smarty->display($_SERVER["DOCUMENT_ROOT"].$templateFile);
}
```

Строку `<абсолютный путь к движку Smarty>` нужно везде заменить на абсолютный путь к движку Smarty в рамках вашей установки. Подробности по установке движка на сайт есть в системе помощи по Smarty.

В примере кода в массиве `$arCustomTemplateEngines` регистрируется движок Smarty. В функции **SmartyEngine** инициализируются параметры движка в соответствии с требованиями системы (см. документацию [Smarty](http://www.smarty.net/documentation)). Далее в Smarty передаются переменные результатов работы компонента, входных параметров, языковых сообщений и т.д. И в конце вызывается метод обработки и показа шаблона Smarty.

### Подключение XML/XSLT

Полный пример подключения движка XML/XSLT

В файл `/bitrix/php_interface/init.php` необходимо добавить код:

```
global $arCustomTemplateEngines;
$arCustomTemplateEngines = array(
	"xslt" => array(
		"templateExt" => array("xsl"),
		"function" => "XSLTEngine"
	),
);

function CreateXMLFromArray($xDoc, $xNode, $ar)
{
	foreach($ar as $key=>$val)
	{
		if(!is_string($key) || strlen($key)<=0)
			$key = "value";

	$xElement = $xDoc->createElement($key);
	if(is_array($val))
	{
		CreateXMLFromArray($xDoc, $xElement, $val);
	}
	else
	{
		$xElement->appendChild($xDoc->createTextNode(iconv(SITE_CHARSET, "utf-8", $val)));
	}
	$xNode->appendChild($xElement);
	}
	return $xNode;
}

function XSLTEngine($templateFile, $arResult, $arParams, $arLangMessages, $templateFolder, $parentTemplateFolder, $template)
{
	$arResult["PARAMS"] = array(
		"templateFolder" => $templateFolder,
		"parentTemplateFolder" => $parentTemplateFolder,
		"arParams" => $arParams,
		"arLangMessages" => $arLangMessages
	);

	$xDoc = new DOMDocument("1.0", SITE_CHARSET);
	$xRoot = $xDoc->createElement('result');
	CreateXMLFromArray($xDoc, $xRoot, $arResult);
	$xDoc->appendChild($xRoot);

	$xXsl = new DOMDocument();
	$xXsl->load($_SERVER["DOCUMENT_ROOT"].$templateFile);

	$xProc = new XSLTProcessor;
	$xProc->importStyleSheet($xXsl);

	echo $xProc->transformToXML($xDoc);
}
```
