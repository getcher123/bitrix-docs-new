# Исходные коды пакетов (начиная с версии 7.3.0!)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8901 — Подключение IDE](lesson_8901.md)
- [Следующий: 11783 — Ручное включение php-расширений →](lesson_11783.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=11161

**Внимание!**

1. Для операций, описанных в данной главе, необходимы знания администрирования *nix-систем. Перед началом проведения данных операций рекомендуется сделать полный бекап *«Виртуальной машины»*.
2. Приведённые настройки выходят за рамки меню Виртуальной машины. Это означает, что информация - ознакомительная и применять её следует с чётким пониманием того что вы делаете и с собственной ответственностью за совершаемые действия. В нашей техподдержке рассматриваются только вопросы по работе пунктов меню ВМ.




При разработке своих решений на основе виртуальной машины *BitrixEnv/VMBitrix.CRM*, может понадобиться отслеживание изменений в версиях файлов. Для этого вы можете подключить репозиторий исходников виртуальной машины.





**Внимание!** Исходные коды пакетов доступны для стабильных и бета-версий *VMBitrix/VMBitrix.CRM*, начиная с версии **7.3.0**.







#### Стабильная VMBitrix/VMBitrix.CRM



1. Добавляем файл для репозитория `/etc/yum.repos.d/bitrix-source-stable.repo` с содержимым:
  ```
  [bitrix-source-stable]
  name=$OS $releasever - source
  failovermethod=priority
  baseurl=https://repo.bitrix24.tech/yum/SRPMS
  enabled=1
  gpgcheck=1
  gpgkey=https://repo.bitrix24.tech/yum/RPM-GPG-KEY-BitrixEnv
  ```
2. Проверяем, что есть пакет **yum-utils**:
  ```
  yum clean all && yum install yum-utils
  ```
3. Скачиваем исходники виртуальной машины:

  - #### VMBitrix:
    ```
    yumdownloader --source bitrix-env
    ```
    ## Примерный ответ в консоли для обычной VMBitrix
    ```
    [root@qa-new ~]# yumdownloader --source bitrix-env
    Loaded plugins: etckeeper, fastestmirror
    Enabling epel-source repository
    Enabling updates-source repository
    Enabling base-source repository
    Enabling extras-source repository
    Loading mirror speeds from cached hostfile
    epel-source/x86_64/metalink										|  14 kB  00:00:00
    * base: ftp.heanet.ie
    * epel: s3-mirror-eu-west-1.fedoraproject.org
    * epel-source: mirror.sax.uk.as61049.net
    * extras: ftp.heanet.ie
    * remi: rpms.remirepo.net
    * remi-php70: rpms.remirepo.net
    * remi-safe: rpms.remirepo.net
    * updates: ftp.heanet.ie
    base-source														| 2.9 kB  00:00:00
    epel-source														| 3.5 kB  00:00:00
    extras-source													| 2.9 kB  00:00:00
    updates-source													| 2.9 kB  00:00:00
    (1/5): updates-source/7/primary_db								|  17 kB  00:00:01
    (2/5): epel-source/x86_64/updateinfo							| 921 kB  00:00:01
    (3/5): extras-source/7/primary_db								|  39 kB  00:00:01
    (4/5): base-source/7/primary_db									| 1.0 MB  00:00:01
    (5/5): epel-source/x86_64/primary_db							| 2.3 MB  00:00:02
    No source RPM found for bitrix-env-7.1-0.el7.centos.noarch
    No source RPM found for bitrix-env-7.0-0.el7.centos.noarch
    No source RPM found for bitrix-env-5.2-1.el7.centos.noarch
    No source RPM found for bitrix-env-7.2-1.el7.centos.noarch
    No source RPM found for bitrix-env-7.3-0.el7.centos.noarch
    No source RPM found for bitrix-env-5.1-6.el7.centos.noarch
    No source RPM found for bitrix-env-7.2-2.el7.centos.noarch
    No source RPM found for bitrix-env-5.1-7.el7.centos.noarch
    No source RPM found for bitrix-env-5.1-8.el7.centos.noarch
    No source RPM found for bitrix-env-7.0-1.el7.centos.noarch
    No source RPM found for bitrix-env-7.2-0.el7.centos.noarch
    No source RPM found for bitrix-env-5.1-9.el7.centos.noarch
    No source RPM found for bitrix-env-5.2-0.el7.centos.noarch
    bitrix-env-7.3-0.fc27.src.rpm									| 7.8 MB  00:00:01
    [root@qa-new ~]#
    ```
  - #### VMBitrix.CRM
    ```
    yumdownloader --source bitrix-env-crm
    ```
    ## Примерный ответ в консоли для VMBitrix.CRM
    ```
    [root@qa-new ~]# yumdownloader --source bitrix-env-crm
    Loaded plugins: etckeeper, fastestmirror
    Enabling epel-source repository
    Enabling updates-source repository
    Enabling base-source repository
    Enabling extras-source repository
    Loading mirror speeds from cached hostfile
    * base: ftp.heanet.ie
    * epel: s3-mirror-eu-west-1.fedoraproject.org
    * epel-source: mirror.sax.uk.as61049.net
    * extras: ftp.heanet.ie
    * remi: rpms.remirepo.net
    * remi-php70: rpms.remirepo.net
    * remi-safe: rpms.remirepo.net
    * updates: ftp.heanet.ie
    No source RPM found for bitrix-env-crm-7.2-1.el7.centos.noarch
    No source RPM found for bitrix-env-crm-7.2-0.el7.centos.noarch
    No source RPM found for bitrix-env-crm-7.2-2.el7.centos.noarch
    No source RPM found for bitrix-env-crm-7.3-0.el7.centos.noarch
    bitrix-env-crm-7.3-0.fc27.src.rpm								| 7.8 MB  00:00:02
    [root@qa-new ~]#
    ```








#### Бета VMBitrix/VMBitrix.CRM




1. Добавляем файл для репозитория `/etc/yum.repos.d/bitrix-source-beta.repo` с содержимым:
  ```
  [bitrix-source-beta]
  name=$OS $releasever - source
  failovermethod=priority
  baseurl=https://repo.bitrix24.tech/yum-beta/SRPMS
  enabled=1
  gpgcheck=1
  gpgkey=https://repo.bitrix24.tech/yum/RPM-GPG-KEY-BitrixEnv
  ```
2. Проверяем, что есть пакет **yum-utils**:
  ```
  yum clean all && yum install yum-utils
  ```
3. Скачиваем исходники виртуальной машины:

  - #### VMBitrix:
    ```
    yumdownloader --source bitrix-env
    ```
  - #### VMBitrix.CRM
    ```
    yumdownloader --source bitrix-env-crm
    ```
