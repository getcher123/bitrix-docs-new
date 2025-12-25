# Настройка NTLM-авторизации для Apache

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5078 — Настройка NTLM авторизации со стороны продукта](lesson_5078.md)
- [Следующий: 3590 — Настройка NTLM модуля Linux для Битрикс →](lesson_3590.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=2548

Поддержка **NTLM-авторизации** по умолчанию включена в дистрибутив продукта. Для этого рекомендуется использовать виртуальную машину VMBitrix, в ней настройка окружения для NTLM-авторизации выполняется через [меню](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8859&LESSON_PATH=3908.8809.8847.8859).

Если вы не используете рекомендуемый компанией *"1С-Битрикс"* пакет, то вам необходимо в настройках вашего окружения сделать следующее:

### Для Centos 6

1. [Загрузите](http://sourceforge.net/projects/mod-auth-sspi/) модуль **mod_auth_sspi** и установите его:
  ```
  LoadModule sspi_auth_module modules/mod_auth_sspi.so
  ```
2. В файле **httpd.conf** добавьте строку:
  ```
  LoadModule sspi_auth_module modules/mod_auth_sspi.so.
  ```
3. В файле **.htaccess** добавьте следующие строки:
  ```
  AuthName "My Intranet"
  AuthType SSPI
  SSPIAuth On
  SSPIPackage NTLM
  SSPIDomain MYDOMAIN
  SSPIPerRequestAuth On
  SSPIAuthoritative On
  SSPIOfferBasic On
  Require valid-user
  ```
  При использовании стандартного пакета *Битрикс: Веб-окружение* указанные строчки в этом файле необходимо не создавать, а раскомментировать.

### Для Centos 7

1. Загрузите модуль **auth_ntlm_winbind_module** и установите его:
  ```
    LoadModule auth_ntlm_winbind_module modules/mod_auth_ntlm_winbind.so
  ```
2. Для SSL обязательно  добавьте:
  ```
    LoadModule ssl_module modules/mod_ssl.so
    # httpd 2.4
    LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
  ```

### Для всех видов установки

1. В строке `SSPIDomain MYDOMAIN` файла **.htaccess** смените `MYDOMAIN` на имя вашего домена.
2. Сохраните внесенные изменения.
