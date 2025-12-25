# Подписка на события модуля

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2282 — Push & Pull для гостей](lesson_2282.md)
- [Следующий: 2290 — Примеры агентов →](lesson_2290.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=12173

### Подписка

До версий  pull 18.5.7 (для десктопов) и mobile 18.5.10 (для мобильных устройств) для разработчиков существовали три проблемы при подписке на события модуля Push&Pull:

1. Невозможно было одним кодом реализовать подписку на обоих типах устройств.
2. В силу первого пункта приходилось обрабатывать много разных команд, получая "лапшу" из if'ов, что, помимо сложной ориентации в коде, выдавало неинформативный результат в отладчике в случае возникновения ошибки (вывод стек-трейса).
3. Если требовалось обработать всего одну команду, то использование конструкции с одним if или целом классом было слишком многословным.

Начиная с указанных версий подключение к событиям модуля Push&Pull реализовано с помощью метода [BX.PULL.subscribe](https://dev.1c-bitrix.ru/api_help/push_pull/classes/bx_pull_subscribe/index.php). Как работать с этим методом, рассказано ниже.

### Подключение библиотеки

В рамках компонентов, которые используются только в браузере, нужно обязательно проверить наличие модуля Push & Pull, а также подключить библиотеку **pull.client**:

- Укажите CoreJS зависимость pull.client в описании вашего расширения или вызовите `\Bitrix\Main\UI\Extension::load('pull.client')`;
- Для веб-страницы укажите CoreJS зависимость **mobile.pull.client** в описании расширения или вызовите `\Bitrix\Main\UI\Extension::load('mobile.pull.client')`;
- Для JaNative component, укажите зависимость `pull/client/events` в файле **deps.php**.
- Для Offline WebComponent укажите зависимость `pull/client/events` в файле **config.php** в разделе deps.

В рамках мобильного расширения вы можете использовать методы:

BX.PULL.subscribe(...),
 BX.PULL.extendWatch(...),
 BX.PULL.clearWatch(...),
 BX.PULL.capturePullEvent(),
 BX.PULL.getDebugInfo().

Для подписки есть три формата, вы можете выбрать для себя подходящий в зависимости от ваших задач.

### Одна команда

Подписка на одну команду:

```
BX.PULL.subscribe({
	type: BX.PullClient.SubscriptionType.Server,
	moduleId: 'im',
	command: 'messageChat',
	callback: function (params, extra, command) {
		console.warn('Receive message:', params.message.text)
	}.bind(this)
});
```

Где:

**type** - тип подписки (Server, Client, Online) - можно не указывать, по умолчанию будет тип Server,

**moduleId** - модуль отправивший команду

**command** - команда на которую осуществляется подписка

**callback** - функция обработчик.

Параметры метода, который будет вызван при наступления события следующие:

- **params** - объект, параметры команды,
- **extra** - объект, дополнительные данные такие как версия модуля, имя и время сервера, время с момента отправки команды,
- **command** - строка, название команды.

Результатом выполнения метода будет функция c помощью которой вы сможете отписаться от указанной команды в будущем:

```
let unsubscibe = BX.PULL.subscribe({...}); // подписка
unsubscibe(); // отписка
```

### Несколько команд

Подписка на множество команд с помощью функции маршрутизатора:

```
BX.PULL.subscribe({
	type: BX.PullClient.SubscriptionType.Server,
	moduleId: 'im',
	callback: function (data) {
		if (data.command == 'messageAdd')
		{
			this.doSomething();
		}
	}.bind(this)
});
```

Где:

**type** - тип подписки (Server, Client, Online) - можно не указывать, по умолчанию будет тип Server,

**moduleId** - модуль отправивший команду,

**callback** - функция обработчик для всех поступающих команд.

В параметре **data** в указанной callback функции будет предоставлен следующий объект:

```
{
	command: '...', // название команды
	params: {...}, // параметры команды
	extra: {...} // дополнительные данные такие как версия модуля, имя и время сервера, время с момента отправки команды
}
```

Результатом выполнения метода будет функция c помощью которой вы сможете отписаться от команд модуля в будущем.

```
let unsubscibe = BX.PULL.subscribe({...}); // подписка
unsubscibe(); // отписка
```

### Класс маршрутизации

Подписка с помощью класса маршрутизации:

```
BX.PULL.subscribe(new CommandHandler(options));
```

В **options** вы можете передать ссылку на нужные вам объекты, например на текущий контекст, чтобы в рамках класса-обработчика вызывать методы из вашего базового класса (если это требуется).

Сам класс маршрутизации выглядит так (обратите внимание: класс написан на ES6, но возможно и применение класса в формате ES5)

```
class CommandHandler
{
	constructor(options = {})
	{
	}

	getModuleId()
	{
		return 'im';
	}

	getSubscriptionType()
	{
		return BX.PullClient.SubscriptionType.Server;
	}

	getMap()
	{
		return {
			message: this.handleMessage.bind(this),
			messageChat: this.handleMessageChat.bind(this),
			startCall: this.handleStartCall.bind(this),
		};
	}

	handleMessage(params, extra, command)
	{
		console.log('exec command - message', params);
	}

	handleMessageChat(params, extra, command)
	{
		console.log('exec command - messageChat', params);
	}

	handleStartCall(params, extra, command)
	{
		console.log('exec command - startCall', params);
	}
}
```

Метод *getModuleId()* должен возвращать идентификатор модуля, команды которого будет обрабатывать данный класс. (Обязательный метод).

Метод *getSubscriptionType()* должен возвращать тип подписки (Server, Client, Online). (Не обязательный метод, если не указать, будет тип Server)

Метод *getMap()*должен возвращать карту соответствия команды поступающей от сервера и метода который будет его обрабатывать.

### Форматы объекта

Возможные форматы объекта возвращаемого функцией *getMap()*.

В формате ссылки на функцию, рекомендованный вариант, т.к. в IDE можно будет быстро перейти к функции просто кликнув на неё:

```
{
	startCall: this.handleStartCall.bind(this),
}
```

В формате строки:

```
{
	startCall: 'handleStartCall',
}
```

В формате callback функции:

```
{
	startCall: function(params, extra, command) {
		console.log('exec command - startCall', params);
	}.bind(this),
}
```

Параметры метода, который будет вызван при наступления события следующие:

- **params** - объект, параметры команды
- **extra** - объект, дополнительные данные такие как версия модуля, имя и время сервера, время с момента отправки команды
- **command** - строка, название команды

**Упрощенный вариант описания**

Вы можете упростить описание класса, опустив описание метода *getMap()*, тогда методы обработки команд должны начинаться со слова **handle**. Далее должно следовать название команды, где первая буква будет заглавной, например у вас есть команда startCall, в классе должен быть метод *handleStartCall*.

```
class CommandHandler
{
	constructor(options = {})
	{
	}

	getModuleId()
	{
		return 'im';
	}

	handleMessage(params, extra, command)
	{
		console.log('exec command - message', params);
	}

	handleMessageChat(params, extra, command)
	{
		console.log('exec command - messageChat', params);
	}

	handleStartCall(params, extra, command)
	{
		console.log('exec command - startCall', params);
	}
}
```

Результатом выполнения метода будет функция, c помощью которой вы сможете отписаться от команд модуля в будущем.

```
let unsubscibe = BX.PULL.subscribe({...}); // подписка
unsubscibe(); // отписка
```

**Гибридный вариант описания**

Вы можете использовать одновременно *getMap()* и методы по стандартам именования **CommandHandler**. Такой вариант подойдет, если вы хотите сделать alias к устаревшему формату команд или если вы отправляете команды в формате который невозможно описать в названии метода.

```
class CommandHandler
{
	constructor(options = {})
	{
	}

	getModuleId()
	{
		return 'im';
	}

	getMap()
	{
		return {
			'Application::send': this.handleApplicationSend.bind(this),
			messageChatAdd: this.handleMessageChat.bind(this)
		};
	}

	handleMessage(params, extra, command)
	{
		console.log('exec command - message', params);
	}

	handleMessageChat(params, extra, command)
	{
		console.log('exec command - messageChat', params);
	}

	handleStartCall(params, extra, command)
	{
		console.log('exec command - startCall', params);
	}

	handleApplicationSend(params, extra, command)
	{
		console.log('exec command - applicationSend', params);
	}
}
```

**Внимание!**. Если команда описана в *getMap()* и у вас есть метод для этой команды названный по стандартам именования CommandHandler, то приоритет вызова будет отдан *getMap()*.

Результатом выполнения метода будет функция c помощью которой вы сможете отписаться от команд модуля в будущем.

```
let unsubscibe = BX.PULL.subscribe({...}); // подписка
unsubscibe(); // отписка
```
