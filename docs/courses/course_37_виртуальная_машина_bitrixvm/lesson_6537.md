# Настройка почтового сервера (Change e-mail settings on site)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6536 — Настройка задач cron (Change cron tasks on site)](lesson_6536.md)
- [Следующий: 6538 — Настройка https на сайте (Change https settings on site) →](lesson_6538.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6537

Для настройки интегрированного почтового сервера выполните следующее:




1. Перейти в главном меню в 6. Manage sites in the pool &gt; 4. Change e-mail settings on site и ввести имя хоста, для которого нужно настроить отправку почты:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_email1_sm.png)
2. Далее ввести необходимые данные для почтового сервера:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_email2_sm.png)

  - **from address** - адрес отправителя, от которого будет осуществляться пересылка писем.
  - **server address or DNS** - ip- или dns-адрес почтового сервера. Если нажать Enter, то будет использован адрес по умолчанию (127.0.0.1)
  - **server port** - порт сервера. Порт зависит от типа соединения, 25 - для обычного и 465 - для зашифрованного (с использованием SSL). Если нажать Enter, то будет использован порт по умолчанию (25).
  - Если необходима SMTP-авторизация, то в строке **SMTP authentication** наберите `y` и введите логин и пароль для доступа к SMTP-серверу, в противном случае - `n`.
  - Если выбрана опция SMTP-авторизации, то понадобится ввести тип авторизации **type of authentication method**: `auto`, `plain`, `scram-sha-1`, `cram-md5`, `gssapi`, `external`, `digest-md5`, `login`, `ntlm`.
  - Если необходим TLS-протокол защищенной передачи данных, то в строке **TLS enabled** наберите `y`, в противном случае - `n`.
3. Дождаться пока задача по настройке почтового сервера будет закончена.
4. Убедиться в правильности введенных данных настройки почтового сервера можно снова в 6. Manage sites in the pool &gt; 4. Change e-mail settings on site:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_email3_sm.png)






**Внимание!** Задачи могут выполняться довольно длительное время (до 2-3 часов и более) в зависимости от сложности задачи, объема данных, используемых в этих задачах, мощности и загруженности сервера. Проверить текущие выполняемые задачи можно с помощью меню 5. Background tasks in the pool &gt; 1. View running tasks.
