# Меню

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/vue_components/system_menu.php

Компонент `ui.system.menu` представляет собой выпадающее меню (попап), которое предназначено для отображения списка действий: настройки, дополнительные опции или контекстные команды. Меню может содержать пункты с иконками, подзаголовками, счетчиками, блокировкой, подменю, секциями и расширенным заголовком. Компонент поддерживает использование как в чистом JavaScript, так и во Vue 3 через расширение.

### Подключение

```
import { Menu, MenuItemDesign } from 'ui.system.menu';
const menu = new Menu({
    bindElement: document.getElementById('menu-button'),
    items: [
        {
            title: 'Открыть',
            onClick: () => console.log('Открыто'),
        },
        {
            title: 'Удалить',
            design: MenuItemDesign.Alert,
            onClick: () => console.log('Удалено'),
        },
    ],
});
menu.show();
```

### Использование в Vue 3

Компонент меню можно использовать в Vue 3 приложениях с помощью расширения `ui.vue3.components.menu`. Доступен компонент `BMenu` и тип `MenuOptions`.

```
import { BMenu, type MenuOptions } from 'ui.vue3.components.menu';

// @vue/component
export const MyComponent = {
    components: {
        BMenu,
    },
    data() {
        return {
            isMenuShown: false,
        };
    },
    computed: {
        menuOptions() {
            return {
                bindElement: this.$refs.button,
                items: [
                    {
                        title: 'Пункт 1',
                        onClick: () => {
                            console.log('Выбран пункт 1');
                        },
                    },
                    {
                        title: 'Подменю',
                        subMenu: {
                            items: [
                                {
                                    title: 'Вложенная опция',
                                    onClick: () => {
                                        console.log('Подменю выбрано');
                                    },
                                },
                            ],
                        },
                    },
                ],
            };
        },
    },
    template: `
        <button ref="button" @click="isMenuShown = true">
            Открыть меню
        </button>
        <BMenu v-if="isMenuShown" :options="menuOptions" @close="isMenuShown = false"/>
    `,
};
```

### Параметры компонента

**MenuOptions** — основные параметры меню, наследуют `PopupOptions` из `main.popup` и расширяют их специфичными полями.

| Параметр<br>`тип` | Описание |
| --- | --- |
| sections<br>`MenuSectionOptions[]` | Массив секций, по которым группируются пункты меню. Список секций, нужен для отделения групп пунктов друг от друга. Все элементы без секции отрисовываются в начале меню. Секции отделяются разделителем, у которого может быть заголовок. |
| items<br>`MenuItemOptions[]` | Массив пунктов меню. Каждый пункт может иметь подменю, иконку, счетчик и так далее. |
| richHeader<br>`RichHeader` | Расширенный заголовок меню с иконкой, названием, подзаголовком и кнопкой. |
| closeOnItemClick<br>`boolean` | Закрывать ли меню при клике на пункт, если у пункта нет подменю. |

**MenuItemOptions** — параметры отдельного пункта меню.

| Параметр<br>`тип` | Описание |
| --- | --- |
| id<br>`string` | Уникальный идентификатор пункта. |
| sectionCode<br>`string` | Код секции, к которой принадлежит пункт. |
| design<br>`string` | Стилевое оформление пункта. |
| onClick<br>`Function` | Функция, вызываемая при клике на пункт. |
| title<br>`string` | Основной текст пункта. |
| subtitle<br>`string` | Дополнительный текст под заголовком. |
| badgeText<br>`{title: string, color: string}` | Текст бейджа справа от заголовка. |
| isSelected<br>`boolean` | Отображать ли галочку выбора слева. |
| icon<br>`string` | Код иконки слева, из иконок `ui.icon-set`. |
| svg<br>`SVGElement` | Кастомный SVG-элемент вместо иконки. |
| extraIcon<br>`object` | Иконка-действие справа, например, звезда. |
| counter<br>`CounterOptions` | Счетчик справа, из `ui.cnt`. |
| subMenu<br>`MenuOptions[]` | Подменю, отображается при наведении. |
| isLocked<br>`boolean` | Показывать значок замка слева. |
| closeOnSubItemClick<br>`boolean` | Закрывать ли основное меню при клике во вложенном меню. |

**MenuSectionOptions** — параметры секции меню.

| Параметр<br>`тип` | Описание |
| --- | --- |
| code<br>`string` | Уникальный код секции, используется для группировки пунктов. |
| title<br>`string` | Заголовок секции, отображается над группой пунктов. Если передать пустым, то секция будет отделена только разделительной чертой. |
| design<br>`'default' \| 'accent'` | Стиль оформления секции. |

**RichHeader** — параметры богатого заголовка.

| Параметр<br>`тип` | Описание |
| --- | --- |
| design<br>`'default' \| 'copilot'` | Дизайн заголовка. |
| title<br>`string` | Текст заголовка. |
| subtitle<br>`string` | Текст подзаголовка. |
| icon<br>`string` | Иконка из `ui.icon-set.api.core`. |
| onClick<br>`function` | Функция, вызываемая при клике на заголовок. |

### Методы компонента

Класс `Menu` предоставляет следующие публичные методы:

| Метод | Описание | Параметры | Возвращаемое значение |
| --- | --- | --- | --- |
| `show(bindElement: HTMLElement): void` | Отображает меню. Если передан `bindElement`, привязывает попап к нему. | `bindElement` — DOM-элемент, к которому привязывается меню | — |
| `updateItems(itemsOptions: MenuItemOptions[]): void` | Обновляет список пунктов меню. Сохраняет состояние открытых подменю, если это возможно. | `itemsOptions` — новый массив пунктов | — |
| `close(): void` | Закрывает меню программно. | — | — |
| `destroy(): void` | Уничтожает меню, удаляет все обработчики и подменю. Вызывается автоматически при закрытии, если установлен `closeByEsc`. | — | — |
| `getOptions(): MenuOptions` | Возвращает текущие параметры меню. | — | `MenuOptions` |
| `getPopup(): Popup` | Возвращает внутренний экземпляр `Popup` из `main.popup`. | — | `Popup` |
| `getPopupContainer(): HTMLElement` | Возвращает контейнер попапа (DOM-элемент). | — | `HTMLElement` |

### Примеры использования

**Меню с секциями и расширенным заголовком**

```
new BX.UI.System.Menu({
    richHeader: {
        design: 'copilot',
        title: 'AI Assistant',
        subtitle: 'Готов помочь',
        icon: 'main-copilot-ai',
        onClick: () => console.log('Header clicked')
    },
    sections: [
        { code: 'actions', title: 'Действия', design: BX.UI.System.MenuSectionDesign.Accent
 },
        { code: 'settings', title: 'Настройки' }
    ],
    items: [
        {
            title: 'Создать',
            sectionCode: 'actions',
            icon: ‘outline-add-l',
        },
        {
            title: 'Редактировать',
            sectionCode: ‘actions',
        },
        {
            title: 'Темная тема',
            sectionCode: 'settings',
            isSelected: true,
        },
    ],
}).show();
```

**Меню с подменю**

```
new BX.UI.System.Menu({
    items: [
        {
            title: 'Экспорт',
            subMenu: {
                items: [
                    { title: 'PDF', onClick: () => console.log('PDF') },
                    { title: 'Excel', onClick: () => console.log('Excel') },
                ],
            },
        },
        {
            title: 'Удалить',
            design: BX.UI.System.MenuItemDesign.Alert,
            onClick: () => confirm(‘Удалить?'),
        },
    ],
}).show();
```
