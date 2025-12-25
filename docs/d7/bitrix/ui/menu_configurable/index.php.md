# Настраиваемое меню

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/menu_configurable/index.php

### Описание

`BX.UI.MenuConfigurable.Menu` используется для отрисовки настраиваемого списка пунктов, разделенных на «видимые» и «скрытые», с возможностью drag-and-drop'а и кнопками Сохранить/Отменить.

Названия и поведение многих параметров аналогичны таким из `{Menu} from 'main.popup'`.

### Публичные методы

- `constructor(parameters: Parameters)` –  Создание объекта.
  `open(bindElement: ?HTMLElement): Promise` – Показывает меню.
  Если передан `bindElement`, то меню будет показано у него.
  Метод возвращает `Promise`, который всегда резолвится. На вход придет объект.
  Если меню закрыли без сохранения (кликнули мимо, или нажали «отмена»), то объект будет иметь вид `{isCanceled: true}`.
  Если пользователь нажал «Сохранить», то объект будет иметь вид `{items: Item[]}`, где `items` – массив элементов в их текущем состоянии (в котором их оставил пользователь).

  - **id: string** – уникальный строковый идентификатор;
  - **items: Item[]** – массив с описанием пунктов, где каждый элемент имеет структуру:
  - **bindElement: ?HTMLElement** – элемент, к которому привязывается выпадающее меню<;/li>
    **maxVisibleItems: ?number** – ограничение на максимальное количество элементов в разделе «видимые».

- `close(): void` – скрывает меню. Промис, который до этого вернул метод `open`, будет выполнен.
- `setItems(items: Item[]): this` – перезапишет состав элементов.
- `getItemsFromMenu(): Item[]` – вернет состав элементов в том виде, в котором его оставил пользователь.

### События

- `Save` – бросается при клике на кнопку «Сохранить».
- `Cancel` – бросается при клике на кнопку «Отмена».

### Пример

```
import {Event, Type} from 'main.core';
import {MenuConfigurable} from 'ui.menu-configurable';

const menuConfigurable = new MenuConfigurable({
	items: [
		{
			id: 'first',
		text: 'visible item',
		},
		{
			id: 'second',
			text: 'hidden item',
			isHidden: true,
		},
	],
	bindElement: document.getElementById('my-button'),
	maxVisibleItems: 1, // only one item can be visible
});
menuConfigurable.subscribe('Cancel', () => {
	console.log('cancel button was clicked');
});

Event.bind(document.getElementById('my-button'), 'click', () => {
	menuConfigurable.open().then((result) => {
		if (result.isCanceled)
		{
			return;
		}
		if (Type.isArray(result.items))
		{
			// save items
		}
	});
});
```
