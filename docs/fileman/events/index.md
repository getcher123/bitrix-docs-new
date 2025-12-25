# Список событий


### Описание и события

Ниже представлен список событий модуля "Управления структурой". Для регистрации обработчика укажите в качестве идентификатора модуля - "fileman".


#### События, связанные с визуальным HTML-редактором


| Событие | Вызывается | Метод | С версии |
| --- | --- | --- | --- |
| [OnBeforeHTMLEditorScriptsGet](onbeforehtmleditorscriptsget.md) | непосредственно перед подключением JavaScript-файлов редактора. Позволяет добавить в список подключаемых файлов дополнительный JavaScript файл или файл стилей. | CFileMan::ShowHTMLEditControl | 6.5.6 |
| OnBeforeLightEditorScriptsGet | перед подключением JavaScript-файлов упрощенного редактора. | CLightHTMLEditor::Init | 8.5.3 |
| [OnIncludeHTMLEditorScript](onincludehtmleditorscript.md) | непосредственно после подключения редактора, на странице вызова, но до его инициализации. | CFileMan::ShowHTMLEditControl | 5.0.2 |
| OnIncludeLightEditorScript | непосредственно после подключения упрощенного редактора, на странице вызова, но до его инициализации. | CLightHTMLEditor::InitScripts | 9.5.3 |
| OnIframeBeforeGetValue | Событие позволяет модифицировать содержимое получаемое из визредактора. |  | 17.5.1 |
| Событие | Вызывается | Метод | С версии |
| OnMedialibItemView | происходит перед созданием и выдачей элемента медиабиблиотеки в виде HTML для показа пользователю. | CMedialib::GetItemViewHTML | 9.0.0 |

---
### Смотрите также


- **События**
- **Взаимодействие модулей**

---

<!-- vault-nav:start -->
## В этой папке

<details>
<summary>Показать файлы и папки</summary>

### Файлы

- [OnBeforeHTMLEditorScriptsGet](onbeforehtmleditorscriptsget.md)
- [OnIncludeHTMLEditorScript](onincludehtmleditorscript.md)

</details>

<!-- vault-nav:end -->
