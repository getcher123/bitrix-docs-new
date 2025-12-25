# Ответ на вопрос

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5315 — Сообщение об успешном создании](lesson_5315.md)
- [Следующий: 4799 — Модерация блогов →](lesson_4799.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=5316

Интерфейс страницы Дать ответ (**answer.php**) создается с помощью компонента **Редактирование результата**. Однако стандартный компонент для наших целей не подходит, поскольку нам необходимо вносить изменения только в поле **Ответ**. Поэтому нам необходимо скопировать полностью компонент в

			собственное пространство имен

                    О размещении компонентов в собственном пространстве имен смотрите в учебном курсе [Разработчик Bitrix Framework](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2826).

		, чтобы отредактировать и код компонента, и шаблон компонента под наши нужды.




### Копирование и размещение компонента




Создадим папку **demo** в `/bitrix/components/`. Выполним

			копирование компонента


Чтобы кастомизировать стандартный компонент, необходимо:

1) Создать новое пространство имён компонентов в папке `/local/components/`,
 например создать директорию `/local/components/my_components/`.

2) В созданную папку необходимо скопировать папку с компонентом,
 который хотите изменить (копировать из папки `/bitrix/components/bitrix/`).

3) Изменить компонент под текущие задачи.

4) Отредактировать шаблон компонента под текущие задачи.

5) Очистите кеш визуального редактора. В результате в визуальном редакторе
 отобразится кастомизированный компонент.

[Подробнее](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=04779&LESSON_PATH=3913.4565.4790.4779)...

		 **Редактирование результата** (form.result.edit) из папки `/bitrix/components/bitrix/` в пространство **demo**, т.е. папка компонента `/form.result.edit` будет располагаться в папке `/bitrix/components/demo`.




