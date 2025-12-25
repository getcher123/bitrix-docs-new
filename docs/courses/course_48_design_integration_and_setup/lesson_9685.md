# Переход на PHP 8.х

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 9223 — Ограничения системы обновлений и лицензии](lesson_9223.md)
- [Следующий: 9117 — Поддержка Битрикс24 в коробке →](lesson_9117.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&LESSON_ID=9685

Для работы продукта минимальная версия PHP – 8.1.





### Почему важно обновить PHP




Версия PHP 7.х [объявлена устаревшей](https://www.php.net/supported-versions.php) и больше не поддерживается, для неё не выпускаются исправления функциональных ошибок и ошибок безопасности. Использование версий PHP ниже 8.1 крайне не рекомендовано.




Вы не сможете установить обновления *«Битрикс24»* для исправления ошибок и получения нового функционала, пока не обновите PHP до минимальной версии 8.1 в своем серверном окружении.






### Как обновить PHP




Обновление версии PHP необходимо произвести поэтапно. Обратитесь к вашему системному администратору или в техподдержку хостинга.




1. Обязательно создайте резервную копию вашей установки. Это может быть как резервная копия средствами продукта, так и полностью всего сервера, например виртуальной машины **VMBitrix**.
2. Обновите ядро и все модули продукта до последних доступных версий в разделе Настройки &gt; Marketplace &gt; Обновление платформы.
3. Обновите все сторонние решения из Маркетплейса до последних доступных версий в разделе Настройки &gt; Marketplace &gt; Обновление решений.
4. Обновите версию PHP до минимальной 8.1 на своем сервере.
  **Примечание.** Если вы используете виртуальную машину **VMBitrix**, то обновить PHP можно через меню VMBitrix: **1. Manage servers in the pool – 6. Update PHP and MySQL**. Подробнее читайте в курсе [Виртуальная машина BitrixVM](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=29266).
5. Еще раз проверьте и установите все доступные обновления платформы и решений из Маркетплейса.








### Куда обращаться в случае ошибок при обновлении версии PHP до 8.х



- Если после обновлений PHP появятся ошибки в работе стандартных модулей *«Битрикс24»*, то обратитесь [в Поддержку24](https://helpdesk.bitrix24.ru/ticket.php).
  Также по модулям из Маркетплейса, в названия которых содержатся `bitrix.*`, нужно обращаться в Поддержку24, например:
  ```
  bitrix.eshop
  bitrix.sitecommunity
  bitrix.sitecorporate
  bitrix.siteinfoportal
  bitrix.sitepersonal
  bitrix.learningtemplates
  ```
- По ошибкам в сторонних модулях из Маркетплейса обращайтесь к разработчикам модуля, их контакты указаны на странице этого модуля во вкладке **Поддержка**.





### Примеры частых ошибок и их решения




#### Возможные причины ошибок после обновления до PHP 8.х:



- До перехода на PHP 8.х не было обновлено ядро и все модули продукта до последних доступных версий в разделе Настройки &gt; Marketplace &gt; Обновление платформы.
- До перехода на PHP 8.х не были уставлены обновления сторонних решений (они в названии имеют точку) на странице Настройки &gt; Marketplace &gt; Обновление решений.
- Разработчик не обновил модуль для поддержки PHP 8.




#### Основные действия по исправлению ошибок после обновления PHP до 8.х:



- Вернитесь на предыдущую версию PHP 7.x, когда все работало, обновите компоненты системы и сторонние модули, а затем повторно обновите версию PHP до 8.х.
- Если предыдущие действия не исправили ошибки, то обратитесь к разработчику модуля – смотрите описание выше [Куда обращаться в случае ошибок](#support).
- Временно отключите модуль с ошибкой, переместив его из директории `/bitrix/modules`.
- Удалите стороннее решение с ошибкой.



Стоить отметить, что в примерах даны лишь решения ошибок для конкретного модуля. Каждая ошибка должна рассматриваться разработчиком индивидуально.




## [Ux11] Ошибка описания модуля "name.module". Не установлено соединение с сервером обновлений. [Ux11] Ошибка описания модуля "name.module".

Ошибка может появиться после повышения версии PHP до 8.0 и выше. Сайт при этом работает, но установить или обновить другие решения нельзя пока сохраняется ошибка.



#### Решение проблемы:



Исправление в общем случае будет таким: в файле `/bitrix/modules/<имя.модуля>/install/index.php` код `function <имя.модуля>()` заменить на `function __construct()`.






## При выполнении скрипта возникла ошибка. Включить расширенный вывод ошибок можно в файле настроек .settings.php.

#### Решение проблемы:



Подключиться по FTP/SFTP или зайти в панель хостинга, включить вывод ошибок в файле `/bitrix/.settings.php`:




```
'debug' => true,
```



После чего на сайте будет выведен текст ошибки:



```
//Пример ошибки
Non-static method Super\Functions\CSuperModRep::checkBack() cannot be called statically (0)
/home/bitrix/modules/super.mod/lib/functions/CSuperModRep.php:52
#0: Super\Functions\CSuperModRep::checkRepActive()
/home/bitrix/modules/super.mod/classes/general/CModEvents.php:1621
#1: CModEvents::OnPageStartHandler()
/home/bitrix/modules/main/classes/general/module.php:480
#2: ExecuteModuleEventEx(array)
/home/bitrix/modules/main/include.php:163
#3: require_once(string)
/home/bitrix/modules/main/include/prolog_before.php:14
#4: require_once(string)
/home/bitrix/modules/main/include/prolog.php:10
#5: require_once(string)
/home/bitrix/header.php:1
#6: require(string)
/home/index.php:1
```




В примере видно, что ошибку отдает сторонний метод `CSuperModRep::checkBack()` решения **super.mod**.



Исправление в общем случае будет таким: в коде `checkBack()` нужно правильно объявить [статическую функцию](https://www.php.net/manual/ru/language.oop5.static.php):



```
function checkBack()
```


заменить на:

```
public static function checkBack()
```





## PHP Fatal error: $GLOBALS can only be modified using the $GLOBALS[$name] = $value syntax in /www/bitrix/modules/main/tools.php

Данная ошибка может появиться после повышения версии PHP до 8.x в случае, если не были установлены все доступные обновления платформы на версии PHP 7.x.



#### Решение проблемы:



Эта ошибка была исправлена в обновлении главного модуля `main 22.100.0`.



Поэтому необходимо понизить версию PHP до 7.x, произвести обновление продукта и модулей до последней доступной версии. И только потом повысить версию PHP до 8.х.





## [TypeError] call_user_func_array(): Argument #1 ($callback) must be a valid callback, non-static method COMP\BXE\EventHandlers::AdminContextMenuShow() cannot be called statically (0)...

Эта ошибка может появиться после повышения версии PHP до 8, но уже не очень очевидна:



```

//Пример ошибки
[TypeError]
call_user_func_array(): Argument #1 ($callback) must be a valid callback, non-static method COMP\BXE\EventHandlers::AdminContextMenuShow() cannot be called statically (0)
/var/www//bitrix/modules/main/classes/general/module.php:480
#0: ExecuteModuleEventEx
/var/www/bitrix/modules/main/interface/admin_ui_list.php:1983
#1: CAdminUiContextMenu->Show
/var/www/bitrix/modules/main/interface/admin_ui_list.php:1168
#2: CAdminUiList->ShowContext
/var/www/bitrix/modules/main/interface/admin_ui_list.php:630
#3: CAdminUiList->DisplayFilter
/var/www/bitrix/modules/iblock/admin/iblock_element_admin.php:5217
#4: include(string)
/var/www/bitrix/admin/cat_product_admin.php:3
```



Из текста ошибки сразу не узнать директорию модуля, но данный метод `COMP\BXE\EventHandlers::AdminContextMenuShow()` принадлежит стороннему модулю.



#### Решение проблемы:



Исправление в общем случае будет таким: в коде `AdminContextMenuShow()` нужно правильно объявить [статическую функцию](https://www.php.net/manual/ru/language.oop5.static.php):



```
function AdminContextMenuShow()
```


заменить на:

```
public static function AdminContextMenuShow()
```







## Белый экран после повышения версии PHP до 8.х, а на PHP 7.4 все работает

Такая ошибка может быть из-за того, что в настройках PHP установлен параметр `short_open_tag = Off`.



#### Решение проблемы:



- нужно задать в конфигурационном файле PHP: `short_open_tag = On`;
- проверить логи веб-сервера на предмет ошибок и устранить их;
- также можно просмотреть ошибки на странице сайта с белым экраном: нажать правую кнопку мыши и выбрать **Просмотр кода страницы**, пролистать страницу вниз и проверить имеются ли ошибки на ней.
