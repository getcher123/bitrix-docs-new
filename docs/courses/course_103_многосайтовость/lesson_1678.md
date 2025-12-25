# Примеры настроек сервера Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 1677 — Псевдомногосайтовость на разных доменах](lesson_1677.md)
- [Следующий: 290 — Выделение разделов сайта в поддомены →](lesson_290.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=103&LESSON_ID=1678

Настройки веб-сервера Apache выполняет, как правило, техническая служба хостера. Приведенные ниже примеры настроек сервера Apache даны для ознакомления и понимания механизма настройки




### Многосайтовость на одном домене





В конфигурационном файле **httpd.conf** веб-сервера Apache должна присутствовать примерно такая запись:




```
<VirtualHost *:80>    ServerAdmin admin@site1.com    DocumentRoot "/home/www/allsites"    ServerName www.site1.com    ErrorLog logs/allsite.log    CustomLog logs/allsite.log  common</VirtualHost>
```




Обратите внимание, что параметр `DocumentRoot` имеет значение `/home/www/allsites` и явно указывает на каталог, в котором установлен продукт. Для двух сайтов параметр DocumentRoot будет иметь одно и то же значение.




Строка **&lt;VirtualHost *:80&gt;** указывает на то, что веб-сервер будет отвечать на любое доменное имя по любому IP адресу. Т.е. при соответствующей настройке DNS сервера, веб-сервер будет отвечать по любому из имен www.site1.com или www.site2.com.





### Многосайтовость на разных доменах




В конфигурационном файле **httpd.conf** веб-сервера *Apache* должны присутствовать две записи, каждая из которых описывает свой "виртуальный сервер" (в терминологии, принятой в Apache):




```
<VirtualHost *:80>    ServerAdmin admin@site1.com    DocumentRoot "/home/www/site1"    ServerName site1.com    ServerAlias *.site1.com    ErrorLog logs/site1.log    CustomLog logs/site1.log  common</VirtualHost>
```




```
<VirtualHost *:80>    ServerAdmin admin@site2.com    DocumentRoot "/home/www/site2"    ServerName site2.com    ServerAlias *.site2.com    ErrorLog logs/site2.log    CustomLog logs/site2.log  common</VirtualHost>
```




Обратите внимание, что параметр `DocumentRoot` для каждого сайта указывает в разный каталог на диске, в котором должен быть размещен соответствующий сайт.




Строки **&lt;VirtualHost *:80&gt;** указывают на то, что веб-сервер будет отвечать на любом IP адресе, но переменная `ServerAlias` говорит о том, что каждый из сайтов будет отвечать только по определенному доменному имени.




Т.е. доменное имя www.site1.com будет обрабатываться одним веб-сервером Apache, который работает с каталогом `/home/www/site1/`, а www.site2.com - другим веб-сервером, работающим с каталогом `/home/www/site2/`.




Возможен так же вариант конфигурирования для разных IP адресов. Ниже приведен пример конфигурации Apache для двух разных IP адресов:




```
<VirtualHost 192.168.0.1:80>    ServerAdmin admin@site1.com    DocumentRoot "/home/www/site1"    ServerName site1.com    ErrorLog logs/site1.log    CustomLog logs/site1.log  common    Options +FollowSymLinks</VirtualHost>
```




```
<VirtualHost 192.168.0.2:80>    ServerAdmin admin@site2.com    DocumentRoot "/home/www/site2"    ServerName site2.com    ErrorLog logs/site2.log    CustomLog logs/site2.log  common    Options +FollowSymLinks</VirtualHost>
```




В этом случае при соответствующей настройке DNS для разных доменных имен каждый "виртуальный сервер" (в терминологии Apache) будет работать на отдельном IP адресе и отвечать только по определенному доменному имени.




**Примечание:**

В силу некоторых причин, например: ограничения хостинга, Администратор сайта может не иметь доступа к файлу **httpd.conf**. В этом случае осуществить разделение информации для сайтов можно следующим образом:




- В корне второго сайта создать папку `/bitrix_personal`
- В этой папке сделать две символьные ссылки на `/bitrix/php_interface/` и `/bitrix/templates/` первого сайта.
- В файле **.htaccess** в корне каждого сайта в самом начале необходимо прописать:
