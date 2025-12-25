# Ошибки подключения к БД

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2712 — Ошибки запросов к БД](lesson_2712.md)
- [Следующий: 2809 — 500 - Internal Server Error →](lesson_2809.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=2711

При возникновении ошибки подключения к базе данных на экран выдается

			сообщение вида

                    Внешний вид сообщения об ошибке определяется в файле `/bitrix/modules/main/include/dbconn_error.php`

		:

![](../../../images/courses/135/dev.1c-bitrix.ru/images/portal_admin/install/additional/db_error_report.png)

Для решения проблемы следует:

- проверить параметры подключения к базе данных (файл `/bitrix/php_interface/dbconn.php` до версии 20.900.0, файл `/bitrix/.settings.php<` с версии 20.900.0);
- проверить доступность базы данных.

Для проверки доступности базы данных можно использовать, в частности, *MySQL GUI* - интерфейс управления для Windows, доступный для скачивания на странице [http://www.mysql.ru/download/](http://www.mysql.ru/download/).
