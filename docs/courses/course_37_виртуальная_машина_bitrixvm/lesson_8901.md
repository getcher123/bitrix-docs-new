# Подключение IDE

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8899 — Опции монтирования](lesson_8899.md)
- [Следующий: 11161 — Исходные коды пакетов (начиная с версии 7.3.0!) →](lesson_11161.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8901

**Внимание!** Приведённые настройки выходят за рамки меню Виртуальной машины. Это означает, что информация - ознакомительная и применять её следует с чётким пониманием того что вы делаете и с собственной ответственностью за совершаемые действия. В нашей техподдержке рассматриваются только вопросы по работе пунктов меню ВМ.




Для упрощения работы с `Bitrix Framework` в виртуальную машину включён **Xdebug**. Работает он по схеме:




![](../../../images/courses/37/dev.1c-bitrix.ru/images/bitrixvm/vmbitrix7/other_options/setting_ide.png)




Перед изменением настроек надо переименовать файл **xdebug.ini.disabled** в **xdebug.ini** и перезапустить **httpd**.




Для настройки машины воспользуйтесь следующим примером:




```
$ cat /etc/php.d/xdebug.ini
; Enable xdebug extension module
zend_extension=/usr/lib64/php/modules/xdebug.so
xdebug.remote_enable=on
xdebug.remote_host=192.168.205.1
xdebug.remote_port=9000
```




**Примечание**: **Xdebug** требует использовать proxy при работе через **Network Address Translation (NAT)**, необходимо открыть порт 9000.
