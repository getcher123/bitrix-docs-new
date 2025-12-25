# Увеличение размера существующего жесткого диска BitrixVM

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6929 — Добавление дополнительного жесткого диска BitrixVM](lesson_6929.md)
- [Следующий: 8909 — Увеличение размера LVM-раздела BitrixVM →](lesson_8909.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6928

Вторым способом увеличения дискового пространства в *BitrixVM* является увеличение размера уже существующего жесткого диска виртуальной машины.





В данном примере воспользуемся виртуальной машиной *BitrixVM для VMWare* и покажем, как увеличить размер системного диска до 100Гб.




1. Для этого необходимо запустить **VMWare Player**, в списке виртуальных машин выбрать виртуальную машину *BitrixVM* и нажать **Edit virtual machine settings**:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase6.png)
2. В окне устройств выбрать **Hard Disk**, размер которого нужно увеличить, и активировать в меню **Utilities** пункт **Expand**:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase7.png)
3. В открывшемся окне **Expand Disk Capacity** в поле **Maximum disk size (GB)** указать необходимый объем виртуального диска в гигабайтах (в данном примере - 100Гб):
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase8.png)
4. Далее необходимо запустить виртуальную машину *BitrixVM*, авторизоваться под **root** и перейти в режим командной строки (консоль), выбрав пункт меню **0. Exit** в виртуальной машине.
5. Смотрим диск и присвоенное ему буквенное обозначение консольной командой:
  ```
  fdisk -c -u -l
  ```
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase9_sm.png)
  где для диска `/dev/sda`:
  Обратите внимание, если BitrixVM установлена на EC2 AWS. На AWS первый сектор раздела может начинаться с `2000`, а не `2048`. В этом случае увеличение размера диска выполняется другим способом. Подробнее на [github](https://github.com/chef-partners/omnibus-marketplace/issues/34). Или можно добавить отдельный диск и перенести на него `/home/bitrix` и/или `/var/lib/mysql`.

  - **sda1** - загрузочный сектор диска;
  - **sda2** - файл подкачки (swap);
  - **sda3** - раздел, в котором установлена операционная система и который как раз и нужно увеличить.
6. Запускаем утилиту **fdisk** для работы с диском `/dev/sda`:
  ```
  fdisk -c -u /dev/sda
  ```
7. Командой **d** удаляем раздел **sda3**, выбрав `Partition number (1-4): 3`:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase10_sm.png)
  **Внимание!** Данные с диска при этом никуда не удаляются, в данном случае удаляется лишь запись о разделе из таблицы разделов диска.
8. Далее командой **n** создаем новый раздел:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase11_sm.png)

  - основной (primary partition) - команда **p** и `Partition number (1-4): 3`;
  - первый и последний сектора при этом выбираем по умолчанию - таким образом, будет создан раздел, используя все свободное пространство на диске.
9. Для сохранения обновленной таблицы разделов и выхода из fdisk введите команду **w**:
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase12_sm.png)
10. Чтобы система подгрузила новую таблицу разделов, необходима перезагрузка виртуальный машины:
  ```
  reboot
  ```
11. После перезагрузки с помощью утилиты **resize2fs** увеличиваем размер файловой системы раздела `/dev/sda3`:
  ```
  resize2fs /dev/sda3
  ```
  ![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase13_sm.png)




Проверить, что раздел увеличен можно с помощью команды **df**:




![](../../../images/courses/37/dev.1c-bitrix.ru/images/portal_admin/install/vmbitrix/vm_disk_increase14_sm.png)




Изменение размера дисков в других средах виртуализации проходит аналогично.






#### Дополнительно:




Если нужен диск объёмом более

			2 Тб

                    Утилита fdisk умеет расширять диск не более чем на 2Тб.

		, это можно [сделать так](https://askubuntu.com/questions/626420/resize-ext4-partition-to-2tb-without-data-loss).
