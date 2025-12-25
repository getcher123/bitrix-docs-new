# Общий алгоритм

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3470 — Составные действия](lesson_3470.md)
- [Следующий: 2903 — Пример создания действия Запись в лог →](lesson_2903.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=23034

|  | ### Общий алгоритм создания действия |
| --- | --- |




Пользовательские действия создаются в папке `/bitrix/activities/custom` относительно корня сайта. Каждое действие располагается в отдельной папке. Название папки должно совпадать с именем класса действия, но без первых символов "CBP". Кроме того, имя папки должно быть записано строчными буквами (в нижнем регистре).




В папке действия должен располагаться файл класса действия. Название этого файла должно совпадать с названием папки действия и иметь расширение **php**. Кроме того, в папке действия могут располагаться другие необходимые действию файлы. Например, файл с описанием, файлы с локализацией, изображения, файлы с ресурсами и т.п.





Файл с описанием действия располагается в папке действия и имеет имя **.description.php**. В этом файле содержится описание, которое необходимо для корректной работы системы. В **.description.php** должен содержаться код типа:




```
<?if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

$arActivityDescription = array(
	"NAME" => GetMessage("MYACTIVITY_DESCR_NAME"),
	"DESCRIPTION" => GetMessage("MYACTIVITY_DESCR_DESCR"),
	"TYPE" => "activity",
	"CLASS" => "MyActivity",
	"JSCLASS" => "BizProcActivity",
	"CATEGORY" => array(
		"ID" => "other",
	),
);
?>
```




C версии 17.0.3 модуля **Бизнес-процессы** появилась возможность при создании своего действия передавать результат его работы в другие действия во время выполнения бизнес-процесса.
Для этого нужно в файле описания действия **.description.php** добавить

			строку

                    Как реализована работа с дополнительными результатами можно посмотреть в файлах активити «Выбор данных CRM» по пути /bitrix/activities/bitrix/crmgetdataentityactivity в файловой структуре.

		 вида :


```

<?
'ADDITIONAL_RESULT' => array('EntityFields')
?>
```





Значения вложенного массива – это ключ, по которому можно получить данные из свойств шаблона.
Когда созданное действие отрабатывает, оно записывает данные в свойства шаблона, а затем в других действиях эти данные можно вставить с помощью формы Вставки значения , из раздела **Дополнительные результаты**.




Здесь определен тип действия в элементе `TYPE`, который имеет два возможных значения: **activity** для действий и **condition** для условий. Кроме того, задаются название и описание, Java-скриптовый класс для отрисовки в визуальном редакторе, категория и т.п.




В подпапке `/lang` папки действия располагаются файлы с локализацией фраз на различные языки.




Файл с классом действия имеет вид типа:




```

<?if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

class CBPMyActivity
	extends CBPActivity
{
	public function __construct($name)
	{
		parent::__construct($name);
		// Определим свойство действия MyText
		// Оно может быть задано в визуальном редакторе при
 		// помещении действия в шаблон бизнес-процесса
		$this->arProperties = array("Title" => "", "MyText" => "");
	}

	// Исполняющийся метод действия
	public function Execute()
	{
		// Суть действия – запись значения свойства в файл
		if (strlen($this->MyText) > 0)
		{
			$f = fopen($_SERVER["DOCUMENT_ROOT"]."/dump.txt", "a");
			fwrite($f, $this->MyText);
			fclose($f);
		}

		// Возвратим исполняющей системе указание, что действие завершено
		return CBPActivityExecutionStatus::Closed;
	}

	// Статический метод возвращает HTML-код диалога настройки
// свойств действия в визуальном редакторе. Если действие не имеет
// свойств, то этот метод не нужен
	public static function GetPropertiesDialog($documentType, $activityName,
 		$arWorkflowTemplate,$arWorkflowParameters, $arWorkflowVariables,
 		$arCurrentValues = null, $formName = "")
	{
		$runtime = CBPRuntime::GetRuntime();

		if (!is_array($arWorkflowParameters))
			$arWorkflowParameters = array();
		if (!is_array($arWorkflowVariables))
			$arWorkflowVariables = array();

		// Если диалог открывается первый раз, то подгружаем значение
 	// свойства, которое было сохранено в шаблоне бизнес-процесса
		if (!is_array($arCurrentValues))
		{
			$arCurrentValues = array("my_text" => "");

			$arCurrentActivity= &CBPWorkflowTemplateLoader::FindActivityByName(
 				$arWorkflowTemplate,
 				$activityName
 		);
			if (is_array($arCurrentActivity["Properties"]))
				$arCurrentValues["my_text "] =
 $arCurrentActivity["Properties"]["MyText"];
		}

		// Код, формирующий диалог, расположен в отдельном файле
		// properties_dialog.php в папке действия.
		// Возвращаем этот код.
		return $runtime->ExecuteResourceFile(
			__FILE__,
			"properties_dialog.php",
			array(
				"arCurrentValues" => $arCurrentValues,
				"formName" => $formName,
			)
		);
	}

	// Статический метод получает введенные в диалоге настройки свойств
// значения и сохраняет их в шаблоне бизнес-процесса. Если действие не
// имеет свойств, то этот метод не нужен.
	public static function GetPropertiesDialogValues($documentType, $activityName,
		&$arWorkflowTemplate, &$arWorkflowParameters, &$arWorkflowVariables,
 	 	$arCurrentValues, &$arErrors)
	{
		$arErrors = array();

		$runtime = CBPRuntime::GetRuntime();

		if (strlen($arCurrentValues["my_text "]) <= 0)
		{
			$arErrors[] = array(
				"code" => "emptyCode",
				"message" => GetMessage("MYACTIVITY_EMPTY_TEXT"),
			);
			return false;
		}

		$arProperties = array("MyText" => $arCurrentValues["my_text "]);

		$arCurrentActivity = &CBPWorkflowTemplateLoader::FindActivityByName(
 			$arWorkflowTemplate,
 			$activityName
 		);
		$arCurrentActivity["Properties"] = $arProperties;

		return true;
	}
}
?>
```




Код в файле **properties_dialog.php**, формирующий диалог настройки свойств действия в визуальном редакторе, может выглядеть примерно так:




```

<?if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
?>
<tr>
	<td align="right" width="40%"><span style="color:#FF0000;">*</span> :</td>
	<td width="60%">
		<textarea name="my_text" id="id_my_text " rows="5" cols="40"><?= htmlspecialchars($arCurrentValues["my_text"]) ?></textarea>
		<input type="button" value="..." onclick="BPAShowSelector('id_my_text', 'string');">
	</td>
</tr>
```




Пользователь может ввести в поле `my_text` явное значение или выбрать одно из значений с помощью диалога, открывающегося по кнопке ![](../../../images/courses/57/dev.1c-bitrix.ru/images/dev_start/bitrix_framework/browse.png). Во втором случае пользователь может установить, что значением свойства будет являться значение свойства корневого действия, которое задается как входящий параметр при запуске бизнес-процесса.
