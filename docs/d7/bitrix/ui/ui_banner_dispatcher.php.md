# Диспетчер баннеров

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/ui_banner_dispatcher.php

Библиотека приоритизирует и упорядочивает вплывающие информационные сообщения или рекламные баннеры. Доступно с версии ui 24.50.0

Общая задержка перед стартом библиотеки — две секунды.

Доступны следующие типы очередей:

- Низкая `BannerDispatcher.low` — элемент очереди отображается после всех элементов нормальной очереди с задержкой в 5 секунд. Будет показан только первый элемент этой очереди. Этот уровень предназначен для совсем не приоритетных и не важных баннеров
- Нормальная `BannerDispatcher.normal` — элемент очереди отображается после всех элементов высокой очереди с задержкой в 1 секунду. Будет показан только первый элемент этой очереди
- Высокая `BannerDispatcher.high` — элемент очереди отображается после всех элементов критичной очереди с задержкой в 1 секунду
- Критическая `BannerDispatcher.critical` — элемент этой очереди отображается первым, независимо от того, в какой последовательности он пришел. Все критичные элементы отображаются с задержкой в 0 сек. Этот уровень предназначен для важных системных сообщений

#### Примеры

1. Низкая очередь `BannerDispatcher.low`
  ```
      import { BannerDispatcher } from 'ui.banner-dispatcher';
      import { Popup } from 'main.popup';
      // Добавляем отображение попапа в низкую очередь.
      BannerDispatcher.low.toQueue((onDone) => {
      				const popup = new Popup({});
      				popup.subscribe('onAfterClose', (event) => {
      					// Внимание. Нужно вызывать callback onDone, когда баннер или попап отработал и был закрыт.
      					// Иначе не будет вызван следующий элемент очереди.
      					onDone();
      				});
      				popup.show();
      			});
  ```
2. Нормальная очередь `BannerDispatcher.normal`
  ```
      import { BannerDispatcher } from 'ui.banner-dispatcher';
      import { Popup } from 'main.popup';
      // Добавляем отображение попапа в нормальную очередь.
      BannerDispatcher.toQueue(() => {})
      // или другой вариант
      BannerDispatcher.normal.toQueue((onDone) => {
      				const popup = new Popup({});
      				popup.subscribe('onAfterClose', (event) => {
      					// Внимание. Нужно вызывать callback onDone, когда баннер или попап отработал и был закрыт.
      					// Иначе не будет вызван следующий элемент очереди.
      				});
      				popup.show();
      			});
  ```
3. Высокая очередь `BannerDispatcher.high`
  ```
      import { BannerDispatcher } from 'ui.banner-dispatcher';
      import { Popup } from 'main.popup';
      // Добавляем отображение попапа в высокую очередь.
      BannerDispatcher.high.toQueue((onDone) => {
      				const popup = new Popup({});
      				popup.subscribe('onAfterClose', (event) => {
      					// Внимание. Нужно вызывать callback onDone, когда баннер или попап отработал и был закрыт.
      					// Иначе не будет вызван следующий элемент очереди.
      					onDone();
      				});
      				popup.show();
      			});
  ```
4. Критическая очередь `BannerDispatcher.critical`
  ```
      import { BannerDispatcher } from 'ui.banner-dispatcher';
      import { Popup } from 'main.popup';
      // Добавляем отображение попапа в критичную очередь.
      BannerDispatcher.critical.toQueue((onDone) => {
      				const popup = new Popup({});
      				popup.subscribe('onAfterClose', (event) => {
      					// Внимание. Нужно вызывать callback onDone, когда баннер или попап отработал и был закрыт.
      					// Иначе не будет вызван следующий элемент очереди.
      					onDone();
      				});
      				popup.show();
      			});
  ```
5. Отключение очередей на странице
  ```
      import { BannerDispatcher } from 'ui.banner-dispatcher';
      import { LaunchPriority, } from 'ui.auto-launch';
      // Если вызвать на странице, будут вызваны только баннеры с приоритетом переданным в массиве.
      BannerDispatcher.only([
          LaunchPriority.NORMAL,
          LaunchPriority.HIGH,
          LaunchPriority.CRITICAL,
      ]);
      // Если передать пустой массив, на странице не будет ничего отображено.
      BannerDispatcher.only([]);
  ```
