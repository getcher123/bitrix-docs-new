# BX.UI.StepProcessing.Dialog

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/stepprocessing/javascript_api/dialog.php

### Конструктор

Конструктор класса

#### constructor(settings: DialogOptions = {})

Поля структуры для инициализации диалога [DialogOptions](#DialogOptions).

### Опции

Список опций – [DialogOptions](#DialogOptions).

`getSetting(name: $Keys, defaultVal: ?any = null)`

`setSetting(name: $Keys, value: any)`

### Установка коллбек фунций на события окна

`setHandler(type: string, handler: any => void)`

`callHandler(type: string, args: {[string]: any})`

### Старт/стоп

`start()`

`stop()`

### Скрыть/показать

`show()`

`close(`

### Кнопки диалога

Поля структуры для инициализации полей ввода на диалоге – [OptionsField](types.php.md#OptionsField).

`getButton(bid: string): ?Button` – Ссылка на объект кнопки.

`lockButton(bid: string, lock: boolean, wait: boolean)` – Блокировка/Ожидание/Разблокировка кнопки.

`showButton(bid: string, show: boolean)` – Скрыть/Показать кнопку.

### Аннотация о ходе прогресса

`setSummary(content: string, isHtml: boolean = false)` – Установка текста аннотации.

`setDownloadButtons(downloadLink: string, fileName: string, purgeHandler: any => {})` – Установка кнопок для скачивания файла.

### Ошибки и предупреждения

`setErrors(errors: Array, isHtml: bool = false)` – Вывод текста ошибки.

`setError(content, isHtml)` – Вывод текста ошибки.

`clearErrors()` – Сброс ошибок.

`setWarning(err: string, isHtml: boolean = false)` – Вывод текста предупреждения.

`clearWarnings()`

### Прогресс-бар

`setProgressBar(totalItems: number, processedItems: number, textBefore: string)` – Установка значения прогресса.

`hideProgressBar()`

### Поля для ввода пользователем

`getOptionField(name: string): ?BaseField` – Ссылка на объект кнопки.

`getOptionFieldValues()` – Установленные значения на полях.

`checkOptionFields(): boolean` – Проверка заполненности полей.

`lockOptionFields(flag: boolean = true)` – Блокировать ввод в поля пользователем.

### BX.UI.StepProcessing.DialogOptions

Поля структуры для инициализации диалога.

`messages?: {}` – Фразы на диалоге:

- `title` – Заголовок.
- `summary` – Аннотация.
- `startButton` – Кнопка старт.
- `stopButton` – Кнопка стоп.
- `closeButton` – Кнопка закрыть.

`minWidth?: number` – Минимальная ширина диалога.

`maxWidth?: number` – Максимальная ширина диалога.

`optionsFields?: Array` – Поля для ввода пользователем [OptionsField](types.php.md#OptionsField).

`optionsFieldsValue?: {}` – Значения для полей ввода.

`showButtons?: {}` – Какие кнопки отобразить на диалоге:

- `start?: boolean`
- `stop?: boolean`
- `close?: boolean`

`handlers?: {}` – Коллбек  функции на окне:

- `start?: function` – Клик по Старт./li>
  `stop?: function` – Клик по Стоп.
  `dialogShown?: function` – Показ диалога.
  `dialogClosed?: function` – Скрытие диалога.
