# Внешняя авторизация

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7957 — Кастомизация административной формы заказа](lesson_7957.md)
- [Следующий: 2289 — Дополнительные методы →](lesson_2289.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3574

Иногда для авторизации (проверки имени входа и пароля) пользователя бывает необходимо использовать свои алгоритмы проверки и(или) внешние БД для хранения пользователей. Например, уже имеется база пользователей и необходимо дать им возможность авторизовываться на сайте под управлением CMS. В таких случаях, иногда, можно просто перенести всех пользователей в БД CMS, используя API функции, но зачастую это просто невозможно по двум причинам:

- Первая - пароли пользователей во внешней БД не хранятся в открытом виде, хранится только хэш от них, поэтому после переноса пользователи не смогут авторизоваться по причине несовпадения пароля.
- Вторая причина заключается в том, что иногда необходимо чтобы база пользователей была единой, т.е. пароли пользователей хранились на одном удаленном сервере и использовались для проверки в нескольких местах, в том числе и в CMS.

Для решения таких задач в Bitrix Framework, реализована возможность добавить к стандартной встроенной системе авторизации свою внешнюю. Для этого необходимо реализовать несколько шагов, которые разберем на примере внешней авторизации, используя БД пользователей популярного форума PHP BB.

Для начала создадим файл, например, `/bitrix/php_interface/scripts/phpbb.php`. В этом файле будет размещён класс с внешним обработчиком, назовем его *__PHPBB2Auth*:

```

class __PHPBB2Auth
{
}
```

Чтобы во время попытки авторизоваться вызвалась наша функция, необходимо установить обработчик события [OnUserLoginExternal](http://dev.1c-bitrix.ru/api_help/main/events/onuserloginexternal.php), который будет вызываться автоматически каждый раз при вводе пользователем имени входа и пароля, перед встроенной проверкой. Для этого в файле `/bitrix/php_interface/init.php` воспользуемся функцией [AddEventHandler](http://dev.1c-bitrix.ru/api_help/main/functions/module/addeventhandler.php):

```

AddEventHandler(
	"main",
	"OnUserLoginExternal",
	Array("__PHPBB2Auth", "OnUserLoginExternal"), 100, $_SERVER['DOCUMENT_ROOT'].'/bitrix/php_interface/scripts/phpbb.php'
);
```



В качестве обработчика мы указали метод нашего класса *__PHPBB2Auth::OnUserLoginExternal*. Обработчик события [OnUserLoginExternal](http://dev.1c-bitrix.ru/api_help/main/events/onuserloginexternal.php) принимает в качестве параметра ссылку на массив с полями для проверки:

```

define("PHPBB2_TABLE_PREFIX", "phpbb_");
function OnUserLoginExternal(&$arArgs)
{
	$table_user = PHPBB2_TABLE_PREFIX."users";
	$table_user_group = PHPBB2_TABLE_PREFIX."user_group";
	extract($arArgs);

	global $DB, $USER, $APPLICATION;

	$strSql = "SELECT * FROM ".
		$table_user.
		" WHERE username='".
		$DB->ForSQL($login).
		"' AND user_password='".
		$DB->ForSql(md5($password))."'";
	$dbRes = $DB->Query($strSql);
	if($arRes = $dbRes->Fetch())
	{
		if($arRes['user_active']!='0')
		{
		// имя пользователя и пароль подошел
		}
	}
}
```

После того как имя входа и пароль проверены по алгоритму PHPBB, необходимо создать внешнего пользователя во внутренней БД, чтобы к нему можно было привязывать внутренние объекты (новости, голосования и т.п.). Для этого воспользуемся методом [CUser::GetList](http://dev.1c-bitrix.ru/api_help/main/reference/cuser/getlist.php) с фильтром по имени входа и коду внешнего источника. Если такой пользователь не существует - создадим его, если существует - обновим информацию о нем.

```

$arFields = Array(
	"LOGIN" => $login,
	"NAME" => $login,
	"PASSWORD" => $password,
	"EMAIL" => $arRes['user_email'],
	"ACTIVE" => "Y",
	"EXTERNAL_AUTH_ID"=>"PHPBB2",
	"LID" => SITE_ID
	);
$oUser = new CUser;
$res = CUser::GetList($O, $B, Array("LOGIN_EQUAL_EXACT"=>$login, "EXTERNAL_AUTH_ID"=>"PHPBB2"));
if(!($ar_res = $res->Fetch()))
	$ID = $oUser->Add($arFields);
else
{
	$ID = $ar_res["ID"];
	$oUser->Update($ID, $arFields);
}
if($ID>0)
{
	// можно авторизовывать
	return $ID;
}
```

Теперь у нас есть идентификатор пользователя в нашей БД и можно его вернуть из функции обработчика, чтобы этот пользователь был авторизован системой, но новый пользователь будет анонимным, т.к. не привязан ни к одной из групп. Воспользуемся привязкой в базе PHPBB, чтобы перенести ее в нашу БД до авторизации.

```

$USER->SetParam("PHPBB2_USER_ID", $arRes['user_id']);
$groups_map = Array(
	/*'PhpBB2 Group ID' => 'Local Group ID',*/
	'2' => '1'
	);

$user_groups = Array();
$dbUserGroup = $DB->Query('SELECT * FROM '.$table_user_group.' WHERE user_id='.$arRes['user_id']);
while($arUserGroup = $dbUserGroup->Fetch())
	$user_groups[] = $arUserGroup['group_id'];

if(count($user_groups)>0)
{
	$arUserGroups = CUser::GetUserGroup($ID);
	foreach($groups_map as $ext_group_id => $group_id)
	{
		if(in_array($ext_group_id, $user_groups))
			$arUserGroups[] = $group_id;
		else
		{
		$arUserGroupsTmp = Array();
		foreach($arUserGroups as $grid)
			if($grid != $group_id)
			$arUserGroupsTmp[] = $grid;
		$arUserGroups = $arUserGroupsTmp;
		}
	}
	CUser::SetUserGroup($ID, $arUserGroups);
}
```

Все, теперь локальный аккаунт пользователя соответствует удаленному, можно возвращать код пользователя и он будет авторизован. Отключим предварительно функцию **запомнить меня на этом компьютере**, если пользователь нажал на "флажок", т.к. при этом мы не сможем корректно проверить права доступа:

```

$arArgs["store_password"] = "N";
return $ID;
```

Для того чтобы зарегистрировать новую внешнюю проверку авторизации в системе, необходимо обработать событие [OnExternalAuthList](http://dev.1c-bitrix.ru/api_help/main/events/onexternalauthlist.php). Добавим в файл `/bitrix/php_interface/init.php` соответствующий вызов:

```

AddEventHandler(
	"main",
	"OnExternalAuthList",
	Array("__PHPBB2Auth", "OnExternalAuthList"), 100, $_SERVER['DOCUMENT_ROOT'].'/bitrix/php_interface/scripts/phpbb.php'
     );
```

Функция обработчик должна вернуть массив из набора обработчиков с полямим ID и NAME.

```

function OnExternalAuthList()
{
    return Array(
        Array("ID"=>"PHPBB2", "NAME"=>"PhpBB2")
        );
}
```

Теперь на странице редактирования пользователя появится выпадающий список со списком внешних источников авторизации. Приведем полный текст файла `/bitrix/php_interface/scripts/phpbb.php`. В нем дополнительно реализован обратный механизм: при авторизации пользователя в нашей системе он автоматически авторизуется на форуме.

```

<?
define("PHPBB2_TABLE_PREFIX", "phpbb_");

class __PHPBB2Auth
{
	function OnUserLoginExternal(&$arArgs)
	{
		////////// <settings> ////////////
		$table_user = PHPBB2_TABLE_PREFIX."users";
		$table_user_group = PHPBB2_TABLE_PREFIX."user_group";
		$groups_map = Array(
			/*'PhpBB2 Group ID' => 'Local Group ID',*/
			'2' => '1'
			);
		////////// </settings> ////////////
		extract($arArgs);

		global $DB, $USER, $APPLICATION;

		$strSql = "SELECT * FROM ".
			$table_user.
			" WHERE username='".
			$DB->ForSQL($login).
			"' AND user_password='".
			$DB->ForSql(md5($password))."'";
		$dbRes = $DB->Query($strSql);
		if($arRes = $dbRes->Fetch())
		{
		if($arRes['user_active']!='0')
		{
			$arFields = Array(
			"LOGIN" => $login,
			"NAME" => $login,
			"PASSWORD" => $password,
			"EMAIL" => $arRes['user_email'],
			"ACTIVE" => "Y",
			"EXTERNAL_AUTH_ID"=>"PHPBB2",
			"LID" => SITE_ID
			);
			$oUser = new CUser;
			$res = CUser::GetList($O, $B,
				Array("LOGIN_EQUAL_EXACT"=>$login,
				"EXTERNAL_AUTH_ID"=>"PHPBB2"));
			if(!($ar_res = $res->Fetch()))
				$ID = $oUser->Add($arFields);
			else
			{
			$ID = $ar_res["ID"];
			$oUser->Update($ID, $arFields);
			}

			if($ID>0)
			{
			$USER->SetParam("PHPBB2_USER_ID", $arRes['user_id']);

			$user_groups = Array();
			$dbUserGroup = $DB->Query('SELECT * FROM '.
				$table_user_group.
				' WHERE user_id='.$arRes['user_id']);
			while($arUserGroup = $dbUserGroup->Fetch())
				$user_groups[] = $arUserGroup['group_id'];

			if(count($user_groups)>0)
				{
				$arUserGroups = CUser::GetUserGroup($ID);
				foreach($groups_map as $ext_group_id => $group_id)
				{
					if(in_array($ext_group_id, $user_groups))
					$arUserGroups[] = $group_id;
				else
				{
				$arUserGroupsTmp = Array();
				foreach($arUserGroups as $grid)
					if($grid != $group_id)
                                        $arUserGroupsTmp[] = $grid;
					$arUserGroups = $arUserGroupsTmp;
				}
			}
			CUser::SetUserGroup($ID, $arUserGroups);
		}
			$arArgs["store_password"] = "N";

                    return $ID;
				}
			}
		}
	}

	function OnExternalAuthList()
	{
		return Array(
			Array("ID"=>"PHPBB2", "NAME"=>"PhpBB2 Board")
		);
	}

	function OnAuthorize(&$arArgs)
	{
		extract($arArgs);

		global $DB, $APPLICATION, $USER;
		$user_id = $USER->GetParam("PHPBB2_USER_ID");
		if($user_id<=0)
			return;
		$table_user = PHPBB2_TABLE_PREFIX."users";
		$table_sessions = PHPBB2_TABLE_PREFIX."sessions";
		$table_config = PHPBB2_TABLE_PREFIX."config";

		$dbConfig = $DB->Query("SELECT * FROM ".
			$table_config.
			" WHERE config_name
				IN ('cookie_name', 'cookie_path', 'cookie_domain', 'cookie_secure')");
		while($arConfig = $dbConfig->Fetch())
			${$arConfig['config_name']} = $arConfig['config_value'];

		if (isset($HTTP_COOKIE_VARS[$cookie_name . '_sid']) ||
			isset($HTTP_COOKIE_VARS[$cookie_name . '_data']))
			$session_id = isset($HTTP_COOKIE_VARS[$cookie_name . '_sid']) ?
				$HTTP_COOKIE_VARS[$cookie_name . '_sid'] : '';

		$ip_sep = explode('.', $_SERVER['REMOTE_ADDR']);
		$user_ip = sprintf('%02x%02x%02x%02x', $ip_sep[0], $ip_sep[1], $ip_sep[2], $ip_sep[3]);
		$current_time = time();
		$sql =
			"UPDATE ".$table_sessions." SET ".
			"    session_user_id = ".$user_id.", ".
			"    session_start = ".$current_time.", ".
			"    session_time = ".$current_time.", ".
			"    session_page = 0, ".
			"    session_logged_in = 1 ".
			"WHERE session_id = '".$DB->ForSQL($session_id)."' ".
			"    AND session_ip = '".$user_ip."'";

		$r = $DB->Query($sql);
		if($r->AffectedRowsCount()<=0)
		{
		$session_id = md5(uniqid($user_ip));
		$sql =
			"INSERT INTO ".
			$table_sessions.
			"(session_id, session_user_id, session_start, session_time, session_ip, session_page, session_logged_in)".
			"VALUES ('".$session_id."', ".$user_id.", ".$current_time.", ".$current_time.", '".$user_ip."', 0, 1)";
		$DB->Query($sql);
		}

		$sql =
			"UPDATE ".$table_user." SET ".
			"    user_session_time = ".$current_time.", ".
			"    user_session_page = 0, ".
			"    user_lastvisit = ".$current_time." ".
			"WHERE user_id = ".$user_id;

		$DB->Query($sql);

		$sessiondata = Array('userid' => $user_id);

		setcookie($cookie_name.'_data',
			serialize($sessiondata),
			$current_time + 31536000,
			$cookie_path,
			$cookie_domain, $cookie_secure);
		setcookie($cookie_name.'_sid',
			$session_id, 0, $cookie_path,
			$cookie_domain, $cookie_secure);
	}
}
?>
```

Следующие строки необходимо добавить в `/bitrix/php_interface/init.php`:

```

<?
AddEventHandler(
	"main",
	"OnUserLoginExternal",
	Array("__PHPBB2Auth", "OnUserLoginExternal"),100, $_SERVER['DOCUMENT_ROOT'].'/bitrix/php_interface/scripts/phpbb.php'
	);

AddEventHandler(
	"main",
	"OnExternalAuthList",
	Array("__PHPBB2Auth", "OnExternalAuthList"), 100, $_SERVER['DOCUMENT_ROOT'].'/bitrix/php_interface/scripts/phpbb.php'
	);

AddEventHandler(
	"main",
	"OnAfterUserAuthorize",
	Array("__PHPBB2Auth", "OnAuthorize"),100
	);
?>
```

В качестве примера ещё один скрипт внешней авторизации - для форума Invision Power Board:

```

<?
define("IPB_TABLE_PREFIX", "ibf_");
define("IPB_VERSION", "2");

AddEventHandler("main", "OnUserLoginExternal", Array("__IPBAuth", "OnUserLoginExternal"));
AddEventHandler("main", "OnExternalAuthList", Array("__IPBAuth", "OnExternalAuthList"));

class __IPBAuth
{
	function OnUserLoginExternal(&$arArgs)
	{
		extract($arArgs);

		////////// <settings> ////////////
		$table_user = IPB_TABLE_PREFIX."members";
		$table_converge = IPB_TABLE_PREFIX."members_converge";
		$groups_map = Array(
			/*'IPB Group ID' => 'Local Group ID',*/
			'4' => '1'
			);
		////////// </settings> ////////////

		global $DB, $USER, $APPLICATION;

		if(IPB_VERSION == '1')
		{
			$strSql = "SELECT * FROM ".$table_user." WHERE name='".$DB->ForSql($login)."' AND password='".md5($password)."'";
		}
		else
		{
		$strSql =
			"SELECT t1.* ".
			"FROM ".$table_user." t1, ".$table_converge." t2 ".
			"WHERE t1.name='".$DB->ForSql($login)."' ".
			"    AND t1.email = t2.converge_email ".
			"    AND t2.converge_pass_hash = MD5(CONCAT(MD5(t2.converge_pass_salt), '".md5($password)."'))";
		}

		$dbAuthRes = $DB->Query($strSql);
		if($arAuthRes = $dbAuthRes->Fetch())
		{
		$arFields = Array(
			"LOGIN" => $login,
			"NAME" => $arAuthRes['title'],
			"PASSWORD" => $password,
			"EMAIL" => $arAuthRes['email'],
			"ACTIVE" => "Y",
			"EXTERNAL_AUTH_ID"=>"IPB",
			"LID" => SITE_ID
			);

		$oUser = new CUser;
		$res = CUser::GetList($O, $B, Array("LOGIN_EQUAL_EXACT"=>$login, "EXTERNAL_AUTH_ID"=>"IPB"));
		if(!($ar_res = $res->Fetch()))
			$ID = $oUser->Add($arFields);
		else
		{
			$ID = $ar_res["ID"];
			$oUser->Update($ID, $arFields);
		}

		if($ID>0)
		{
			$USER->SetParam("IPB_USER_ID", $arAuthRes['id']);

			$user_group = $arAuthRes['mgroup'];
			$arUserGroups = CUser::GetUserGroup($ID);
			foreach($groups_map as $ext_group_id => $group_id)
			{
				if($ext_group_id==$user_group)
				$arUserGroups[] = $group_id;
			else
			{
				$arUserGroupsTmp = Array();
				foreach($arUserGroups as $grid)
					if($grid != $group_id)
					$arUserGroupsTmp[] = $grid;
				$arUserGroups = $arUserGroupsTmp;
			}
			}
			CUser::SetUserGroup($ID, $arUserGroups);
			$arArgs["store_password"] = "N";

			return $ID;
			}
		}
	}

	function OnExternalAuthList()
 	   {
		return Array(
		Array("ID"=>"IPB", "NAME"=>"Invision Power Board")
		);
	}
}
?>
```

Для того чтобы данный скрипт начал работать, его необходимо подключить в  `/bitrix/php_interface/init.php`.
