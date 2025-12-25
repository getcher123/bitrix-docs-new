# Графики нагрузки

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6725 — Действия над сервером](lesson_6725.md)
- [Следующий: 6736 — Роли →](lesson_6736.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=6664

**Внимание**. Модуль Управление масштабированием (scale) устарел и больше не поддерживается.




|  | ### Наглядное отображение |
| --- | --- |





Детальные графики нагрузок различных сервисов на каждом сервере отображаются на странице **Графики нагрузки** (Настройки &gt; Управление масштабированием &gt; Графики нагрузки). Выберите с помощью фильтра нужный сервер, категорию и период для вывода графиков:




![](../../../images/courses/48/dev.1c-bitrix.ru/images/admin_expert/scale/scale_graph_stat1_sm.png)





Система мониторинга позволяет выводить графики сервисов **за день**, **неделю**, **месяц** и **год** для каждого сервера пула, используя панель фильтра:





| **Apache**:
<br>- CPU usage by httpd<br>- Apache accesses<br>- Apache processes<br>- Apache volume | **MySQL**:
<br>- CPU usage by mysqld<br>- MySQL queries<br>- MySQL slow queries<br>- MySQL threads<br>- MySQL throughtput |
| --- | --- |
| **Nginx**:
<br>- CPU usage by nginx<br>- Nginx status<br>- Nginx requests | **Сеть**:
<br>- Connections through firewall<br>- Firewall Throughtput<br>- Netstat<br>- ipconntrack |
| **Система**:
<br>- CPU usage<br>- File table usage<br>- Inode table usage<br>- Load average<br>- Memory usage<br>- Swap in/out<br>- Uptime | **Диски**:
<br>- Disk IOs per device<br>- Disk latency per device<br>- Disk usage per persent<br>- IOstat<br>- Inode usage per persent<br>- Throughtput per device |
| **Процессы**:
<br>- Forkrate<br>- Number of threads<br>- Processes<br>- VMstat |  |






**Внимание**: Для вывода графиков нагрузок предварительно  [включите мониторинг](lesson_6724.md#monitor_on) в меню **Глобальные действия** пула.
