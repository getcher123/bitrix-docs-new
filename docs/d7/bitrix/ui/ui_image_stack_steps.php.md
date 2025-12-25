# Стек изображений с шагами

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/ui_image_stack_steps.php

Расширение `ui.image-stack-steps` отображает и управляет стеками изображений с шагами. Каждый шаг включает заголовок, стек изображений и футер. Можно динамически добавлять, обновлять и удалять шаги.

### Подключение

**JS (ES6)**

```
import { ImageStackSteps } from 'ui.image-stack-steps';

const options = {
    steps: [
        {
            id: 'step1',
            header: { type: 'text', data: { text: 'Заголовок шага 1' } },
            stack: {
                images: [
                    { type: 'image', data: { src: 'image1.jpg', title: 'Изображение 1' } }
                ],
                status: { type: 'ok' }
            },
            footer: { type: 'text', data: { text: 'Футер шага 1' } }
        }
    ]
};

const imageStack = new ImageStackSteps(options);
imageStack.renderTo(document.getElementById('container'));
```

**JS (ES5)**

```
var ImageStackSteps = require('ui.image-stack-steps').ImageStackSteps;

var options = {
    steps: [
        {
            id: 'step1',
            header: { type: 'text', data: { text: 'Заголовок шага 1' } },
            stack: {
                images: [
                    { type: 'image', data: { src: 'image1.jpg', title: 'Изображение 1' } }
                ],
                status: { type: 'ok' }
            },
            footer: { type: 'text', data: { text: 'Футер шага 1' } }
        }
    ]
};

var imageStack = new ImageStackSteps(options);
imageStack.renderTo(document.getElementById('container'));
```

**PHP**

```
<php
use Bitrix\Main\Loader;
use Bitrix\Main\UI\Extension;

Loader::includeModule('ui');

Extension::load('ui.image-stack-steps');

?>
<div id="container"><div>
<script>
    BX.ready(function() {
        var options = {
            steps: [
                {
                    id: 'step1',
                    header: { type: 'text', data: { text: 'Заголовок шага 1' } },
                    stack: {
                        images: [
                            { type: 'image', data: { src: 'image1.jpg', title: 'Изображение 1' } }
                        ],
                        status: { type: 'ok' }
                    },
                    footer: { type: 'text', data: { text: 'Футер шага 1' } }
                }
            ]
        };

        var imageStack = new BX.UI.ImageStackSteps(options);
        imageStack.renderTo(document.getElementById('container'));
    });
</script>
```

### Параметры

**Основные параметры**

| Параметр<br>`тип` | Описание | Обяз. |
| --- | --- | --- |
| steps<br>`Array<StepType>` | Массив шагов, которые будут отображаться в компоненте | Да |

**Параметр StepType**

| Параметр<br>`тип` | Описание | Обяз. |
| --- | --- | --- |
| id<br>`String` | Уникальный идентификатор шага | Да |
| progressBox<br>`Object` | Объект, описывающий прогресс-бокс и содержащий заголовок | Нет |
| header<br>`HeaderType` | Заголовок шага, определяемый типом и данными | Да |
| stack<br>`StackType` | Стек изображений, содержащий изображения и их статус | Да |
| footer<br>`FooterType` | Футер шага, определяемый типом и данными | Да |
| styles<br>`Object` | Стили для шага. Например, минимальная ширина | Нет |

**Параметр HeaderType**

| Параметр<br>`тип` | Описание | Обяз. |
| --- | --- | --- |
| type<br>`String` | Тип заголовка | Да |
| data<br>`Object` | Данные заголовка | Да |
| styles<br>`Object` | Стили заголовка | Нет |

**Параметр StackType**

| Параметр<br>`тип` | Описание | Обяз. |
| --- | --- | --- |
| images<br>`Array<ImageType>` | Массив изображений | Да |
| status<br>`StackStatusType` | Статус стека | Нет |

**Параметр ImageType**

| Параметр<br>`тип` | Описание | Обяз. |
| --- | --- | --- |
| type<br>`String` | Тип изображения | Да |
| data<br>`Object` | Данные изображения | Да |

**Параметр FooterType**

| Параметр<br>`тип` | Описание | Обяз. |
| --- | --- | --- |
| type<br>`String` | Тип футера | Да |
| data<br>`Object` | Данные футера | Да |
| styles<br>`Object` | Стили футера | Нет |

### Класс ImageStackSteps

Класс `ImageStackSteps` предоставляет методы для управления стеками изображений и шагами. Методы позволяют динамически изменять шаги в компоненте.

**Методы класса**

| Метод | Описание | Параметры | Возвращаемое значение |
| --- | --- | --- | --- |
| `renderTo(node: HTMLElement)` | Рендерит компонент в указанный DOM-элемент | `node` — DOM-элемент, в который будет отрисован компонент | — |
| `getSteps(): Array<StepType>` | Возвращает массив текущих шагов. Каждый шаг возвращается как копия, чтобы избежать изменений исходных данных | — | Массив объектов `StepType` |
| `addStep(stepData: StepType): boolean` | Добавляет новый шаг в стек. Если данные шага некорректны, шаг не будет добавлен | `stepData` — данные нового шага | `true`, если шаг успешно добавлен, иначе `false` |
| `updateStep(stepData: StepType, stepId: string): boolean` | Обновляет данные шага с указанным `stepId`. Если данные некорректны, шаг не будет обновлен | `stepData` — новые данные шага.<br>`stepId` — идентификатор шага, который нужно обновить | `true`, если шаг успешно обновлен, иначе `false` |
| `deleteStep(stepId: string): boolean` | Удаляет шаг с указанным `stepId` | `stepId` — идентификатор шага, который нужно удалить | `true`, если шаг успешно удален, иначе `false` |
| `destroy()` | Уничтожает компонент, освобождая ресурсы и отключая его от DOM | — | — |

### Примеры использования

Простой стек с одним шагом

```
const options = {
    steps: [
        {
            id: 'step1',
            header: { type: 'text', data: { text: 'Заголовок шага 1' } },
            stack: {
                images: [
                    { type: 'image', data: { src: 'image1.jpg', title: 'Изображение 1' } }
                ],
                status: { type: 'ok' }
            },
            footer: { type: 'text', data: { text: 'Футер шага 1' } }
        }
    ]
};

const imageStack = new ImageStackSteps(options);
imageStack.renderTo(document.getElementById('container'));
```

Как добавить шаг динамически

```
const newStep = {
    id: 'step2',
    header: { type: 'text', data: { text: 'Заголовок шага 2' } },
    stack: {
        images: [
            { type: 'image', data: { src: 'image2.jpg', title: 'Изображение 2' } }
        ],
        status: { type: 'wait' }
    },
    footer: { type: 'text', data: { text: 'Футер шага 2' } }
};

imageStack.addStep(newStep);
```

### Дополнительная информация

- Расширение использует `EventEmitter` для уведомлений об изменениях. Например, можно подписаться на событие `UI.ImageStackSteps.onUpdateSteps`, чтобы отслеживать обновления шагов.
- Для работы с расширением требуется подключение библиотек `main.core`, `main.core.events` и `ui.vue3`.
- Расширение поддерживает различные типы изображений, включая пользовательские аватары, иконки и счетчики.
- Для кастомизации внешнего вида можно использовать параметры `styles` в шагах, заголовках и футерах.
