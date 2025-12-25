# Структура комплексного компонента

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2818 — Структура компонента](lesson_2818.md)
- [Следующий: 2826 — Размещение в системе и подключение компонента →](lesson_2826.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2749

Комплексный компонент служит для организации целого раздела сайта (форум, каталог и т.п.). Для вывода данных он подключает обычные компоненты. По сути, он является контроллером (менеджером) простых компонентов. Комплексный компонент определяет на основании HTTP запроса страницу, которую требуется вывести посетителю, и подключает шаблон этой страницы.



Пример кода комплексного компонента:



```
<?
if (!defined('B_PROLOG_INCLUDED') || B_PROLOG_INCLUDED !== true) {
    die();
}

$arDefaultUrlTemplates404 = [
	'list'    => 'index.php',
	'element' => '#ELEMENT_ID#.php',
];

$arDefaultVariableAliases404 = [];
$arDefaultVariableAliases    = [];
$arComponentVariables        = ['IBLOCK_ID', 'ELEMENT_ID'];
$SEF_FOLDER                  = '';
$arUrlTemplates              = [];

if ($arParams['SEF_MODE'] == 'Y') {

	$arVariables = [];

	$arUrlTemplates = CComponentEngine::MakeComponentUrlTemplates(
		$arDefaultUrlTemplates404,
		$arParams['SEF_URL_TEMPLATES']
	);

	$arVariableAliases = CComponentEngine::MakeComponentVariableAliases(
		$arDefaultVariableAliases404,
	$arParams['VARIABLE_ALIASES']
	);

	$componentPage = CComponentEngine::ParseComponentPath(
		$arParams['SEF_FOLDER'],
		$arUrlTemplates,
		$arVariables
	);

	if (strlen($componentPage) <= 0) {
		$componentPage = 'list';
	}

	CComponentEngine::InitComponentVariables(
		$componentPage,
		$arComponentVariables,
		$arVariableAliases,
		$arVariables);

	$SEF_FOLDER = $arParams['SEF_FOLDER'];
} else {
	$arVariables = [];

	$arVariableAliases = CComponentEngine::MakeComponentVariableAliases(
		$arDefaultVariableAliases,
		$arParams['VARIABLE_ALIASES']
	);

	CComponentEngine::InitComponentVariables(
		false,
		$arComponentVariables,
		$arVariableAliases,
		$arVariables
	);

	$componentPage = '';

	if (intval($arVariables['ELEMENT_ID']) > 0) {
		$componentPage = 'element';
	} else {
		$componentPage = 'list';
	}

}

$arResult = [
	'FOLDER'        => $SEF_FOLDER,
	'URL_TEMPLATES' => $arUrlTemplates,
	'VARIABLES'     => $arVariables,
	'ALIASES'       => $arVariableAliases,
];

$this->IncludeComponentTemplate($componentPage);

?>
```



В начале кода определяются массивы:

- `$arDefaultUrlTemplates404` - для задания путей по умолчанию для работы в ЧПУ режиме. Каждый элемент массива является шаблоном пути и задается в виде:
  ```
  "код шаблона пути" => "шаблон пути"
  ```
     В шаблоне пути могут быть использованы конструкции вида 	"**#слово#**", которые при формировании реального пути заменяются на значения соответствующих переменных. Например, для шаблона пути:
  ```
  "element" => "#ELEMENT_ID#.php"
  ```
     реальный путь будет иметь вид **195.php** или **7453.php**. Шаблоны путей могут иметь параметры, например:
  ```
  "element" => "#IBLOCK_ID#/#ELEMENT_ID#.php?SECTION_ID=#SECTION_ID#"
  ```
     Должны быть заданы все шаблоны путей, с которыми работает компонент.
- `$arDefaultVariableAliases404` - для задания псевдонимов по умолчанию переменных в режиме ЧПУ. Как правило, этот массив 	пуст (используются реальные имена переменных). В случае, если необходимо, чтобы в HTTP запросе (в адресе) переменная называлась по другому, можно задать псевдоним этой переменной, а при работе компонента восстанавливать значение переменной из псевдонима. Если для какого-либо шаблона пути нужно задать псевдоним для одной или более переменных, то в этом массиве должен появиться элемент вида:
  ```
  "код шаблона пути" => array(
  	"название переменной 1" => "псевдоним переменной 1",
  	"название переменной 2" => "псевдоним переменной 2",
      * * *
      )
  ```
     Например, если требуется, чтобы ссылка на страницу детальной информации об элементе инфоблока (например, карточки товара) имела вид:
  ```
  "/<мнемонический код инфоблока>/.php?SID=<код группы элементов>"
  ```
     то шаблон пути можно задать в виде:
  ```
  "element" => "#IBLOCK_ID#/#ELEMENT_ID#.php?SID=#SECTION_ID#"
  ```
     а в массиве `$arDefaultVariableAliases404` задать псевдоним для переменной 	`SECTION_ID` в виде:
  ```
  "element" => array(
  	"SECTION_ID" => "SID"
  	)
  ```
     В этом случае ссылки (адреса) будут формироваться с параметром 	`SID`, а в компонентах будет установлена переменная `SECTION_ID`.
- `$arDefaultVariableAliases` - для задания псевдонимов по умолчанию переменных в режиме не ЧПУ. Как правило, этот массив 	пуст, то есть используются реальные имена переменных. В случае, если необходимо, чтобы в HTTP запросе (в адресе) переменная называлась по другому, можно задать псевдоним этой переменной, а при работе компонента восстанавливать значение переменной из псевдонима. Если для какой-либо переменной нужно задать псевдоним, то в этом массиве должен появиться элемент вида:
  ```
  "название переменной" => "псевдоним переменной"
  ```
     Например, если название переменной в компоненте `SECTION_ID`, но требуется, чтобы в ссылках использовалась переменная 	`SID`, то псевдоним для `SECTION_ID` можно задать в виде
  ```
  "SECTION_ID" => "SID"
  ```
     В этом случае, ссылки (адреса) будут формироваться с параметром 	`SID`, а в компонентах будет установлена переменная `SECTION_ID`. Все эти массивы или их части могут быть переопределены с помощью входных параметров компонента (при вызове компонента). Например, во входном параметре 	`SEF_URL_TEMPLATES` в ЧПУ режиме может быть задан массив:
  ```
  "SEF_URL_TEMPLATES" => array(
  	"element" => "#IBLOCK_CODE#/#ELEMENT_ID#.php?GID=#SECTION_ID#"
  	)
  ```
     а во входном параметре `VARIABLE_ALIASES` может быть задан параметр:
  ```
  "VARIABLE_ALIASES" => array(
  	"element" => array(
  	"SECTION_ID" => "GID",
  	),
  )
  ```
     Тогда в адресах (ссылках) пути будут иметь вид типа `/phone/3425.php?GID=28`, а в компоненте из них будут восстанавливаться переменные 	`IBLOCK_CODE = phone`, `ELEMENT_ID = 3425` и `SECTION_ID = 28`.
- `$arComponentVariables` - для задания списка переменных, которые компонент может принимать в HTTP запросе и которые могут иметь псевдонимы. Каждый элемент массива является именем переменной.



Входной параметр с предопределённым именем `SEF_MODE` может иметь два значения: `Y`и `N`. Если `$arParams["SEF_MODE"]` равен `Y`, значит компонент работает в режиме ЧПУ, иначе - нет.



Входной параметр с предопределённым именем `SEF_FOLDER` имеет смысл в том случае, если компонент работает в режиме ЧПУ. В этом случае он содержит путь, по которому работает компонент. Путь может быть виртуальным (т.е. физически он может не существовать). Например, компонент из примера может лежать в файле `/fld/n.php`, при этом он работает в режиме ЧПУ и входной параметр `SEF_FOLDER` равен `/company/news/`. Тогда компонент будет откликаться на запросы по адресам `/company/news/index.php, /company/news/25.php` и т.п.



Для определения, какую страницу должен показать комплексный компонент, а так же для восстановления переменных компонента из пути и из псевдонимов используются следующие методы.

- *CComponentEngine::MakeComponentUrlTemplates*
  ```
  CComponentEngine::MakeComponentUrlTemplates(
  	$arDefaultUrlTemplates404,
  	$arParams['SEF_URL_TEMPLATES']
  );
  ```
     Метод объединяет массив по умолчанию шаблонов путей и шаблоны путей, которые были переданы во входных параметрах компонента в один массив. При этом, если в 	`$arParams["SEF_URL_TEMPLATES"]` определён шаблон какого-либо пути, то он переопределяет шаблон 	по умолчанию этого пути.
- *CComponentEngine::MakeComponentVariableAliases*
  ```
  CComponentEngine::MakeComponentVariableAliases(
  	$arDefaultVariableAliases404,
  	$arParams['VARIABLE_ALIASES']
  );
  ```
     Метод объединяет массив по умолчанию псевдонимов переменных и псевдонимы переменных, которые были переданы во входных параметрах компонента в один массив. При этом, если псевдоним некоторой переменной определён и в массиве 	по умолчанию, и во входных параметрах, то возвращается псевдоним из входных параметров.
- *CComponentEngine::ParseComponentPath*
  ```
  CComponentEngine::ParseComponentPath(
  	$arParams['SEF_FOLDER'],
  	$arUrlTemplates,
  	$arVariables
  );
  ```
     Метод на основании параметра `$arParams["SEF_FOLDER"]` и массива шаблонов путей (который вернул метод 	*MakeComponentUrlTemplates*) определяет, какому шаблону пути соответствует запрошенный адрес. Если шаблон был найден, возвращается его код, иначе возвращается пустая строка. Кроме того, в переменной 	`$arVariables` возвращается массив переменных компонента, который был восстановлен из шаблона пути без параметров. Например, если массив шаблонов путей (который получился из массива 	`$arDefaultUrlTemplates404` после переопределения всех или части шаблонов через входные параметры компонента) имеет вид:
  ```
  $arUrlTemplates = array(
  	"list" => "index.php",
  	"element" => "#IBLOCK_ID#/#ELEMENT_ID#.php?SID=#SECTION_ID#"
  );
  ```
     	Если входной параметр `SEF_FOLDER` равен `/company/news/`, а запрошенный адрес равен 	`/company/news/15/7653.php?SID=28`, то метод *ParseComponentPath* вернет строку "`element`" (код соответствующего шаблона), а массив 	`$arVariables` будет иметь вид:
  ```
  $arVariables = array(
  	"IBLOCK_ID" => 15,
  	"ELEMENT_ID" => 7653
  )
  ```
- *CComponentEngine::InitComponentVariables*
  ```
  CComponentEngine::InitComponentVariables(
  	$componentPage,
  	$arComponentVariables,
  	$arVariableAliases,
  	$arVariables
  );
  ```
     где:
  Метод восстанавливает переменные из `$_REQUEST` c учётом их возможных псевдонимов и возвращает их в переменной 	`$arVariables`. Например, если для кода, приведенного выше, в массиве `$arVariableAliases` есть запись вида
  ```
  "element" => array(
  	"SECTION_ID" => "SID",
  )
  ```
     то метод *InitComponentVariables* в параметре `$arVariables` вернет массив вида
  ```
  $arVariables = array(
  	"IBLOCK_ID" => 15,
  	"ELEMENT_ID" => 7653,
  	"SECTION_ID" => 28
  )
  ```
     Здесь методом *InitComponentVariables* был инициализирован третий элемент массива. Первые два были инициализированы методом 	*ParseComponentPath* в примере выше. В случае работы компонента не в режиме ЧПУ, в метод *InitComponentVariables* первым параметром передается значение `False`.

  - `$componentPage` - код шаблона, который вернул метод *ParseComponentPath* и которому соответствует запрошенный адрес;
  - `$arComponentVariables` - массив переменных, которые компонент может принимать в HTTP запросе и которые могут иметь псевдонимы;
  - `$arVariableAliases` - массив псевдонимов (который вернул метод 			*MakeComponentVariableAliases*).



В случае работы компонента в режиме ЧПУ на основании кода шаблона пути и переменных из HTTP запроса (а в случае не-ЧПУ адресов, только на основании переменных из HTTP запроса) компонент определяет, какая страница из шаблона компонента должна подключиться, и передает ее имя в вызов метода:

```
$this->IncludeComponentTemplate($componentPage);
```



На страницах шаблона комплексного компонента подключаются обычные компоненты и настраиваются их входные параметры на основании входных параметров комплексного компонента, некоторых вычисляемых значений и констант. Например, страница "**element**" шаблона компонента из примера (файл типа `/templates/.default/element.php` относительно папки компонента) может иметь вид типа:

```
<?
if (!defined('B_PROLOG_INCLUDED') || B_PROLOG_INCLUDED !== true) {
	die();
}

$APPLICATION->IncludeComponent(
	'bitrix:news.detail',
	'',
	[
		'IBLOCK_ID'  => $arParams['IBLOCK_ID'],
		'ELEMENT_ID' => $arResult['VARIABLES']['ELEMENT_ID'],
		'SECTION_ID' => $arResult['VARIABLES']['SECTION_ID'],
		'CACHE_TIME' => $arParams['CACHE_TIME'],
	],
	$component
);
?>
```

Последний параметр `$component` в подключении компонента — объект, представляющий текущий компонент. Он передается в вызов подключения компонента. Таким образом, подключаемый компонент будет знать, что он подключается из комплексного компонента. Соответственно, он сможет пользоваться ресурсами комплексного компонента, вызывать его методы и т.п.

Получить ссылку на родительский компонент:

```
$this->getParent()
```
