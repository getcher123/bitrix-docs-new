# События


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterBuildSceleton | в момент вывода на страницу базовой верстки календаря. | CCalendarSceleton::Build | 11.0.0 |
| OnAfterCalendarEventDelete | после удаления события календаря. | CCalendarEvent::Delete | 11.5.6 |
| OnAfterCalendarEventEdit | после изменения события календаря. | CCalendarEvent::Edit | 12.0.2 |
| OnAfterCalendarEventUserFieldsUpdate | после обновления пользовательских полей календаря. | CCalendarEvent::UpdateUserFields | 12.0.2 |
| OnBeforeBuildSceleton | перед выводом на страницу базовой верстки календаря. | CCalendarSceleton::Build | 11.0.0 |
| OnBeforeCalendarEventDelete | перед удалением события календаря. | CCalendarEvent::Delete | 11.5.6 |
| OnRemindEvent | в момент отсылки напоминания о событии календаря. | CCalendar::ReminderAgent | 11.0.0 |
| OnSendInvitationMessage | при отсылке ряда уведомлений календаря. | CCalendar::SendMessage | 11.0.0 |
