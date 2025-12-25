# Список констант


### Константы CTasks


#### Статусы


| Константа | Описание | Числовые значения |
| --- | --- | --- |
| CTasks::METASTATE_VIRGIN_NEW | Новая задача (не просмотрена). | -2 |
| CTasks::METASTATE_EXPIRED | Задача просрочена. | -1 |
| CTasks::METASTATE_EXPIRED_SOON | Задача почти просрочена. | -3 |
| CTasks::STATE_NEW | Новая задача. (Не используется) | 1 |
| CTasks::STATE_PENDING | Задача принята исполнителем. (Не используется) | 2 |
| CTasks::STATE_IN_PROGRESS | Задача выполняется. | 3 |
| CTasks::STATE_SUPPOSEDLY_COMPLETED | Условно завершена (ждет контроля постановщиком). | 4 |
| CTasks::STATE_COMPLETED | Задача завершена. | 5 |
| CTasks::STATE_DEFERRED | Задача отложена. | 6 |
| CTasks::STATE_DECLINED | Задача отклонена исполнителем. (Не используется) | 7 |


#### Приоритеты


| Константа | Описание |
| --- | --- |
| CTasks::PRIORITY_LOW | Низкий приоритет. |
| CTasks::PRIORITY_AVERAGE | Нормальный приоритет. |
| CTasks::PRIORITY_HIGH | Высокий приоритет. |



---
### Константы CTaskItem


#### Действия над задачей (для проверки прав)


| Константа | Описание |
| --- | --- |
| CTaskItem::ACTION_ACCEPT | Принятие задачи (смена статуса в **CTasks::STATE_PENDING**). |
| CTaskItem::ACTION_DECLINE | Отклонение задачи (смена статуса в **CTasks::STATE_DECLINED**). |
| CTaskItem::ACTION_COMPLETE | Завершение задачи (смена статуса в **CTasks::STATE_COMPLETED**, либо в **CTasks::STATE_SUPPOSEDLY_COMPLETED** — если постановщиком затребован контроль задачи и завершает задачу не постановщик). |
| CTaskItem::ACTION_APPROVE | Одобрение задачи, требующей контроля (перевод из статуса **CTasks::STATE_SUPPOSEDLY_COMPLETED** в **CTasks::STATE_COMPLETED**). |
| CTaskItem::ACTION_DISAPPROVE | Возврат в работу задачи, требующей контроля (перевод из статуса **CTasks::STATE_SUPPOSEDLY_COMPLETED** в **CTasks::STATE_NEW** или **CTasks::STATE_PENDING**, если исполнитель является подчиненным постановщика). |
| CTaskItem::ACTION_START | Перевод задачи в статус "выполняется" (**CTasks::STATE_IN_PROGRESS**). |
| CTaskItem::ACTION_DELEGATE | Делегирование задачи подчиненному. |
| CTaskItem::ACTION_REMOVE | Удаление задачи. |
| CTaskItem::ACTION_EDIT | Редактирование задачи. |
| CTaskItem::ACTION_DEFER | Откладывание задачи на потом (перевод в статус **CTasks::STATE_DEFERRED**). |
| CTaskItem::ACTION_RENEW | Возврат задачи в статус "Новая" (**CTasks::STATE_NEW**) или "Принята" (**CTasks::STATE_PENDING**, если исполнитель является подчиненным постановщика). |
| CTaskItem::ACTION_CREATE | Создание задачи. |
| CTaskItem::ACTION_CHANGE_DEADLINE | Смена крайнего срока у задачи. |


#### Роли пользователя в задаче (для проверки прав)


| Константа | Описание |
| --- | --- |
| CTaskItem::ROLE_NOT_A_MEMBER | Не является участником задачи. |
| CTaskItem::ROLE_DIRECTOR | Постановщик. |
| CTaskItem::ROLE_RESPONSIBLE | Исполнитель. |
| CTaskItem::ROLE_ACCOMPLICE | Соисполнитель. |
| CTaskItem::ROLE_AUDITOR | Наблюдатель. |


#### Формат описания (при получении описания задачи)


| Константа | Описание |
| --- | --- |
| CTaskItem::DESCR_FORMAT_RAW | Формат "как есть" - может быть HTML и BBCode, в зависимости от задачи. |
| CTaskItem::DESCR_FORMAT_HTML | Формат HTML. Если описание задачи в формате BBCode, то оно будет автоматически преобразовано в HTML. Если оно уже в формате HTML, то будет применен санитайзер в соответствии с настройками в модуле задач. |
| CTaskItem::DESCR_FORMAT_PLAIN_TEXT | Формат "только текст". Все HTML/BB теги будут вырезаны. |



---
### Константы CTaskFilterCtrl


#### Идентификаторы предустановленных наборов фильтров


| Константа | Описание |
| --- | --- |
| CTaskFilterCtrl::ROOT_PRESET | Псевдонабор, не содержит условия. Является родительским элементов для всех остальных наборов. |
| CTaskFilterCtrl::STD_PRESET_ACTIVE_MY_TASKS | "Мои задачи". |
| CTaskFilterCtrl::STD_PRESET_ACTIVE_I_AM_DOER | "Поставленные мне". |
| CTaskFilterCtrl::STD_PRESET_ACTIVE_I_AM_ORIGINATOR | "Созданные мной". |
| CTaskFilterCtrl::STD_PRESET_ACTIVE_I_AM_AUDITOR | "Наблюдаемые". |
| CTaskFilterCtrl::STD_PRESET_DEFERRED_MY_TASKS | "Отложенные". |
| CTaskFilterCtrl::STD_PRESET_COMPLETED_MY_TASKS | "Завершенные". |
| CTaskFilterCtrl::STD_PRESET_ACTIVE_I_AM_RESPONSIBLE | "Я исполнитель". |
| CTaskFilterCtrl::STD_PRESET_ACTIVE_I_AM_ACCOMPLICE | "Я соисполнитель". |
| CTaskFilterCtrl::STD_PRESET_ALL_MY_TASKS | "Все". |
| CTaskFilterCtrl::STD_PRESET_ALIAS_TO_DEFAULT | Это синоним для **CTaskFilterCtrl::STD_PRESET_ACTIVE_MY_TASKS**. |

---
