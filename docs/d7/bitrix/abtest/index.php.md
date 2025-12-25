# А/В тестирование

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/abtest/index.php

**А/В тестирование** – это инструмент маркетингового исследования, с помощью которого можно сравнить два варианта страницы, шаблона сайта или сайта целиком, чтобы убедиться какой из вариантов имеет более высокую конверсию и многие другие дополнительные показатели.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'abtest'
);
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [ABTestTable](https://dev.1c-bitrix.ru/api_d7/bitrix/abtest/abtesttable/index.php) | Класс для работы с данными А/В-тестов. |  |
| [AdminHelper](https://dev.1c-bitrix.ru/api_d7/bitrix/abtest/adminhelper/index.php) | Служебный класс для проведения А/В-тестирований. |  |
| [EventHandler](https://dev.1c-bitrix.ru/api_d7/bitrix/abtest/eventhandler/index.php) | Обработчики событий. |  |
| [Helper](https://dev.1c-bitrix.ru/api_d7/bitrix/abtest/helper/index.php) | Служебный класс для проведения А/В-тестирований. |  |

#### Смотрите также:

- [А/В тестирование (учебный курс)](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&CHAPTER_ID=07200)
