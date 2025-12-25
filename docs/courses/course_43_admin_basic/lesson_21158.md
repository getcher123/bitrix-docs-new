# Практика. Интеграция с модулем REST

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2692 — Практика. Постраничная навигация](lesson_2692.md)
- [Следующий: 21162 — Практика. Внедрение зависимостей →](lesson_21162.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=21158

Если запрограммированы контроллеры внутри модуля, то их легко сделать доступными для модуля **REST**. Это удобно, так как мы повторно используем уже написанный код.

Для этого нужно лишь поправить конфиг модуля `.settings.php`.

**Важно!** Это новый способ, должна быть проставлена зависимость от **REST 18.5.1**.

**Важно!** Если вы включили интеграцию с модулем **REST**, то все контроллеры и их действия будут доступны по REST API.

Поэтому, если вы не хотите, чтобы какой-то контроллер был доступен по REST API, то:

- либо не включайте интеграцию с модулем rest для этого модуля;
- либо сделайте [префильтр](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/actionfilter/index.php) по умолчанию в контроллере вашего модуля, который будет проверять, что текущий запрос не по REST, а в нужных действиях просто его убирайте.

```
protected function getDefaultPreFilters()
	{
		return [
			parent::getDefaultPreFilters(),
			new Engine\ActionFilter\Scope(Engine\ActionFilter\Scope::NOT_REST),
		];
	}
```

Итак, как включить в модуле интеграцию:

```
<?php
#.settings.php
return [
	'controllers' => [
		'value' => [
			'defaultNamespace' => '\\Bitrix\\Disk\\Controller',
			'restIntegration' => [
				'enabled' => true,
			],
		],
		'readonly' => true,
	]
];
```

### Как использовать в ajax-действии \CRestServer?

Если вдруг ajax-действие должно использовать *\CRestServer* для какой-то специфической задачи, то это можно легко решить, объявив одним из параметров *\CRestServer*.

Пример:

```

public function getStorageForAppAction($clientName, \CRestServer $restServer)
{
	$clientId = $restServer->getClientId();
	...
}
```

Будьте внимательны, в примере выше действие не будет работать через обычный ajax, так как `\CRestServer  $restServer` там отсутствует и не может быть внедрен. Оно будет доступно только для модуля **REST**. Если же объявить его необязательным, то всё будет работать.

```

public function getStorageForAppAction($clientName, \CRestServer $restServer = null)
{
	if ($restServer)
	{
		$clientId = $restServer->getClientId();
	}
	...
}
```

### Как понять, вызываются ли действия в REST или AJAX окружении?

Может возникнуть задача, что нужно отличить в каком контексте сейчас выполняется действие: это REST или это AJAX? Для этого можно спросить у контролера:

```

\Bitrix\Main\Engine\Controller::getScope()

//возможные варианты
\Bitrix\Main\Engine\Controller::SCOPE_REST
\Bitrix\Main\Engine\Controller::SCOPE_AJAX
\Bitrix\Main\Engine\Controller::SCOPE_CLI
```
