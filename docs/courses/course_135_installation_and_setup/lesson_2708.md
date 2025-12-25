# Использование файлов .htaccess

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2707 — Необходимый уровень прав на сервере](lesson_2707.md)
- [Следующий: 2712 — Ошибки запросов к БД →](lesson_2712.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=2708

### Что такое .htaccess

> **.htaccess** (от англ. hypertext access) - файл дополнительной конфигурации веб-сервера *Apache*. Позволяет задавать большое количество дополнительных параметров и разрешений для работы веб-сервера в отдельном каталоге без изменения главного конфигурационного файла **httpd.conf**.

Файл **.htaccess** является подобием **httpd.conf** с той разницей, что действует только на каталог, в котором располагается, и на его дочерние каталоги.  Директивы этого файла действуют на все файлы в текущем каталоге и во всех его подкаталогах, если только эти директивы не переопределены директивами нижележащих файлов **.htaccess**.

Чтобы файлы **.htaccess** можно было использовать в настройках главного конфигурационного файла **httpd.conf** значение директивы **AllowOverride** должно быть установлено как **All**.

|  |
| --- |

### Как использовать

Пути к файлам и каталогам должны указываться от корня сервера.

При внесении изменений в файл **.htaccess** нет необходимости перезапускать сервер. Файл **.htaccess** проверяется при каждом обращении к серверу, так что изменения вступают в силу сразу после их внесения. Так как файл является служебным, он не доступен пользователям из веб-браузера.

**Обратите внимание!** При установке на шаге предварительной проверки производится проверка обработки файлов **.htaccess**.

В демонстрационном сайте файл **.htaccess** по умолчанию содержит следующие директивы:

```
Options -Indexes
ErrorDocument 404 /404.php

<IfModule mod_php5.c>
  php_flag session.use_trans_sid off
  #php_flag default_charset UTF-8
  #php_value display_errors 1
</IfModule>

<IfModule mod_php7.c>
  php_flag session.use_trans_sid off
  #php_flag default_charset UTF-8
  #php_value display_errors 1
</IfModule>

<IfModule mod_rewrite.c>
  Options +FollowSymLinks
  RewriteEngine On
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-l
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_FILENAME} !/bitrix/urlrewrite.php$
  RewriteRule ^(.*)$ /bitrix/urlrewrite.php [L]
  RewriteRule .* - [E=REMOTE_USER:%{HTTP:Authorization}]
</IfModule>

<IfModule mod_dir.c>
  DirectoryIndex index.php index.html
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive on
  ExpiresByType image/jpeg "access plus 3 day"
  ExpiresByType image/gif "access plus 3 day"
  ExpiresByType image/png "access plus 3 day"
  ExpiresByType text/css "access plus 3 day"
  ExpiresByType application/javascript "access plus 3 day"
</IfModule>

```

**Внимание!** Для активизации закомментированных PHP директив необходимо снять знак комментария (**#**) в начале строки. Если на вашем сервере *Apache* не установлено разрешение на использование PHP-флагов, выполнение данных директив приведет к возникновению внутренней ошибки (500). В случае возникновения ошибки необходимо снова закомментировать директивы, поместив в начало каждой знак **#**.

Для остальных PHP директив, не обозначенных знаком комментария (**#**), добавлена проверка на наличие необходимых модулей *Apache* в системе. Выполнение данных директив не приведет к возникновению ошибки в системе.

1. PHP директива `php_flag session.use_trans_sid off` производит отключение подстановки идентификатора сессии в ссылке на сайте.
2. Значение PHP флага `php_value display_errors 1`, указывает на то, что включено разрешение на вывод сообщений о возникновении ошибок. Директива `php_value error_reporting` определяет уровень ошибок, при возникновении которых будет выводиться сообщение. С помощью указанных директив можно настроить режим вывода интерпретатором PHP сообщений об ошибках.
3. Блок директив `IfModule mod_rewrite.c` - это настройка правил для `mod_rewrite`.
4. Директива `ExpiresActive on` включает кеширование изображений, позволяющее ускорить их загрузку при повторном обращении к страницам сайта.
5. Директивы `ExpiresByType image/jpeg "access plus 3 day"`, `ExpiresByType image/gif "access plus 3 day"`,  `ExpiresByType image/png "access plus 3 day"`, `ExpiresByType text/css "access plus 3 day"`, `ExpiresByType application/javascript "access plus 3 day"` в свою очередь, определяют формат изображений, стилей, скриптов и срок, на который будет произведено кеширование. По умолчанию, выполняется кеширование файлов формата **.jpeg**, **.gif**, **.png**, **css** и **.js** сроком на 3 дня.

**Внимание!** После внесения изменений, файл **.htaccess** должен быть сохранен в UNIX-формате (для оболочки FAR опция **Сохранить как UNIX-текст**).

|  |
| --- |

### Авторизация в режиме CGI

В некоторых случаях может не работать авторизация при обмене данными с 1С. Часто проблема возникает в результате работы php в режиме **CGI**. В этом режиме есть проблемы с передачей данных авторизации HTTP в php. Можно это проверить, посмотрев **phpinfo()** в разделе `Server API: CGI`.

Можно обойти проблему, но необходимо чтобы на сервере была включена обработка **.htaccess** и поддержка **mod_rewrite**. Для этого выполните следующие действия:

- В корне сайта в файл **.htaccess** добавьте строки:
  ```
      RewriteEngine on
      RewriteRule .* - [E=REMOTE_USER:%{HTTP:Authorization},L]
  ```
- Закоментируйте следующие строки в файле `bitrix/admin/.htaccess`, которые отключают **mod_rewrite**:
  ```
      #<ifmodule mod_rewrite.c="">
      # RewriteEngine Off
      #</ifmodule>
  ```
- В файл `bitrix/php_interface/dbconn.php` добавьте строки:
  ```
      $remote_user = $_SERVER["REMOTE_USER"]
      ? $_SERVER["REMOTE_USER"] : $_SERVER["REDIRECT_REMOTE_USER"];
      $strTmp = base64_decode(substr($remote_user,6));
      if ($strTmp)
          list($_SERVER['PHP_AUTH_USER'], $_SERVER['PHP_AUTH_PW']) = explode(':', $strTmp);
  ```

Для проверки работоспособности HTTP-авторизации воспользуйтесь [скриптом](http://ru2.php.net/manual/ru/features.http-auth.php).



**Внимание!** Данный вариант обхода не всегда может решить проблему. Если при выполнении всех рекомендаций HTTP-авторизация не заработала, то следует обратиться к хостинг-провайдеру с этой проблемой.
