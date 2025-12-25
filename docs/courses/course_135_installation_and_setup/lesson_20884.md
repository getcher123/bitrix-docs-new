# Конфигурация MariaDB

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 20882 — Конфигурация Apache](lesson_20882.md)
- [Следующий: 20886 — Конфигурация Redis →](lesson_20886.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20884

Для конфигурации MariaDB требуется выполнить такие настройки:

- **transaction-isolation** изменить на `READ-COMMITTED`;
- **innodb_flush_method** установить равным `O_DIRECT` (желательная, но не обязательная настройка);
- **innodb_flush_log_at_trx_commit** установить равным **2** (желательная, но не обязательная настройка).

Все конфигурационные файлы можно [скачать в архиве](/docs/chm_files/sles15.zip). Конфигурационные файлы для MariaDB находятся в папке: `sles15/my.cnf.d`.

Разместите их в директории `/etc/my.cnf.d/`.

Запустите сервис:

```
systemctl --now enable mariadb
```

Настройки сервис выполняются через **mysql_secure_installation**.
