# Пространство имён Bitrix

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/index.php

`\Bitrix` - пространство имён, в котором размещаются методы D7. Система допускает разработку разработчиками собственных классов и методов, но размещать их следует в собственных пространствах имён.

Понятие пространств имен позволяет давать элементам системы более четкие имена, избавиться от множества префиксов имен, а также избежать потенциальных конфликтов. Все классы, поставляемые в стандартном дистрибутиве, должны находиться в пространстве имен `\Bitrix`, которое не пересекается ни с PHP, ни с разработками партнёров. Каждый стандартный модуль определяет в пространстве имен `\Bitrix` свое подпространство, совпадающее с именем модуля. Например, для модуля **forum** пространством имен будет `\Bitrix\Forum`, а для модуля main - `\Bitrix\Main`.

При необходимости модуль может организовывать подпространства внутри своего пространства имен. Например, `\Bitrix\Main\IO`, `\Bitrix\Forum\SomeName\SomeNameTwo`. Но такой возможностью следует пользоваться только если это оправдано для организации правильной архитектуры данного модуля.

> Допустимо сокращение полной записи. Вместо `\Bitrix\Main\Class::Function()` можно писать `Main\Class::Function()`.

<!-- vault-nav:start -->
## В этой папке

<details>
<summary>Показать файлы и папки</summary>

### Папки

- [А/В тестирование](abtest/index.php.md)
- [Реклама](advertising/index.php.md)
- [Бизнес-процессы](bizproc/index.php.md)
- [Блоги](blog/index.php.md)
- [Календарь](calendar/index.php.md)
- [Торговый каталог](catalog/index.php.md)
- [Контроллер сайтов](controller/index.php.md)
- [Конверсия](conversion/index.php.md)
- [CRM](crm/index.php.md)
- [Валюты](currency/index.php.md)
- [Dav](dav/index.php.md)
- [Диск](disk/index.php.md)
- [Генератор документов](documentgenerator/index.php.md)
- [Экстранет](extranet/index.php.md)
- [Управление структурой](fileman/index.php.md)
- [Forum](forum/index.php.md)
- [Highload-блоки](highloadblock/index.php.md)
- [Информационные блоки](iblock/index.php.md)
- [Менеджер идей](idea/index.php.md)
- [Веб-мессенджер](im/index.php.md)
- [Коннекторы для внешних мессенджеров](imconnector/index.php.md)
- [Открытые линии](imopenlines/index.php.md)
- [Intranet](intranet/index.php.md)
- [Сайты](landing/index.php.md)
- [Универсальные списки](lists/index.php.md)
- [Адреса и местоположения](location/index.php.md)
- [Почта](mail/index.php.md)
- [Главный модуль](main/index.php.md)
- [Bitrix\Messageservice](messageservice/index.php.md)
- [Bitrix\Mobileapp](mobileapp/index.php.md)
- [Монитор производительности](perfmon/index.php.md)
- [Push and Pull](pull/index.php.md)
- [Корзина удаленных сущностей](recyclebin/index.php.md)
- [Конструктор отчетов](report/index.php.md)
- [Обзор модуля](rpa/index.php.md)
- [Интернет-магазин](sale/index.php.md)
- [Масштабирование](scale/index.php.md)
- [Проактивная защита](security/index.php.md)
- [E-mail Маркетинг](sender/index.php.md)
- [Поисковая оптимизация](seo/index.php.md)
- [Социальная сеть](socialnetwork/index.php.md)
- [Bitrix\Socialservices](socialservices/index.php.md)
- [Задачи](tasks/index.php.md)
- [Конвертер файлов](transformer/index.php.md)
- [UI-библиотека](ui/index.php.md)
- [Опросы, голосования](vote/index.php.md)
- [Телефония](voximplant/index.php.md)

### Файлы

- [Модули](identifiers.php.md)

</details>

<!-- vault-nav:end -->
