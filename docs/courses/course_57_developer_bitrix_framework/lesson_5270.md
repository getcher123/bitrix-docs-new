# Подготовка списка и его настройка

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 12305 — Техническое задание](lesson_12305.md)
- [Следующий: 5271 — Настройка внешнего вида и доступа для списка →](lesson_5271.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=5270

|  | ### Подготавливаем и настраиваем список |
| --- | --- |




Согласно условиям ТЗ наиболее подходящим под нашу задачу будет функционал

			Универсальные списки

                    **Универсальные списки** – инструмент для удобного хранения и работы с любой структурированной информацией.
 Подробнее в курсе [Администратор сервиса Битрикс24 (коробочная версия)](http://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=04656)

		.








#### Подготовка списка и его настройка




В нашем примере мы будем работать со списками продукта *«Битрикс24 в коробке»* (Сервисы &gt; Списки).




![Нажмите на рисунок, чтобы увеличить](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_path_sm.png)





- Создадим новый список с
  			поддержкой бизнес-процессов
                      ![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/list_create_1new.png)
  		 и произведем настройку подписей. Разделы мы использовать не будем, поэтому оставляем их как есть.
  ![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/list_create_2new.png)
- Добавим поля согласно ТЗ: во вкладке **Действия** выбираем
  			Настроить поля
                      ![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_set_field_1.png)
  		. В открывшемся окне – ![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_add_field.png). Не забудем отметить нужные поля, как обязательные к заполнению.



## Примеры настройки поля типа список

Поле **Тип закупки**.

![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_type_zakup.png)



![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_type_zak_2_.png)


Поле **Статус закупки**.

![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_status_zakup.png)



![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_status_zak_2_.png)




В обязательных полях, которые будут заполняться автоматически, установим в поле **Значение по умолчанию** текст-пояснение:



![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_ini_automat.png)



**Примечание:** Такими полями будут **Инициатор**, **Непосредственный руководитель**, **Главный бухгалтер**, **Финансовый директор**.




## Пример настройки поля с автоматическим значением по умолчанию, равному дате и времени создания заявки

![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_time_date.png)




По ТЗ не требуется выбор пользователей системы, поэтому укажем требуемых сотрудников текстом с использованием поля типа **Cписок**:

![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_example_collegues_list.png)




**Примечание:** Такими полями будут **Бюджетный контролер**, **Юрист**.




Результат создания нами полей, согласно ТЗ, мы увидим в виде

			списка

                    ![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_fields_all.png)

		.




Теперь форма создания

			новой заявки

                    ![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_create_new_request.png)

		 будет иметь вид:



![](../../../images/courses/57/dev.1c-bitrix.ru/images/curs_b24/bizproc/examples/lists/lists_new_element_create_2.png)
