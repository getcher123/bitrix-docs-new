# История изменений

Источник: https://dev.1c-bitrix.ru/api_d7/history.php

#### Сентябрь 2025

- Добавлено описание метода [resolveHighloadblock](bitrix/highloadblock/highloadblocktable/resolvehighloadblock.php.md) в классе [HighloadBlockTable](bitrix/highloadblock/highloadblocktable/index.php.md)

#### Август 2025

- Добавлено расширение [ui.avatar](bitrix/ui/ui_avatar.php.md) для отображения аватаров пользователей в различных стилях и формах
- Добавлено расширение [ui.field-selector](bitrix/ui/ui_field_selector.php.md), которое создает поле выбора сущностей

#### Июль 2025

- Добавлен компонент [ui.system.menu](bitrix/ui/vue_components/system_menu.php.md), который представляет собой выпадающее меню
- Добавлено расширение [ui.actions-bar](bitrix/ui/ui_actions_bar.php.md). Оно задает стили для компоновки панели действий

## 2024

#### Март 2024

- Добавлена библиотека [iblock.field-selector](bitrix/iblock/iblock_field_selector.php.md) для реализации списочных полей с быстрым поиском

#### Январь 2024

- Добавлено событие [OnHttpClientBuildRequest](bitrix/main/web/httpclient/events/onhttpclientbuildrequest.php.md), которое вызывается после создания объекта запроса, позволяя донастроить опции клиента и изменить объект запроса.
- В разделе [HttpClient](bitrix/main/web/httpclient/index.php.md) новые страницы:

  - [Режим legacy](bitrix/main/web/httpclient/legacy.php.md)
  - [PSR-18: HTTP Client](bitrix/main/web/httpclient/psr18.php.md)
  - [Асинхронные запросы](bitrix/main/web/httpclient/asynchronous_requests.php.md)
  - [Библиотека CURL](bitrix/main/web/httpclient/curl.php.md)
  - [Proxy](bitrix/main/web/httpclient/proxy.php.md)
  - [Логирование](bitrix/main/web/httpclient/logging.php.md)

## 2023

#### Декабрь 2023

- Добавлены [идентификаторы](bitrix/iblock/propertytable/index.php.md) пользовательских типов свойств инфоблока.
- Добавлена глава [Служба сообщений](bitrix/messageservice/index.php.md) о работе с провайдерами и отправке сообщений.

#### Июль 2023

- [Новый раздел](bitrix/ui/stepprocessing/javascript_api/index.php.md) JS API для диалога для пошаговых процессов.
- Компонент-обёртка [ui.stepbystep](bitrix/ui/stepbystep/index.php.md) для пошаговых блоков.
- Добавлено расширение [ui.menu-configurable](bitrix/ui/menu_configurable/index.php.md) для отрисовки настраиваемого списка пунктов меню.
- Добавлены примеры типового использования внутреннего контента слайдера [ui.sidepanel-content](bitrix/ui/sidepanel_content/index.php.md).
- Добавлена глава о верстке контентного слайдера [ui.sidepanel.layout](bitrix/ui/sidepanel_layout/index.php.md).
- Добавлено Javascript-расширение [ui.viewer](bitrix/ui/viewer/index.php.md), позволяющее автоматически просматривать разные типы файлов.
- Добавлено Javascript-расширение [ui.viewer](bitrix/ui/viewer/index.php.md), позволяющее автоматически просматривать разные типы файлов.
- Добавлено Javascript-расширение [ui.labels](bitrix/ui/labels/index.php.md), позволяющее показывать информационные метки (labels, badges) на странице.
- [Компонент](bitrix/ui/reactions_select/index.php.md) для выбора реакции.
- [Компонент](bitrix/ui/select/index.php.md) для выбора элемента из списка.
- Добавлено Javascript-расширение [ui.layout-form](bitrix/ui/layout_form/index.php.md), содержащее стили для построения сетки для форм.
- Добавлено Javascript-расширение [ui.feedback.form](bitrix/ui/feedback_form/index.php.md) для вызова формы обратной связи.
- Добавлено Javascript-расширение [ui.ears](bitrix/ui/ears/index.php.md) для подключения для нужного элемента на странице кнопок прокрутки.
- Добавлено Javascript-расширение [ui.confetti](bitrix/ui/confetti/index.php.md) Конфетти.
- Добавлено Javascript-расширение [ui.textanimate](bitrix/ui/textanimate/index.php.md) для анимации смены текста.
- Добавлено Javascript-расширение [ui.tour](bitrix/ui/tour/index.php.md) для организации визуального тура по странице.

