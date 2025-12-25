# Компонент аватара

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/ui_avatar.php

Расширение `ui.avatar` — это инструмент для отображения аватаров пользователей в различных стилях и формах. Он поддерживает круглые, шестиугольные и квадратные аватары, а также специальные стили для гостей, пользователей экстранета и акцентных аватаров с градиентами. Компонент автоматически генерирует инициалы, поддерживает изображения и иконки по умолчанию. Позволяет настраивать цвета, размеры и обработку событий.

### Подключение

**JS (ES6)**

```
import { AvatarRound, AvatarHexagonAccent, AvatarSquareGuest } from 'ui.avatar';

const avatar = new AvatarRound({
    title: 'Иван Петров',
    size: 40,
    baseColor: '#4a7cf5'
});

avatar.renderTo(document.getElementById('avatar-container'));
```

**JS (ES5)**

```
var AvatarRound = require('ui.avatar').AvatarRound;
var AvatarHexagonAccent = require('ui.avatar').AvatarHexagonAccent;

var avatar = new AvatarRound({
    title: 'Иван Петров',
    size: 40,
    baseColor: '#4a7cf5'
});

avatar.renderTo(document.getElementById('avatar-container'));
```

**PHP**

```
<?php
use Bitrix\UI\Extension;

// Подключаем расширение ui.avatar
Extension::load('ui.avatar');
?>

<div id="avatar-container"></div>

<script>
    BX.ready(function() {
        var AvatarRound = BX.UI.AvatarRound;
        var avatar = new AvatarRound({
            title: 'Иван Петров',
            size: 40,
            baseColor: '#4a7cf5'
        });
        avatar.renderTo(document.getElementById('avatar-container'));
    });
</script>
```

### Типы аватаров

Расширение `ui.avatar` поддерживает три основные формы и несколько стилей для каждой.

- **Круглые**: `AvatarRound`, `AvatarRoundGuest`, `AvatarRoundExtranet`, `AvatarRoundAccent`, `AvatarRoundCopilot`.
- **Шестиугольные**: `AvatarHexagon`, `AvatarHexagonGuest`, `AvatarHexagonExtranet`, `AvatarHexagonAccent`.
- **Квадратные**: `AvatarSquare`, `AvatarSquareGuest`, `AvatarSquareExtranet`, `AvatarSquareAccent`.

Каждый тип наследуется от базового класса `AvatarBase` и может иметь дополнительные визуальные эффекты: рамки, градиенты или специальные маски.

**Особенности стилей**

- `--base` — минимальный стиль без рамок,
- `--guest` — двойная граница, используется для гостевых пользователей,
- `--extranet` — стиль для пользователей экстранета,
- `--accent` — акцентный стиль с градиентной заливкой,

### Параметры конструктора AvatarOptions

Объект параметров, который передавается в конструктор любого аватара. Все параметры опциональны.

| Параметр<br>`тип` | Описание | Возможные значения | По умолчанию |
| --- | --- | --- | --- |
| title<br>`string` | Текст, который отображается как подсказка. Используется для генерации инициалов, если они не заданы | Любая строка | `''` |
| userName<br>`string` | Имя пользователя, резервное поле для `title` | Любая строка | `''` |
| initials<br>`string` | Инициалы, которые отображаются в аватаре. Если не заданы — извлекаются из `title` | Строка из 1–2 символов (например, ИП) | `null` |
| userpicPath / picPath<br>`string` | Путь к изображению аватара. `picPath` — синоним для совместимости | URL изображения | `null` |
| size<br>`number` | Размер аватара в пикселях. Управляет CSS-переменной `--ui-avatar-size` | Любое положительное число | `32` |
| baseColor<br>`string` | Цвет фона аватара в формате HEX. Например, `#4a7cf5`. Преобразуется в RGB для CSS | HEX-код цвета | `null` |
| borderColor<br>`string` | Цвет внешней границы, в HEX | HEX-код цвета | `null` |
| borderInnerColor<br>`string` | Цвет внутренней границы, в HEX | HEX-код цвета | `null` |

### Методы

