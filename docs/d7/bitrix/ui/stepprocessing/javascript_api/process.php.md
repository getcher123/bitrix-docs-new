# BX.UI.StepProcessing.Process

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/stepprocessing/javascript_api/process.php

### Конструктор

Конструктор класса

#### constructor(options: ProcessOptions)

Поля структуры для инициализации процесса [ProcessOptions](types.php.md#ProcessOptions).

### Старт / стоп

`start(startStep?: number = 1)` – Стартует обработку очереди заданий. Необязательный аргумент  – номер позиции в очереди.

`stop()`  – Отмена обработки очереди.

`startRequest()`  – Отправляет запрос текущего задания

`stopRequest()`  – Прерывает запрос текущего задания и отправляет на дефолтный контролер действие `cancel`. Контроллер должен реализовать действие с таким именем.

`finalizeRequest()`  – отправляет на дефолтный контролер действие `finalize`, предназначенное для освобождения ресурсов и очистки временных данных. Контроллер должен реализовать действие с таким именем.

### Установка заданий очереди

Поля структуры задания очереди – [QueueAction](types.php.md#QueueAction).

`setQueue(queue: Array)` – Установить всю очередь заданий.

`addQueueAction(action: QueueAction)` – Добавить отдельное задание.

`getQueueLength(): number` – Длина очереди.

### ID процесса

Уникальный код процесса в контексте страницы.

`setId(id: string)`

`getId(): string`

### Опции процесса

Опции описаны в структуре для инициализации процесса – [ProcessOptions](types.php.md#ProcessOptions).

`setOption(name: $Keys, value: any)`

`getOption(name: $Keys, defaultValue?: any = null): any`

### Поля для ввода пользователем на стартовой странице

Поля структуры для инициализации полей ввода на диалоге – [OptionsField](types.php.md#OptionsField).

`setOptionsFields(optionsFields: {[id: string]: OptionsField})` – Установить сразу все поля.

`addOptionsField(id: string, field: OptionsField)` – Добавить отдельное поле.

`storeOptionFieldValues(values: {[name: string]: any})` – Сохранить стартовые значения в sessionStorage.

`restoreOptionFieldValues()` – Восстановить значения из sessionStorage.

### Параметры запроса

`setParams(params: {[name: string]: any})`

`getParams(): {[string]:any}`

`setParam(key: string, value: any)`

`getParam(key: string): any | null`

### Состояние процесса

Описания состояний – [ProcessState](types.php.md#ProcessState).

`setState(state: $Values, result?: ProcessResult = {})` – Устанавливает новое состояние процесса.

`getState(): $Values`

### Контроллер

Описание контроллера.

`setController(controller: string)` – Устанавливает контроллер, которому будут отправляться запросы.

`getController(): string`

`setComponent(component: string, componentMode: 'class'|'ajax' = 'class')` – Устанавливает контроллер компонента, которому будут отправляться запросы.

`getComponent(): string`

### Действие

Описание действий контроллера.

`setAction(action: string)`

`getAction(): string callAction(action: string)`

### Функции коллбеки

Типы вызовов – [ProcessCallback](types.php.md#ProcessCallback).

`setHandlers(handlers: {[$Keys]: any => {}})`

`setHandler(type: $Keys, handler: any => {})`

`hasHandler(type: $Keys)`

`callHandler(type: $Keys, args: any)`

`hasActionHandler(type: $Keys)`

`callActionHandler(type: $Keys, args: any)`

### Фразы, выводимые на диалог и кнопки

[Типы фраз](types.php.md#Phrases).

`setMessages(messages: {[string]: string})`

`setMessage(id: string, text: string)`

`getMessage(id: string, placeholders?: {[string]: string} = null): strin`

### Диалог

`getDialog(): Dialog` – Получить ссылку на инстанс объекта диалога для текущего процесса [Dialog](dialog.php.md).

`showDialog ()` – Отобразить диалог.

`closeDialog ()` – Скрыть диалог.