#### Июнь 2023

- Добавлены [константы](bitrix/iblock/propertytable/index.php.md) пользовательских типов свойств инфоблока.
- [Метод](bitrix/imconnector/connector/getimmessengerurl.php.md) получения ссылки на Telegram-бота.
- [Чат-трекер](bitrix/imopenlines/tracker/index.php.md) для связи чата открытой линии с другими сущностями.
- В классе [Restriction](bitrix/sale/classes/services/base/restriction/index.php.md) новые методы: [delete](bitrix/sale/classes/services/base/restriction/delete.php.md), [getCode](bitrix/sale/classes/services/base/restriction/getcode.php.md), [getOnApplyErrorMessage](bitrix/sale/classes/services/base/restriction/getonapplyerrormessage.php.md) и [save](bitrix/sale/classes/services/base/restriction/save.php.md).
- Класс [RestrictionInfo](bitrix/sale/classes/services/base/restrictioninfo/index.php.md) описывает формат, в котором ограничения сервисов хранятся в коллекции.
- Класс [RestrictionManager](bitrix/sale/classes/services/base/restrictionmanager/index.php.md) – менеджер ограничений для сервисов интернет-магазина.

#### Май 2023

- [Новый раздел](bitrix/main/systemcomponents/gridandfilter/mainuigrid/index.php.md) о системном компоненте main.ui.grid для визуального представления данных в виде таблицы.

## 2022

#### Май 2022

- [Новый параметр](bitrix/sale/events/sale_entitysaved.php.md) `IS_NEW` для события `OnSaleShipmentEntitySaved`.

#### Апрель 2022

- [События объединения сущностей](bitrix/crm/merger/events/index.php.md)
- [Клиенты в CRM](bitrix/crm/clients_crm.php.md)
- [Работа с элементами](bitrix/crm/elements.php.md)

#### Февраль 2022

- Новая опция [avatarOptions](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/entity_selector/dialog/javascript_api/item.php), отвечающая за дополнительные настройки аватара элемента. Новые методы **getAvatarOption**, **setAvatarOption** и **setAvatarOptions**.
- Новые стандартные провайдеры: [Провайдер чатов](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/entity_selector/providers/standard_providers/chat_provider.php) и [Провайдер чат-ботов](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/entity_selector/providers/standard_providers/bot_provider.php).

#### Январь 2022

- Новые методы работы с сущностью Сайт: [addFolder](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/addfolder.php), [updateFolder](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/updatefolder.php), [getFolder](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/getfolder.php), [getFolders](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/getfolders.php), [copyFolders](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/copyfolders.php), [getPreview](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/getpreview.php), [publication](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/publication.php), [unpublic](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/unpublic.php), [markFolderDelete](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/markfolderdelete.php), [markFolderUnDelete](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/markfolderundelete.php).
- Новые методы работы с объектом: [clearFolderIndex](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/clearfolderindex.php), [clearFolderIndex](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/clearfolderindex.php), [favoriteBlock](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/favoriteblock.php), [move](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/move.php), [resolveIdByPublicUrl](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/resolveidbybublicurl.php).
- Новые методы работы с правами в модуле Сайты24: [clearContextUserId](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/rights/general/clearcontextuserid.php), [setContextUserId](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/rights/general/setcontextuserid.php).
- Новое событие в модуле Сайты24: [onBeforeFolderRecycle](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/events/onbeforefolderrecycle.php).
- Новые параметры в компоненте: [ui.sidepanel.wrapper](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/sidepanel_wrapper/view_params.php).

## 2021

#### Декабрь 2021

- Новая страница о [Новый счетах](bitrix/crm/smart_invoice.php.md).
- Новый раздел [Типы сущностей CRM](bitrix/crm/crm_owner_type/index.php.md).

#### Ноябрь 2021

- Новый раздел [Штрих-коды](bitrix/ui/barcode/index.php.md).
- Изменения под версию UI 21.800:

  - Новые разделы: [Счётчики](bitrix/ui/counter/index.php.md) и [Сокращение текста по высоте](bitrix/ui/textcrop/index.php.md)
  - Новый метод: [BX.UI.Icons.Generator.FileIcon](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/icons/icons_generator_fileicon.php)
  - Обновлены: [Параметры отображения](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/sidepanel_wrapper/view_params.php), [API](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/progressbar/api.php), [API Круглого ПрогрессБара](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/progressbar/api_progressround.php)

