# Исходные коды пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 29414 — Подключение IDE](lesson_29414.md)
- [Следующий: 29420 — Ручное включение php-расширений →](lesson_29420.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=29416

**Внимание!**

1. Для операций, описанных в данной главе, необходимы знания администрирования *nix-систем. Перед началом проведения данных операций рекомендуется сделать полный бекап *«Виртуальной машины»*.
2. Приведённые настройки выходят за рамки меню Виртуальной машины. Это означает, что информация - ознакомительная и применять её следует с чётким пониманием того что вы делаете и с собственной ответственностью за совершаемые действия. В нашей техподдержке рассматриваются только вопросы по работе пунктов меню ВМ.




При разработке своих решений на основе виртуальной машины *BitrixEnv/VMBitrix*, может понадобиться отслеживание изменений в версиях файлов. Для этого вы можете подключить репозиторий исходников виртуальной машины.




1. Добавляем файл для репозитория `/etc/yum.repos.d/bitrix-source-9.repo` с содержимым:
  ```
  [bitrix-source-9]
  name=Bitrix Packages Source for Enterprise Linux 9 - x86_64
  baseurl=https://repo.bitrix24.tech/dnf/SRPMS
  enabled=1
  gpgcheck=1
  priority=1
  failovermethod=priority
  gpgkey=https://repo.bitrix24.tech/dnf/RPM-GPG-KEY-BitrixEnv-9
  ```
2. Проверяем, что есть пакеты **dnf-utils** и **yum-utils**:
  ```
  dnf clean all && dnf install -y dnf-utils yum-utils
  ```
3. Скачиваем все исходники (bitrix-env, bx-nginx, bx-ansible-core, bx-push-server):
  ```
  yumdownloader --source bitrix-env bx-nginx bx-ansible-core bx-push-server
  ```
  ## Примерный ответ в консоли для VMBitrix
  ```
  [root@server1 ~]# yumdownloader --source bitrix-env bx-nginx bx-ansible-core bx-push-server
  enabling baseos-source repository
  enabling appstream-source repository
  enabling crb-source repository
  enabling extras-common-source repository
  enabling centos-kmods-source repository
  enabling centos-kmods-userspace-source repository
  enabling epel-source repository
  enabling epel-cisco-openh264-source repository
  enabling epel-next-source repository
  CentOS Stream 9 - BaseOS - Source               299 kB/s | 509 kB     00:01
  CentOS Stream 9 - AppStream - Source            670 kB/s | 1.2 MB     00:01
  CentOS Stream 9 - CRB - Source                  124 kB/s | 170 kB     00:01
  CentOS Stream 9 - Extras packages - Source       13 kB/s |  14 kB     00:01
  CentOS 9 - Kmods - Source                        12 kB/s |  13 kB     00:01
  CentOS 9 - Kmods - User Space - Source          3.1 kB/s | 3.5 kB     00:01
  Extra Packages for Enterprise Linux 9 - x86_64  2.9 MB/s | 4.3 MB     00:01
  Extra Packages for Enterprise Linux 9 openh264  675  B/s | 1.2 kB     00:01
  Extra Packages for Enterprise Linux 9 - Next -  6.7 kB/s |  58 kB     00:08
  (1/4): bx-push-server-3.0.0-0.el9.src.rpm       394 kB/s | 104 kB     00:00
  (2/4): bx-ansible-core-2.14.2-4.el9.src.rpm     1.9 MB/s |  12 MB     00:06
  (3/4): bitrix-env-9.0-0.el9.src.rpm             830 kB/s | 7.0 MB     00:08
  (4/4): bx-nginx-1.26.1-0.el9.ngx.src.rpm        2.4 MB/s |  84 MB     00:35
  [root@server1 ~]#
  ```
