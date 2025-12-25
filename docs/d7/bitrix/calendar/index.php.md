# Календарь

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/calendar/index.php

`\Bitrix\Calendar` - пространство имен модуля **Календарь**.

Перед использованием модуля необходимо проверить установлен ли он, и подключить его при помощи конструкции:

```
\Bitrix\Main\Loader::includeModule('calendar');
```

| Класс, пространство имен | Описание |
| --- | --- |
| [Integration](https://dev.1c-bitrix.ru/api_d7/bitrix/calendar/integration/index.php)Пространство содержит классы для интеграции календаря событий с Живой Лентой, а также с модулями системы. |  |
| [PushTable](https://dev.1c-bitrix.ru/api_d7/bitrix/calendar/pushtable/index.php)Таблица, содержащая описание мобильных устройств, для дальнейшей отправки по ней push-уведомлений. |  |
| [Sync](https://dev.1c-bitrix.ru/api_d7/bitrix/calendar/sync/index.php)Пространство содержит классы для текущих и будущих синхронизаций с различными внешними системами и сервисами (например, Google Calendar). |  |
| [Update](https://dev.1c-bitrix.ru/api_d7/bitrix/calendar/update/index.php)Пространство содержит служебные классы для обновления модуля. |  |
