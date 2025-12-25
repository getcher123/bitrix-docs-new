# Главный модуль

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/main/index.php

**Main** - пространство имён для классов и методов **Главного модуля** системы. Модуль не нуждается в специальном коде для подключения.

| Класс, простраство имён | Описание |
| --- | --- |
| [Application](application/index.php.md) | Базовый класс для любых приложений. |
| [Authentication](authentication/index.php.md) | Пространство имён для классов аутентификации пользователей. |
| [Context](context/index.php.md) | Класс для работы с контекстом |
| [Config](config/index.php.md) | Пространство имён для классов настроек. |
| [Data](data/index.php.md) | Пространство имён классов для работы с кешем, в том числе с управляемым. |
| [DB](db/index.php.md) | Пространства имён для классов, работающих с Базой данных |
| [Diag](diag/index.php.md) | Пространства имён для классов диагностики. |
| [Entity](entity/index.php.md) | Пространство имён для работы с сущностями. |
| [Environment](environment/index.php.md) | Класс работы с окружением. |
| [EventManager](EventManager/index.php.md) | Класс кратко- и долгосрочной регистрации обработчиков событий. |
| [FinderDestTable](finderdesttable/index.php.md) | класс для работы с таблицей сущностей, выбираемые в диалоге выбора, в списке **Последние**. |
| [Grid](grid/index.php.md) | Пространство имён для работы с гридом (табличным элементом управления). |
| [GroupTaskTable](grouptasktable/index.php.md) | класс описывает ORM-сущность GroupTaskTable. |
| [HttpApplication](httpapplication/index.php.md) | класс отвечает за обычный http-хит на сайте. |
| [HttpRequest](httprequest/index.php.md) | Класс управляет объектом HTTP запросов, содержащим информацию о текущем запросе. |
| [IO](io/index.php.md) | Объектно-ориентированная работа с файлами. |
| [Loader](loader/index.php.md) | класс для загрузки необходимых файлов, классов и модулей. |
| [Localization](localization/index.php.md) | Пространство имён для работы с языковыми файлами. |
| [Mail](mail/index.php.md) | Описание пространства имён. |
| [Page](page/index.php.md) | Пространство имён для классов, работающих со страницей продукта. |
| [Replica](replica/index.php.md) | Пространство имён для классов репликации главного модуля. |
| [Request](request/index.php.md) | Класс для работы с объектом запроса. |
| [Result](result/index.php.md) | Класс результата выполнения запроса. |
| [Security](security/index.php.md) | Пространство имён для классов, отвечающих за безопасность. |
| [Server](server/index.php.md) | Класс объектов сервера. |
| [Service](service/index.php.md) | Пространство имён для классов интеграций с различными сервисами. |
| [Text](text/index.php.md) | пространство имён для работы с текстом: классы для конвертации текста и другие. |
| [Type](type/index.php.md) | Пространство имён для работы с типами данных: дата, файл и другие. |
| [UI](ui/index.php.md) | Пространство имён пользовательских интерфейсов. |
| [UrlPreview](urlpreview/index.php.md) | Пространство имён для работы с "богатыми ссылками". |
| [UrlRewriterRuleMaker](urlrewriterrulemaker/index.php.md) | Класс для работы с правилами переадресации. |
| [UserConsent](userconsent/index.php.md) | Пространство имён для работы с соглашениями пользователей. |
| [UserField](userfield/index.php.md) | Пространство имён для классов и событий Пользовательских полей. |
| [UserTable](usertable/index.php.md) | Класс для работы с пользователями. |
| [UserUtils](userutils/index.php.md) | Класс утилит для работы с пользователями. |
| [Web](web/index.php.md) | Пространство имён для классов, работающих с WEB. |
| [XmlWriter](xmlwriter/index.php.md) | класс для экспорта в XML. |
| Классы для работы с ошибками |  |
| [Error](error/index.php.md) | Класс ошибок. |
| [ErrorCollection](errorcollection/index.php.md) | Коллекция ошибок. |
| Классы для работы с исключениями |  |
| [SystemException](systemexception/index.php.md) | Базовый класс фатальных исключений. |
| [ArgumentException](argumentexception/index.php.md) | Исключение выводится когда аргумент функции не валидный |
| [ArgumentNullException](argumentnullexception/index.php.md) | Исключение выводится когда передаётся пустое значение в метод который не принимает такого значения как валидное. |
| [ArgumentOutOfRangeException](argumentoutofrangeexception/index.php.md) | Исключение выводится когда значение аргумента находится вне допустимого диапазона значений. |
| [ArgumentTypeException](argumenttypeexception/index.php.md) | Исключение выводится, когда тип аргумента не принимается функцией. |
| [ObjectNotFoundException](objectnotfoundexception/index.php.md) | Исключение выводится когда отсутствует объект. |
| [ObjectException](objectexception/index.php.md) | Исключение выводится, когда объект не может быть создан. |
| [ObjectPropertyException](objectpropertyexception/index.php.md) | Исключение выводится когда свойство объекта не валидно. |
| InvalidOperationException | Исключение выводится когда вызываемый метод не является валидным для текущего состояния объекта. |
| [NotSupportedException](notsupportedexception/index.php.md) | Исключение выводится когда операция не поддерживается. |
| [NotImplementedException](notimplementedexception/index.php.md) | Исключение выводится, когда операция не осуществлена, хотя должна была быть выполнена. |
