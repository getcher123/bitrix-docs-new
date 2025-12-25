# Создание поля ввода с поиском и выбором значений из списка

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/ui_field_selector.php

Расширение `ui.field-selector` позволяет создать поле выбора сущностей, передав минимальный набор параметров. Достаточно указать контейнер, имя поля и типы сущностей. Все остальное обрабатывается автоматически.

### Подключение

**JS (ES6)**

```
import { FieldSelector } from 'ui.field-selector';

const selector = new FieldSelector({
    containerId: 'field-selector-container',
    fieldName: 'selected_id',
    multiple: true,
    collectionType: 'int',
    entities: [
        {
            id: 'user',
            options: { enableSearch: true }
        }
    ],
    selectedItems: [['user', 123]]
});

selector.render();
```

**JS (ES5)**

```
var FieldSelector = require('ui.field-selector').FieldSelector;

var selector = new FieldSelector({
    containerId: 'field-selector-container',
    fieldName: 'selected_id',
    multiple: true,
    collectionType: 'int',
    entities: [
        {
            id: 'user',
            options: { enableSearch: true }
        }
    ],
    selectedItems: [['user', 123]]
});

selector.render();
```

**PHP**

```
<?php
use Bitrix\Main\UI\Extension;
// Подключаем расширение
Extension::load('ui.field-selector');
$containerId = 'field-selector-container';
?>
<div id="<?= $containerId ?>"></div>
<script>
function () {
    const selector = new BX.UI.FieldSelector({
        containerId: '<?= $containerId ?>',
        fieldName: 'selected_id',
        multiple: false,
        collectionType: 'int',
        entities: [
            {
                id: 'crm_contact',
                options: { enableSearch: true }
            }
        ],
        selectedItems: [['crm_contact', 456]]
    });
    selector.render();
})();
</script>
```

> Расширение `ui.field-selector` является оберткой над `ui.entity-selector` и автоматически загружает все зависимости. В PHP используйте `Extension::load('ui.field-selector')` для подключения JS-модуля.

### Параметры конструктора FieldSelectorConfig

Конфигурация передается в конструктор класса `FieldSelector`. Все параметры, кроме отмеченных как опциональные, обязательны.

| Параметр<br>`тип` | Описание | Обяз. | Значения по умолчанию |
| --- | --- | --- | --- |
| containerId<br>`string` | Идентификатор DOM-элемента, в который будет вставлен селектор | Да | — |
| fieldName<br>`string` | Имя поля формы, в которое будут записаны выбранные значения.<br><br> <br><br>> Для множественного выбора рекомендуется добавлять `[]` в конец,  например, `user_ids[]` | Да | — |
| multiple<br>`boolean` | Разрешить множественный выбор | Да | `false` |
| collectionType<br>`string` | Тип значений, которые может принимать поле. Определяет валидацию выбранных данных | Да | `'int'`, `'string'` |
| entities<br>`EntityOptions[]` | Список сущностей, доступных для выбора. Например, `user`, `crm_contact` | Да | — |
| selectedItems<br>`Array<[string, number \| string]>` | Изначально выбранные элементы в формате `[entityId, value]` | Нет | `[]` |
| context<br>`string\|null` | Контекст диалога выбора. Используется для сохранения состояния | Нет | `null` |
| searchMessages<br>`TabMessages` | Заголовок и подзаголовок для вкладки поиска | Нет | `{ title: '', subtitle: '' }` |
| changeEvents<br>`string[]` | Список имен событий, которые будут выброшены через `EventEmitter` при изменении выбора | Нет | `[]` |

### Методы класса FieldSelector

| Метод | Описание | Параметры | Возвращаемое значение |
| --- | --- | --- | --- |
| `render(): void` | Отрисовывает селектор в контейнере. Создает внутренние DOM-элементы и инициализирует `TagSelector`. | — | — |
| `getValues(): Array<[string, number \| string]>` | Возвращает текущие выбранные значения в формате `[entityId, value]`. | — | Массив выбранных элементов |
| `setValues(rawValues: Array<[string, number \| string]>): void` | Устанавливает новые значения. Вызывает валидацию и обновляет отображение. | `rawValues` — массив в формате `[entityId, value]` | — |
| `renderSelectedItems(items: Array<[string, number \| string]>): void` | Генерирует hidden-поля в DOM на основе переданных значений. Полностью заменяет содержимое контейнера результатов. | `items` — массив значений | — |
| `updateSelectedItems(event: BaseEvent): void` | Вызывается при выборе или удалении элемента. Обновляет внутреннее состояние и hidden-поля, эмитит события. | `event` — событие от `TagSelector` | — |

