# Класс CUser


### Описание и поля

**CUser** - класс для работы с пользователями.

При запуске каждой страницы автоматически создаётся объект этого класса $USER - данные о текущем пользователе.

Аналог класса в новом ядре D7 - *Bitrix\Main\UserTable*.

**Внимание!** с версии 20.0.1300 формы авторизации/регистрации теперь принимают данные только POST-запросом.


#### Поля


| Поле | Тип | Описание |
| --- | --- | --- |
| ID | int | ID пользователя. |
| XML_ID | int | ID пользователя для связи с внешними источниками (например, ID пользователя в какой-либо внешний базе). |
| TIMESTAMP_X | datetime | Последнее изменение. |
| LOGIN | varchar (50) | Имя входа. |
| PASSWORD | varchar (50) | Хеш от пароля. |
| STORED_HASH | varchar (32) | Хеш от пароля хранимый в куках пользователя. |
| CHECKWORD | varchar (50) | Контрольная строка для смены пароля. |
| ACTIVE | char | Активен (Y\|N). |
| NAME | varchar (50) | Имя. |
| LAST_NAME | varchar (50) | Фамилия. |
| SECOND_NAME | varchar (50) | Отчество. |
| EMAIL | varchar (255) | E-mail адрес. |
| LAST_LOGIN | datetime | Дата последней авторизации. |
| LAST_ACTIVITY_DATE | datetime | Дата последнего хита на сайте. |
| DATE_REGISTER | datetime | Дата регистрации. |
| LID | char (2) | ID сайта по умолчанию для уведомлений. |
| ADMIN_NOTES | varchar (2000) | Заметки администратора. |
| EXTERNAL_AUTH_ID | varchar (255) | Код источника **Внешней авторизации**. |
| Личные данные: |  |  |
| PERSONAL_PROFESSION | varchar (255) | Профессия. |
| PERSONAL_WWW | varchar (255) | WWW-страница. |
| PERSONAL_ICQ | varchar (255) | ICQ. |
| PERSONAL_GENDER | char (1) | Пол. |
| PERSONAL_BIRTHDAY | date | Дата рождения. |
| PERSONAL_PHOTO | int | Фотография. |
| PERSONAL_PHONE | varchar (255) | Телефон. |
| PERSONAL_FAX | varchar (255) | Факс. |
| PERSONAL_MOBILE | varchar (255) | Мобильный телефон. |
| PERSONAL_PAGER | varchar (255) | Пэйджер. |
| PERSONAL_STREET | varchar (2000) | Улица, дом. |
| PERSONAL_MAILBOX | varchar (255) | Почтовый ящик. |
| PERSONAL_CITY | varchar (255) | Город. |
| PERSONAL_STATE | varchar (255) | Область / край. |
| PERSONAL_ZIP | varchar (255) | Индекс. |
| PERSONAL_COUNTRY | varchar (255) | Страна. |
| PERSONAL_NOTES | varchar (2000) | Дополнительные заметки. |
| Информация о работе: |  |  |
| WORK_COMPANY | varchar (255) | Наименование компании. |
| WORK_DEPARTMENT | varchar (255) | Департамент / Отдел. |
| WORK_POSITION | varchar (255) | Должность. |
| WORK_WWW | varchar (255) | WWW-страница. |
| WORK_PHONE | varchar (255) | Телефон. |
| WORK_FAX | varchar (255) | Факс. |
| WORK_PAGER | varchar (255) | Пэйджер. |
| WORK_STREET | varchar (2000) | Улица, дом. |
| WORK_MAILBOX | varchar (255) | Почтовый ящик. |
| WORK_CITY | varchar (255) | Город. |
| WORK_STATE | varchar (255) | Область / край. |
| WORK_ZIP | varchar (255) | Индекс. |
| WORK_COUNTRY | varchar (255) | Страна. |
| WORK_PROFILE | varchar (2000) | Направления деятельности. |
| WORK_LOGO | int | Логотип. |
| WORK_NOTES | varchar (2000) | Дополнительные заметки. |

---
### Методы класса


