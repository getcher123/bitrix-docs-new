# Внешний вид редактора

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9201 — Где используется редактор](lesson_9201.md)
- [Следующий: 9235 — Форматирование текста →](lesson_9235.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&LESSON_ID=6301

### Из чего состоит редактор

В предыдущем уроке мы узнали, где в системе *"1С-Битрикс: Управление сайтом"* используется визуальный редактор. Во всех этих случаях общий внешний вид редактора остается неизменным. Давайте разберем внешний вид редактора и его панели подробнее.

![Нажмите на рисунок, чтобы увеличить](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/window_small2.png)

1 - панель переключения режимов редактирования. На этой панели мы переключаемся между визуальным режимом и режимом исходного кода.

2 - панель инструментов визуального редактора. Здесь расположены все те инструменты и команды, которые мы будем использовать для работы с текстом и графикой.

3 - рабочая область. Это непосредственно зона для редактирования.

4 - панель компонентов и сниппетов.

5 - панель навигации.

Теперь разберемся для чего нужна каждая панель.

### Видеоурок

### Панель переключения режимов редактирования

Визуальный редактор может работать в двух режимах. Визуальный режим - более простой и интуитивно понятный вариант. Мы сразу видим, как будут выглядеть элементы на странице и используем панель инструментов для форматирования текста. Второй вариант - режим исходного кода. Он предназначен для опытных пользователей, умеющих работать с кодом, и позволяет произвести дополнительную настройку (например, задать значения параметров). В этом режиме панель инструментов становится неактивной.

Также существует совмещенный режим - рабочая область делится на

			две части

                    ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/window_split.png)

		 для визуального режима и режима кода.

Соответственно на панели мы видим кнопки для переключения между этими режимами:

![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/edit_mode.png)

- ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/source_code.png) - режим исходного кода.
- ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/visual_mode.png) - режим визуального редактирования.
- ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/combined_mode_horizontal.png) - совмещенный режим по горизонтали.
- ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/combined_mode_vertical.png) - совмещенный режим по вертикали.

### Панель инструментов

![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/instrument_panel.png)

Кнопки инструментов разделены по группам по своему назначению. Например, группа для форматирования текста включает в себя кнопки жирного текста, курсива, подчеркивания и т.д. Обратите внимание - набор кнопок на панели может немного отличаться в зависимости
    от режима работы и настроек.

**Описание кнопок:**

| \| Кнопка \| Описание \|<br>\| --- \| --- \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/cancel.png) \| Отменить выполненное действие. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/return.png) \| Вернуть отменённое действие. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/style.png) \| Стиль и форматирование текста. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/font.png) \| Шрифт. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/font_size.png) \| Размер шрифта. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/B.png) \| Жирный. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/I.png) \| Курсив. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/U.png) \| Подчёркнутый. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/S.png) \| Зачеркнутый. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/T.png) \| Удалить форматирование. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/A.png) \| Цвет текста. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/format_button_6.png) \| Нумерованный список. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/format_button_7.png) \| Маркированный список. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/indent.png) \| Увеличить отступ. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/decrease_indent.png) \| Уменьшить отступ. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/left.png) \| Выравнивание абзаца по выбранному краю. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/add_ref.png) \| Вставить ссылку. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/del_ref.png) \| Удалить ссылку. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/add_image.png) \| Добавить изображение. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/add_video.png) \| Вставить видеоролик. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/create_anchor2.png) \| Добавить якорь. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/create_table.png) \| Создать таблицу. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/site_template.png) \| Шаблон сайта. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/all_monitor.png) \| Переключение в полноэкранный режим. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/add_specsimvol.png) \| Вставить специальный символ. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/add_break_for_print.png) \| Вставить разрыв страницы для печати. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/add_page_break.png) \| Вставить разделитель страниц. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/spell.png) \| Проверка орфографии. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/seo_button.png) \| Отправить уникальный текст в Яндекс. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/sub_index.png) \| Нижний индекс. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/sup_index.png) \| Верхний индекс. \|<br>\| ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/visual_editor/interface/buttons/settings.png) \| Настройки. \| |
| --- |

### Панель компонентов и сниппетов

![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/components_in_ve4_new.png)

**Компоненты**

                    Компонент – это программный код, оформленный в визуальную оболочку, выполняющий определённую функцию какого-либо модуля по выводу данных в Публичной части. Мы можем вставлять этот блок кода на страницы сайта без непосредственного написания кода. [Подробнее...](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&CHAPTER_ID=04457)

		  - это своеобразный блок из конструктора LEGO. И из этих блоков мы "выстраиваем" публичную часть сайта.

Обратите внимание, что при работе с информационными блоками панель **Компоненты** не отображается. Также панель может быть скрыта при редактировании страницы. Раскройте её нажатием на

			стрелочку



		 в правой части формы.

**Сниппет** - это заранее подготовленный фрагмент текста или кода, этакие заготовки. Предположим, что вам каждый день приходится вставлять на страницы сайта одну и ту же таблицу или форму. Вы можете сохранить эту таблицу в сниппетах и затем простым перетаскиванием размещать ее в нужном месте.

## Пример работы со сниппетами

Например, вам часто приходится размещать на страницах сайта фрагмент, который включает в себя заголовок, текст и небольшую таблицу. Добавим этот фрагмент в сниппеты, это сэкономит значительное количество времени.

Сниппеты редактируются, добавляются и удаляются прямо в визуальном редакторе. Мы можем создать целую структуру сниппетов для того, чтобы было удобнее ориентироваться в заготовках. Добавим новый сниппет:

1. В панели задач визуального редактора выберем Сниппеты -
  			Добавить сниппет
                      ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/controls/snippet_add.png)
  		;
2. На закладке
  			Основные параметры
                      ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/controls/snippet_main.png)
  		 укажем название и добавим код нужного нам фрагмента;
3. На закладке
  			Дополнительные параметры
                      ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/controls/snippet_additional.png)
  		 укажите текст для всплывающей подсказки, он будет появляться при наведении мыши на сниппет в списке. Также укажите раздел, в котором расположить нашу заготовку.

После сохранения сниппет

			появится

                    ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/controls/snippet_in_list.png)

		 в списке.

Для использования сниппета просто перетащим его мышью на рабочее поле.



Готово

                    ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/controls/snippet_final.png)

		, теперь нам останется только заполнить необходимый текст.

### Панель навигации по элементам и сущностям

Панель навигации помогает нам работать с выбранным в рабочей зоне элементом (то есть с тем элементом, на котором находится фокус мыши). Проще говоря, если мы выбрали в рабочей зоне ссылку - с помощью панели навигации можем

			настроить

                    ![](../../../images/courses/34/dev.1c-bitrix.ru/images/content_manager/new_visual_editor/component_parameters_2b_new.png)

		 ее параметры. Выбрали компонент - можем настроить его параметры и т.д.

### Заключение

Визуальный редактор состоит из следующих панелей: инструменты, режимы отображения, компоненты/сниппеты и навигация. Состав панелей может быть разным в зависимости от ситуации. Дальше мы подробнее рассмотрим работу с текстом и графикой в редакторе.