### Примеры использования

**Базовое использование — одиночный выбор контакта CRM**

Минимальная конфигурация: достаточно указать контейнер, имя поля и тип сущности.

```
new BX.UI.FieldSelector({
    containerId: 'contact-selector',
    fieldName: 'contact_id',
    multiple: false,
    collectionType: 'int',
    entities: [{ id: 'crm_contact' }]
}).render();
```

**Множественный выбор с предустановленными значениями**

Передаем массив выбранных элементов. Указываем `fieldName` с `[]` для корректной передачи в PHP.

```
const selector = new BX.UI.FieldSelector({
    containerId: 'user-selector',
    fieldName: 'user_ids[]',
    multiple: true,
    collectionType: 'int',
    entities: [{ id: 'user' }],
    selectedItems: [
        ['user', 101],
        ['user', 102]
    ]
});

selector.render();
```

**Реагирование на изменения через события**

При изменении выбора можно отслеживать кастомные события, чтобы обновлять интерфейс или выполнять логику.

```
const selector = new BX.UI.FieldSelector({
    containerId: 'tag-selector',
    fieldName: 'tag_ids[]',
    multiple: true,
    collectionType: 'int',
    entities: [{ id: 'tags' }],
    changeEvents: ['onTagsChanged']
});

selector.render();

BX.EventEmitter.subscribe('onTagsChanged', function() {
    const values = selector.getValues();
    console.log('Текущие теги:', values);
});
```

**Программное обновление значений**

Можно вручную устанавливать значения через `setValues` и обновлять DOM.

```
// Добавляем новый элемент
function addItem(entityId, value)
{
    const current = selector.getValues();
    current.push([entityId, value]);
    selector.setValues(current);
    selector.renderSelectedItems(current);
}

// Использование
addItem('user', 999);
```

**Контрол для выборки сотрудников**

Выбор сотрудников из структуры компании с возможностью просмотра отделов.

```
$userOptions = [
    'collabers' => false,
    'intranetUsersOnly' => true,
    'emailUsers' => false,
    'inviteEmployeeLink' => false,
];

$entities = [
    [
        'id' => 'user',
        'dynamicLoad' => true,
        'dynamicSearch' => true,
        'options'=> $userOptions,
    ],
    [
        'id' => 'structure-node',
        'dynamicLoad' => true,
        'dynamicSearch' => true,
        'options'=> [
            'selectMode' => 'usersOnly',
            'flatMode' => false,
            'fillRecentTab' => false,
            'restricted' => 'view',
            'includedNodeEntityTypes' => ['department'],
            'useMultipleTabs' => false,
            'userOptions' => $userOptions,
        ],
    ],
];

$entityValues = [
    [
        'user', 12
    ],
    [
        'user', 14
    ],
];

$multiple = true;
$config = \Bitrix\Main\Web\Json::encode([
    'containerId' => 'doc-selector',
    'fieldName' => 'EMPLOYEE' . ($multiple ? '[]' : ''),
    'context' => null,
    'multiple' => $multiple,
    'collectionType' => 'int',
    'selectedItems' => $entityValues,
    'entities' => $entities,
]);

\Bitrix\Main\UI\Extension::load('ui.field-selector');

return <<<HTML
    <div id="doc-selector"></div>
    <script>
    (function() {
        const selector = new BX.UI.FieldSelector({$config});
        selector.render();
    })();
    </script>
    HTML
;
```

**Кастомизация вкладки поиска**

Можно задать заголовок и подзаголовок, чтобы улучшить UX.

```
new BX.UI.FieldSelector({
    containerId: 'doc-selector',
    fieldName: 'doc_id',
    multiple: false,
    collectionType: 'int',
    entities: [{ id: 'documents' }],
    searchMessages: {
        title: 'Найти документ',
        subtitle: 'Введите название или номер'
    }
}).render();
```

### Дополнительная информация

- Не требуется вручную управлять hidden-полями, синхронизацией или событиями — все делается автоматически.
- Тип `collectionType` определяет, какие значения считаются валидными:

  - `'int'` — только положительные целые числа.
  - `'string'` — непустые строки.
- При `multiple: false` диалог закрывается после выбора элемента.
- Метод `renderSelectedItems` полностью заменяет содержимое контейнера результатов — дублирования не происходит.
- Если `containerId` не найден в DOM, инициализация прерывается с ошибкой в консоли.
