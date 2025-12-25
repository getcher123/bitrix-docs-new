# 8. Настройка xmppd|smtpd сервисов для сайта (8. Configure optional services (xmppd|smtpd) for site)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8859 — 7. Настройка NTLM-авторизации на всех сайтах (7. Configure NTLM auth for all sites)](lesson_8859.md)
- [Следующий: 8865 — Условия работы композитного кеша →](lesson_8865.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8861

Мастер позволяет управлять работой сервисов **XMPP** и **SMTP** с помощью *Cron*. Это может понадобится, если необходимо рассылать jabber- и почтовые сообщения в случае, если на сайте нет активности, т.е если все события на сайте работают на хитах.








Для управления необходимо:



- Из административного меню запустить мастер 6. Configure pool sites &gt; 8 Configure optional services (xmppd|smtpd) for site:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sites/vm_manage_xmppd1.png)
- Далее указать:

  - **Enter site-name** - имя сайта;
  - **Enter service name** - имя сервиса **xmppd** или **smtpd**.
- И согласиться на активацию работы сервисов через *Cron*:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sites/vm_manage_xmppd2.png)
- После завершения данной задачи jabber-уведомления и почтовые сообщения будут отправляться по cron-расписанию, независимо от активности на сайте.






Аналогичным образом отключается данные опции:



![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sites/vm_manage_xmppd3.png)








**Внимание!** Задачи могут выполняться довольно длительное время (до 2-3 часов и более) в зависимости от сложности задачи, объема данных, используемых в этих задачах, мощности и загруженности сервера. Проверить текущие выполняемые задачи можно с помощью меню 10. Background pool tasks &gt; 1. View running tasks. Если по каким-либо причинам нужно посмотреть лог-файлы выполнения задач, то они находятся в директории `/opt/webdir/temp`.
