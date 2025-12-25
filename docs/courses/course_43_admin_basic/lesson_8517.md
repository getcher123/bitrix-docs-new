# Пользовательские правила компаний

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7352 — Пользовательские ограничения](lesson_7352.md)
- [Следующий: 7849 — Кастомизация типов дополнительных услуг →](lesson_7849.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=8517

Вы можете дополнить стандартный набор правил компаний своими собственными правилами. Для этого следует использовать событие *onSaleCompanyRulesClassNamesBuildList*:

```

Bitrix\Main\EventManager::getInstance()->addEventHandler(
	"sale",
	"onSaleCompanyRulesClassNamesBuildList",
	"myCompanyRulesFunction"
);
```

В обработчике события следует вернуть ваш класс правил:

```

function myCompanyRulesFunction()
{
	return new \Bitrix\Main\EventResult(
		\Bitrix\Main\EventResult::SUCCESS,
		array(
			'\MyCompanyRules' => '/bitrix/php_interface/include/mycompanyrules.php',
		)
	);
}
```

Описывая уже само правило, вы можете определять какие-то собственные условия. Например, в примере приведено правило автоназначения компании в зависимости от лунных суток:

```

use Bitrix\Sale\Services\Base;
use Bitrix\Sale\Internals\Entity;

class MyCompanyRules extends Base\Restriction
{
	public static function getClassTitle()
	{
		return 'по лунным суткам';
	}

	public static function getClassDescription()
	{
		return 'компания будет использоваться только в указанном диапазоне лунных суток';
	}

public static function check($params, array $restrictionParams, $serviceId = 0)
{
	if ($params < $restrictionParams['MIN_MOONDAY'] || $params > $restrictionParams['MAX_MOONDAY'])
		return false;

	return true;
}
protected static function extractParams(Entity $entity)
{
	$json = file_get_contents('http://moon-today.com/api/index.php?get=moonday');
	$res = json_decode($json, true);
	return !empty($res['moonday']) ? intval($res['moonday']) : 0;
}
public static function getParamsStructure($entityId = 0)
	{
		return array(
			"MIN_MOONDAY" => array(
				'TYPE' => 'NUMBER',
				'DEFAULT' => "1",
				'LABEL' => 'Минимальные сутки'
			),
			"MAX_MOONDAY" => array(
				'TYPE' => 'NUMBER',
				'DEFAULT' => "30",
				'LABEL' => 'Максимальные сутки'
			)
		);
	}
}
```
