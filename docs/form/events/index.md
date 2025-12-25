# События веб-форм

Все события вызываются **перед** соответствующим вызовом файлов-обработчиков статуса результата. Возврат обработчиком каких-либо значений не предполагается. Те обработчики, для которых это указано (onBefore*), могут возвращать какие-либо сообщения посредством генерации системного исключения (CMain::ThrowException()). В случае появления такого исключения все последующие операции с результатом прерываются (включая обработчики статусов веб-формы). При этом все равно вызываются все обработчики текущего события. Данные, передаваемые по ссылкам, допускают непосредственное изменение значений.


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnAfterFormCrmAdd | после добавления сервера CRM, с которым можно связать форму. | CFormCrm::Add | 11.5.0 |
| OnAfterFormCrmDelete | после удаления сервера CRM, с которым может быть связана форма. | CFormCrm::Delete | 11.5.0 |
| OnAfterFormCrmUpdate | после обновления сервера CRM, с которым может быть связана форма. | CFormCrm::Update | 11.5.0 |
| OnBeforeFormCrmAdd | перед добавлением сервера CRM, с которым может быть связана форма. | CFormCrm::Add | 11.5.0 |
| OnBeforeFormCrmDelete | перед удалением сервера CRM, с которым может быть связана форма. | CFormCrm::Delete | 11.5.0 |
| OnBeforeFormCrmUpdate | перед обновлением сервера CRM, с которым может быть связана форма. | CFormCrm::Update | 11.5.0 |
| onBeforeResultAdd | перед добавлением нового результата веб-формы. | [CFormResult::Add](../classes/cformresult/add.md) | 6.5.2 |
| onAfterResultAdd | после добавления нового результата веб-формы. | [CFormResult::Add](../classes/cformresult/add.md) | 6.5.2 |
| onBeforeResultUpdate | перед сохранением изменений существующего результата. | [CFormResult::Update](../classes/cformresult/update.md) | 6.5.2 |
| onAfterResultUpdate | после сохранения изменений результата веб-формы. | [CFormResult::Update](../classes/cformresult/update.md) | 6.5.2 |
| onBeforeResultDelete | перед удалением результата веб-формы. | [CFormResult::Delete](../classes/cformresult/delete.md) | 6.5.2 |
| onBeforeResultStatusChange | перед изменением статуса результата веб-формы. | [CFormResult::SetStatus](../classes/cformresult/setstatus.md) | 6.5.2 |
| onAfterResultStatusChange | после изменения статуса результата веб-формы. | [CFormResult::SetStatus](../classes/cformresult/setstatus.md) | 6.5.2 |
| onFormValidatorBuildList | при сборе списка кастомных валидаторов полей формы. | CFormValidator::GetAllList | 6.0.0 |
