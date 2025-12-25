# Ошибки подключения к БД

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3295 — Использование файлов .htaccess](lesson_3295.md)
- [Следующий: 3297 — Ошибки запросов к БД →](lesson_3297.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=3296

При возникновении ошибки подключения к базе данных на экран выдается сообщение вида:




![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/additional/db_error_report.png)




Для решения проблемы следует:




- проверить параметры подключения к базе данных (файл `/bitrix/php_interface/dbconn.php` до версии 20.900.0 и файл `/bitrix/.settings.php` с версии 20.900.0);
- проверить доступность базы данных.




Внешний вид сообщения об ошибке определяется в файле `/bitrix/modules/main/include/dbconn_error.php`:




```
<br>
<table cellpadding="1" cellspacing="0" width="35%" bgcolor="#9C9A9C">
	<tr>
		<td><table cellpadding="5" cellspacing="0" width="100%">
			<tr>
				<td bgcolor="#FFFFFF" align="center"><FONT face="Verdana, Arial, Helvetica, sans-serif" size="-1">
				<font color="#FF0000"><b><?echo "Error connecting to database."?></b></font><br>Please try again.</font></td>
			</tr>
		</table></td>
	</tr>
</table>
<br><br><br>
```




Для проверки доступности базы данных можно использовать, в частности, **MySQLGUI** - интерфейс управления для Windows, доступный для скачивания на странице [http://www.mysql.ru/download/](http://www.mysql.ru/download/).
