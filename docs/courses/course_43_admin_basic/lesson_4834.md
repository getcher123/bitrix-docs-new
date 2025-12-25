# Правила форматирования HTML

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 4641 — Правила оформления HTML](lesson_4641.md)
- [Следующий: 2506 — Правила оформления CSS →](lesson_2506.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=4834

#### Новая строка для каждого блочного или табличного элемента

Выделяйте новую строку для каждого блочного элемента, ставьте отступы для каждого дочернего элемента.

Плохо:

```
<div class="menu">
<div class="menu-item"><span class="menu-item-title">Home</span></div><div class="menu-item"><span class="menu-item-title">Search</span></div>
</div><div class="breadcrumb"></div>
```

Хорошо:

```
<div class="menu">
	<div class="menu-item">
		<span class="menu-item-title">Home</span>
	</div>
	<div class="menu-item">
		<span class="menu-item-title">Search</span>
	</div>
</div>
<div class="breadcrumb"></div>
```

#### Двойные кавычки в атрибутах

Значения HTML-атрибутов рекомендуется писать в двойных кавычках.

Плохо:

```
<div class='navigation'>
    <div class=menu></div>
</div>
```

Хорошо:

```
<div class="navigation">
    <div class="menu"></div>
</div>
```

#### Множественные атрибуты

Теги с большим количеством атрибутов можно переносить на новые строки. Это улучшит читаемость кода, а также облегчит сравнивание файлов в системе контроля версий (**diff**).

Атрибуты в одну строку:

```
<a class="task-detail-special-link" id="task-detail-special-link-id" href="" title="Special Link" data-id="13">
    <span class="task-detail-special-text">Link</span>
</a>
```

Атрибуты с разбивкой на две строки:

```
<a class="task-detail-special-link" id="task-detail-special-link-id"
   href="" title="Special Link" data-id="13">
      <span class="task-detail-special-text">Link</span>
</a>
```

#### Сортировка атрибутов

HTML-атрибуты должны быть перечислены в следующем порядке:

1. `class`
2. `id`
3. атрибуты тега (`src`, `href`, `title` и другие.)
4. `data-*`
