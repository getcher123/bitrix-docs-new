# CRM

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/crm/index.php

Раздел содержит информацию о классах модуля **CRM**, относящихся к ядру D7 и находящихся соответственно в пространстве имен **\Bitrix\Crm**.

Базовые методы сущностей:

- **CCrmLead** - лиды,
- **CCrmDeal** - сделки,
- **CCrmCompany** - компании,
- **CCrmContact** - контакты,
- **CCrmQuote** - предложения,
- **CCrmInvoice** - счета.

> Классы CCrmQuote и CCrmInvoice не имеют методов getListEx, но имеют полностью аналогичный getList.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('crm');
```

| Класс, пространство имён | Описание |
| --- | --- |
| [Activity](activity/index.php.md) | Пространство имён содержит классы для работы с делами в CRM. |
| [Automation](automation/index.php.md) | Пространство имён cодержит классы для автоматизации продаж в CRM. |
| [BankDetailTable](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/bankdetailtable/index.php) | Класс предназначен для работы с банковскими реквизитами. |
| [Binding](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/binding/index.php) | Пространство имён классов для множественных привязок сущностей CRM. |
| [CallList](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/calllist/index.php) | Подпространство имён содержит классы для работы со звонками. |
| [Category](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/category/index.php) | Пространство имён классов для работы с Направлениями. |
| [Color](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/color/index.php) | Пространство имён классов для хранения цветовых схем стадий Сделки, статусов Лида и Предложения в CRM. |
| [CommunicationType](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/communicationtype/index.php) | класс для работы с типами связей. |
| [CompanyAddress](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/companyaddress/index.php) | Класс для хранения адресов Компаний. |
| [Config](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/config/index.php) | Пространство имён классов для хранения пользовательских настроек в контексте определенной сущности. |
| [ContactAddress](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/contactaddress/index.php) | Класс для хранения адресов Контактов. |
| [Conversion](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/conversion/index.php) | Пространство имён классов для конвертации сущностей CRM. |
| [Entity](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/entity/index.php) | Пространство имён содержит классы для работы с сущностями. |
| [EntityAddress](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/entityaddress/index.php) | Класс для хранения адресов сущностей. |
| [EntityBankDetail](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/entitybankdetail/index.php) | Класс для работы с банковскими реквизитами. |
| [EntityRequisite](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/entityrequisite/index.php) | Класс для работы с реквизитами сущности. |
| [Entry](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/entry/index.php) | Пространство имён содержит классы для хранения отдельных записей. |
| [Integration](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/integration/index.php) | Пространство имён классов для для взаимодействия с другими модулями - интеграции. |
| [Integrity](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/integrity/index.php) | Пространство имён содержит классы для контроля, поиска, отслеживания и объединения дубликатов. |
| [InvoiceTable](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/invoicetable/index.php) | Класс предназначен для работы с таблицей счетов. |
| [Kanban](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/kanban/index.php) | Пространство имён содержит классы для работы с канбаном. |
| [LeadAddress](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/leadaddress/index.php) | Класс для хранения адресов Лидов. |
| [Merger](merger/index.php.md) | Пространство имён классов, используемых при управлении дубликатами, при конвертации и для объединения полей сущностей. |
| [PresetTable](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/presettable/index.php) | Класс ORM для работы с шаблонами реквизитов CRM. |
| [Preview](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/preview/index.php) | Пространство имён классов, используемых при формировании "богатых ссылок" на сущности CRM. |
| [Requisite](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/requisite/index.php) | Пространство имён классов, используемых для конвертации реквизитов из сущностей. |
| [RequisiteAddress](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/requisiteaddress/index.php) | Класс для хранения адресов реквизитов. |
| [RequisiteTable](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/requisitetable/index.php) | Класс для работы с реквизитами сущностей. |
| [Restriction](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/restriction/index.php) | Пространство имён содержит классы для работы с ограничениями. |
| [Settings](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/settings/index.php) | Пространство имён классов и методов для выполнения различных неосновных настроек системы CRM. |
| [Statistics](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/statistics/index.php) | Пространство имён классов, используемых для сбора данных для построения аналитических отчетов. |
| [Synchronization](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/synchronization/index.php) | Пространство имён классов, используемых для синхронизации наборов пользовательских полей между различными типами сущностей. |
| [Widget](https://dev.1c-bitrix.ru/api_d7/bitrix/crm/widget/index.php) | Виджеты, используемые для построения аналитических отчётов. |
