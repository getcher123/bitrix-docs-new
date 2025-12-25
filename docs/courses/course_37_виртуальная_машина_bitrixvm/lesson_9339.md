# 6. Удаление slave сервера MySQL (6. Remove slave MySQL server)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9337 — 5. Смена master сервера MySQL (5. Change master MySQL server)](lesson_9337.md)
- [Следующий: 9341 — 1. Настройка службы memcached (1.Configure memcached service) →](lesson_9341.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=9339

Для удаления slave сервера MySQL необходимо:




- Выбрать пункт меню 3. Configure MySQL service for the pool &gt; 6. Remove slave MySQL server.
  **Примечание**: Данный пункт меню появится только тогда, когда будет создан хотя бы 1 slave-сервер MySQL с помощью меню 3. Configure MySQL servers &gt; 4. Create slave MySQL server.
- Ввести имя хоста удаляемого slave сервера (например **server1**):
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/configure_mysql/vm_mysql_remove_slave1.png)
- Подождать, пока задача по удалению будет закончена.
- В итоге серверы станут: master (**server2**) и один slave (**server3**):
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/configure_mysql/vm_mysql_remove_slave2.png)




Таким образом, мы освободили ресурсы машины **server1** под другие роли.








**Внимание!** Задачи могут выполняться довольно длительное время (до 2-3 часов и более) в зависимости от сложности задачи, объема данных, используемых в этих задачах, мощности и загруженности сервера. Проверить текущие выполняемые задачи можно с помощью меню 10. Background tasks in the pool &gt; 1. View running tasks. Если по каким-либо причинам нужно посмотреть лог-файлы выполнения задач, то они находятся в директории `/opt/webdir/temp`.
