# Поисковая оптимизация

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/seo/index.php

Раздел содержит информацию о классах модуля **Поисковая оптимизация**, относящихся к ядру D7 и находящихся соответственно в пространстве имен **\Bitrix\Seo**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'seo'
);
```

| Класс, простраство имён | Описание |
| --- | --- |
| [Adv](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/adv/index.php) | Пространство имён классов для работы с рекламными кампаниями, объявлениями, баннерами. |
| [AdvEntity](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/adventity/index.php) | Базовый класс для сущностей внешнего сервиса рекламы. |
| [Engine](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/engine/index.php) | Пространство имён транспортных классов для работы с Яндекс.Директ и класса для поддержки централизованной авторизации при работе с Яндекс.Директ. |
| [SitemapFile](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/sitemapfile/index.php) | Класс для работы с файлами sitemap. |
| [SitemapIblock](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/sitemapiblock/index.php) | Класс, отвечающий за обслуживание событий инфоблоков с целью автоматического отражения изменения в файлах карты сайта. |
| [SitemapIblockTable](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/sitemapiblocktable/index.php) | Класс для работы с хранилищем привязок инфоблоков к механизму генерации файлов карты сайта. |
| [SitemapRuntime](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/sitemapruntime/index.php) | Класс для работы с временным файлом карты сайта. |
| [SitemapTable](https://dev.1c-bitrix.ru/api_d7/bitrix/seo/sitemaptable/index.php) | Класс для работы с хранилищем настроек генерации файлов карты сайта. |
