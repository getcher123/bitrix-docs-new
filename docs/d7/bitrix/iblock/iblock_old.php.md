# Информационные блоки в старом ядре

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/iblock/iblock_old.php

### Классы

| Класс | Описание | С версии |  |
| --- | --- | --- | --- |
| [CIBlock](../../../iblock/classes/ciblock/index.md) | Класс для работы с информационными блоками. | 3.0.3 |  |
| Событие | Вызывается | Метод | С версии |
| [OnBeforeIBlockAdd](../../../iblock/events/onbeforeiblockadd.md) | перед добавлением информационного блока. | CIBlock::CheckFields | 4.0.6 |
| [OnAfterIBlockAdd](../../../iblock/events/onafteriblockadd.md) | после добавления информационного блока. | [Add](../../../iblock/classes/ciblock/add.md) | 4.0.6 |
| [OnBeforeIBlockUpdate](../../../iblock/events/onbeforeiblockupdate.md) | перед изменением информационного блока. | CIBlock::CheckFields | 4.0.6 |
| [OnAfterIBlockUpdate](../../../iblock/events/onafteriblockupdate.md) | после изменения информационного блока. | [Update](../../../iblock/classes/ciblock/update.md) | 4.0.6 |
| [OnBeforeIBlockDelete](../../../iblock/events/onbeforeiblockdelete.md) | перед удалением информационного блока. | [Delete](../../../iblock/classes/ciblock/delete.md) | 3.3.8 |
| [OnIBlockDelete](../../../iblock/events/oniblockdelete.md) | при удалении информационного блока. | [Delete](../../../iblock/classes/ciblock/delete.md) | 3.2.1 |
| [OnBeforeIBlockPropertyAdd](../../../iblock/events/onbeforeiblockpropertyadd.md) | перед добавлением свойства. | CIBlockProperty::CheckFields | 4.0.6 |
| [OnAfterIBlockPropertyAdd](../../../iblock/events/onafteriblockpropertyadd.md) | после добавления свойства. | [Add](../../../iblock/classes/ciblockproperty/add.md) | 4.0.6 |
| [OnBeforeIBlockPropertyUpdate](../../../iblock/events/onbeforeiblockpropertyupdate.md) | перед изменением свойства. | CIBlockProperty::CheckFields | 4.0.6 |
| OnIBlockPropertyDelete | при удалении свойства. | [Delete](../../../iblock/classes/ciblockproperty/delete.md) | 4.0.6 |
| [OnAfterIBlockPropertyUpdate](../../../iblock/events/onafteriblockpropertyupdate.md) | после изменения свойства. | [Update](../../../iblock/classes/ciblockproperty/update.md) | 4.0.6 |
| [OnBeforeIBlockPropertyDelete](../../../iblock/events/onbeforeiblockpropertydelete.md) | перед удалением свойства. | [Delete](../../../iblock/classes/ciblockproperty/delete.md) | 4.0.6 |
| [OnIBlockPropertyBuildList](../../../iblock/events/OnIBlockPropertyBuildList.md) | при построении списка свойств. | [GetUserType](../../../iblock/classes/ciblockproperty/GetUserType.md) | 5.1.0 |
| [OnBeforeIBlockSectionAdd](../../../iblock/events/onbeforeiblocksectionadd.md) | перед добавлением раздела. | CIBlockSection::CheckFields | 4.0.6 |
| [OnAfterIBlockSectionAdd](../../../iblock/events/onafteriblocksectionadd.md) | после добавления раздела. | [Add](../../../iblock/classes/ciblocksection/add.md) | 4.0.6 |
| [OnBeforeIBlockSectionUpdate](../../../iblock/events/onbeforeiblocksectionupdate.md) | перед изменением раздела. | CIBlockSection::CheckFields | 4.0.6 |
| [OnAfterIBlockSectionUpdate](../../../iblock/events/onafteriblocksectionupdate.md) | после изменения раздела. | [Update](../../../iblock/classes/ciblocksection/update.md) | 4.0.6 |
| [OnBeforeIBlockSectionDelete](../../../iblock/events/onbeforeiblocksectiondelete.md) | перед удалением раздела. | [Delete](../../../iblock/classes/ciblocksection/delete.md) | 4.0.6 |
| OnAfterIBlockSectionDelete | после удаления раздела. | [Delete](../../../iblock/classes/ciblocksection/delete.md) | 7.0.3 |
| [OnBeforeIBlockElementAdd](../../../iblock/events/onbeforeiblockelementadd.md) | перед добавлением элемента. | CIBlockElement::CheckFields | 4.0.6 |
| [OnStartIBlockElementAdd](../../../iblock/events/OnStartIBlockElementAdd.md) | в момент начала добавления элемента. | CIBlockElement::CheckFields | 7.1.8 |
| [OnAfterIBlockElementAdd](../../../iblock/events/onafteriblockelementadd.md) | после добавления элемента. | [Add](../../../iblock/classes/ciblockelement/add.md) | 4.0.6 |
| [OnBeforeIBlockElementUpdate](../../../iblock/events/onbeforeiblockelementupdate.md) | перед изменением элемента. | CIBlockElement::CheckFields | 4.0.6 |
| [OnStartIBlockElementUpdate](../../../iblock/events/OnStartIBlockElementUpdate.md) | в момент начала изменения элемента. | CIBlockElement::CheckFields | 7.1.8 |
| [OnAfterIBlockElementUpdate](../../../iblock/events/onafteriblockelementupdate.md) | после изменения элемента. | [Update](../../../iblock/classes/ciblockelement/update.md) | 4.0.6 |
| [OnBeforeIBlockElementDelete](../../../iblock/events/onbeforeiblockelementdelete.md) | перед удалением элемента. | [Delete](../../../iblock/classes/ciblockelement/delete.md) | 4.0.6 |
| [OnAfterIBlockElementDelete](../../../iblock/events/onafteriblockelementdelete.md) | после удаления элемента. | [Delete](../../../iblock/classes/ciblockelement/delete.md) | 5.0.0 |
| [OnIBlockElementDelete](../../../iblock/events/oniblockelementdelete.md) | при удалении элемента информационного блока. | [Delete](../../../iblock/classes/ciblockelement/delete.md) | 3.1.3 |
| OnBeforeEventLog | перед внесением записи в лог. | [Update](../../../iblock/classes/ciblockelement/update.md) | 11.0.8 |
| OnSearchGetFileContent | при поиске файла. | CIBlockElement::__GetFileContent | 7.1.1 |
| GetAuditTypesIblock | при возвращении описания журналу событий | CEventIBlock::GetAuditTypes | 11.0.0 |
| OnAdminSubContextMenuShow | аналог [OnAdminContextMenuShow](../../../main/events/onadmincontextmenushow.md) для списка SKU | CAdminSubContextMenu::Show | 11.0.12 |
| OnAdminSubListDisplay | аналог [OnAdminListDisplay](../../../main/events/onadminlistdisplay.md) для списка SKU | CAdminSubList::Display | 10.0.3 |
| [OnAfterIBlockElementSetPropertyValues](../../../iblock/events/onafteriblockelementsetpropertyvalues.md) | после сохранения значений всех свойств элемента методом [CIBlockElement::SetPropertyValues](../../../iblock/classes/ciblockelement/setpropertyvalues.md). | [CIBlockElement::SetPropertyValues](../../../iblock/classes/ciblockelement/setpropertyvalues.md) | 14.5.1 |
| [OnAfterIBlockElementSetPropertyValuesEx](../../../iblock/events/onafteriblockelementsetpropertyvaluesex.md) | после сохранения значений свойств элемента методом [CIBlockElement::SetPropertyValuesEx](../../../iblock/classes/ciblockelement/setpropertyvaluesex.md). | [CIBlockElement::SetPropertyValuesEx](../../../iblock/classes/ciblockelement/setpropertyvaluesex.md) | 14.5.1 |
| [OnIBlockElementAdd](../../../iblock/events/oniblockelementadd.md) | в момент добавления элемента информационного блока. | [CIBlockElement::Add](../../../iblock/classes/ciblockelement/add.md) | 15.5.12 |
| [OnIBlockElementUpdate](../../../iblock/events/oniblockelementupdate.md) | в момент изменения элемента информационного блока. | [CIBlockElement::Update](../../../iblock/classes/ciblockelement/update.md) | 15.5.12 |
| [OnIBlockElementSetPropertyValues](../../../iblock/events/oniblockelementsetpropertyvalues.md) | в момент сохранения значений свойств элемента инфоблока. | [CIBlockElement::SetPropertyValues](../../../iblock/classes/ciblockelement/setpropertyvalues.md) | 15.5.12 |
| Метод | Описание | С версии |  |
| [GetIBlockList](../../../iblock/functions/getiblocklist.md) | Возвращает список информационных блоков по фильтру. | 3.0.5 |  |
| [GetIBlock](../../../iblock/functions/getiblock.md) | Возвращает информационный блок по заданному коду. | 3.0.5 |  |
| [GetIBlockElementListEx](../../../iblock/functions/getiblockelementlistex.md) | Возвращает список элементов по фильтру. | 3.0.5 |  |
| [GetIBlockElementList](../../../iblock/functions/getiblockelementlist.md) | Возвращает список элементов из определённого информационного блока. | 3.0.5 |  |
| [GetIBlockElement](../../../iblock/functions/getiblockelement.md) | Возвращает элемент по заданному коду. | 3.0.5 |  |
| [GetIBlockSectionList](../../../iblock/functions/getiblocksectionlist.md) | Возвращает список папок из определённого информационного блока. | 3.0.5 |  |
| [GetIBlockSection](../../../iblock/functions/getiblocksection.md) | Возвращает раздел по заданному коду. | 3.0.5 |  |
| [ImportXMLFile](../../../iblock/functions/importxmlfile.md) | Выполняет импорт xml-файла в инфоблок. | 6.5.0 |  |