#### Октябрь 2021

- Новый раздел [Section](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/model/section/index.php).

#### Июль 2021

- Новый раздел [Новое API CRM](bitrix/crm/crm_new_api.php.md).
- Новый раздел [Таймлайн](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/timeline/index.php) в CRM.
- Новый раздел [Смарт-процессы](bitrix/crm/dynamic/index.php.md) в CRM.
- Новая страница [EntityContactTable](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/binding/entitycontacttable/index.php) в \Crm\Binding\.
- Новая страница [Связи](bitrix/crm/relation.php.md).

#### Июнь 2021

- Добавлено описание нового типа entity_selector в [main.ui.filter](bitrix/main/systemcomponents/gridandfilter/mainuifilter.php.md).
- Новый раздел [Диалог выбора сущностей](bitrix/ui/entity_selector/index.php.md) (ui.entity-selector).
- Новая страница [Настраиваемые разделы в левом меню](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/custom_section.php).
- Новая страница [Подготовка платёжной системы](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/cashbox/preparation.php).
- Новая страница [Методы реализации кассы](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/cashbox/cashbox_implementation.php).

#### Март 2021

- Новая глава [Диалог для пошагового процесса](bitrix/ui/stepprocessing/index.php.md).

## 2020

#### Ноябрь 2020

- Новый модуль [Адреса и местоположения](bitrix/location/index.php.md).
- Новая страница [Сайты на локальной установке](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/local.php).
- Новая страница [Entity](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/kanban/entity.php) в CRM/Kanban.
- Новый раздел [Системные компоненты](bitrix/crm/systemcomponents/index.php.md) и компонент [crm.entity.details](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/systemcomponents/crmentitydetails.php) в нём.
- Новый метод [getDefaultValue](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/uf-fieldclass.php).

#### Октябрь 2020

