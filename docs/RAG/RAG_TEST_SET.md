# Тестовый набор контрольных вопросов для RAG

Этот список нужен для ручной проверки качества RAG‑системы.  
Заполняйте колонку “Ожидаемый файл/раздел” после того, как RAG даёт корректный ответ.

## Формат проверки

- Ожидается ответ с 2–4 локальными ссылками `docs/...`
- Если ответ не найден — фиксировать как “miss”
- Для каждого вопроса отмечать релевантный раздел (classic/D7/REST/user_help/courses)

## Контрольные вопросы

| ID | Вопрос | Раздел | Ожидаемый файл/раздел | Примечание |
| --- | --- | --- | --- | --- |
| Q001 | Как получить список элементов инфоблока через `CIBlockElement::GetList`? | classic | [iblock/classes/ciblockelement/getlist.md](../iblock/classes/ciblockelement/getlist.md) |  |
| Q002 | Где описан класс `CUser` и основные методы? | classic | [main/reference/cuser/index.md](../main/reference/cuser/index.md) |  |
| Q003 | Какие события есть у модуля `main` (пример: `OnAfterUserAdd`)? | classic | [main/events/index.md](../main/events/index.md) |  |
| Q004 | Как получить значения свойств элемента инфоблока? | classic | [iblock/classes/ciblockelement/getproperty.md](../iblock/classes/ciblockelement/getproperty.md) |  |
| Q005 | Как создавать/редактировать разделы инфоблока? | classic | [iblock/classes/ciblocksection/add.md](../iblock/classes/ciblocksection/add.md)<br>[iblock/classes/ciblocksection/update.md](../iblock/classes/ciblocksection/update.md) |  |
| Q006 | Как подключить обработчик события в классическом API? | classic | [main/functions/module/addeventhandler.md](../main/functions/module/addeventhandler.md) |  |
| Q007 | Что такое `CDBResult` и как с ним работать? | classic | [main/reference/cdbresult/index.md](../main/reference/cdbresult/index.md) |  |
| Q008 | Как получить товары и цены через модуль `catalog`? | classic | [catalog/price.md](../catalog/price.md) |  |
| Q009 | Какие классы используются для работы с заказом в `sale`? | classic | [sale/classes/index.md](../sale/classes/index.md) |  |
| Q010 | Как работать с корзиной в классическом API? | classic | [catalog/basket.md](../catalog/basket.md) |  |
| Q011 | Что такое D7 ORM и где основные сущности? | D7 | [d7/bitrix/main/entity/index.php.md](../d7/bitrix/main/entity/index.php.md) |  |
| Q012 | Как использовать `Bitrix\\Main\\EventManager`? | D7 | [d7/bitrix/main/EventManager/index.php.md](../d7/bitrix/main/EventManager/index.php.md) |  |
| Q013 | Где документация по `Bitrix\\Main\\DB\\Connection`? | D7 | [d7/bitrix/main/db/index.php.md](../d7/bitrix/main/db/index.php.md) |  |
| Q014 | Как подключать модули в D7 (`Loader::includeModule`)? | D7 | [d7/bitrix/main/loader/index.php.md](../d7/bitrix/main/loader/index.php.md) |  |
| Q015 | Как работать с таблицами сущностей D7 (`DataManager`)? | D7 | [d7/bitrix/main/entity/index.php.md](../d7/bitrix/main/entity/index.php.md) |  |
| Q016 | Где описан `Bitrix\\Sale\\Order`? | D7 | [d7/bitrix/sale/index.php.md](../d7/bitrix/sale/index.php.md) |  |
| Q017 | Как создать пользователя через D7 (`Bitrix\\Main\\UserTable`)? | D7 | [d7/bitrix/main/usertable/index.php.md](../d7/bitrix/main/usertable/index.php.md) |  |
| Q018 | Где описаны исключения и ошибки D7 (`Main\\SystemException`)? | D7 | [d7/bitrix/main/systemexception/index.php.md](../d7/bitrix/main/systemexception/index.php.md) |  |
| Q020 | Где находится документация по REST‑методу `crm.lead.add`? | REST | [bitrix24_api/b24-rest-docs/api-reference/crm/leads/crm-lead-add.md](../bitrix24_api/b24-rest-docs/api-reference/crm/leads/crm-lead-add.md) |  |
| Q021 | Как создать смарт‑процесс через REST (`crm.type.add`)? | REST | [bitrix24_api/b24-rest-docs/api-reference/crm/universal/user-defined-object-types/crm-type-add.md](../bitrix24_api/b24-rest-docs/api-reference/crm/universal/user-defined-object-types/crm-type-add.md) |  |
| Q022 | Как обновить смарт‑процесс через REST (`crm.type.update`)? | REST | [bitrix24_api/b24-rest-docs/api-reference/crm/universal/user-defined-object-types/crm-type-update.md](../bitrix24_api/b24-rest-docs/api-reference/crm/universal/user-defined-object-types/crm-type-update.md) |  |
| Q023 | Где посмотреть справочник статусов CRM для смарт‑процессов? | REST | [bitrix24_api/b24-rest-docs/api-reference/crm/status/index.md](../bitrix24_api/b24-rest-docs/api-reference/crm/status/index.md) |  |
| Q024 | Как получить список задач через REST (`tasks.task.list`)? | REST | [bitrix24_api/b24-rest-docs/api-reference/tasks/tasks-task-list.md](../bitrix24_api/b24-rest-docs/api-reference/tasks/tasks-task-list.md) |  |
| Q025 | Какой формат ответа REST и где описаны ошибки? | REST | [bitrix24_api/b24-rest-docs/settings/how-to-call-rest-api/list-methods-pecularities.md](../bitrix24_api/b24-rest-docs/settings/how-to-call-rest-api/list-methods-pecularities.md) |  |
| Q026 | Где настраиваются смарт‑процессы в интерфейсе Bitrix24? | courses | [courses/course_57_developer_bitrix_framework/lesson_13640.md](../courses/course_57_developer_bitrix_framework/lesson_13640.md)<br>[courses/course_57_developer_bitrix_framework/lesson_20858.md](../courses/course_57_developer_bitrix_framework/lesson_20858.md) |  |
| Q027 | Как открыть настройки прав доступа в админке? | courses | [courses/course_35_администратор._базовый/lesson_2023.md](../courses/course_35_администратор._базовый/lesson_2023.md) |  |
| Q028 | Как настроить меню на сайте (админка)? | courses | [courses/course_35_администратор._базовый/lesson_11799.md](../courses/course_35_администратор._базовый/lesson_11799.md) |  |
| Q029 | Как создать новую страницу и раздел через административную панель? | courses | [courses/course_35_администратор._базовый/lesson_2021.md](../courses/course_35_администратор._базовый/lesson_2021.md) |  |
| Q030 | Где описание работы с визуальным редактором? | courses | [courses/course_35_администратор._базовый/lesson_4482.md](../courses/course_35_администратор._базовый/lesson_4482.md) |  |
| Q031 | Что такое «многосайтовость» и как её включить? | courses | [courses/course_103_многосайтовость/lesson_286.md](../courses/course_103_многосайтовость/lesson_286.md)<br>[courses/course_103_многосайтовость/lesson_287.md](../courses/course_103_многосайтовость/lesson_287.md) |  |
| Q032 | Как установить продукт 1C‑Bitrix (общие шаги)? | courses | [courses/course_135_installation_and_setup/lesson_12964.md](../courses/course_135_installation_and_setup/lesson_12964.md) |  |
| Q033 | Как настроить модуль «Перевод»? | courses | [courses/course_35_администратор._базовый/lesson_12980.md](../courses/course_35_администратор._базовый/lesson_12980.md) |  |
| Q034 | Какие уровни доступа существуют? | courses | [courses/course_35_администратор._базовый/lesson_2015.md](../courses/course_35_администратор._базовый/lesson_2015.md) |  |
| Q035 | Как настроить проактивную защиту? | courses | [courses/course_35_администратор._базовый/lesson_9113.md](../courses/course_35_администратор._базовый/lesson_9113.md) |  |
| Q036 | Как работает двухэтапная авторизация? | courses | [courses/course_35_администратор._базовый/lesson_5002.md](../courses/course_35_администратор._базовый/lesson_5002.md) |  |
| Q037 | Как включить кеширование компонентов и меню? | courses | [courses/course_35_администратор._базовый/lesson_7077.md](../courses/course_35_администратор._базовый/lesson_7077.md) |  |
| Q038 | Как выполнить резервное копирование сайта? | courses | [courses/course_35_администратор._базовый/lesson_5330.md](../courses/course_35_администратор._базовый/lesson_5330.md) |  |
| Q039 | Где посмотреть уроки по производительности? | courses | [courses/course_35_администратор._базовый/lesson_7167.md](../courses/course_35_администратор._базовый/lesson_7167.md) |  |
| Q040 | Где описано управление облачными хранилищами? | courses | [courses/course_35_администратор._базовый/lesson_4826.md](../courses/course_35_администратор._базовый/lesson_4826.md) |  |
