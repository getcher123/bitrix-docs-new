# Настройка резервного копирования сайта (Change backup settings on site)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6538 — Настройка https на сайте (Change https settings on site)](lesson_6538.md)
- [Следующий: 6540 — Настройка NTLM-авторизации на всех сайтах (Configure NTLM auth for all sites) →](lesson_6540.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6539

При разворачивании проектов на базе **BitrixVM**, часто встает задача создания резервной копии проекта по расписанию.




В *«1C-Битрикс: Виртуальная машина»* версии 4.х появился функционал автоматического резервного копирования сайта, находящегося в директории `/bitrix/home/www/`, и базы данных. Бекап будет создан по расписанию в виде архива **.tar.gz** и записан в директории `/home/bitrix/backup/archive/`.





У данного способа есть как преимущества, так и недостатки в сравнении с встроенным в продукты «1С-Битрикс» механизмом создания резервной копии:



- **К преимуществам** относятся более высокая скорость создания резервной копии и независимость от работоспособности проекта.
- **Из недостатков** стоит отметить то, что при использование данного способа нельзя сделать резервную копию файлов, расположенных в облачных хранилищах.







Для создания расписания автоматического резервного копирования средствами BitrixVM необходимо:




- В меню виртуальной машины выбрать пункт 6. Manage sites in the pool &gt; 6. Change backup settings on site.
- Выбрать из списка имя хоста и согласиться на изменение настроек расписания автоматического резервного копирования:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_backup1_sm.png)
- Выбрать периодичность и час запуска автоматического резервного копирования:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_backup2_sm.png)
  Если необходимо выполнить более точную настройку бэкапов, можно воспользоваться утилитой командной строки:
  ```
  /opt/webdir/bin/bx-sites -a backup -d dbcp --enable --minute=10 --hour=18 --day=any --month=any --weekday=any
  ```
  **Примечание**: Как настроить правильное время в *«1C-Битрикс: Виртуальная машина»* см. [здесь](lesson_6524.md).
- На этом работа мастера настройки завершена, и в Cron (`/etc/crontab`) добавляется задача резервного копирования проекта:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vmbitrix5/manage_pool/site/vm_backup3_sm.png)
  Бэкап делается для ядра (сайта типа **kernel** и **ext_kernel**) и всех его **link**, если такие существуют.
  Для этого создается задание в crontab-файле:
  ```
  10 22 * * * bitrix /opt/webdir/bin/bx_backup.sh sitemanager0 /home/bitrix/backup/archive
  ```
  В качестве первой опции указывается **имя БД**, второй опцией указывается **каталог**, в котором будет создан архив.
  В итоге скрипт создаст архив следующего вида:  **www_backup__DD.MM.YYYY_&lt;random_string&gt;.tar.gz** (например - www_backup_dbcp_21.10.2014_1RJKXbMv.tar.gz).
  Внутри архива должны присутствовать следующие файлы:

  1. дамп БД `/home/bitrix/mysql_dump__DD.MM.YYYY_.sql`
  2. данные сайта ядра
  3. данные сайтов  типа ссылок с полным путем








#### Управление бэкапами через bx-sites



- `-a|--action` - действие по управлению сайтами, в данном случае это backup
- `-d|--database` - название БД (в бэкапе будут содержаться данные для всех сайтов, которые используют эту БД)
- `--enable|--disable` - включение или отключение бэкапа для сайтов
- `--minute` - параметры записи в crontab файле (минуты)
- `--hour` - параметры записи в crontab файле (часы)
- `--day` - параметры записи в crontab файле (день)
- `--month` - параметры записи в crontab файле (месяц)
- `--weekday` - параметры записи в crontab файле (день недели)




В случае успешного выполнения утилита вернет новые опции для сайта:



```

/opt/webdir/bin/bx-sites -a backup -d sitemanager0 --enable --minute=10 --hour=23 --day=1 --month=any --weekday=any -o json | python -mjson.tool
...
            "BackupCronFile": "/etc/crontab",
            "BackupDay": "1",
            "BackupFolder": "/home/bitrix/backup/archive",
            "BackupHour": "23",
            "BackupMinute": "10",
            "BackupMonth": "*",
            "BackupTask": "enable",
            "BackupVersion": "v5",
            "BackupWeekDay": "*",
...
```







#### Списки исключений




Ряд файлов/каталогов необходимо исключить из резервной копии. Список таких исключений можно найти в файле **/opt/webdir/bin/ex.txt**.



По умолчанию, в нем находятся следующие подкаталоги:



```

bitrix/cache
bitrix/managed_cache
bitrix/stack_cache
bitrix/local_cache
bitrix/backup
bitrix/tmp
upload/tmp
upload/resize_cache
```








#### Содержимое бэкапа/восстановление




Как уже сказано выше, в бэкап включается:



- сам каталог сайта ядра (**kernel** или **ext_kernel**);
- файл dump БД (`/home/bitrix/mysql_dump_<db>.sql`);
- каталоги сайтов (**link**), которые используют ядро.




Например команда:

```

/opt/webdir/bin/bx_backup.sh sitemanager0 /home/bitrix/backup/archive
```



создает файл **www_backup_sitemanager0_30.01.2015_bnnW1NPm.tar.gz** в директории  `/home/bitrix/backup/archive/`





Для восстановления, нужно перейти в DocumentRoot ядра, выполнить:



```

tar xzvvf www_backup_sitemanager0_30.01.2015_zEQkXREd.tar.gz ./
...
-rw-r--r-- bitrix/bitrix    5013 2015-01-30 14:02 ./workgroups/.left.menu_ext.php
-rw-r--r-- bitrix/bitrix     319 2015-01-30 14:01 ./.top_links.menu.php
-rw-r--r-- root/root     5313008 2015-01-30 14:22 home/bitrix/mysql_dump_sitemanager0_30.01.2015_bnnW1NPm.sql
drwxr-xr-x                    Creating directory: home
drwxr-xr-x                    Creating directory: home/bitrix
-rw-r--r-- root/root          44 2015-01-30 14:22 home/bitrix/mysql_dump_sitemanager0_30.01.2015_bnnW1NPm_after_connect.sql
```





После чего нужно восстановить БД:



```

mysql sitemanager0 < home/bitrix/mysql_dump_sitemanager0_30.01.2015_bnnW1NPm_after_connect.sql
```




И данные дополнительных сайтов, если они есть:



```

rsync -av home/bitrix/ext_www/ /home/bitrix/ext_www/
```





Если необходимо осуществить перенос сайта, то воспользуйтесь [инструкцией по переносу](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&CHAPTER_ID=02014).










**Примечание**: Не забывайте следить за свободным местом на диске и периодически удалять старые резервные копии.
