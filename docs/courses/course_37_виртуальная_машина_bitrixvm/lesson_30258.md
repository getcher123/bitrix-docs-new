# 2. Обновить настройки sphinx (2. Update sphinx instance on server)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 30256 — 1. Создать инстанс sphinx на сервере (1. Create sphinx instance on server)](lesson_30256.md)
- [Следующий: 30262 — 3. Удалить sphinx на сервере (3. Remove sphinx instance on server) →](lesson_30262.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=30258

Чтобы обновить настройки Sphinx-инстанса, нужно перейти в главном меню *5. Configure Sphinx service for the pool &gt; 2. Update sphinx instance on the server (add index)*:




- Далее ввести имя хоста, где будет запущен сервер поиска. В примере это `server1`.
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix9/menu_bitrixv/update_sphinx_2.png)
- Выбрать базу данных ядра системы сайта из списка.
  ![Нажмите на рисунок, чтобы увеличить](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix9/menu_bitrixv/update_sphinx_3_sm.png)
- Дать согласие на запуск полной переиндексации после установки сервера.
  ![Нажмите на рисунок, чтобы увеличить](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix9/menu_bitrixv/update_sphinx_4_sm.png)
- Подождать, пока задача по установке и переиндексации будет закончена.
  ![Нажмите на рисунок, чтобы увеличить](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix9/menu_bitrixv/update_sphinx_5_sm.png)




Опция запускает проверку текущей конфигурации Sphinx-инстанса и принудительную переиндексацию.






**Примечание.** Задачи могут выполняться длительное время. Время зависит от сложности задачи, объема данных, используемых в этих задачах, мощности и загруженности сервера.
Проверить текущие выполняемые задачи можно с помощью меню 10. Background pool tasks &gt; 1. View running tasks. Лог-файлы выполнения задач находятся в директории `/opt/webdir/temp`.




#### Дополнительно




Ручная настройка поискового механизма **Sphinx** описана в учебном курсе [Администратор. Базовый](/learning/course/index.php?COURSE_ID=35&LESSON_ID=5935).
