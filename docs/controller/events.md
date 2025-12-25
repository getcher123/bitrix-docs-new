# События


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| **OnAfterCloseMember** | После отключения управляемого сайта. | CAllControllerMember::CloseMember | 6.5.3 |
| **OnBeforeUpdateCounters** | Перед обновлением счётчиков сайта. Позволяет модифицировать код обновляющего счётчика. В обработчик могут передаваться пользовательские поля группы контроллера. | CAllControllerMember::UpdateCounters | 11.5.0 |
| **OnBeforeControllerMemberAdd** | Перед добавлением клиента. | CControllerMember::CheckFields | 12.5.0 |
| **OnBeforeControllerMemberUpdate** | Перед обновлением клиента. | CControllerMember::CheckFields | 12.5.0 |
| **OnBeforeSendCheckAuth** | Используется для модификации полей пользователя, отправляемых на подключенный сайт при авторизации через контроллер. | CControllerMember::CheckFields | 14.5.0 |
| **OnBeforeTaskAdd** | Перед добавлением задачи. | CControllerTask::CheckFields | 15.5.0 |
| **OnBeforeSetGroupSettings** | Перед установкой настроек группы. | CControllerMember::SetGroupSettings | 16.0.1 |
