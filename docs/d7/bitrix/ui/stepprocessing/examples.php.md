# Примеры

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/stepprocessing/examples.php

### Импорт данных из файла

```
// javascript
var progress = (new BX.UI.StepProcessing.Process({
		'id': 'awesome',
		'controller': 'bitrix:awesome.dancer'
	})
	// установить всю очередь заданий
	.setQueue([
		{'action': 'upload', 'title': 'Загрузка'},
		{'action': 'parse', 'title': 'Разбор'}
	])
	// добавить отдельное задание
	.addQueueAction({'action': 'finalize', 'finalize':  true})

	// установить поля на стартовый диалог
	.setOptionsFields({
		'convertEncoding': {
			'name' 'allowConvert',
			'type' 'checkbox',
			'title' Loc::getMessage('ALLOW_CONVERT'),
			'value' true,
		},
		'languages': {
			'name': 'languages',
			'type': 'select',
			'multiple': true,
			'size': 10,
			'title': Loc::getMessage('LANGUAGES'),
			'list': ['all': Loc::getMessage('LANGUAGES_ALL'), 'ru': 'ru', ...],
			'value': 'all',
		},
	})
	// добвить отдельное поле
	.addOptionsField('csvFile', {
		'name': 'csvFile',
		'type': 'file',
		'title': Loc::getMessage('TR_UPLOAD_CSV_FILE'),
		'obligatory': true,
		'emptyMessage': Loc::getMessage('TR_UPLOAD_CSV_FILE_EMPTY_ERROR'),
	})

	// параметры запроса
	.setParams({
		'key': 'any value',
		'path': '/somewhere/',
	})
	.setParam('key', 'any value')

	// фразы, выводимые на диалог и кнопки
	.setMessages({
		'DialogTitle': 'Импорт', // обязательно необходимо определить
		'DialogSummary': 'Импорт данных', // обязательно необходимо определить
		'DialogStartButton': 'Старт',
		'DialogStopButton': 'Стоп',
		'DialogCloseButton': 'Закрыть',
		'RequestCanceling': 'Отменяю..',
		'RequestCanceled': 'Процесс остановлен',
		'RequestCompleted': 'Готово!',
	})
	.setMessage('DialogStartButton', 'Старт')

	// функции коллбеки
	.setHandler(
		BX.UI.StepProcessing.ProcessCallback.StateChanged,
		function (state, result)
		{
		/** @type {BX.UI.StepProcessing.Process} this */
		if (state === BX.UI.StepProcessing.ProcessResultStatus.completed)
			{
				var grid = BX.Main.gridManager.getById(gridId);
				grid.reload();
				this.closeDialog();
			}
		}
	)
;
```

```
HTML
<button onclick="BX.UI.StepProcessing.ProcessManager.get('awesome').showDialog()" class="ui-btn ui-btn-primary">Импорт</button>
```

### Дополнить параметры запроса на шаге

```
// javascript
var progress = (new BX.UI.StepProcessing.Process({
		'id': 'awesome',
		'controller': 'bitrix:awesome.dancer'
	})
	// функция колбек, вызываемая непосредственно для отправки ajax запроса
		.setHandler(
			BX.UI.StepProcessing.ProcessCallback.RequestStart,
			function(actionData)
			{
				/**
				* @var {FormData} actionData
				* @var {BX.UI.StepProcessing.Process} this
				*/
			actionData.append('smthg', 'got it!');
			}
		);
```

### Параметры для запроса с формы на странице

```
// процесс
var process = (new BX.UI.StepProcessing.Process({
		id: 'import',
		controller: 'bitrix:jobworking'
	}))
	// очередь заданий
	.addQueueAction({'action': 'dosmth', 'title': 'Делаю'})
	.setMessag('RequestCompleted', 'Сделал!');

var form = document.forms['form'];
process
	.setParams(BX.ajax.prepareForm(form).data)
	.showDialog()
	.start();
```

### Перехват события DropFile в рабочей области

```
// capture file drop event
	BX("adm-workarea").ondrop = function (evt)
	{
		// процесс
		var process = (new BX.UI.StepProcessing.Process({
			id: 'import',
			controller: 'bitrix:importer'
		}))
		// поле типа файл
		.addOptionsField('File', {'type': 'file'})
		 // очередь заданий
		.addQueueAction({'action': 'upload', 'title': 'Загрузка'})
		.addQueueAction({'action': 'parse', 'title': 'Разбор'})
		.addQueueAction({'action': 'finalize', 'finalize':  true})
		.setMessag('RequestCompleted', 'Готово!')
		// вывести диалог
		.showDialog();

		// поле ввода типа file
		var fileInput = process.getDialog().getOptionField('File');
		if (fileInput)
		{
			// установка значания файла из события
			fileInput.setValue(evt.dataTransfer.files);
		}

		// старт
		process.start();

		evt.preventDefault();
	};
```

### Передача данных между итерациями

Если требуется передавать данные между итерациями одного шага то используйте колбек `StepCompleted`, который вызывается каждый раз когда приходит ответ от сервера.

```
// payload action step
.addQueueAction({
	'title': 'Действие',
	'action': 'someAction',
	'handlers': {
		// сохраним значения total и processed между запросами
		'StepCompleted': function (state, result)
		{
			 /** @type {BX.UI.StepProcessing.Process} this */
			if (state === BX.UI.StepProcessing.ProcessResultStatus.progress)
			{
				var fields = this.getParam('fields') || [];
				if (result.TOTAL_ITEMS)
				{
					fields.totalItems = parseInt(result.TOTAL_ITEMS);
				}
				if (result.PROCESSED_ITEMS)
				{
					fields.processedItems = parseInt(result.PROCESSED_ITEMS);
				}
				this.setParam('fields', fields);
			}
		}
	}
})
```
