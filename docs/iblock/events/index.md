# События

**Внимание!**Если инфоблок участвует в документообороте, то событие будет вызываться дважды, на элемент и его копию. Чтобы избежать повторного вызова рекомендуется уже в событии проверять элемент и дальше либо обрабатывать его, либо нет. Проверять можно по полю [WF_PARENT_ELEMENT_ID](../classes/ciblockelement/getlist.md).

В некоторых случаях (например, в событии **OnAfterIBlockElementAdd**) использовать это поле напрямую нельзя: поле элемента **WF_PARENT_ELEMENT_ID** в обоих вызовах заполнено и равно одному и тому же ID. В этом случае необходимо сравнить **WF_PARENT_ELEMENT_ID** с **ID** элемента и если они совпадают, то это и есть искомый элемент из двух.


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| [OnBeforeIBlockAdd](onbeforeiblockadd.md) | перед добавлением информационного блока. | CIBlock::CheckFields | 4.0.6 |
| [OnAfterIBlockAdd](onafteriblockadd.md) | после добавления информационного блока. | [Add](../classes/ciblock/add.md) | 4.0.6 |
| [OnBeforeIBlockUpdate](onbeforeiblockupdate.md) | перед изменением информационного блока. | CIBlock::CheckFields | 4.0.6 |
| [OnAfterIBlockUpdate](onafteriblockupdate.md) | после изменения информационного блока. | [Update](../classes/ciblock/update.md) | 4.0.6 |
| [OnBeforeIBlockDelete](onbeforeiblockdelete.md) | перед удалением информационного блока. | [Delete](../classes/ciblock/delete.md) | 3.3.8 |
| [OnIBlockDelete](oniblockdelete.md) | при удалении информационного блока. | [Delete](../classes/ciblock/delete.md) | 3.2.1 |
| [OnBeforeIBlockPropertyAdd](onbeforeiblockpropertyadd.md) | перед добавлением свойства. | CIBlockProperty::CheckFields | 4.0.6 |
| [OnAfterIBlockPropertyAdd](onafteriblockpropertyadd.md) | после добавления свойства. | [Add](../classes/ciblockproperty/add.md) | 4.0.6 |
| [OnBeforeIBlockPropertyUpdate](onbeforeiblockpropertyupdate.md) | перед изменением свойства. | CIBlockProperty::CheckFields | 4.0.6 |
| OnIBlockPropertyDelete | при удалении свойства. | [Delete](../classes/ciblockproperty/delete.md) | 4.0.6 |
| [OnAfterIBlockPropertyUpdate](onafteriblockpropertyupdate.md) | после изменения свойства. | [Update](../classes/ciblockproperty/update.md) | 4.0.6 |
| [OnBeforeIBlockPropertyDelete](onbeforeiblockpropertydelete.md) | перед удалением свойства. | [Delete](../classes/ciblockproperty/delete.md) | 4.0.6 |
| [OnIBlockPropertyBuildList](OnIBlockPropertyBuildList.md) | при построении списка свойств. | [GetUserType](../classes/ciblockproperty/GetUserType.md) | 5.1.0 |
| [OnBeforeIBlockSectionAdd](onbeforeiblocksectionadd.md) | перед добавлением раздела. | CIBlockSection::CheckFields | 4.0.6 |
| [OnAfterIBlockSectionAdd](onafteriblocksectionadd.md) | после добавления раздела. | [Add](../classes/ciblocksection/add.md) | 4.0.6 |
| [OnBeforeIBlockSectionUpdate](onbeforeiblocksectionupdate.md) | перед изменением раздела. | CIBlockSection::CheckFields | 4.0.6 |
| [OnAfterIBlockSectionUpdate](onafteriblocksectionupdate.md) | после изменения раздела. | [Update](../classes/ciblocksection/update.md) | 4.0.6 |
| [OnBeforeIBlockSectionDelete](onbeforeiblocksectiondelete.md) | перед удалением раздела. | [Delete](../classes/ciblocksection/delete.md) | 4.0.6 |
| OnAfterIBlockSectionDelete | после удаления раздела. | [Delete](../classes/ciblocksection/delete.md) | 7.0.3 |
| [OnBeforeIBlockElementAdd](onbeforeiblockelementadd.md) | перед добавлением элемента. | CIBlockElement::CheckFields | 4.0.6 |
| [OnStartIBlockElementAdd](OnStartIBlockElementAdd.md) | в момент начала добавления элемента. | CIBlockElement::CheckFields | 7.1.8 |
| [OnAfterIBlockElementAdd](onafteriblockelementadd.md) | после добавления элемента. | [Add](../classes/ciblockelement/add.md) | 4.0.6 |
| [OnBeforeIBlockElementUpdate](onbeforeiblockelementupdate.md) | перед изменением элемента. | CIBlockElement::CheckFields | 4.0.6 |
| [OnStartIBlockElementUpdate](OnStartIBlockElementUpdate.md) | в момент начала изменения элемента. | CIBlockElement::CheckFields | 7.1.8 |
| [OnAfterIBlockElementUpdate](onafteriblockelementupdate.md) | после изменения элемента. | [Update](../classes/ciblockelement/update.md) | 4.0.6 |
| [OnBeforeIBlockElementDelete](onbeforeiblockelementdelete.md) | перед удалением элемента. | [Delete](../classes/ciblockelement/delete.md) | 4.0.6 |
| [OnAfterIBlockElementDelete](onafteriblockelementdelete.md) | после удаления элемента. | [Delete](../classes/ciblockelement/delete.md) | 5.0.0 |
| [OnIBlockElementDelete](oniblockelementdelete.md) | при удалении элемента информационного блока. | [Delete](../classes/ciblockelement/delete.md) | 3.1.3 |
| OnBeforeEventLog | перед внесением записи в лог. | [Update](../classes/ciblockelement/update.md) | 11.0.8 |
| OnSearchGetFileContent | при поиске файла. | CIBlockElement::__GetFileContent | 7.1.1 |
| GetAuditTypesIblock | при возвращении описания журналу событий | CEventIBlock::GetAuditTypes | 11.0.0 |
| OnAdminSubContextMenuShow | аналог [OnAdminContextMenuShow](../../main/events/onadmincontextmenushow.md) для списка SKU | CAdminSubContextMenu::Show | 11.0.12 |
| OnAdminSubListDisplay | аналог [OnAdminListDisplay](../../main/events/onadminlistdisplay.md) для списка SKU | CAdminSubList::Display | 10.0.3 |
| [OnAfterIBlockElementSetPropertyValues](onafteriblockelementsetpropertyvalues.md) | после сохранения значений всех свойств элемента методом [CIBlockElement::SetPropertyValues](../classes/ciblockelement/setpropertyvalues.md). | [CIBlockElement::SetPropertyValues](../classes/ciblockelement/setpropertyvalues.md) | 14.5.1 |
| [OnAfterIBlockElementSetPropertyValuesEx](onafteriblockelementsetpropertyvaluesex.md) | после сохранения значений свойств элемента методом [CIBlockElement::SetPropertyValuesEx](../classes/ciblockelement/setpropertyvaluesex.md). | [CIBlockElement::SetPropertyValuesEx](../classes/ciblockelement/setpropertyvaluesex.md) | 14.5.1 |
| [OnIBlockElementAdd](oniblockelementadd.md) | в момент добавления элемента информационного блока. | [CIBlockElement::Add](../classes/ciblockelement/add.md) | 15.5.12 |
| [OnIBlockElementUpdate](oniblockelementupdate.md) | в момент изменения элемента информационного блока. | [CIBlockElement::Update](../classes/ciblockelement/update.md) | 15.5.12 |
| [OnIBlockElementSetPropertyValues](oniblockelementsetpropertyvalues.md) | в момент сохранения значений свойств элемента инфоблока. | [CIBlockElement::SetPropertyValues](../classes/ciblockelement/setpropertyvalues.md) | 15.5.12 |
| [OnIBlockElementSetPropertyValuesEx](oniblockelementsetpropertyvaluesex.md) | до внесения изменений в базу после валидации входящих данных. | [CIBlockElement::SetPropertyValuesEx](../classes/ciblockelement/setpropertyvaluesex.md) | 17.6.5 |
