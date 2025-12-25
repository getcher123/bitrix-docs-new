# Настройка почты на Linux

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7475 — Почтовые сервисы](lesson_7475.md)
- [Следующий: 2967 — Настройка почты на VMBitrix →](lesson_2967.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=2945

Рассмотрим вариант настройки почты на примере **CentOS 5** (для других ОС команды и пути могут отличаться).




1. Удалите **sendmail**:
  ```
  # rpm -e --nodeps sendmail
  ```
2. Установите **postfix**:
  ```
  # yum install postfix
  # /etc/postfix/post-install upgrade-package
  ```
3. Перекомпилируйте базу алиасов:
  ```
  # cd /etc
  # newaliases
  ```
4. Измените **sendmail_path** в `/etc/php.ini`:
  ```
  sendmail_path = /usr/sbin/sendmail -t -i
  ```
5. Запустите **postfix**:
  ```
  # service postfix restart
  ```
6. Перезапустите apache:
  ```
  # service zend-server restart
  ```
7. Проверьте наличие **postfix** в автозагрузке
  ```
  # chkconfig --list|grep postfix
  ```
  (по умолчанию есть):
  ```
  postfix         0:off   1:off   2:on    3:on    4:on    5:on    6:off
  ```
  если нет:
  ```
  # chkconfig postfix on
  ```
8. Проверьте работу:
  ```
  <?
  if (mail("moe_mylo@mail.ru","test subject", "test body","From: otpravitel@bitrix.ru"))
  echo "Сообщение передано функции mail, проверьте почту в ящике.";
  else
  echo "Функция mail не работает, свяжитесь с администрацией хостинга.";
  ?>
  ```







|  | #### Материалы по теме: |
| --- | --- |




- [Настройка Postfix для отправки почты (блог разработчика)](https://dev.1c-bitrix.ru/community/webdev/user/8078/blog/4546/)
