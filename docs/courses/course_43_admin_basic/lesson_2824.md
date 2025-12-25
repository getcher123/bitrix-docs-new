# Описание и параметры

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2823 — Структура файлов](lesson_2823.md)
- [Следующий: 3491 — Административные скрипты →](lesson_3491.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2824

### Описание

Каждый модуль должен быть корректно описан в системе для того, чтобы система знала, как с этим модулем работать. Некорректно описанные модули могут привести к полной или частичной неработоспособности системы (например, может не работать система обновлений).

Основным файлом, используемым системой для манипуляции модулем, является `/bitrix/modules/ID модуля/install/index.php`. (ID модуля в этом случае - это полный код партнерского модуля, который задается в формате: **код_партнера.код_модуля**.) Основное назначение этого файла - это размещение в нем класса с именем, совпадающим с **ID модуля**. (ID модуля здесь используется в формате **код_партнера_код_модуля**, так как в имени класса точка недопустима.)

Пример:

```

01 <?
02 	Class mymodule extends CModule
03 	{
04 		var $MODULE_ID = "mymodule";
05 		var $MODULE_NAME;
06
07 		function DoInstall()
08 		{
09 		global $DB, $APPLICATION, $step;
10 		$APPLICATION->IncludeAdminFile(GetMessage("FORM_INSTALL_TITLE"), $_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/mymodule/install/step1.php");
11 		}
12
13 		function DoUninstall()
14 		{
15 		global $DB, $APPLICATION, $step;
16 		$APPLICATION->IncludeAdminFile(GetMessage("FORM_INSTALL_TITLE"), $_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/mymodule/install/unstep1.php");
17
18 		}
19 	}
20 ?>
```

Обязательные методы этого класса:

- `DoInstall` - запускается при нажатии кнопки **Установить** на странице **Модули** административного раздела, осуществляет инсталляцию модуля.
  	`DoUninstall` - запускается при нажатии кнопки **Удалить** на странице **Модули** административного раздела, осуществляет деинсталляцию модуля.

Необязательный метод этого класса:

- [GetModuleRightList](http://dev.1c-bitrix.ru/api_help/main/reference/cmodule/getmodulerightlist.php) - возвращает список уникальных прав (или ролей) модуля.

Обязательные свойства объекта этого класса:

- `MODULE_ID` - хранит **ID модуля** (полный код партнерского модуля);
  	`MODULE_VERSION` - текущая версия модуля в формате XX.XX.XX;
  	`MODULE_VERSION_DATE` - строка содержащая дату версии модуля; дата должна быть задана в формате YYYY-MM-DD HH:MI:SS;
  	`MODULE_NAME` - имя модуля;
  	`MODULE_DESCRIPTION` - описание модуля;
  	`MODULE_GROUP_RIGHTS` - если задан метод *GetModuleRightList*, то данное свойство должно содержать `Y`.

#### Примеры

Пример файла с описанием модуля **Веб-формы**:

```
<?
global $MESS;
$PathInstall = str_replace("\\", "/", __FILE__);
$PathInstall = substr($PathInstall, 0, strlen($PathInstall)-strlen("/index.php"));
IncludeModuleLangFile($PathInstall."/install.php");
include($PathInstall."/version.php");
if(class_exists("form")) return;
Class form extends CModule
{
	var $MODULE_ID = "form";
	var $MODULE_VERSION;
	var $MODULE_VERSION_DATE;
	var $MODULE_NAME;
	var $MODULE_DESCRIPTION;
	var $MODULE_GROUP_RIGHTS = "Y";

	function __construct()
	{
		$this->MODULE_VERSION = FORM_VERSION;
		$this->MODULE_VERSION_DATE = FORM_VERSION_DATE;
		$this->MODULE_NAME = GetMessage("FORM_MODULE_NAME");
		$this->MODULE_DESCRIPTION = GetMessage("FORM_MODULE_DESCRIPTION");
	}

	function DoInstall()
	{
		global  $APPLICATION;
		$FORM_RIGHT = $APPLICATION->GetGroupRight("form");
		if ($FORM_RIGHT=="W")
		{
		$step = IntVal($step);
		if($step<2)
			$APPLICATION->IncludeAdminFile(GetMessage("FORM_INSTALL_TITLE"),
			$_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/form/install/step1.php");
		elseif($step==2)
			$APPLICATION->IncludeAdminFile(GetMessage("FORM_INSTALL_TITLE"),
			$_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/form/install/step2.php");
		}
	}

	function DoUninstall()
	{
		global $APPLICATION;
		$FORM_RIGHT = $APPLICATION->GetGroupRight("form");
		if ($FORM_RIGHT=="W")
		{
			$step = IntVal($step);
			if($step<2)
			$APPLICATION->IncludeAdminFile(GetMessage("FORM_UNINSTALL_TITLE"),
			$_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/form/install/unstep1.php");
			elseif($step==2)
			$APPLICATION->IncludeAdminFile(GetMessage("FORM_UNINSTALL_TITLE"),
			$_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/form/install/unstep2.php");
		}
	}

	function GetModuleRightList()
	{
		global $MESS;
		$arr = array(
			"reference_id" => array("D","R","W"),
			"reference" => array(
				GetMessage("FORM_DENIED"),
				GetMessage("FORM_OPENED"),
				GetMessage("FORM_FULL"))
			);
		return $arr;
	}
}
?>
```

Пример файла с указанием версии модуля

```
<?
$arModuleVersion = array(
	"VERSION" => "11.0.4",
	"VERSION_DATE" => "2011-11-17 14:00:00"
);
?>
```

### Параметры

**Параметры модуля** доступны для изменения в административном интерфейсе на странице **Настройки модулей** (Настройки &gt; Настройки продукта &gt; Настройки модулей). При выборе модуля на данной странице, система подключает файл `/bitrix/modules/my_module_id/options.php`, предназначенный для управления параметрами модуля, назначения прав на модуль и т.п.

Параметры модуля хранятся в базе данных.

При получении параметров модуля, может использоваться значение по умолчанию, задаваемое в файле `/bitrix/modules/my_module_id/default_option.php`. В данном файле определяется массив `my_module_id_default_option`, хранящий значения по умолчанию.

Пример файла `/bitrix/modules/my_module_id/default_option.php`:

```
<?
/*
* Файл local/modules/my_module_id/default_option.php
*/
$my_module_id_default_option = array(
	"MY_PARAMETER_ID"  =>  "DEFAULT_VALUE"
	);
?>
```

Для работы с параметрами модуля предназначен класс [COption](http://dev.1c-bitrix.ru/api_help/main/reference/coption/index.php). Методы класса:

- [SetOptionString](http://dev.1c-bitrix.ru/api_help/main/reference/coption/setoptionstring.php) - установка строковых параметров
- [SetOptionInt](http://dev.1c-bitrix.ru/api_help/main/reference/coption/setoptionint.php) - установка числовых параметров
- [GetOptionString](http://dev.1c-bitrix.ru/api_help/main/reference/coption/getoptionstring.php) - получение строковых параметров
- [GetOptionInt](http://dev.1c-bitrix.ru/api_help/main/reference/coption/getoptionint.php) - получение числовых параметров
- [RemoveOption](http://dev.1c-bitrix.ru/api_help/main/reference/coption/removeoption.php) - удаление параметра

#### Примеры использования

Строковый параметр

```
<?
// установим строковый параметр
COption::SetOptionString("my_module_id", "MY_PARAMETER_ID", "VALUE");

// получим строковый параметр
$value = COption::GetOptionString("my_module_id", "MY_PARAMETER_ID", "DEFAULT_VALUE");
?>
```

**Примечание**: При использовании файла **default_option.php**, заданные в нем значения параметров по умолчанию, не нужно передавать третьим аргументом *def* при вызове метода [GetOptionString](http://dev.1c-bitrix.ru/api_help/main/reference/coption/getoptionstring.php).

Названия параметров, должны быть идентичными в файле **default_option.php** и в методах класса COption.

Параметр типа файл. (Загрузка файла в модуле)

```
<table>
<tr> <td width="40%">
	<?
	$path_file = COption::GetOptionString("my_module_id", 'CLEVERSCRIPT_IMG_DESCTOP_BTN');
	CAdminFileDialog::ShowScript
	(
		Array(
			"event" => "BtnClick_0",
			"arResultDest" => array("FORM_NAME" => "cleverscriptwantcheaper", "FORM_ELEMENT_NAME" => "CLEVERSCRIPT_IMG_DESCTOP_BTN"),
			"arPath" => array("PATH" => GetDirPath($path_file)),
			"select" => 'F',// F - file only, D - folder only
			"operation" => 'S',// O - open, S - save
			"showUploadTab" => true,
			"showAddToMenuTab" => false,
			"fileFilter" => 'jpg,jpeg,gif,png',
			"allowAllFiles" => true,
			"SaveConfig" => true,
		)
	);
	?>
	<?echo Loc::getMessage("T_CLEVERSCRIPT_IMG_DESCTOP_BTN")?>
</td>
	<td width="60%">
		<input type="text" name="CLEVERSCRIPT_IMG_DESCTOP_BTN" size="50" maxlength="255" value="<?echo $path_file?>"> <input type="button" name="browse_0" value="..." onClick="BtnClick_0()">
   </td>
</tr>
</table>

```

### Дополнительно

- [Option](https://dev.1c-bitrix.ru/api_d7/bitrix/main/config/option/index.php) - класс для работы с параметрами модулей, хранимых в базе данных. Аналог класса COption в старом ядре.
