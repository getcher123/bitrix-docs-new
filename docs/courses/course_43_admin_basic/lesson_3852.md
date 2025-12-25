# Toolbar компонента

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3851 — Добавление контекстного меню](lesson_3851.md)
- [Следующий: 22638 — Страница со списком элементов →](lesson_22638.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3852

Для вывода toolbar'a компонента используйте в **component.php** следующий код:

```
$this->AddIncludeAreaIcons(
	Array( //массив кнопок toolbar'a
		Array(
			"ID" => "Идентификатор кнопки",
			"TITLE" => "Название кнопки toolbar'a",
			"URL" => "ссылка для перехода", //или javascript:MyJSFunction ()
			"ICON" => "menu-delete", //CSS-класс с иконкой
			"MENU" => Array(
				//массив пунктов контекстного меню
			),
			"HINT" => array( //тултип кнопки
				"TITLE" => "Заголовок тултипа",
				"TEXT" => "Текст тултипа" //HTML допускается
			),
			"HINT_MENU" => array ( //тултип кнопки контекстного меню
				"TITLE" => "Заголовок тултипа",
				"TEXT" => "Текст тултипа" //HTML допускается
			),
			"IN_PARAMS_MENU" => true, //показать в контекстном меню
			"IN_MENU" => true //показать в подменю компонента
		)
	)
);
```

```
//Режим редактирования включён?
if ($APPLICATION->GetShowIncludeAreas())
{
	$this->AddIncludeAreaIcons(Array(
		//массивы кнопок toolbar'a
	));
}
```
