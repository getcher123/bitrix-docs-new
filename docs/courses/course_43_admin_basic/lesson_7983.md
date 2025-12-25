# "Ленивые" параметры в событиях

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2816 — Дополнительно](lesson_2816.md)
- [Следующий: 3578 — Комплексный компонент и SEF режим →](lesson_3578.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=7983

Чтобы отправить событие выполните следующее:

```
use Bitrix\Main\EventManager;

$event = new \Bitrix\Main\Event('moduleName', 'onEventName', array(
	'data' => array(
		'name' => 'John',
		'sex' => 'male',
		),
	'datetime' => new \Datetime(),
));

$event->send();
```

Таким образом отправится событие от модуля **moduleName** с именем **onEventName** и данными, которые будут доступны в обработчиках этого события.

В некоторых ситуациях вычисление данных для отправки требует привлечения дополнительных ресурсов. В такой ситуации  сконфигурируйте объект иначе:

```
use Bitrix\Main\EventManager;

$lazyEvent = new \Bitrix\Main\Event('moduleName', 'onEventName', function() use ($userId){

//какая-то работа, которая получает данные
	$groups = loadUserGroups($userId);

	return array(
		'data' => array(
			'name' => 'John',
			'sex' => 'male',
			'groups' => $groups,
		),
		'datetime' => new \Datetime(),
	);
});

$Lazyevent->send();
```

В таком случае вычисление параметров события будет отложено до первого обращения к ним в обработчике. В итоге получается два преимущества:

1. Если нет обработчиков, то не будут запускаться вычисления.
2. Если в обработчиках не используются параметры события, то снова не будут запускаться вычисления.

**Примечание**: Доступно с версии главного модуля 17.0.0.