- [Smtp](https://dev.1c-bitrix.ru/api_d7/bitrix/mail/smtp/index.php) - Класс для работы с почтой по SMTP.
- [SessionLocalStorage](https://dev.1c-bitrix.ru/api_d7/bitrix/main/data/localstorage/sessionlocalstorage.php) - АПИ для работы с локальным хранилищем сессий.
- [SessionInterface](https://dev.1c-bitrix.ru/api_d7/bitrix/main/session/sessionInterface/index.php) - АПИ для работы с $_SESSION.
- [ServiceLocator](https://dev.1c-bitrix.ru/api_d7/bitrix/main/di/servicelocator/index.php) - АПИ сервиса локаторов.
- [ActionFilter](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/actionfilter/index.php) -  Фильтры действий AJAX
- [Controller](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/controller/index.php) - Класс методов Контроллера
- [CurrentUser](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/currentuser/index.php) - Класс текущего пользователя
- [Converter](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/response/converter/index.php) - Класс, выполняющий конвертацию строк или массивов, содержащих строки.
- [UrlManager](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/urlmanager/index.php) - Класс-синглтон для построения ссылок на действия AJAX-контроллеров.
- [setLastModified](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/setlastmodified.php) - Метод устанавливает время изменения полей заголовков.
- [Redirect](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/redirect.php) - Класс редиректа
- [AjaxJson](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/ajaxjson.php) - Методы json-ответов.
- [Component](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/component.php) - Методы работы с компонентами.
- [Archive](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/archive.php) - методы работы с архивами.
- [ArchiveEntry](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/archiveentry.php) - Объект, который описывает элемент zip-архива
- [BFile](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/bfile.php) - методы работы с файлами.
- [ResizedImage](https://dev.1c-bitrix.ru/api_d7/bitrix/main/httpresponse/resizedimage.php) - Методы для уменьшения изображений.

#### Сентябрь 2020

- Новая страница [метод addBackgroundJob](https://dev.1c-bitrix.ru/api_d7/bitrix/main/application/addbackgroundjob.php) в классе Application Главного модуля.

#### Июль 2020

- Новая страница [Ограничение времени жизни файлов](https://dev.1c-bitrix.ru/api_d7/bitrix/disk/daylimit.php) в Диске.
- Новый раздел [Права доступа](bitrix/main/access/index.php.md) в Главном модуле.

#### Июнь 2020

- Новая страница [Попап со списком типов полей](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/creationmenu.php) в библиотеке интерфейсов.
- Новая страница [Стандартный список полей](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/fieldtypes.php) в библиотеке интерфейсов.
- Новая страница [Конфигуратор](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/configurator.php) в библиотеке интерфейсов.
- Новая страница [Фабрика настроек пользовательских полей](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/userfieldfactory.php) в библиотеке интерфейсов.
- Новый раздел [Таймлайн](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/timeline/timelineitem.php) в библиотеке интерфейсов.
- Новый раздел [Последовательность стадий](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/stageflow/stageflow.php) в библиотеке интерфейсов.
- Новый раздел [Пользовательские поля](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/userfield/userfield.php) в библиотеке интерфейсов.
- Новый раздел [Настройки полей](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/settings/index.php) в пользовательских полях (main).
- Новый раздел [Internal](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/internal/index.php) в пользовательских полях (main).
- Новый раздел [по модулю RPA](bitrix/rpa/index.php.md).

#### Апрель 2020

- [Компонент](https://dev.1c-bitrix.ru/api_d7/bitrix/currency/currencyfield.php) отрисовки пользовательских полей в модуле currency.
- [Компоненты](bitrix/iblock/iblockfield.php.md) отрисовки пользовательских полей в модуле iblock.
- [Компоненты](bitrix/main/systemcomponents/mainfield.php.md) отрисовки пользовательских полей в модуле main.
- **UserField** - пространство имён для классов и событий Пользовательских полей:

  - [Введение](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/introduction.php)
  - [Класс UF-поля](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/uf-fieldclass.php)
  - [Компонент для отрисовки UF-поля](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/uf-fieldcomponent.php)
  - [Отрисовка поля через новое api](https://dev.1c-bitrix.ru/api_d7/bitrix/main/userfield/fieldrendering.php)
- Работа с сущностями интернет-магазина через [реестр](bitrix/sale/registry_work.php.md).
- Пример работы с [рекуррентными платежами](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/technique/payment_systems/recurring.php) (в дальнейшем примеры работы с платежными системами будут публиковаться в новой [главе](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/technique/payment_systems/index.php)).
- Добавлено описание метода [switchDomain](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/site/methods/switchdomain.php), "перебрасывающего" домены сайтов между собой.
- Добавлено описание метода [getCode](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/getcode.php), возвращающего символьный код текущей страницы.
- Добавлено описание метода [addByTemplate](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/static/addbytemplate.php), добавляющего страницу по шаблону.

#### Февраль 2020

- Новый раздел [Формы](bitrix/ui/forms/index.php.md) в [Библиотеке интерфейсов](bitrix/ui/index.php.md).
- Новый раздел [Стандартные диалоги Alert и Confirm](bitrix/ui/dialogs/index.php.md).

#### Январь 2020

- Добавлен пример на страницу [Нумератор](https://dev.1c-bitrix.ru/api_d7/bitrix/documentgenerator/numerator.php).
- События платежных систем [События платежных систем](bitrix/sale/events/payment_events.php.md).

## 2019

#### Декабрь 2019

- новый раздел с описанием компонента [main.user.selector](bitrix/main/systemcomponents/mainuserselector/index.php.md).
- новый метод [compileEntityId](bitrix/highloadblock/highloadblocktable/compileentityid.php.md) с версии Highloadblock 20.0.0.
- новые методы: [getFolderId](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/getfolderid.php), [getDomainId](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/getdomainid.php), [getSiteTitle](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/landing/methods_object/getsitetitle.php) и [getHostUrl](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/domain/gethosturl.php)
- новая страница [Работа с типами сайтов, скоупы](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/scoupe.php)
- новый раздел [Компонент-обёртка для слайдера](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/scoupe.php) в библиотеке интерфейсов

#### Ноябрь 2019

- новая страница [API Круглого ПрогрессБара](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/progressbar/api_progressround.php).
- новый раздел [Системные компоненты](bitrix/main/systemcomponents/index.php.md).

#### Октябрь 2019

- Описание работы с сущностью [Динамические блоки](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/dinamic_block/index.php) для Сайтов24 в версии 19.0.0.

#### Июль 2019

- новый раздел [Общее](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/rights/general/index.php) в главе Права для версии 18.7.500.
- добавлено Событие [onBuildTemplateCreateUrl](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/events/onbuildtemplatecreateurl.php).
- обновлён раздел [Сайты24](bitrix/landing/index.php.md) под версию 18.7.500.

#### Июнь 2019

- новый раздел [UserTable](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/usertable/index.php) для модуля Intranet
- [события](bitrix/sale/events/sale_deleted.php.md) при непосредственном удалении сущностей Интернет-магазина из базы.
- добавлено событие [onLandingAfterUnPublication](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/events/onlandingafterunpublication.php) для Сайты24.
- добавлено событие [выполнения хука](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/hooks.php).
- добавлено описание библиотеки [Диалог выбора цвета](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/color_picker/introduction.php).
- добавлено описание [Spotlight](bitrix/ui/spotlight/introduction.php.md) в библиотеке интерфейсов.

#### Май 2019

- новый раздел [События](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/events/index.php) для модуля Landing
- новый раздел [Права](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/rights/index.php) на Сайты (18.7.0)
- новый раздел [События](https://dev.1c-bitrix.ru/api_d7/bitrix/intranet/events/index.php) для модуля Intranet

#### Март 2019

- обновлён раздел [Сайты24](bitrix/landing/index.php.md) под версию 18.6.0.
- обновлён раздел [Шаблоны представлений](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/template/index.php), добавлен метод [Template::getList](https://dev.1c-bitrix.ru/api_d7/bitrix/landing/template/getlist.php)
- добавлены методы работы с сущностью "Отгрузки":

  - [Shipment](bitrix/sale/classes/shipment/index.php.md)
  - [ShipmentCollection](bitrix/sale/classes/shipmentcollection/index.php.md)
  - [ShipmentItem](bitrix/sale/classes/shipmentitem/index.php.md)
- добавлены методы работы с сущностью "Оплаты":

  - [Payment](bitrix/sale/classes/payment/index.php.md)
  - [PaymentCollection](bitrix/sale/classes/paymentcollection/index.php.md)
- добавлен класс [\Bitrix\Sale\PropertyValueCollectionBase](bitrix/sale/classes/propertyvaluecollectionbase/index.php.md).
- добавлен новый параметр метода [Bitrix\Main\Config\Configuration::getInstance](https://dev.1c-bitrix.ru/api_d7/bitrix/main/config/configuration/getinstance.php).

#### Февраль 2019

- добавлен раздел [Приёмы работы с методами интернет-магазина](bitrix/sale/technique/index.php.md).
- добавлены методы работы с сущностью [Корзина](bitrix/sale/classes/basket/index.php.md).
- добавлены методы работы с сущностью [Заказ](bitrix/sale/classes/order/index.php.md).
- Добавлен класс для работы с [чек-листами](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/CTaskCheckListItem/index.php) в модуле задач.
- добавлено копирование [описаний полей провайдера](https://dev.1c-bitrix.ru/api_d7/bitrix/documentgenerator/own_provider.php) по ключу COPY.

#### Январь 2019

- изменения документации по модулю **Задачи**:

  - добавлен класс [\Bitrix\Задачи\Integration\Forum\Task\Comment\](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/integration/forum/task/comment/index.php).
  - добавлен раздел [Template](https://dev.1c-bitrix.ru/api_d7/bitrix/tasks/rest/controllers/template/index.php).

- изменения документации по модулю **Интернет-магазин**:

  - добавлен класс [\Bitrix\Sale\Delivery\CalculationResult](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/classes/delivery/calculationresult/index.php).
  - добавлена страница [События служб доставок](bitrix/sale/events/delivery_events.php.md).

## 2018

#### Декабрь 2018

- изменения документации по модулю **Конструктор отчетов**:

  - добавлен класс [\Bitrix\Report\VisualConstructor\Category](https://dev.1c-bitrix.ru/api_d7/bitrix/report/visualconstructor/category/index.php).
  - добавлен класс [\Bitrix\Report\VisualConstructor\Form](https://dev.1c-bitrix.ru/api_d7/bitrix/report/visualconstructor/form/index.php).

#### Ноябрь 2018

- опубликован раздел по модулю [Блоги](bitrix/blog/index.php.md).
- обновлено описание события [OnSaleCheckPrepareData](bitrix/sale/events/cash_desk_and_checks.php.md).
- изменения документации по модулю **Информационные блоки**:

  - добавлен метод [\Bitrix\Iblock\InheritedProperty\BaseValues::queue](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/inheritedproperty/basevalues/queue.php).
  - добавлен класс [\Bitrix\Iblock\Model\PropertyFeature](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/model/propertyfeature/index.php).

добавлено описание класса [\Bitrix\Sale\Discount\Formatter](https://dev.1c-bitrix.ru/api_d7/bitrix/sale/classes/discount/formatter/index.php).

добавлено описание события [OnCheckCollateDocuments](bitrix/sale/events/cash_desk_and_checks.php.md).
