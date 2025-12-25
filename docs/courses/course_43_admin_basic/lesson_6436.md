# Контроллер

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 14032 — Сервис Локатор](lesson_14032.md)
- [Следующий: 14014 — Контроллеры и компонент →](lesson_14014.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=6436

> **Контроллеры** - это часть [MVC архитектуры](lesson_2817.md), которая отвечает за обработку запроса и генерирование ответа.



### Действия

Контроллеры состоят из действий, которые являются основной сутью и их в конечном итоге запрашивает пользователь для получения результата. В одном контроллере может быть одно или несколько действий. Для примера сделаем контроллер с двумя действиями **item.add** и **item.view** в модуле *example*. В рамках примера контроллер располагается по пути `/modules/vendor.example/lib/controller/item.php`.

Первый шаг - создать в корне модуля файл `.settings.php`.

```
<?php
//modules/vendor.example/.settings.php
return [
	'controllers' => [
		'value' => [
			'defaultNamespace' => '\\Vendor\\Example\\Controller',
		],
		'readonly' => true,
	]
];
```

Далее создаётся сам файл контроллера (смотри подробное описание [доступных методов](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/controller/index.php)):

```
namespace Vendor\Example\Controller;
use \Bitrix\Main\Error;
class Item extends \Bitrix\Main\Engine\Controller
{
	public function addAction(array $fields):? array
	{
		$item = Item::add($fields);
		if (!$item)
		{
			$this->addError(new Error('Could not create item.', {код_ошибки}));
			return null;
		}
		return $item->toArray();
	}
	public function viewAction($id):? array
	{
		$item = Item::getById($id);
		if (!$item)
		{
			$this->addError(new Error('Could not find item.', {код_ошибки}));

			return null;
		}
		return $item->toArray();
	}
}
```

В действии **add** (определенным методом `Item::addAction`) сначала идёт попытка создания некого *Item* по переданным `$fields`.

**Примечание**. Массив *$fields* получается путем автоматического связывания параметров метода и `$_REQUEST`. Подробнее о принципах в уроке [Внедрение зависимостей](lesson_21162.md).

Если не удалось выполнить создание по каким-то причинам, то возвращаем *null* и наполняем ошибками сам контроллер. В этом случае ядро сгенерирует ответ:

```
{
	"status": "error", //обратите внимание, что статус автоматически сменился
	"data": null,
	"errors": [
		{
			"message": "Could not create item.",
			"code": {код}
		}
	]
}
```

Иначе добавляем *Item* и возвращаем из действия его представление в виде массива `$item->toArray()`. Таким образом ядро сгенерирует ответ:

```
{
	"status": "success",
	"data": {
		"ID": 1,
		"NAME": "Nobody",
		//...поля элемента
	},
	"errors": null
}
```

В целом, действие может вернуть не просто скаляры, но и объекты.

В действии **view** (определенным методом `Item::viewAction`) сначала идёт попытка загрузки некого объекта *Item* по переданному параметру `$id`. Важно заметить, что *$id* будет автоматически получен из `$_POST['id']` или `$_GET['id']`.

Если данный параметр не найден, то ядро сгенерирует ответ с ошибкой:

```
{
	"status": "error",
	"data": null,
	"errors": [
		{
			"message": "Could not find value for parameter {id}",
			"code": 0
		}
	]
}
```

### Как обратиться к действию контроллера?

Для вызова конкретного аякс-действия нужно знать и пользоваться [соглашением по именованию](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=03750#sogl). В нашем случае: `Item::addAction -> vendor:example.Item.add` `Item::viewAction -> vendor:example.Item.view`.

*vendor:example.Item.add*, *vendor:example.Item.view* можно использовать для вызова действий через *BX.ajax.runAction*:

```
BX.ajax.runAction('vendor:example.Item.add', {
	data: {
		fields: {
			ID: 1,
			NAME: "test"
		}
	}
}).then(function (response) {
	console.log(response);
	/**
	{
		"status": "success",
		"data": {
			"ID": 1,
			"NAME": "test"
		},
		"errors": []
	}
	**/
}, function (response) {
	//сюда будут приходить все ответы, у которых status !== 'success'
	console.log(response);
	/**
	{
		"status": "error",
		"errors": [...]
	}
	**/
});
```

Либо можно получить [ссылку](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/urlmanager/index.php) на действие и послать http-запрос самостоятельно.

```
/** @var \Bitrix\Main\Web\Uri $uri **/
$uri = \Bitrix\Main\Engine\UrlManager::getInstance()->create('vendor:example.Item.view', ['id' => 1]);
echo $uri;
// /bitrix/services/main/ajax.php?action=vendor:example.Item.view&id=1
// выполняем GET-запрос
```

### Создание контроллеров и действий

#### Создание контроллеров

Контроллеры должны быть унаследованы от [\Bitrix\Main\Engine\Controller](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/controller/index.php) или его потомков. Контроллеры могут располагаться внутри модуля, либо внутри [компонента](lesson_14014.md) в файле **ajax.php** и быть контроллером для компонента.

#### Создание действий

Создание действий, это создание просто методов в конкретном контроллере. Метод обязан быть public и иметь суффикс Action.

```
namespace Vendor\Example\Controller;
class Item extends \Bitrix\Main\Engine\Controller
{
	public function addAction(array $fields)
	{
		//...
	}
}
```

Возвращаемое значение действия представляет собой данные ответа, которые будут высланы клиенту.

Если действие возвращает [\Bitrix\Main\HttpResponse](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/index.php) или его наследников, то данный объект и будет отправлен клиенту. Если действие возвращает некие данные, то они должны приводиться к скаляру или объекту, который после будет превращен в JSON и на основе него будет сформирован `\Bitrix\Main\Engine\Response\AjaxJson`.

В целом действие может вернуть не просто скаляры, но и объекты, которые реализуют следующие интерфейсы:

- `\JsonSerializable`
- `\Bitrix\Main\Type\Contract\Arrayable`
- `\Bitrix\Main\Type\Contract\Jsonable`

Либо конкретные наследники \Bitrix\Main\HttpResponse:

- [Redirect](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/redirect.php)
- [JSON](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/json.php)
- [Типовой JSON](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/ajaxjson.php)
- [Файл b_file](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/bfile.php)
- [Ресайзенное изображение](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/resizedimage.php)
- [Архив](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/archive.php)
- [Компонент](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/component.php)

### Создание классов-действий

Есть возможность создавать классы-действия, которые унаследованы от `\Bitrix\Main\Engine\Action`. Подобная возможность может потребоваться, когда необходимо повторно использовать логику в нескольких контроллерах. Например, если реализуется одинаковый протокол обмена в разных модулях (стандартный поиск, выполнение пошаговых действий с прогрессом и тому подобное.). Для использования нужно описать в карте конфигурации контроллера метод *configureActions*:

```
class Test extends \Bitrix\Main\Engine\Controller
{
	public function configureActions()
	{
		return [
			'testoPresto' => [
				'class' => \TestAction::class,
				'configure' => [
					'who' => 'Me',
				],
			],
		];
	}
}
```

И вот сам TestAction:

```
<?php

use \Bitrix\Main\Engine\Action;

class TestAction extends Action
{
	protected $who;

	//метод для дополнительного конфигурирования из контроллера. Если требуется установить
	//какие-то значения во внутреннее состояние
	public function configure($params)
	{
		parent::configure($params);

		$this->who = $params['who']?: 'nobody';
	}

	//основной метод работы. Параметры так же автоматически связываются, как и в методе
	//аякс-действии
	public function run($objectId = null)
	{
		return "Test action is here! Do you know object with id {$objectId}? Mr. {$this->who}";
	}
}
```

Для вызова этого действия нужно обращаться к нему **testoPresto**, как описано в карте конфигурации. Класс-действие поддерживает пре- и пост-фильтры и по сути ничем не отличается от обычного метода-действия. Смысл метода *run()* аналогичен другим методам аякс-действиям.

#### Использование контроллеров внутри компонентов

Предпочтительно создавать и использовать классы контроллеров, которые располагаются в модулях, как указано в данной статье, так как позволяет лучше организовать повторное использование вспомогательного кода и бизнес-логики.

В простых случаях, если компонент самодостаточен и не используется активно с API-модуля, то можно использовать [контроллеры внутри компонента](lesson_14014.md).



### Жизненный цикл контроллера

При обработке запроса [Application](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/index.php) создаёт контроллер на основе [соглашения по именованию](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=03750#sogl). Далее работу выполняет контроллер:

- *Controller::init()* будет вызван после того, как контроллер создан и сконфигурирован.
- Контроллер создает объект действия

  - Если действие не удалось создать, выкидывается исключение.
- Контроллер вызывает метод подготовки параметров *Controller::prepareParams*.
- Контроллер вызывает метод *Controller::processBeforeAction(Action $action)*, в случае возврата *true* выполнение продолжается.
- Контроллер выкидывает событие модуля **main** *{полное_имя_класс_контроллера}::onBeforeAction*, в случае возврата *EventResult* не равном `EventResult::SUCCESS` выполнение блокируется. На данном событии выполняются [префильтры](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/actionfilter/index.php).
- Контроллер запускает действие

  - Параметры действия будут [сопоставлены](lesson_21162.md) с данными из запроса
- Контроллер выкидывает событие модуля **main** *{полное_имя_класс_контроллера}::onAfterAction*. На данном событии выполняются [постфильтры](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/actionfilter/index.php).
- Контроллер вызывает метод`Controller::processAfterAction(Action $action, $result)`.
- Приложение получает результат выполнения действия и если это данные, то создает `\Bitrix\Main\Engine\Response\AjaxJson` с этими данными, либо отправляет объект ответа от действия.
- Приложение вызывает метод *Controller::finalizeResponse($response)*, передавая финальный вариант ответа, который будет отправлен пользователю после всех событий и подготовок.
- Вывод $response пользователю.



### Несколько namespaces

Указание нескольких namespaces в модуле.

В **.settings.php** можно указать несколько namespaces, помимо defaultNamespace. Это может быть необходимо, когда контроллеры расположены рядом со своими бизнес-сущностями. Например, в некотором модуле "Диск" у нас есть интеграция с облаками.

```
<?php
return [
	'controllers' => [
		'value' => [
			'namespaces' => [
				'\\Bitrix\\Disk\\CloudIntegration\\Controller' => 'cloud', //cloud - это альяс
			],
			'defaultNamespace' => '\\Bitrix\\Disk\\Controller',
		],
		'readonly' => true,
	]
];
```

Теперь у нас доступны для вызова контроллеры, которые расположены в обоих namespaces. Оба из них поддерживают вызов через полное имя действия и через сокращенную запись, так как у нас есть альяс cloud.

Равносильны:

```
disk.CloudIntegration.Controller.GoogleFile.get
disk.cloud.GoogleFile.get

disk.Controller.File.get
disk.File.get
```

### Вызов модульного контроллера с подписанными параметрами компонента

В случае, если вам нужно обратиться к контроллеру, реализованному в модуле, из контекста [компонента](lesson_14014.md), прокинув подписанные параметры, используйте следующий способ:

```
BX.ajax.runAction('socialnetwork.api.user.stresslevel.get', {
	signedParameters: this.signedParameters, // результат $this->getComponent()->getSignedParameters()
	data: {
		c: myComponentName, // например, 'bitrix:intranet.user.profile', параметры которого нам будут нужны
		fields: {
			//..
		}
	}
});
```

После этого внутри кода действия используйте:

```
<?php
	//...
	public function getAction(array $fields)
	{
		//внутри распакованный, проверенный массив параметров
		$parameters = $this->getUnsignedParameters();

		return $parameters['level'] * 100;
	}
```

### Документация

- [АPI класса \Bitrix\Main\Engine\Controller](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/controller/index.php)