Теперь откроем на редактирование страницу **answer.php** в визуальном редакторе и

			разместим скопированный компонент

                    Если компонент не отобразится в дереве компонентов после копирования, то необходимо [очистить закешированные данные](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2164)

		 **Редактирование результата** (**demo:

			form.result.edit

                    Компонент служит для редактирования результатов заполнения веб-форм.




						[Описание компонента «Редактирование результата» в пользовательской документации.](http://dev.1c-bitrix.ru/user_help/detail.php?ID=63060)**):



![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/form_result_edit_new.png)




Настраиваем компонент следующим образом:




- В поле **ID результата** оставляем код `={$_REQUEST[RESULT_ID]}`, предложенный по умолчанию.
- В поле **Выводить на редактирование дополнительные поля** обязательно указываем `Да`.
- В обоих параметрах **Страница со списком результатов** и **Страница просмотра результата** указываем `index.php`, чтобы со страницы составления ответа осуществлялся переход только на главную страницу системы **Вопрос-ответ**.
- Параметры **Игнорировать свой шаблон** и **Выводить форму смены статуса** можно не настраивать, поскольку они не будут использоваться в компоненте и мы их потом удалим за ненадобностью.



Сохраняем компонент и переходим к редактированию файла параметров компонента `/bitrix/components/demo/form.result.edit/.parameters.php`.





### Редактирование параметров компонента




В форме добавления ответа на вопрос не будет поля для смены статуса. При нажатии на кнопку **Отправить**, расположенной на форме, статус будет автоматически меняться на **Ответ**. Поэтому в параметры компонента необходимо добавить возможность указания этого статуса (чтобы компонент "знал", с каким статусом работать). В связи с этим в файле `/bitrix/components/demo/form.result.edit/.parameters.php` перед строкой:

```

$arComponentParameters = array(...
```




добавляем код формирования списка веб-форм сайта и списка статусов веб-формы, зависящего от выбранной впоследствии в параметрах компонента веб-формы:




```

$arrForms = array();
$rsForm = CForm::GetList($by='s_sort', $order='asc', array("SITE" => $_REQUEST["site"]), $v3);
while ($arForm = $rsForm->Fetch())
{
	$arrForms[$arForm["ID"]] = "[".$arForm["ID"]."] ".$arForm["NAME"];
}

$arrStatuses = array();
$rsStat = CFormStatus::GetList($arCurrentValues["WEB_FORM_ID"], $by='s_sort', $order='asc');
while ($arStatus = $rsStat->Fetch())
{
	$arrStatuses[$arStatus["ID"]] = "[".$arStatus["ID"]."] ".$arStatus["TITLE"];
}
```





Находим массив `PARAMETERS` и добавляем в него код

			после массива **RESULT_ID**

                    ![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/edit_parameters.png)

		 для отображения параметров выбора веб-формы и статуса :




```

		"WEB_FORM_ID" => array(
			"NAME" => GetMessage("COMP_FORM_PARAMS_WEB_FORM_ID"),
			"TYPE" => "LIST",
			"VALUES" => $arrForms,
			"ADDITIONAL_VALUES" => "Y",
			"DEFAULT" => "={\$_REQUEST[WEB_FORM_ID]}",
			"PARENT" => "DATA_SOURCE",
			"REFRESH" => "Y",
		),
		"STATUS_ID" => array(
			"NAME" => GetMessage("COMP_FORM_PARAMS_STATUS_ID"),
			"TYPE" => "LIST",
			"VALUES" => $arrStatuses,
			"DEFAULT" => '',
			"PARENT" => "DATA_SOURCE",
		),
```




Для новых параметров `COMP_FORM_PARAMS_WEB_FORM_ID` и `COMP_FORM_PARAMS_STATUS_ID` задаем языковые сообщения в файле `/bitrix/components/demo/form.result.edit/lang/ru/.parameters.php`:




```

$MESS ['COMP_FORM_PARAMS_WEB_FORM_ID'] = "ID веб-формы системы \"Вопрос-ответ\"(используется только для проверки)";
$MESS ['COMP_FORM_PARAMS_STATUS_ID'] = "ID статуса, когда дан ответ на вопрос";
```




Теперь параметры компонента полностью готовы под наши нужды. Форма настройки параметров компонента приобретает следующий вид:



![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/form_result_edit_params.png)




В настройках компонента указываем нашу веб-форму **Вопрос-ответ** и статус **Ответ**.




Переходим к изменению логики компонента, т.е к редактированию файла `/bitrix/components/demo/form.result.edit/component.php`.





### Изменение логики компонента




Необходимо сформировать массив данных компонента так, чтобы только в поле ответа можно было вносить данные, а сами вопросы формы не были доступны для редактирования. Публикация вопроса (т.е. смена его статуса на **Ответ**) должна происходить сразу же по нажатии кнопки **Отправить**. Поэтому полностью изменяем код компонента в файле `/bitrix/components/demo/form.result.edit/component.php`:




```

<?if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();?><?

if (CModule::IncludeModule("form"))
{
	$GLOBALS['strError'] = '';

	$arDefaultComponentParameters = array(
		"RESULT_ID" => $_REQUEST["RESULT_ID"],
		"EDIT_ADDITIONAL" => "Y",
		"WEB_FORM_ID" => $_REQUEST["WEB_FORM_ID"],
		"STATUS_ID" => $_REQUEST["STATUS_ID"],
		"USE_EXTENDED_ERRORS" => "N",
	);

	$arParams['NAME_TEMPLATE'] = empty($arParams['NAME_TEMPLATE'])
		? (method_exists('CSite', 'GetNameFormat') ? CSite::GetNameFormat() : "#NAME# #LAST_NAME#")
		: $arParams["NAME_TEMPLATE"];

	foreach ($arDefaultComponentParameters as $key => $value) if (!is_set($arParams, $key)) $arParams[$key] = $value;

	$arDefaultUrl = array(
		'LIST' => $arParams["SEF_MODE"] == "Y" ? "list/" : "result_list.php",
		'VIEW' => $arParams["SEF_MODE"] == "Y" ? "view/#RESULT_ID#/" : "result_view.php",
	);

	foreach ($arDefaultUrl as $action => $url)
	{
		if (strlen($arParams[$action.'_URL']) <= 0)
		{
			if (!is_set($arParams, 'SHOW_'.$action.'_PAGE') || $arParams['SHOW_'.$action.'_PAGE'] == 'Y')
				$arParams[$action.'_URL'] = $url;
		}
	}

	if ($arParams["SEF_MODE"] == "Y" && empty($arParams["RESULT_ID"]))
	{
		$arDefaultUrlTemplates404 = array(
			"edit" => "#RESULT_ID#/",
		);

		$arDefaultVariableAliases404 = array(
		);

		$arDefaultVariableAliases = array();

		$arComponentVariables = array("RESULT_ID");

		$arUrlTemplates = CComponentEngine::MakeComponentUrlTemplates($arDefaultUrlTemplates404, $arParams["SEF_URL_TEMPLATES"]);
		$arVariableAliases = CComponentEngine::MakeComponentVariableAliases($arDefaultVariableAliases404, $arParams["VARIABLE_ALIASES"]);
		CComponentEngine::ParseComponentPath($arParams["SEF_FOLDER"], $arUrlTemplates, $arVariables);

		$arParams["RESULT_ID"] = intval($arVariables["RESULT_ID"]);
	}

	$arResult["FORM_SIMPLE"] = COption::GetOptionString("form", "SIMPLE", "N") == "N" ? "N" : "Y";
	$arResult["bAdmin"] = defined("ADMIN_SECTION") && ADMIN_SECTION===true ? "Y" : "N";

	// if form taken from admin interface - check rights to form module
	if ($arResult["bAdmin"] == "Y")
	{
		$FORM_RIGHT = $APPLICATION->GetGroupRight("form");
		if($FORM_RIGHT<="D") $APPLICATION->AuthForm(GetMessage("ACCESS_DENIED"));
	}

	/****************************************************************************/

	// if there's result ID try to get form ID
	if (intval($arParams["RESULT_ID"] > 0))
	{
		$DBRes = CFormResult::GetByID($arParams["RESULT_ID"]);

		if ($arResultData = $DBRes->Fetch())
		{
			$arParams["WEB_FORM_ID"] = intval($arResultData["FORM_ID"]);
		}
	}

	if (intval($arParams["RESULT_ID"]) <= 0 || intval($arParams["WEB_FORM_ID"]) <= 0)
	{
		$arResult["ERROR"] = "FORM_RECORD_NOT_FOUND";
	}


	if (strlen($arResult["ERROR"]) <= 0)
	{
		// check WEB_FORM_ID and get web form data
		$arParams["WEB_FORM_ID"] = CForm::GetDataByID($arParams["WEB_FORM_ID"], $arResult["arForm"],
                                                                $arResult["arQuestions"], $arResult["arAnswers"], $arResult["arDropDown"], $arResult["arMultiSelect"],
                                                                $arResult["bAdmin"] || $arParams["SHOW_ADDITIONAL"] == "Y" || $arParams["EDIT_ADDITIONAL"] == "Y" ? "ALL" : "N");
	$arResult["WEB_FORM_NAME"] = $arResult["arForm"]["SID"];

		// if wrong WEB_FORM_ID return error;
		if ($arParams["WEB_FORM_ID"] > 0)
		{
			//  insert chain item
			if (strlen($arParams["CHAIN_ITEM_TEXT"]) > 0)
			{
				$APPLICATION->AddChainItem($arParams["CHAIN_ITEM_TEXT"], $arParams["CHAIN_ITEM_LINK"]);
			}

			// check web form rights;
			$arResult["F_RIGHT"] = intval(CForm::GetPermission($arParams["WEB_FORM_ID"]));

			// in no form access - return error
			if ($arResult["F_RIGHT"] >= 15)
			{
				//if (!empty($_REQUEST["strFormNote"])) $arResult["FORM_NOTE"] = $_REQUEST["strFormNote"];
				if (!empty($_REQUEST["formresult"]))
				{
					$formResult = strtoupper($_REQUEST['formresult']);
					switch ($formResult)
					{
						case 'ADDOK':
							$arResult['FORM_NOTE'] = str_replace("#RESULT_ID#", $arParams["RESULT_ID"], GetMessage('FORM_NOTE_ADDOK'));
						break;
						default:
							$arResult['FORM_NOTE'] = str_replace("#RESULT_ID#", $arParams["RESULT_ID"], GetMessage('FORM_NOTE_EDITOK'));
					}
				}

				if ($arResult["F_RIGHT"]>=20 || ($arResult["F_RIGHT"]>=15 && $USER->GetID()==$arResultData["USER_ID"]))
				{
					$arResult["arrRESULT_PERMISSION"] = CFormResult::GetPermissions($arParams["RESULT_ID"], $v);

					// check result rights
					if (!in_array("EDIT", $arResult["arrRESULT_PERMISSION"]))
					{
						$arResult["ERROR"] = "FORM_RESULT_ACCESS_DENIED";
					}
					else
					{
						if (!$arResultData)
						{
							$z = CFormResult::GetByID($arParams["RESULT_ID"]);
							$arResult["arResultData"] = $z->Fetch();
						}
						else
						{
							$arResult["arResultData"] = $arResultData;
						}

						if ($arResult["arResultData"])
						{
							$arResult["arrVALUES"] = CFormResult::GetDataByIDForHTML($arParams["RESULT_ID"], $arParams["EDIT_ADDITIONAL"]);
						}
						else
						{
							$arResult["ERROR"] = "FORM_RECORD_NOT_FOUND";
						}
					}
				}
				else
				{
					$arResult["ERROR"] = "FORM_ACCESS_DENIED";
				}

				$arResult["arForm"]["USE_CAPTCHA"] = "N";
			}
			else
			{
				$arResult["ERROR"] = "FORM_RESULT_ACCESS_DENIED";
			}
		}
		else
		{
			$arResult["ERROR"] = "FORM_NOT_FOUND";
		}
	}

	// if there's no error
	if (strlen($arResult["ERROR"]) <= 0)
	{
		// ************************************************************* //
		//                                             get/post processing                                             //
		// ************************************************************* //

		if (strlen($_REQUEST["web_form_submit"])>0 || strlen($_REQUEST["web_form_apply"])>0)
		{
				reset($arResult["arQuestions"]);
				foreach ($arResult["arQuestions"] as $key => $arQuestion)
				{
					$FIELD_SID = $arQuestion["SID"];
                	if (is_array($arResult["arQuestions"][$FIELD_SID]) && $arResult["arQuestions"][$FIELD_SID]["ADDITIONAL"] == "Y")
					{
						$temp="form_";
						switch ($arResult["arQuestions"][$FIELD_SID]["FIELD_TYPE"])
						{
						case "text":
							$temp.="textarea_ADDITIONAL_";
							break;
						case "integer":
							$temp.="text_ADDITIONAL_";
							break;
						case "date":
							$temp.="date_ADDITIONAL_";
							break;
						}
						$temp.=$arResult["arQuestions"][$FIELD_SID]["ID"];
                    	$arResult["arrVALUES"][$temp]= $_REQUEST[$temp];
					}
				}
			// check errors
				$arResult["FORM_ERRORS"] = CForm::Check($arParams["WEB_FORM_ID"], $arResult["arrVALUES"], $arParams["RESULT_ID"], "Y", $arParams['USE_EXTENDED_ERRORS']);

			if (
				$arParams['USE_EXTENDED_ERRORS'] == 'Y' && (!is_array($arResult["FORM_ERRORS"]) || count($arResult["FORM_ERRORS"]) <= 0)
				||
				$arParams['USE_EXTENDED_ERRORS'] != 'Y' && strlen($arResult["FORM_ERRORS"]) <= 0
			)
			{//echo "<pre>error "; print_r("enter"); echo "</pre>";
				// check session id
				if (check_bitrix_sessid())
				{
					$return = false;

					if (CFormResult::Update($arParams["RESULT_ID"], $arResult["arrVALUES"], $arParams["EDIT_ADDITIONAL"]))
					{
						CFormResult::SetStatus($arParams["RESULT_ID"],$arParams["STATUS_ID"],"Y");
						$arResult["FORM_RESULT"] = 'editok';

						if (strlen($_REQUEST["web_form_submit"])>0 && !(defined("ADMIN_SECTION") && ADMIN_SECTION===true))
						{
							if ($arParams["SEF_MODE"] == "Y")
							{
								//LocalRedirect($arParams["LIST_URL"]."?strFormNote=".urlencode($arResult["FORM_NOTE"]));
								LocalRedirect(
									str_replace(
										array('#WEB_FORM_ID#', '#RESULT_ID#'),
										array($arParams['WEB_FORM_ID'], $arParams["RESULT_ID"]),
										$arParams["LIST_URL"]
									)."?formresult=".urlencode($arResult["FORM_RESULT"])
								);
							}
							else
							{
								//LocalRedirect($arParams["LIST_URL"].(strpos($arParams["LIST_URL"], "?") === false ? "?" : "&")."WEB_FORM_ID=".$arParams["WEB_FORM_ID"]."&strFormNote=".urlencode($arResult["FORM_NOTE"]));
								LocalRedirect(
									$arParams["LIST_URL"]
									.(strpos($arParams["LIST_URL"], "?") === false ? "?" : "&")
									."WEB_FORM_ID=".$arParams["WEB_FORM_ID"]
									."&RESULT_ID=".$arParams["RESULT_ID"]
									."&formresult=".urlencode($arResult["FORM_RESULT"])
								);
							}

							die();
						}

						if (strlen($_REQUEST["web_form_apply"])>0 && !(defined("ADMIN_SECTION") && ADMIN_SECTION===true))
						{
							if ($arParams["SEF_MODE"] == "Y")
							{
								LocalRedirect(
									$APPLICATION->GetCurPageParam(
										"formresult=".urlencode($arResult["FORM_RESULT"]),
										array('formresult', 'SEF_APPLICATION_CUR_PAGE_URL')
									)
								);
							}
							else
							{
								LocalRedirect(
									$APPLICATION->GetCurPageParam(
										"WEB_FORM_ID=".$arParams["WEB_FORM_ID"]
										."&RESULT_ID=".$arParams["RESULT_ID"]
										."&formresult=".urlencode($arResult["FORM_RESULT"]),
										array('WEB_FORM_ID', 'RESULT_ID', 'formresult')
									)
								);
							}
							die();
						}

						if (defined("ADMIN_SECTION") && ADMIN_SECTION === true)
						{
							if (strlen($_REQUEST["web_form_submit"])>0)
							{
								LocalRedirect(BX_ROOT."/admin/form_result_list.php?lang=".LANG."&WEB_FORM_ID=".$arParams["WEB_FORM_ID"]."&formresult=".urlencode($arResult["FORM_RESULT"]));
							}
							elseif (strlen($_REQUEST["web_form_apply"])>0)
							{
								LocalRedirect(BX_ROOT."/admin/form_result_edit.php?lang=".LANG."&WEB_FORM_ID=".$arParams["WEB_FORM_ID"]."&RESULT_ID=".$arParams["RESULT_ID"]."&form_result=".urlencode($arResult["FORM_RESULT"]));
							}
							die();
						}
					}
					else
						$arResult['FORM_ERRORS'] = $GLOBALS['strError'];
				}
			}
		}

		/*
if (is_array($arResult["FORM_ERRORS"]))*/


		$arResult["isFormErrors"] =
			(
				is_array($arResult["FORM_ERRORS"]) && count($arResult["FORM_ERRORS"]) > 0
				||
				!is_array($arResult['FORM_ERRORS']) && strlen($arResult["FORM_ERRORS"]) > 0
			)
			? "Y" : "N";

		//echo "<pre>ar "; print_r($arResult); echo "</pre>";
		if ($arResult['isFormErrors'] == 'Y')
		{
			unset($arResult['FORM_RESULT']);
			unset($arResult['FORM_NOTE']);
		}

		// ************************************************************* //
		//                                             output                                                                    //
		// ************************************************************* //
		// include CSS with additional icons for Site Edit mode
		if ($APPLICATION->GetShowIncludeAreas() && $USER->IsAdmin())
		{
			// define additional icons for Site Edit mode
			$arIcons = array(
				array(
					'URL' => "javascript:".$APPLICATION->GetPopupLink(
						array(
							'URL' => "/bitrix/admin/form_edit.php?bxpublic=Y&from_module=form&lang=".LANGUAGE_ID."&ID=".$arParams['WEB_FORM_ID']."&back_url=".urlencode($_SERVER["REQUEST_URI"]),
							'PARAMS' => array(
								'width' => 700,
								'height' => 500,
								'resize' => false,
							)
						)
					),
					'ICON' => 'bx-context-toolbar-edit-icon',
					'TITLE' => GetMessage("FORM_PUBLIC_ICON_EDIT"),
				),
			);

			$this->AddIncludeAreaIcons($arIcons);
		}

		if (intval($arResult["arResultData"]["USER_ID"])>0)
		{
			$rsUser = CUser::GetByID($arResult["arResultData"]["USER_ID"]);
			$arUser = $rsUser->Fetch();

			$arResult["RESULT_USER_ID"] = $arResult["arResultData"]["USER_ID"];
			$arResult["RESULT_USER_LOGIN"] = $arUser["LOGIN"];
			$arResult["RESULT_USER_EMAIL"] = $arUser["USER_EMAIL"];
			$arResult["RESULT_USER_FIRST_NAME"] = $arUser["NAME"];
			$arResult["RESULT_USER_LAST_NAME"] = $arUser["LAST_NAME"];
			$arResult["RESULT_USER_SECOND_NAME"] = $arUser["SECOND_NAME"];
		}

		// define variables to assign
		$arResult = array_merge(
			$arResult,
			array(
				"RESULT_ID" => $arParams["RESULT_ID"],
				"WEB_FORM_ID" => $arParams["WEB_FORM_ID"],
				"RESULT_USER_AUTH" => $arResult["arResultData"]["USER_AUTH"] == "Y" ? "Y" : "N",
				"RESULT_DATE_CREATE" => $arResult["arResultData"]["DATE_CREATE"],
				"RESULT_TIMESTAMP_X" => $arResult["arResultData"]["TIMESTAMP_X"],
				"RESULT_STAT_GUEST_ID" => $arResult["arResultData"]["STAT_GUEST_ID"],
				"RESULT_STAT_SESSION_ID" => $arResult["arResultData"]["STAT_SESSION_ID"],
				"isFormNote"			=> strlen($arResult["FORM_NOTE"]) ? "Y" : "N", // flag "is there a form note"
				"isAccessFormParams"	=> $arResult["F_RIGHT"] >= 25 ? "Y" : "N", // flag "does current user have access to form params"
				"isStatisticIncluded"	=> CModule::IncludeModule('statistic') ? "Y" : "N", // flag "is statistic module included"

				"FORM_HEADER" => sprintf( // form header (<form> tag and hidden inputs)
					"<form name=\"%s\" action=\"%s\" method=\"%s\" enctype=\"multipart/form-data\">",
					$arResult["arForm"]["SID"], POST_FORM_ACTION_URI, "POST"
				),

				"FORM_TITLE"			=> trim(htmlspecialcharsbx($arResult["arForm"]["NAME"])), // form title

				"FORM_DESCRIPTION" => // form description
					$arResult["arForm"]["DESCRIPTION_TYPE"] == "html" ?
					trim($arResult["arForm"]["DESCRIPTION"]) :
					nl2br(htmlspecialcharsbx(trim($arResult["arForm"]["DESCRIPTION"]))),

				"isFormTitle"			=> strlen($arResult["arForm"]["NAME"]) > 0 ? "Y" : "N", // flag "does form have title"
				"isFormDescription"		=> strlen($arResult["arForm"]["DESCRIPTION"]) > 0 ? "Y" : "N", // flag "does form have description"
				"isFormImage"			=> intval($arResult["arForm"]["IMAGE_ID"]) > 0 ? "Y" : "N", // flag "does form have image"
				"isUseCaptcha"			=> $arResult["arForm"]["USE_CAPTCHA"] == "Y", // flag "does form use captcha"
				"DATE_FORMAT"			=> CLang::GetDateFormat("SHORT"), // current site date format
				"REQUIRED_SIGN"			=> CForm::ShowRequired("Y"), // "required" sign
				"FORM_FOOTER"			=> "</form>", // form footer (close <form> tag)
			)
		);

		// get template vars for form image
		if ($arResult["isFormImage"] == "Y")
		{
			$arResult["FORM_IMAGE"]["ID"] = $arResult["arForm"]["IMAGE_ID"];
			// assign form image url
			$arImage = CFile::GetFileArray($arResult["arForm"]["IMAGE_ID"]);
			$arResult["FORM_IMAGE"]["URL"] = $arImage["SRC"];

			// check image file existance and assign image data
			if (substr($arImage["SRC"], 0, 1) == "/")
			{
				$arSize = CFile::GetImageSize($_SERVER["DOCUMENT_ROOT"].$arImage["SRC"]);
				if (is_array($arSize))
				{
					list(
						$arResult["FORM_IMAGE"]["WIDTH"],
						$arResult["FORM_IMAGE"]["HEIGHT"],
						$arResult["FORM_IMAGE"]["TYPE"],
						$arResult["FORM_IMAGE"]["ATTR"]
					) = $arSize;
				}
			}
			else
			{
				$arResult["FORM_IMAGE"]["WIDTH"] = $arImage["WIDTH"];
				$arResult["FORM_IMAGE"]["HEIGHT"] = $arImage["HEIGHT"];
				$arResult["FORM_IMAGE"]["TYPE"] = false;
				$arResult["FORM_IMAGE"]["ATTR"] = false;
			}

			$arResult["FORM_IMAGE"]["HTML_CODE"] = CFile::ShowImage($arResult["arForm"]["IMAGE_ID"]);
		}

		$arResult["QUESTIONS"] = array();
		reset($arResult["arQuestions"]);

		// assign questions data
		foreach ($arResult["arQuestions"] as $key => $arQuestion)
		{
			$FIELD_SID = $arQuestion["SID"];
			$arResult["QUESTIONS"][$FIELD_SID] = array(
				"CAPTION" => // field caption
					$arResult["arQuestions"][$FIELD_SID]["TITLE_TYPE"] == "html" ?
					$arResult["arQuestions"][$FIELD_SID]["TITLE"] :
					nl2br(htmlspecialcharsbx($arResult["arQuestions"][$FIELD_SID]["TITLE"])),

				"IS_HTML_CAPTION"			=> $arResult["arQuestions"][$FIELD_SID]["TITLE_TYPE"] == "html" ? "Y" : "N",
				"REQUIRED"					=> $arResult["arQuestions"][$FIELD_SID]["REQUIRED"] == "Y" ? "Y" : "N",
				"IS_INPUT_CAPTION_IMAGE"	=> intval($arResult["arQuestions"][$FIELD_SID]["IMAGE_ID"]) > 0 ? "Y" : "N",
			);

			// ******************************** customize answers ***************************** //

			$arResult["QUESTIONS"][$FIELD_SID]["HTML_CODE"] = array();
			if (is_array($arResult["arQuestions"][$FIELD_SID]) && $arResult["arQuestions"][$FIELD_SID]["ADDITIONAL"] == "Y")
			{
				$res = "";
				switch ($arResult["arQuestions"][$FIELD_SID]["FIELD_TYPE"])
				{
					case "text":
						$value = CForm::GetTextAreaValue("ADDITIONAL_".$arResult["arQuestions"][$FIELD_SID]["ID"], array(), $arResult["arrVALUES"]);
						$res .= CForm::GetTextAreaField(
							"ADDITIONAL_".$arResult["arQuestions"][$FIELD_SID]["ID"],
							"60",
							"5",
							"",
							$value
							);

						$arResult["QUESTIONS"][$FIELD_SID]["HTML_CODE"][] = $res;

						break;
					case "integer":
						$value = CForm::GetTextValue("ADDITIONAL_".$arResult["arQuestions"][$FIELD_SID]["ID"], array(), $arResult["arrVALUES"]);
						$res .= CForm::GetTextField(
							"ADDITIONAL_".$arResult["arQuestions"][$FIELD_SID]["ID"],
							$value);

						$arResult["QUESTIONS"][$FIELD_SID]["HTML_CODE"][] = $res;

						break;
					case "date":
						$value = CForm::GetDateValue("ADDITIONAL_".$arResult["arQuestions"][$FIELD_SID]["ID"], array(), $arResult["arrVALUES"]);
						$res .= CForm::GetDateField(
							"ADDITIONAL_".$arResult["arQuestions"][$FIELD_SID]["ID"],
							$arResult["arForm"]["SID"],
							$value);

						$arResult["QUESTIONS"][$FIELD_SID]["HTML_CODE"][] = $res." (".CSite::GetDateFormat("SHORT").")";

						break;
				} //endswitch;
			}

			$arResult["QUESTIONS"][$FIELD_SID]["HTML_CODE"] = implode("<br />", $arResult["QUESTIONS"][$FIELD_SID]["HTML_CODE"]);

			// ******************************************************************************* //

			if ($arResult["QUESTIONS"][$FIELD_SID]["IS_INPUT_CAPTION_IMAGE"] == "Y")
			{
				$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["ID"] = $arResult["arQuestions"][$FIELD_SID]["IMAGE_ID"];
				// assign field image path
				$arImage = CFile::GetFileArray($arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["ID"]);
				$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["URL"] = $arImage["SRC"];

				// check image file existance and assign image data
				if (substr($arImage["SRC"], 0, 1) == "/")
				{
					$arSize = CFile::GetImageSize($_SERVER["DOCUMENT_ROOT"].$arImage["SRC"]);
					if (is_array($arSize))
					{
						list(
							$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["WIDTH"],
							$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["HEIGHT"],
							$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["TYPE"],
							$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["ATTR"]
						) = $arSize;
					}
				}
				else
				{
					$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["WIDTH"] = $arImage["WIDTH"];
					$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["HEIGHT"] = $arImage["HEIGHT"];
					$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["TYPE"] = false;
					$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["ATTR"] = false;
				}

				$arResult["QUESTIONS"][$FIELD_SID]["IMAGE"]["HTML_CODE"] = CFile::ShowImage($arResult["arQuestions"][$FIELD_SID]["IMAGE_ID"]);
			}

			// get answers raw structure
			$arResult["QUESTIONS"][$FIELD_SID]["STRUCTURE"] = $arResult["arAnswers"][$FIELD_SID];
			// nullify value
			$arResult["QUESTIONS"][$FIELD_SID]["VALUE"] = "";
		}

		if ($arResult["isFormErrors"] == "Y")
		{
			ob_start();
			if ($arParams['USE_EXTENDED_ERRORS'] == 'N' || !is_array($arResult['FORM_ERRORS']))
				ShowError($arResult["FORM_ERRORS"]);
			else
				ShowError(implode('<br />', $arResult["FORM_ERRORS"]));

			$arResult["FORM_ERRORS_TEXT"] = ob_get_contents();
			ob_end_clean();
		}

		$arResult["SUBMIT_BUTTON"] = "<input ".(intval($arResult["F_RIGHT"]) < 10 ?
                           "disabled=\"disabled\"" : "")." type=\"submit\" name=\"web_form_submit\" value=\"".(strlen(trim($arResult["arForm"]["BUTTON"])) <= 0 ?
                           GetMessage("FORM_ADD") : $arResult["arForm"]["BUTTON"])."\" />";
		$arResult["RESET_BUTTON"] = "<input type=\"reset\" value=\"".GetMessage("FORM_RESET")."\" />";
		$arResult["REQUIRED_STAR"] = $arResult["REQUIRED_SIGN"];

		// include default template
		$this->IncludeComponentTemplate();
	}
	else
	{
		echo ShowError(GetMessage($arResult["ERROR"]));
	}
}
else
{
	echo ShowError(GetMessage("FORM_MODULE_NOT_INSTALLED"));
}
?>
```




Теперь необходимо изменить шаблон компонента под нашу логику.





### Редактирование шаблона компонента




В форме ответа на вопрос помимо поля ввода ответа должны отображаться следующие данные: фамилия, имя, отчество пользователя, создавшего вопрос, текст вопроса, дата создания и дата ответа на вопрос. В связи заменим код шаблона компонента в файле `/bitrix/components/demo/form.result.edit/templates/.default/template.php` будет следующим:




## Код шаблона компонента

```

<?
if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
?>

<?
if ($arParams["VIEW_URL"])
{
	$href = $arParams["SEF_MODE"] == "Y" ? str_replace("#RESULT_ID#", $arParams["RESULT_ID"], $arParams["VIEW_URL"]) :
                $arParams["VIEW_URL"].(strpos($arParams["VIEW_URL"], "?") === false ?
                "?" : "&")."RESULT_ID=".$arParams["RESULT_ID"]."&WEB_FORM_ID=".$arParams["WEB_FORM_ID"];
?>
<p>[ <a href="<?=$href?>"><?=GetMessage("FORM_VIEW_NEW")?></a> ]</p>
<?
}
?>

<?=$arResult["FORM_HEADER"]?>
<?=bitrix_sessid_post()?>

<br />
<?

/***********************************************************************************
					Form questions
***********************************************************************************/
		?>
<?if ($arResult["FORM_NOTE"]):?><?=$arResult["FORM_NOTE"]?><?endif?>
<?if ($arResult["isFormErrors"] == "Y"):?><?=$arResult["FORM_ERRORS_TEXT"];?><?endif;?>
<table class="form-table data-table">
	<thead>
		<tr>
			<th colspan="2"> </th>
		</tr>
	</thead>
	<tbody>
<tr>
			<td><b><?=GetMessage("FORM_DATE_CREATE")?></b></td>
			<td><?=FormatDateFromDB($arResult["RESULT_DATE_CREATE"])?></td>
		</tr>
		<tr>
			<td><b><?=GetMessage("FORM_TIMESTAMP")?></b></td>
			<td><?=FormatDateFromDB($arResult["RESULT_TIMESTAMP_X"])?></td>
		</tr>
		<tr>
			<td><b><?=$arResult["arQuestions"]["name"]["TITLE"]?></b></td>
			<td><?=$arResult["arrVALUES"]["form_text_29"]?></td>
		</tr>
		<tr>
			<td><b><?=$arResult["arQuestions"]["text"]["TITLE"]?></b></td>
			<td><?=$arResult["arrVALUES"]["form_textarea_30"]?></td>
		</tr>
	<?
	foreach ($arResult["QUESTIONS"] as $FIELD_SID => $arQuestion)
	{
	if ($FIELD_SID == "our_answer")
	{
	?>
	<tr>
		<td>
			<?if (is_array($arResult["FORM_ERRORS"]) && array_key_exists($FIELD_SID, $arResult['FORM_ERRORS'])):?>
			<span class="error-fld" title="<?=$arResult["FORM_ERRORS"][$FIELD_SID]?>"></span>
			<?endif;?>
			<b><?=$arQuestion["CAPTION"]?></b>
			</td>
		<td><?=$arQuestion["HTML_CODE"]?></td>
	</tr>
	<?
	}
} //endwhile

	?>
	</tbody>
	<tfoot>
	<tr>
		<th colspan="2">
			<input type="submit" name="web_form_submit" value="<?=htmlspecialcharsbx(strlen(trim($arResult["arForm"]["BUTTON"])) <= 0 ? GetMessage("FORM_ADD") : $arResult["arForm"]["BUTTON"]);?>" />
			 <input type="reset" value="<?=GetMessage("FORM_RESET");?>" />
		</th>
	</tr>
	</tfoot>
</table>

<?=$arResult["FORM_FOOTER"]?>
```




Чтобы отобразить введенные пользователем значения вопросов **Фамилия, имя, отчество** и **Вопрос**, необходимо знать

			названия их html-полей

                    При выводе веб-формы все ответы на вопросы представляются в виде HTML полей, заполняя которые, пользователи отвечают на тот или иной вопрос.
[Подробнее...](http://dev.1c-bitrix.ru/api_help/form/htmlnames.php)

		. Например, если вопрос имеет ответ типа **text**, то поле формы будет иметь имя `form_text_id`, где **id** - это идентификатор значения ответа, который можно посмотреть в форме настройки вопроса:




![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/qa_ans_id.png)




Таким образом, поля формы **Фамилия, имя, отчество** и **Вопрос** имеют имена `form_text_29` и `form_textarea_30` соответственно, которые и используются в коде шаблона компонента. Найдите идентификаторы ваших вопросов и замените их в шаблоне.




**Примечание:** если в параметры компонента добавить настройку выбора отображаемых полей формы, то в коде не придется указывать имена полей явно (см. пример выше по добавлению параметров идентификаторов веб-формы и статуса).




В файл языковых сообщений шаблона компонента `/bitrix/components/demo/form.result.edit/templates/.default/lang/ru/template.php` добавим новую строку:




```
$MESS ['FORM_VIEW_NEW'] = "Вернуться к списку вопросов";
```




И внесем изменения в существующие:



```

$MESS ['FORM_DATE_CREATE'] = "Дата создания вопроса";
$MESS ['FORM_TIMESTAMP'] = "Дата ответа на вопрос";
```







В результате проделанных операций, когда модератор системы или администратор сайта со страницы со списком вопросов переходят по ссылке **Ответить**, открывается страница ответа на вопрос:




![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/ques_answer/answer_pub.png)
