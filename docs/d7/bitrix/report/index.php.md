# Конструктор отчетов

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/report/index.php

`\Bitrix\Report` – пространство имен модуля **Конструктор отчетов**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule(
	'report'
);
```

| Класс | Описание | С версии |
| --- | --- | --- |
| [Internals](https://dev.1c-bitrix.ru/api_d7/bitrix/report/internals/index.php) | Пространство содержит классы для работы с таблицами модуля. | 16.0.1 |
| [RightsManager](https://dev.1c-bitrix.ru/api_d7/bitrix/report/rightsmanager/index.php) | Класс для управления правами отчётов. | 16.0.1 |
| [ReportTable](https://dev.1c-bitrix.ru/api_d7/bitrix/report/reporttable/index.php) | Класс для работы с таблицей отчётов. |  |
| [Sharing](https://dev.1c-bitrix.ru/api_d7/bitrix/report/sharing/index.php) | Класс для управления общим доступом. | 16.0.1 |
| [VisualConstructor](https://dev.1c-bitrix.ru/api_d7/bitrix/report/visualconstructor/index.php) | Подпространство содержит классы для визуального конструктора отчетов. | 18.0.0 |

#### Смотрите также

- [Конструктор отчетов (API для старой версии ядра)](../../../report/index.md)
- [Конструктор отчетов (учебный курс)](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=52&CHAPTER_ID=06429)
