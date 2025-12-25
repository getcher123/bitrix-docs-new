# Установка и настройка ОС

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 15280 — Конфигурация сайта](lesson_15280.md)
- [Следующий: 33048 — Установка пакетов →](lesson_33048.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=33046

### Установка




Приобретите дистрибутив АЛЬТ СП 10 и установите его. В процессе доступен выбор набора пакетов. Можно выбрать минимальный набор пакетов для сервера, а остальные отключить.




Все последующие шаги описаны для сервера с минимальными настройками.






### Настройка репозиториев




Откройте на редактирование файл `/etc/apt/sources.list`.




```
vim /etc/apt/sources.list
```




Добавьте следующие строки в конец файла:




```
rpm [cert8] http://update.altsp.su/pub/distributions/ALTLinux c10f2/branch/x86_64 classic gostcrypto
rpm [cert8] http://update.altsp.su/pub/distributions/ALTLinux c10f2/branch/x86_64-i586 classic
rpm [cert8] http://update.altsp.su/pub/distributions/ALTLinux c10f2/branch/noarch classic
```




Подробную информацию по репозиториям читайте [в документации Альт СП Сервер](https://docs.altlinux.org/ru-RU/cloud/10.0/html/cloud-server-sp/ch06.html). Ветка для Альт СП 10 называется `c10f2`.




В Альт СП 10 применяется система управления программными пакетами `apt-get`. С ее помощью установите обновления до последней стабильной версии и перезапустите систему.




```
su -
apt-get update
apt-get dist-upgrade
reboot
```





### Настройка портов




Обязательно откройте порты:




- 22 — ssh доступ,
- 80 / 443 — http / https web-сервер.




Остальные порты для ntlm, сервера мгновенных сообщений нужно открыть, если только они используются. Можно выбрать произвольные порты, а можно те, что используются в [CentOS](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8811):




- 8890 / 8891 — http/https ntlm,
- 8893 / 8894 — http/https сервер мгновенных сообщений.
