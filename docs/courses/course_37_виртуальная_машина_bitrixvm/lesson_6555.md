# Корректное монтирование Windows-ресурсов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 6554 — Подключение Swap-раздела](lesson_6554.md)
- [Следующий: 6556 — Настройка memcached →](lesson_6556.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=6555

**Внимание!** Для операций, описанных в данном уроке, необходимы знания администрирования *nix-систем. Перед началом проведения данных операций рекомендуется сделать полный бекап *BitrixVM*.






В случае необходимости подключения сетевого диска Windows в качестве хранилища для **WebDAV** можно воспользоваться следующей командой:




```

mount -t cifs -o -fstype=cifs,iocharset=utf8,username=XXXX,password=XXXX,uid=500,gid=501,fmode=0777,noserverino //xxx.xxx.xxx.xxx/folder /home/bitrix/www/docs/folder/smb
```


где:

- `uid` - идентификатор пользователя **bitrix**;
- `gid` - идентификатор группы **bitrix**;
- `//xxx.xxx.xxx.xxx/folder` - путь к сетевому ресурсу;
- `/home/bitrix/www/docs/folder/smb` - папка, куда будет смонтирован диск.




**Примечание**: Использование опции **noserverino** является обязательным, так как в PHP есть [уязвимость](https://bugs.php.net/bug.php?id=51404).
