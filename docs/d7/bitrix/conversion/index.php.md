# Конверсия

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/conversion/index.php

Модуль **Конверсия** позволяет не только вычислить конверсию для любого выбранного целевого действия, но и получить отчет, позволяющий понять, что влияет на ее значение и как ее можно улучшить.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'conversion'
);
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [Internals](https://dev.1c-bitrix.ru/api_d7/bitrix/conversion/internals/index.php) | Пространство имён содержит классы для работы с основными сущностями модуля. | 15.5.1 |
| [DayContext](https://dev.1c-bitrix.ru/api_d7/bitrix/conversion/daycontext/index.php) | Класс для работы с уникальным ежедневным контекстом. |  |
| [MobileDetect](https://dev.1c-bitrix.ru/api_d7/bitrix/conversion/mobiledetect/index.php) | Класс для работы с контекстом мобильных устройств. |  |

#### Смотрите также

- [Конверсия (API для старой версии ядра)](../../../conversion/index.md)
- [Конверсия (учебный курс)](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&CHAPTER_ID=07212)
