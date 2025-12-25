# Сайты с ошибками (Show sites with errors)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3086 — Конфигурационный файл сайта](lesson_3086.md)
- [Следующий: 6517 — Управление sphinx (Manage sphinx in the pool) →](lesson_6517.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=7773

Если по каким-либо причинам на сайтах появились серьезные ошибки: отсутствие модулей на сайте или нет подключения к БД (не получается подключиться с данными настроек сайта), то в меню виртуальной машины появляется пункт меню 6. Manage sites in the pool &gt; 10. Show sites with errors:




![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_site_error1_sm.png)





Выбрав этот пункт меню, отобразится список сайтов с кратким описанием ошибки (в данном примере - нет соединения с базой данных mysql):




![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_site_error2_sm.png)







**Примечание**: Пункт меню **6. Manage sites in the pool &gt; 10. Show sites with errors** является скрытым и появляется только тогда, когда есть ошибки на сайтах под управлением виртуальной машиной *BitrixVM* или linux-окружением *BitrixEnv*. Как только ошибки будут исправлены, данный пункт снова скроется.
