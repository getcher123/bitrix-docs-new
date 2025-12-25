# Уровни доступа для стандартных групп пользователей

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 7175 — Управление группами пользователей](lesson_7175.md)
- [Следующий: 2004 — Работа с учетными записями пользователей →](lesson_2004.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=6767

|  | ### Таблица прав доступа по умолчанию |
| --- | --- |

В таблице приведены

			уровни доступа

                    
**Уровень доступа** — это набор разрешенных операций (например, загрузка файлов, создание заказов, редактирование страниц и другие), привязанный к модулям и группам пользователей. Уровни доступа применяются в системе управления пользователями, определяются администратором, который может создавать или изменять их. 

[Подробнее о создании и настройке уровней доступа](lesson_2015.md)...

		 по умолчанию к модулям системы для

			стандартных групп пользователей

                    В дистрибутивах разных редакций и решений списки групп по умолчанию могут быть разными.

		.

Следующие модули не включены в таблицу, так как настройка прав доступа для них не выполняется. По умолчанию полный доступ к настройкам этих модулей задан для группы **Администраторы**:

| - [CRM](http://dev.1c-bitrix.ru/user_help/service/crm/index.php)<br>- [DAV](https://dev.1c-bitrix.ru/user_help/settings/dav/settings.php)<br>- [Push and Pull](http://dev.1c-bitrix.ru/user_help/settings/pull/index.php)<br>- [Библиотека документов](https://dev.1c-bitrix.ru/user_help/content/webdav/settings.php)<br>- [Бизнес процессы](http://dev.1c-bitrix.ru/user_help/service/bizproc/index.php)<br>- [Веб-кластер](http://dev.1c-bitrix.ru/user_help/settings/cluster/index.php) | - [Веб-мессенджер](http://dev.1c-bitrix.ru/user_help/service/im/index.php)<br>- [Веб-сервисы](http://dev.1c-bitrix.ru/user_help/settings/webservice/index.php)<br>- [Задачи](http://dev.1c-bitrix.ru/user_help/content/tasks/index.php)<br>- [Интранет](http://dev.1c-bitrix.ru/user_help/service/intranet/index.php)<br>- [Информационные блоки](http://dev.1c-bitrix.ru/user_help/content/iblock/index.php)<br>- [Календарь событий](http://dev.1c-bitrix.ru/user_help/service/event_calendar/index.php) | - [Облако 1С-Битрикс](http://dev.1c-bitrix.ru/user_help/settings/bitrixcloud/index.php)<br>- [Поиск](http://dev.1c-bitrix.ru/user_help/settings/search/index.php)<br>- [Социальные сервисы](http://dev.1c-bitrix.ru/user_help/service/socialservices/index.php)<br>- [Фотогалерея 2.0](https://dev.1c-bitrix.ru/user_help/content/iblock/photogallery/settings.php)<br>- [Экстранет](http://dev.1c-bitrix.ru/user_help/service/extranet/index.php) |
| --- | --- | --- |

Существуют также две стандартные группы пользователей, не включенные в таблицу: 

- Пользователи, имеющие право голосовать за рейтинг
- Пользователи имеющие право голосовать за авторитет

Их права на доступ к модулям совпадают с группой **"Все пользователи (в том числе неавторизованные)"**, за исключением дополнительных прав: права **голосовать за рейтинг** и права **голосовать за авторитет** соответственно.

| \| **Модуль, права доступа** \| **Стандартные группы пользователей** \|  \|  \|  \|  \|<br>\| --- \| --- \| --- \| --- \| --- \| --- \|<br>\| **Администраторы** \| **Все пользователи (в том числе неавторизованные)** \| **Зарегистрированные пользователи** \| **Администраторы интернет-магазина** \| **Контент-редакторы** \|  \|<br>\| **Главный модуль**<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/settings/settings.php#access) \| Полный \| Доступ закрыт \| Изменение своего профиля \| Полный доступ к управлению интернет-магазином и параметрами торгового каталога \| Изменение своего профиля \|<br>\| **AD/LDAP**(ldap)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/ldap/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Email-маркетинг**(sender)<br>[Описание прав доступа](https://dev.1c-bitrix.ru/user_help/marketing/sender/settings_email_marketing.php) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Wiki**(wiki)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/content/wiki/settings.php#access) \| Полный \| Чтение страниц \|  \|  \|  \|<br>\| **XMPP сервер**(xmpp)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/xmpp/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Блоги**(blog)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/blogs/settings.php#access) \| Полный \| Чтение блогов \|  \|  \|  \|<br>\| **Валюты**(currency)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/currency/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Веб-аналитика**(statistic)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/statistic/settings.php#tab_access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Веб-формы**(form)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/form/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Документооборот**(workflow)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/content/workflow/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Интеграция с Битрикс24**(b24connector) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Интернет-магазин**(sale)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/store/sale/settings_sale.php#access) \| Полный \| Доступ закрыт \| Обработка заказов \| Доступ закрыт \|  \|<br>\| **Торговый каталог**(catalog)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/store/catalog/settings.php#access) \| Полный \| Доступ закрыт \| Редактирование цен \| Доступ закрыт \|  \|<br>\| **Контроллер**(controller)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/controller/settings.php#access) \| Полный \| Доступ запрещен \|  \|  \|  \|<br>\| **Монитор производительности**(perfmon)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/perfmon/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Облачные хранилища**(clouds)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/content/clouds/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Обучение**(learning)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/learning/settings.php#access) \| Управление правами; редактирование / удаление / создание / привязывание / отвязывание уроков и курсов как в качестве родителя, так и в качестве потомка \| Просмотр \|  \|  \|  \|<br>\| **Опросы, голосования**(vote)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/vote/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Перевод**(translate)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/translate/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Подписка, рассылки**(subscribe)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/subscribe/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Поисковая оптимизация**(seo)<br>[Описание прав доступа](https://dev.1c-bitrix.ru/user_help/marketing/seo/index.php) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Почта**(mail)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/mail/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \|<br>\| **Проактивная защита**(security)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/settings/security/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Баннерная реклама**(advertising)<br>[Описание прав доступа](https://dev.1c-bitrix.ru/user_help/marketing/advertising/index.php) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Сайты 24**(landing)<br>[Описание прав доступа](https://dev.1c-bitrix.ru/user_help/sites24/settings.php) \| Полный \| Доступ запрещен \|  \|  \|  \|<br>\| **Социальная сеть**(socialnetwork)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/socialnetwork/settings.php#access) \| Полный \| Работа в публичной части \|  \|  \|  \|<br>\| **Техподдержка**(support)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/support/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Торговый каталог**(catalog)<br>[Описание прав доступа](https://dev.1c-bitrix.ru/user_help/store/catalog/settings_catalog.php) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Управление структурой**(fileman)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/content/fileman/settings.php#access) \| Полный \| Доступ закрыт \|  \|  \|  \|<br>\| **Учет рабочего времени**(timeman)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/timeman/settings.php#access) \| Полный \| В соответствии с субординацией: <br>сотрудники могут редактировать свой рабочий день; <br>руководители могут управлять рабочими днями и отчетами \|  \|  \|  \|<br>\| **Форум**(forum)<br>[Описание прав доступа](http://dev.1c-bitrix.ru/user_help/service/forum/settings.php#access) \| Полный \| Закрыт \|  \|  \|  \| |
| --- |

 

 

 

|  | ### Документация по теме: |
| --- | --- |

- [Уровни доступа](https://dev.1c-bitrix.ru/user_help/settings/users/task_admin.php)
- [Создание и редактирование уровня доступа](https://dev.1c-bitrix.ru/user_help/settings/users/task_edit.php)
