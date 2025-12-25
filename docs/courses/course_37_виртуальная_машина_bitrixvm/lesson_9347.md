# 1. Создать инстанс sphinx на сервере (1. Create sphinx instance on server)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8869 — 11. Сайты с ошибками (11. Show sites with errors)](lesson_8869.md)
- [Следующий: 9349 — 2. Обновить настройки sphinx (создать индекс) (2. Update sphinx instance on server (add index)) →](lesson_9349.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=9347

Для установки **Sphinx** на сервер необходимо:




- Установить и обновить проект до последней актуальной версии;
- В меню виртуальной машины выбрать пункт 7. Configure Sphinx service for the pool &gt; 1. Create sphinx instance on server:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sphinx/vm_sphinx1.png)
- Далее ввести имя хоста, где будет запущен сервер поиска (в данном примере **server1**):
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sphinx/vm_add_sphinx1.png)
- Выбрать базу данных ядра системы сайта из списка:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sphinx/vm_add_sphinx2.png)
- Дать согласие на запуск полной переиндексации после установки сервера:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sphinx/vm_add_sphinx3.png)
- Подождать, пока задача по установке и переиндексации будет закончена:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/manage_sphinx/vm_add_sphinx4.png)






**Внимание!** Задачи могут выполняться довольно длительное время (до 2-3 часов и более) в зависимости от сложности задачи, объема данных, используемых в этих задачах, мощности и загруженности сервера. Проверить текущие выполняемые задачи можно с помощью меню 10. Background pool tasks &gt; 1. View running tasks. Если по каким-либо причинам нужно посмотреть лог-файлы выполнения задач, то они находятся в директории `/opt/webdir/temp`.






**Примечание:** Ручная настройка поискового механизма **Sphinx** описана в данном [уроке](/learning/course/index.php?COURSE_ID=35&LESSON_ID=5935).