Общие методы, которые доступны во всех классах аватаров. Наследуются от `AvatarBase`.

| Метод | Описание | Параметры | Возвращаемое значение |
| --- | --- | --- | --- |
| `renderTo(node: HTMLElement): void` | Отрисовывает аватар в указанном DOM-узле | `node` — HTML-элемент, в который будет добавлен аватар | `void` |
| `setPic(url: string): this` | Устанавливает изображение аватара по URL | `url` — путь к изображению | Экземпляр аватара для цепочки вызовов |
| `removePic(): this` | Удаляет изображение аватара и восстанавливает инициалы или иконку по умолчанию | — | Экземпляр аватара |
| `setTitle(text: string): this` | Устанавливает текст подсказки и обновляет инициалы, если они не заданы вручную | `text` — строка с именем пользователя | Экземпляр аватара |
| `setInitials(text: string): this` | Устанавливает инициалы в аватаре | `text` — строка с инициалами, например, ИП | Экземпляр аватара |
| `setSize(size: number): this` | Устанавливает размер аватара в пикселях | `size` — положительное число | Экземпляр аватара |
| `setBaseColor(colorCode: string): this` | Устанавливает цвет фона аватара в формате HEX | `colorCode` — HEX-код цвета | Экземпляр аватара |
| `setBorderColor(colorCode: string): this` | Устанавливает цвет внешней границы | `colorCode` — HEX-код цвета | Экземпляр аватара |
| `setBorderInnerColor(colorCode: string): this` | Устанавливает цвет внутренней границы | `colorCode` — HEX-код цвета | Экземпляр аватара |
| `setEvents(events: {[key: string]: Function}): this` | Назначает обработчики событий, например, click. Добавляет класс `--cursor-pointer` | `events` — объект с парами тип события → функция | Экземпляр аватара |
| `getContainer(): HTMLElement` | Возвращает корневой DOM-элемент аватара. Создается при первом вызове | — | HTML-элемент `<div class="ui-avatar ...">` |

### Примеры использования

**1. Простой круглый аватар с инициалами**

```
import { AvatarRound } from 'ui.avatar';

const avatar = new AvatarRound({
    title: 'Анна Смирнова',
    size: 48
});

avatar.renderTo(document.getElementById('container'));
```

**2. Аватар с изображением и обработкой клика**

```
import { AvatarSquareAccent } from 'ui.avatar';

const avatar = new AvatarSquareAccent({
    title: 'Иван Иванов',
    userpicPath: '/images/user.jpg',
    size: 64
});

avatar.setEvents({
    click: () => {
        console.log('Аватар кликнут!');
    }
});

avatar.renderTo(document.getElementById('container'));
```

**3. Динамическое изменение аватара**

```
const avatar = new AvatarHexagon({
    title: 'Максим Петров',
    baseColor: '#ff5733'
});

avatar
    .setSize(40)
    .setBaseColor('#2ecc71')
    .setPic('/images/new-photo.jpg');

avatar.renderTo(document.getElementById('container'));
```

**4. Аватар для пользователя экстранета**

```
import { AvatarRoundExtranet } from 'ui.avatar';

const extranetAvatar = new AvatarRoundExtranet({
    title: 'John Doe',
    size: 32
});

extranetAvatar.renderTo(document.getElementById('extranet-container'));
```

### Дополнительная информация

- Все аватары используют SVG для масштабируемого отображения и наложения масок.
- Для генерации инициалов используется первая буква каждого слова из `title`, до двух букв.
- Аватары с суффиксом `Guest` (например, `AvatarRoundGuest`) имеют двойную границу и используют отдельную маску для изображения.
- Акцентные аватары `Accent` используют градиентную заливку через CSS-переменные:

  - `--ui-avatar-color-gradient-start`
  - `--ui-avatar-color-gradient-stop`
- Иконка по умолчанию пользователя отображается, если не заданы ни изображение, ни инициалы.
- Метод `setEvents` автоматически добавляет стиль `cursor: pointer`.
- Размер аватара управляется через CSS-переменную `--ui-avatar-size`, что позволяет легко кастомизировать внешний вид.
