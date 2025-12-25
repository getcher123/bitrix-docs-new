# REST API для инфоблоков

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/rest/index.php

REST API для инфоблоков доступен с версии **20.5.0** модуля Информационные блоки.

Общая концепция работы описана на странице [Концепция](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/rest/concept.php).

В настоящий момент работает Read-only режим доступа к элементам инфоблока. Доступны следующие методы получения и фильтрации записей:

| Метод | Описание |
| --- | --- |
| [iblock.Element.get](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/rest/iblockelementget.php) | Получение элемента инфоблока по его идентификатору ID. |
| [iblock.Element.list](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/rest/iblockelementlist.php) | Получение элементов инфоблока по заданному фильтру. |

Также доступна своя [реализация контроллера](https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/rest/custom_controller.php): как создание полностью своего контроллера, так и наследование от штатного с переопределением нужных методов.
