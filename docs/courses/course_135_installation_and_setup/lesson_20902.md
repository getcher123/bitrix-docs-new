# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20900 — Конфигурация Apache](lesson_20900.md)
- [Следующий: 20904 — Конфигурация Redis →](lesson_20904.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20902

Для конфигурации MariaDB выполните следующие настройки:

- **transaction-isolation** измените на `READ-COMMITTED`;
- **innodb_flush_method** установите равным `O_DIRECT` (рекомендованная, но не обязательная настройка);
- **innodb_flush_log_at_trx_commit** установить равным **2** (рекомендованная, но не обязательная настройка).

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/redos.zip). Конфигурационные файлы для MariaDB расположены в папке: `redos/my.cnf.d`.

Разместите их в директории `/etc/my.cnf.d/`.

Запустите сервис:

```

systemctl --now enable mariadb
```

Настройка сервиса выполняется через **mysql_secure_installation**.