| Метод | Описание | С версии |
| --- | --- | --- |
| GetList | Возвращает список пользователей. |  |
| GetByID | Возвращает пользователя по его ID. |  |
| GetByLogin | Возвращает пользователя по его логину. | 3.0.12 |
| GetUserGroup | Возвращает ID всех групп, которым принадлежит пользователь. |  |
| Add | Создает нового пользователя. |  |
| Update | Изменяет параметры пользователя. |  |
| Delete | Удаляет пользователя. |  |
| GetID | Возвращает ID текущего авторизованного пользователя. |  |
| GetAnonymousUserID | Метод возвращает ID анонимного (системного) пользователя. |  |
| GetLogin | Возвращает логин текущего авторизованного пользователя. |  |
| GetEmail | Возвращает E-Mail текущего авторизованного пользователя. | 4.0.4 |
| GetFullName | Возвращает имя и фамилию текущего авторизованного пользователя. |  |
| GetFirstName | Возвращает имя текущего авторизованного пользователя. | 4.0.4 |
| GetLastName | Возвращает фамилию текущего авторизованного пользователя. | 4.0.4 |
| GetParam | Возвращает один из параметров пользователя. |  |
| GetUserGroupArray | Возвращает ID всех групп которым принадлежит текущий пользователь. |  |
| GetUserGroupList | Выводит список групп, в которых состоит пользователь. | 4.1.0 |
| GetUserGroupString | Возвращает строку с перечисленными группами пользователя. | 4.0.4 |
| IsAdmin | Проверяет принадлежность пользователя группе администраторов. |  |
| IsAuthorized | Проверяет авторизован ли пользователь. |  |
| IsOnLine | Метод предназначен для определения статуса "Сейчас на сайте" по ID пользователя. | 7.1.6 |
| Login | Авторизует пользователя по введенному логину. |  |
| LoginByHash | Авторизует пользователя по хранимому в куках хешу. | 3.3.7 |
| Authorize | Непосредственно осуществляет процесс авторизации пользователя. Инициализирует необходимые сессионные переменные и переменные объекта класса CUser. | 3.3.7 |
| Logout | Заканчивает сеанс авторизации пользователя. |  |
| Register | Создает нового пользователя, авторизует его и отсылает письмо по шаблону типа NEW_USER. |  |
| SimpleRegister | Создает нового пользователя с генерацией логина и пароля, затем авторизует его. На вход метода поступает только E-Mail. |  |
| ChangePassword | Изменяет пароль пользователя. |  |
| SendPassword | Создает почтовое событие для отправки пользователю сообщения для смены пароля. |  |
| SendUserInfo | Создает почтовое событие для отправки пользователю сообщения с его параметрами. |  |
| GetCount | Возвращает количество пользователей в базе. | 3.3.0 |
| GetExternalAuthList | Возвращает список всех источников внешней авторизации. | 4.0.6 |
| SetParam | Метод устанавливает произвольный параметр пользователя param_name для хранения в сессии авторизации. | 4.0.6 |
| SetUserGroup | Метод устанавливает привязку пользователя user_id к группам groups | 4.0.6 |
| SetUserGroupArray | Метод устанавливает привязку текущего пользователя к группам groups | 4.0.6 |
| SetLastActivityDate | Метод обновляет LAST_ACTIVITY_DATE | 7.1.6 |
| CanDoFileOperation | Операции над файлами | 6.5.0 |

---




| ![](../images/e34d72accd.jpg) 4 **oleg@prilepa.ru**29.04.2014 11:54:56 |  |  |
| --- | --- | --- |
| \| Цитата \| \| --- \| \| // регистрируем последнюю активность пользователя, если модуль соцсетей не установлен if(!IsModuleInstalled('socialnetwork')) { AddEventHandler('main', 'OnBeforeProlog', 'CustomSetLastActivityDate'); function CustomSetLastActivityDate() { if($GLOBALS['USER']->IsAuthorized()) { CUser::SetLastActivityDate($GLOBALS['USER']->GetID()); } } } \| **http://dev.1c-bitrix.ru/community/webdev/user/2854/blog/2222/index.php**? | Цитата | // регистрируем последнюю активность пользователя, если модуль соцсетей не установлен if(!IsModuleInstalled('socialnetwork')) { AddEventHandler('main', 'OnBeforeProlog', 'CustomSetLastActivityDate'); function CustomSetLastActivityDate() { if($GLOBALS['USER']->IsAuthorized()) { CUser::SetLastActivityDate($GLOBALS['USER']->GetID()); } } } |
| Цитата |  |  |
| // регистрируем последнюю активность пользователя, если модуль соцсетей не установлен if(!IsModuleInstalled('socialnetwork')) { AddEventHandler('main', 'OnBeforeProlog', 'CustomSetLastActivityDate'); function CustomSetLastActivityDate() { if($GLOBALS['USER']->IsAuthorized()) { CUser::SetLastActivityDate($GLOBALS['USER']->GetID()); } } } |  |  |
|  |  |  |


| ![](../images/6ddc32eb79.jpg) 1 **Иван Неслуховский**03.11.2009 13:37:35 |
| --- |
| Поле LAST_ACTIVITY_DATE и соответственно метод IsOnLine() не работают для редакций "Старт" и "Стандарт". От разработчиков: пока да, только для редакций с соцсетью. |
|  |
