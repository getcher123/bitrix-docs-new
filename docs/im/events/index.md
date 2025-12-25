# Список событий


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| OnBeforeMessagesAdd | перед добавлением сообщения | CIMMessage::Add | 11.0.1 |
| OnAfterConfirmNotify | после подтверждения уведомления | CIMNotify::Confirm | 11.0.3 |
| OnBeforeConfirmNotify | перед подтверждением уведомления | CIMNotify::Confirm | 11.0.3 |
| OnAfterDeleteNotify | после удаления уведомления | CIMNotify::DeleteWithCheck | 11.0.3 |
| OnAfterNotifyAdd | после добавления уведомления | CIMMessenger::Add | 11.5.6 |
| OnAfterDeleteMessage | после удаления сообщения | CIMMessage::Delete | 11.5.6 |
| OnAfterContactListGetList | после получения контакт листа | CIMContactList::GetList | 12.1.3 |
| [OnBeforeMessageNotifyAdd](onbeforemessagenotifyadd.md) | перед добавлением уведомления или сообщения | CIMNotify:add, CIMMessage::Add CIMChat::AddMessage | 12.1.3 |
| OnAfterMessagesUpdate | после редактирования сообщения | CIMMessenger::Update | 15.0.0 |
| OnAfterMessagesDelete | после удаления сообщения | CIMMessenger::Delete | 15.0.0 |
| OnAfterFileUpload | после загрузки файла | CIMDisk::UploadFile | 15.0.3 |
| [OnAfterChatRead](onafterchatread.md) | после прочтения чата | CIMChat::SetReadMessage | 16.5.0 |

<!-- vault-nav:start -->
## В этой папке

<details>
<summary>Показать файлы и папки</summary>

### Файлы

- [OnAfterChatRead](onafterchatread.md)
- [OnBeforeMessageNotifyAdd](onbeforemessagenotifyadd.md)

</details>

<!-- vault-nav:end -->
