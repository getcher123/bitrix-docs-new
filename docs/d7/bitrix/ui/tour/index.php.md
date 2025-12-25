# Тур

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/tour/index.php

Tour - расширение для создания

			тура

                    **Интерактивный визуальный тур** - это совокупность нескольких всплывающих подсказок и/или popup-окон, которые появляются по мере продвижения пользователя по сайту/

		 на странице.

Cоздать тур можно 2 способами:

1. Подключить js-расширение `ui.tour` и воспользоваться [JavaScript API](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/tour/js_api/index.php).
  ```
  \Bitrix\Main\UI\Extension::load("ui.tour");
  ```
2. Подключить на странице компонент [bitrix:ui.tour](https://dev.1c-bitrix.ru/api_d7/bitrix/ui/tour/component.php), указав нужные настройки.
