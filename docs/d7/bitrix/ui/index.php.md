# UI-библиотека

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/index.php

UI-библиотека (user interface) — это библиотека пользовательских интерфейсов. Основная задача модуля — стандартизировать и централизовать управление стилями и поведением типовых элементов, таких как: кнопки, формы, иконки, табы и так далее.

Модуль несет системный характер. Его нельзя ни отключить, ни удалить. Он подключается автоматически при его использовании. Остальное время модуль неактивен.

### Расширения

| Название | Описание |
| --- | --- |
| [color_picker](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/color_picker/introduction.php) | Диалог выбора цвета |
| [spotlight](spotlight/introduction.php.md) | Элемент интерфейса в виде пульсирующего круга |
| [ui.advice](ui_advice.php.md) | Блок с советом |
| [ui.alerts](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/messages/alerts.php) | Сообщения |
| [ui.banner-dispatcher](ui_banner_dispatcher.php.md) | Диспетчер баннеров |
| [ui.buttons](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/buttons/button.php) | Кнопки |
| [ui.confetti](confetti/index.php.md) | Конфетти |
| [ui.countdown](ui_countdown.php.md) | Таймер обратного отсчета |
| [ui.counter](counter/index.php.md) | Счетчики |
| [ui.dialogs.checkbox-list](ui_dialogs_checkbox_list.php.md) | Попап с чекбоксами для настройки вывода вашего контента |
| [ui.dialogs.messagebox](dialogs/index.php.md) | Создание стандартных диалогов типа alert и confirm |
| [ui.ears](ears/index.php.md) | Кнопки прокрутки «уши» |
| [ui.entity-catalog](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/entity_catalog/intro.php) | Каталог элементов |
| [ui.entity-selector](entity_selector/index.php.md) | Диалог выбора сущностей |
| [ui.feedback.form](feedback_form/index.php.md) | Формы обратной связи |
| [ui.forms](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/forms/common.php) | Формы |
| [ui.hint](hint/index.php.md) | Подсказки |
| [ui.icons](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/icons/common.php) | Иконки |
| [ui.icon-set](icon_set/index.php.md) | Сет иконок из библиотеки |
| [ui.inputmask](ui_inputmask.php.md) | Маска ввода |
| [ui.label](labels/index.php.md) | Метки |
| [ui.layout-form](layout_form/index.php.md) | Формы с сеткой |
| [ui.menu-configurable](menu_configurable/index.php.md) | Настраиваемое меню |
| [ui.notification](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/notification/start.php) | Нотификации |
| [ui.progressbar](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/progressbar/common.php) | ПрогрессБар |
| [ui.progressround](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/progressbar/api_progressround.php) | Круглый ПрогрессБар |
| [ui.reactions-select](reactions_select/index.php.md) | Компонент для выбора реакции |
| [ui.select](select/index.php.md) | Компонент для выбора элемента из списка |
| [ui.sidepanel-content](sidepanel_content/index.php.md) | Типовое использование контентного слайдера |
| [ui.sidepanel.layout](sidepanel_layout/index.php.md) | Верстка контентного слайдера |
| [ui.stageflow](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/stageflow/stageflow.php) | Отрисовка последовательности стадий в верхней карточке элемента |
| [ui.stepbystep](stepbystep/index.php.md) | Компонент-обёртка для пошаговых блоков |
| [ui.stepprocessing](stepprocessing/basics.php.md) | Диалог для пошагового процесса |
| [ui.textanimate](textanimate/index.php.md) | Анимация смены текста |
| [ui.textcrop](textcrop/index.php.md) | Сокращение текста по высоте |
| [ui.timeline](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/timeline/timelineitem.php) | Таймлайн |
| [ui.toolbar](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/toolbar/get_started.php) | Тулбар |
| [ui.tooltip](tooltip/index.php.md) | Тултип с карточкой пользователя |
| [ui.tour](tour/index.php.md) | Тур |
| [ui.video-player](uivideoplayer/index.php.md) | Видеоплеер |
| [ui.viewer](viewer/index.php.md) | Просмотрщик |
| [ui.userfield](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/userfield.php) | Модель настроек пользовательского поля |
| [ui.userfieldfactory](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/userfieldfactory.php) | Фабрика настроек пользовательских полей |

### Компоненты

| Название | Описание |
| --- | --- |
| [bitrix:spotlight](spotlight/bitrix_spotlight.php.md) | Выводит подсказку на странице около указанного DOM-элемента |
| [bitrix:ui.sidepanel.wrapper](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/sidepanel_wrapper/start.php) | Является оберткой для вывода целевого компонента в слайдере |
| [bitrix:ui.button.panel](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/button_panel/start.php) | Выводит панель с кнопками отправки формы |
| [bitrix:ui.toolbar](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/toolbar/get_started.php) | Выводит тулбар с кнопками и фильтром |
| [bitrix:ui.tour](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/tour/component.php) | Выводит подсказку на странице около указанного DOM-элемента |

### Примеры

Универсальный пример  получения доступа к API поля. С помощью этого API устанавливаются значения, удаляются значения и так далее.

```
// Получаем ссылку на DOM-элемент поля
var element = document.querySelector("[data-name=\"sEmployeeGroup\"]");
// Получаем запись из BX.Main.ui.Factory
var field = BX.Main.ui.Factory.get(element);

if (field)
{
	// Получаем ссылку на экземпляр класса поля
	var fieldInstance = field.instance;

	// Далее можно использовать API:

	// Установка значения для поля типа main-ui-select
	fieldInstance.updateValue(fieldInstance.getItems()[0]);
	fieldInstance.updateDataValue(fieldInstance.getItems()[0]);

	// Установка значения для поля типа main-ui-multi-select
	fieldInstance.selectItem(fieldInstance.getItems()[0]);
	// Удаление значения для поля типа main-ui-multi-select
	fieldInstance.unselectItem(fieldInstance.getItems()[0]);
}
```

Как через js библиотеку BX поменять настройки фильтра на странице.

```
var filter = BX.Main.filterManager.getById('my_filter_id');

if (filter) {
	var filterApi = filter.getApi();
	filterApi.setFields({'NAME': 'main 17.0.7'});
	filterApi.apply();
}
```

#### Смотрите также:

- [Стандартные диалоги Alert и Confirm](https://dev.1c-bitrix.ru/api_help/js_lib/dialogs/index.php)
- [SidePanel - Слайдер](../../../js_lib/sidepanel/index.md)
