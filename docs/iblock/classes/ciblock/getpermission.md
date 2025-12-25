# GetPermission


### Описание и параметры


```
string
CIBlock::GetPermission(
	int IBLOCK_ID,
	int FOR_USER_ID = false
);
```

Возвращает право доступа к информационному блоку *IBLOCK_ID* для пользователя с кодом *FOR_USER_ID* или для текущего пользователя (если код не задан). Нестатический метод.

**Примечание:**метод считается устаревшим (не работает при использовании расширенных прав). Рекомендуется использовать **CIBlockElementRights::UserHasRightTo**и **CIBlockSectionRights::UserHasRightTo**.


#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| IBLOCK_ID | Код информационного блока. |  |
| FOR_USER_ID | Код пользователя. Необязательный параметр. До версии 11.5.1 параметр назывался USER_ID. | 8.5.0 |


#### Возвращаемое значение

Символ права доступа: "D" - запрещён, "R" - чтение, "U" - изменение через документооборот, "W" - изменение, "X" - полный доступ (изменение + право изменять права доступа).

---
### Смотрите также


- [CIBlock::GetGroupPermissions](getgrouppermissions.md)
- CUser::GetUserGroupString

---
### Примеры использования


```
<?
$iblock_permission = CIBlock::GetPermission($id);
if($iblock_permission<"X")
	return false;
?>
```

Пример получения уровня доступа с расширенным управлением правами:


```
$tRight = 'element_edit';
$canEdit = CIBlockElementRights::UserHasRightTo($IBLOCK_ID, $ELEMENT_ID, $tRight);
if (!$tRight) echo "access denied";
```

$tRight может принимать значения:

**section_element_bind**- Добавление элемента в раздел (создание элемента)
**element_bizproc_start**- Запуск бизнес-процесса для элемента
**iblock_edit**- Изменение параметров инфоблока
**iblock_rights_edit**- Изменение прав доступа к инфоблоку
**section_rights_edit**- Изменение прав доступа к разделу
**element_rights_edit**- Изменение прав доступа к элементу
**section_edit**- Изменение раздела
**element_edit**- Изменение элемента
**element_edit_any_wf_status**- Изменение элемента в любом статусе документооборота
**iblock_admin_display**- Показ инфоблока в административном разделе
**element_edit_price**- Редактирование цен, относящихся к элементу
**section_section_bind**- Создание подраздела в разделе
**iblock_delete**- Удаление инфоблока
**section_delete**- Удаление раздела
**element_delete**- Удаление элемента
**section_read**- Чтение параметров раздела
**element_read**- Чтение элемента
**iblock_export**- Экспорт инфоблока. ---
