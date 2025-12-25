# Пример создания действия Создать задачу

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2903 — Пример создания действия Запись в лог](lesson_2903.md)
- [Следующий: 5815 — Выполнение «задания» бизнес-процесса, используя API →](lesson_5815.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=2904

|  | ### Создаём своё действие |
| --- | --- |




Действие для создания задачи 2.0 (**task2activity**) создано по алгоритму, описанному выше. Поэтому просто приведем структуру действия и коды файлов. Функционал полностью повторяет стандартное действие для создания задачи.



#### Структура файлов Activity



- `/task2activity/`

  - `/lang/`

    - `/en/`
    - `/ru/`

      - **.description.php**
      - **properties_dialog.php**
      - **task2activity.php**
  - **icon.gif**
  - **.description.php**
  - **properties_dialog.php**
  - **task2activity.php**




#### Код файлов




`task2activity\.description.php`



```
<?
if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();

$arActivityDescription = array(
	"NAME" => GetMessage("BPTA2_DESCR_NAME"),
	"DESCRIPTION" => GetMessage("BPTA2_DESCR_DESCR"),
	"TYPE" => "activity",
	"CLASS" => "Task2Activity",
	"JSCLASS" => "BizProcActivity",
	"CATEGORY" => array(
		"ID" => "interaction",
	),
);
?>
```




`task2activity\properties_dialog.php`



```
<?
if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
?>

<tr>
	<td align="right" width="40%"><span style="color:#FF0000;">* <?= GetMessage("BPTA1A_TASKNAME") ?>:</td>
	<td width="60%">
		<input type="text" name="task_name" id="id_task_name" value="<?= htmlspecialchars($arCurrentValues["task_name"]) ?>" size="50">
		<input type="button" value="..." onclick="BPAShowSelector('id_task_name', 'string');">
	</td>
</tr>
<tr>
	<td align="right" width="40%"><span style="color:#FF0000;">*</span> <?= GetMessage("BPTA1A_TASKCREATEDBY") ?>:</td>
	<td width="60%">
		<input type="text" name="task_created_by" id="id_task_created_by" value="<?= htmlspecialchars($arCurrentValues["task_created_by"]) ?>" size="50">
		<input type="button" value="..." onclick="BPAShowSelector('id_task_created_by', 'user');">
	</td>
</tr>
<tr>
	<td align="right" width="40%"><span style="color:#FF0000;">*</span> <?= GetMessage("BPTA1A_TASKASSIGNEDTO") ?>:</td>
	<td width="60%">
		<input type="text" name="task_assigned_to" id="id_task_assigned_to" value="<?= htmlspecialchars($arCurrentValues["task_assigned_to"]) ?>" size="50">
		<input type="button" value="..." onclick="BPAShowSelector('id_task_assigned_to', 'user');">
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_TASKACTIVEFROM") ?>:</td>
	<td width="60%">
		<span style="white-space:nowrap;"><input type="text" name="task_active_from" id="id_task_active_from" size="30" value="<?= htmlspecialchars($arCurrentValues["task_active_from"]) ?>"><?= CAdminCalendar::Calendar("task_active_from", "", "", true) ?></span>
		<input type="button" value="..." onclick="BPAShowSelector('id_task_active_from', 'datetime');">
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_TASKACTIVETO") ?>:</td>
	<td width="60%">
		<span style="white-space:nowrap;"><input type="text" name="task_active_to" id="id_task_active_to" size="30" value="<?= htmlspecialchars($arCurrentValues["task_active_to"]) ?>"><?= CAdminCalendar::Calendar("task_active_to", "", "", true) ?></span>
		<input type="button" value="..." onclick="BPAShowSelector('id_task_active_to', 'datetime');">
	</td>
</tr>

<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_TASKDETAILTEXT") ?>:</td>
	<td width="60%">
		<textarea name="task_detail_text" id="id_task_detail_text" rows="7" cols="40"><?= htmlspecialchars($arCurrentValues["task_detail_text"]) ?></textarea>
		<input type="button" value="..." onclick="BPAShowSelector('id_task_detail_text', 'string');">
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_TASKPRIORITY") ?>:</td>
	<td width="60%">
		<select name="task_priority">
			<?
			foreach ($arTaskPriority as $key => $value)
			{
				?><option value="<?= $key ?>"<?= $arCurrentValues["task_priority"] == $key ? " selected" : "" ?>><?= $value ?></option><?
			}
			?>
		</select>
	</td>
</tr>
<tr>
	<td align="right" width="40%"> <?= GetMessage("BPTA1A_TASKGROUPID") ?>:</td>
	<td width="60%">
		<select name="task_group_id" id="id_task_group_id">
			<?
			foreach ($arGroups as $key => $value)
			{
				?><option value="<?= $key ?>"<?= $arCurrentValues["task_group_id"] == $key ? " selected" : "" ?>><?= $value ?></option><?
			}
			?>
		</select>
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_CHANGE_DEADLINE") ?>:</td>
	<td width="60%">
		<input type="checkbox" name="task_change_deadline" id="id_task_change_deadline" <?= ($arCurrentValues["task_change_deadline"] == "Y")? "checked":""?>>
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_CHECK_RESULT") ?>:</td>
	<td width="60%">
            <input type="checkbox" name="task_check_result" id="id_task_check_result" <?= ($arCurrentValues["task_check_result"] == "Y")? "checked":""?>>
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_ADD_TO_REPORT") ?>:</td>
	<td width="60%">
		<input type="checkbox" name="task_report" id="id_task_report" <?= ($arCurrentValues["task_report"] == "Y")? "checked":""?>>
	</td>
</tr>
<tr>
	<td align="right" width="40%"><?= GetMessage("BPTA1A_TASKTRACKERS") ?>:</td>
	<td width="60%">
		<input type="text" name="task_trackers" id="id_task_trackers" value="<?= htmlspecialchars($arCurrentValues["task_trackers"]) ?>" size="50">
		<input type="button" value="..." onclick="BPAShowSelector('id_task_trackers', 'user');">
	</td>
</tr>
```




`task2activity\task2activity.php`



```
<?
if (!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();

class CBPTask2Activity
	extends CBPActivity
{
	public function __construct($name)
	{
		parent::__construct($name);
		$this->arProperties = array(
			"Title" => "", //название действия
			"TaskGroupId" => "", //личная или группа
			"TaskOwnerId" => "", //
			"TaskCreatedBy" => "", //автор
			"TaskActiveFrom" => "", //от
			"TaskActiveTo" => "", //до
			"TaskName" => "", //название задачи
			"TaskDetailText" => "", //описание
			"TaskPriority" => "", //приоритет
			"TaskAssignedTo" => "", //ответственный
			"TaskTrackers" => "", //следящие
			"TaskCheckResult" => "", //
			"TaskReport" => "", //
			"TaskChangeDeadline" => "",
		);
	}

	private function __GetUsers($arUsersDraft)
	{

		$arUsers = array();

		$rootActivity = $this->GetRootActivity();
		$documentId = $rootActivity->GetDocumentId();

		$documentService = $this->workflow->GetService("DocumentService");

		$arUsersDraft = (is_array($arUsersDraft) ? $arUsersDraft : array($arUsersDraft));
		$l = strlen("user_");
		foreach ($arUsersDraft as $user)
		{
			if (substr($user, 0, $l) == "user_")
			{
				$user = intval(substr($user, $l));
				if ($user > 0)
					$arUsers[] = $user;
			}
			else
			{
				$arDSUsers = $documentService->GetUsersFromUserGroup($user, $documentId);
				foreach ($arDSUsers as $v)
				{
					$user = intval($v);
					if ($user > 0)
						$arUsers[] = $user;
				}
			}
		}

		return $arUsers;
	}

	public function Execute()
	{

		if (!CModule::IncludeModule("tasks"))
			return CBPActivityExecutionStatus::Closed;

		$arTaskCreatedBy = $this->__GetUsers($this->TaskCreatedBy);
		$arTaskAssignedTo = $this->__GetUsers($this->TaskAssignedTo);

		if (count($arTaskCreatedBy) <= 0 || count($arTaskAssignedTo) <= 0)
			return CBPActivityExecutionStatus::Closed;

		$arTaskTrackers = $this->__GetUsers($this->TaskTrackers);

		$bFirst = true;
		$ACCOMPLICES = array();
		foreach($arTaskAssignedTo as $respUser)
		{
			if ($bFirst)
			{
				$RESPONSIBLE_ID = $respUser;
				$bFirst = false;
			}
			else
				$ACCOMPLICES[] = $respUser;
		}

		$arFields = array(
			"MODIFIED_BY" => $arTaskCreatedBy[0],
			"CREATED_BY" => $arTaskCreatedBy[0],
			"SITE_ID" => SITE_ID,
			"STATUS" => "1",
			"DATE_CREATE" => date($GLOBALS["DB"]->DateFormatToPHP(FORMAT_DATETIME)),
			"START_DATE_PLAN" => $this->TaskActiveFrom,
			"END_DATE_PLAN" => $this->TaskActiveTo,
			"DEADLINE" => $this->TaskActiveTo,
			"TITLE" => $this->TaskName,
			"DESCRIPTION" => $this->TaskDetailText,
			"PRIORITY" => $this->TaskPriority,
			"RESPONSIBLE_ID" => $RESPONSIBLE_ID,
			"AUDITORS" => $arTaskTrackers,
			"ADD_IN_REPORT" => $this->TaskReport,
			"TASK_CONTROL" => $this->TaskCheckResult,
			"ALLOW_CHANGE_DEADLINE" => $this->TaskChangeDeadline,
		);
		if ($this->TaskGroupId && $this->TaskGroupId !== 0)
			$arFields["GROUP_ID"] = $this->TaskGroupId;

		if (count ($ACCOMPLICES) > 0)
			$arFields["ACCOMPLICES"] = $ACCOMPLICES;

			$task = new CTasks;
			$result = $task->Add($arFields);

		if ($result)
			$this->WriteToTrackingService(str_replace("#VAL#", $result, GetMessage("BPSA_TRACK_OK")));

			$arErrors = $task->GetErrors();
		if (count($arErrors) > 0)
			$this->WriteToTrackingService(GetMessage("BPSA_TRACK_ERROR"));

		return CBPActivityExecutionStatus::Closed;
	}

	public static function ValidateProperties($arTestProperties = array(), CBPWorkflowTemplateUser $user = null)
	{
		$arErrors = array();

		if ((!array_key_exists("TaskAssignedTo", $arTestProperties) || count($arTestProperties["TaskAssignedTo"])) <= 0)
			$arErrors[] = array(
				"code" => "NotExist",
				"parameter" => "TaskAssignedTo",
				"message" => GetMessage("BPSNMA_EMPTY_TASKASSIGNEDTO")
				);
		if ((!array_key_exists("TaskName", $arTestProperties) || count($arTestProperties["TaskName"]) <= 0)
			$arErrors[] = array(
				"code" => "NotExist",
				"parameter" => "TaskName",
				"message" => GetMessage("BPSNMA_EMPTY_TASKNAME")
				);

		return array_merge($arErrors, parent::ValidateProperties($arTestProperties, $user));
	}

	public static function GetPropertiesDialog($documentType, $activityName, $arWorkflowTemplate, $arWorkflowParameters, $arWorkflowVariables, $arCurrentValues = null, $formName = "")
	{
		$runtime = CBPRuntime::GetRuntime();

		if (!CModule::IncludeModule("socialnetwork"))
			return;

		$arMap = array(
			"TaskGroupId" => "task_group_id",
			"TaskOwnerId" => "task_owner_id",
			"TaskCreatedBy" => "task_created_by",
			"TaskActiveFrom" => "task_active_from",
			"TaskActiveTo" => "task_active_to",
			"TaskName" => "task_name",
			"TaskDetailText" => "task_detail_text",
			"TaskPriority" => "task_priority",
			"TaskAssignedTo" => "task_assigned_to",
			"TaskTrackers" => "task_trackers",
			"TaskCheckResult" => "task_check_result",
			"TaskReport" => "task_report",
			"TaskChangeDeadline" => "task_change_deadline",
		);

		if (!is_array($arWorkflowParameters))
			$arWorkflowParameters = array();
		if (!is_array($arWorkflowVariables))
			$arWorkflowVariables = array();

		if (!is_array($arCurrentValues))
		{
			$arCurrentActivity = &CBPWorkflowTemplateLoader::FindActivityByName($arWorkflowTemplate, $activityName);
			if (is_array($arCurrentActivity["Properties"]))
			{
				foreach ($arMap as $k => $v)
				{
					if (array_key_exists($k, $arCurrentActivity["Properties"]))
					{
						if ($k == "TaskCreatedBy" || $k == "TaskAssignedTo" || $k == "TaskTrackers")
							$arCurrentValues[$arMap[$k]] = CBPHelper::UsersArrayToString($arCurrentActivity["Properties"][$k], $arWorkflowTemplate, $documentType);
						else
							$arCurrentValues[$arMap[$k]] = $arCurrentActivity["Properties"][$k];
					}
					elseif ($k == "TaskPriority")
					{
						$arCurrentValues[$arMap[$k]] = "1";
					}
					else
					{
						$arCurrentValues[$arMap[$k]] = "";
					}
				}
			}
			else
			{
				foreach ($arMap as $k => $v)
					$arCurrentValues[$arMap[$k]] = "";
			}

		}


		$arGroups = array(GetMessage("TASK_EMPTY_GROUP"));
		$db = CSocNetGroup::GetList(array("NAME" => "ASC"), array("ACTIVE" => "Y"), false, false, array("ID", "NAME"));
		while ($ar = $db->GetNext())
			$arGroups[$ar["ID"]] = "[".$ar["ID"]."]".$ar["NAME"];

		$arTaskPriority = array(0, 1, 2);
		foreach($arTaskPriority as $k => $v)
			$arTaskPriority[$v] = GetMessage("TASK_PRIORITY_".$v);

		return $runtime->ExecuteResourceFile(
			__FILE__,
			"properties_dialog.php",
			array(
				"arCurrentValues" => $arCurrentValues,
				"formName" => $formName,
				"arGroups" => $arGroups,
				"arTaskPriority" => $arTaskPriority,
			)
		);
	}

	public static function GetPropertiesDialogValues($documentType, $activityName, &$arWorkflowTemplate, &$arWorkflowParameters, &$arWorkflowVariables, $arCurrentValues, &$arErrors)
	{
		$arErrors = array();

		$runtime = CBPRuntime::GetRuntime();

		$arMap = array(
			"task_group_id" => "TaskGroupId",
			"task_owner_id" => "TaskOwnerId",
			"task_created_by" => "TaskCreatedBy",
			"task_active_from" => "TaskActiveFrom",
			"task_active_to" => "TaskActiveTo",
			"task_name" => "TaskName",
			"task_detail_text" => "TaskDetailText",
			"task_priority" => "TaskPriority",
			"task_assigned_to" => "TaskAssignedTo",
			"task_trackers" => "TaskTrackers",
			"task_forum_id" => "TaskForumId",
			"task_check_result" => "TaskCheckResult",
			"task_report" => "TaskReport",
			"task_change_deadline" => "TaskChangeDeadline",
		);

		$arProperties = array();
		foreach ($arMap as $key => $value)
		{
			if ($key == "task_created_by" || $key == "task_assigned_to" || $key == "task_trackers")
				continue;
			$arProperties[$value] = $arCurrentValues[$key];
		}

		$arProperties["TaskCreatedBy"] = CBPHelper::UsersStringToArray($arCurrentValues["task_created_by"], $documentType, $arErrors);
		if (count($arErrors) > 0)
			return false;

		$arProperties["TaskAssignedTo"] = CBPHelper::UsersStringToArray($arCurrentValues["task_assigned_to"], $documentType, $arErrors);
		if (count($arErrors) > 0)
			return false;

		$arProperties["TaskTrackers"] = CBPHelper::UsersStringToArray($arCurrentValues["task_trackers"], $documentType, $arErrors);
		if (count($arErrors) > 0)
			return false;

		$arErrors = self::ValidateProperties($arProperties, new CBPWorkflowTemplateUser(CBPWorkflowTemplateUser::CurrentUser));
		if (count($arErrors) > 0)
			return false;

		$arCurrentActivity = &CBPWorkflowTemplateLoader::FindActivityByName($arWorkflowTemplate, $activityName);
		$arCurrentActivity["Properties"] = $arProperties;

		return true;
	}
}
?>
```




`task2activity\lang\ru\.description.php`



```
<?
$MESS ['BPTA2_DESCR_DESCR'] = "Добавление задачи 2.0";
$MESS ['BPTA2_DESCR_NAME'] = "Задача 2.0";
?>
```




`task2activity\lang\ru\properties_dialog.php`



```
<?
$MESS ['BPTA1A_TASKGROUPID'] = "Группа соц. сети";
$MESS ['BPTA1A_TASKCREATEDBY'] = "Задача создается от имени";
$MESS ['BPTA1A_TASKASSIGNEDTO'] = "Ответственный";
$MESS ['BPTA1A_TASKACTIVEFROM'] = "Начало";
$MESS ['BPTA1A_TASKACTIVETO'] = "Окончание";
$MESS ['BPTA1A_TASKNAME'] = "Название задачи";
$MESS ['BPTA1A_TASKDETAILTEXT'] = "Описание задачи";
$MESS ['BPTA1A_TASKTRACKERS'] = "Следящие";
$MESS ['BPTA1A_TASKPRIORITY'] = "Важность";
$MESS ['BPTA1A_TASKFORUM'] = "Форум для комментариев";
$MESS ['BPTA1A_ADD_TO_REPORT'] = "Проконтролировать результат выполнения";
$MESS ['BPTA1A_CHECK_RESULT'] = "Включить задачу в отчет по эффективности";
$MESS ['BPTA1A_CHANGE_DEADLINE'] = "Разрешить ответственному менять сроки";
?>
```




`task2activity\lang\ru\task2activity.php`



```
<?
$MESS ['BPSNMA_EMPTY_TASKASSIGNEDTO'] = "Свойство 'Ответственный' не указано.";
$MESS ['BPSNMA_EMPTY_TASKNAME'] = "Свойство 'Название задачи' не указано.";
$MESS ['TASK_PRIORITY_0'] = "Низкая";
$MESS ['TASK_PRIORITY_1'] = "Средняя";
$MESS ['TASK_PRIORITY_2'] = "Высокая";
$MESS ['TASK_EMPTY_GROUP'] = "Персональная задача";
$MESS ['BPSA_TRACK_OK'] = "Создана задача с ID ##VAL#";
$MESS ['BPSA_TRACK_ERROR'] = "При создании задачи произошла ошибка.";
?>
```
