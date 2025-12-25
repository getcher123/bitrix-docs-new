# OnBeforeHTMLEditorScriptsGet


### Описание и параметры


```
array функция-обработчик(
	string editorName
	array arEditorParams
);
```

Событие "OnBeforeHTMLEditorScriptsGet" вызывается перед загрузкой JavaScript и CSS файлов редактора и позволяет добавить пользовательские файлы, которые будут подгружаться после файлов визуального редактора. Создание обработчика данного представляет собой простейший способ модифицировать встроенный визуальный редактор путём расширения или переопределения текущего функционала.

**Внимание**. Событие работает только в рамках старого визуального редактора.


#### Параметры


| Параметр | Описание |
| --- | --- |
| *editorName* | Имя подключаемого редактора. |
| *arEditorParams* | Массив параметров подключаемого редактора. |


#### Структура результата

Результатом выполнения функции-обработчика должен быть ассоциативный массив, который может содержать поля "JS" и "CSS" каждое из которых должно являться линейным массивом имен подключаемых файлов c соответствующим расширением.

Файлы, имена которых возвращаются в качестве элементов массивов в полях "JS" и "CSS" должны находиться в папке */bitrix/admin/htmleditor2*

---
### Смотрите также


- [Событие "OnIncludeHTMLEditorScript"](onincludehtmleditorscript.md)

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("fileman", "OnBeforeHTMLEditorScriptsGet", "addEditorScriptsHandler");
public static function addEditorScriptsHandler($editorName,$arEditorParams)
{
	// Проверяем, если подключается редактор для редактирования статических страниц
	if ($editor_name == 'filesrc')
		return array(
			"JS" => array('my_scripts.js'),
			"CSS" => array('my_styles.css')
		);

	return array();
}
?>

<?
// файл /bitrix/admin/htmleditor2/my_scripts.js
// Переопределяем стандартную панель инструментов, удаляя из нее кнопки "Настройки", "Выделить все" и "Проверка орфографии"
arToolbars['standart'] = [
	BX_MESS.TBSStandart,
		[
		arButtons['Fullscreen'], 'separator',
		arButtons['Cut'], arButtons['Copy'], arButtons['Paste'], arButtons['pasteword'], arButtons['pastetext'], arButtons['separator'],
		arButtons['Undo'], arButtons['Redo'], arButtons['separator'],
		arButtons['borders'], 'separator',
		arButtons['table'], arButtons['anchor'], arButtons['CreateLink'], arButtons['deletelink'], arButtons['image'], 'separator',
		arButtons['SpecialChar'], arButtons['spellcheck']
		]
	];
?>

/* файл /bitrix/admin/htmleditor2/my_styles.css
переопределяем цвет фона редактора (только для Mozilla Firefox) */
.bxedmainframe IFRAME{
	background-color: #CCCCCC;
}
```

---




| ![](../images/431c4acd91.png) 1 **Дмитрий Иванов**13.11.2011 16:45:14 |  |  |
| --- | --- | --- |
| Рабочий пример: \| Код \| \| --- \| \| ``` func tion print_r(theObj){//Аналог php print_r для script if(theObj.constructor == Array \\|\\| theObj.constructor == Object){ document.write("<ul st yle='font-size:9px;'>" for(var p in theObj){ if(theObj.constructor == Array\\|\\| theObj.constructor == Object){ document.write("<li>["+p+"] => "+typeof(theObj)+"</li>"; document.write("<ul>" print_r(theObj); document.write("</ul>" } else { document.write("<li>["+p+"] => "+theObj+"</li>"; } } document.write("</ul>" } } /*Переопределяем и создаём кнопки*/ arButtons['HeadingList'] = ['BXEdList', { field_size: 100, width: 210, title: '(' + BX_MESS.Format + ')', disableOnCodeView: true, bAdminConfigure: true, //bSetGlobalStyles: false, values: [ {value: 'p', name: 'Абзац'}, {value: 'h1', name: 'Заголовок 1'}, {value: 'h2', name: 'Заголовок 2'}, {value: 'h3', name: 'Заголовок 3'}, {value: 'h4', name: 'Заголовок 4'}, {value: 'h5', name: 'Заголовок 5'}, {value: 'h6', name: 'Заголовок 6'}, {value: 'pre', name: 'Preformatted'} ], OnSelectionChange: f unction (){ var sel = 0; var frm = this.pMainObj.queryCommand('FormatBlock'); if(frm) { var re = /[1-6]/; var r = frm.match(re); if(r>0) sel = r; else if(frm == 'pre') sel = 7; } this.Select(sel); }, OnChange: f unction (selected){this.pMainObj.executeCommand('FormatBlock', (selected['value'].length>0?'<' + selected['value']+'>':'<p>'));}, OnDrawItem: f unction (item) { if (!styleList_render_style) return item['name']; return (item['value'].length <= 0 ? item['name'] : '<'+item['value']+'>'+item['name']+'</'+item['value']+'>'); } } ]; arButtons['Cite'] = ['BXButton', { id : 'Cite', src : '/bitrix/templates/.default/images/fileman/icon_cite.gif', name : 'Цитата', title : 'Вставить цитату', show_name : true, handler: f unction(){ this.pMainObj.insertHTML('<cite>Цитата</cite>'); } } ]; /* Добавим свою кнопку за место разделится(separator) после hr(Горизонтальный разделитель). Для этого обновим объект arToolbars['formating'] и arGlobalToolbar объявленные в toolbarbuttons.js Для не административной части (arGlobalToolbar) требуется поиск элемента по id. В административной элемент находится в объекте formating 0 месте в массиве. Разделитель(separator) следует сразу за hr. Заодно изменим выпадающий список формат. */ try{//Публичный режим (Просто проверяем код на истинность, иначе режим административной части) if(wind ow .lightMode) не сработает var j_chet=0; var j_pos_formating=-1; while(arGlobalToolbar[j_chet]){ if(arGlobalToolbar[j_chet][1]['title']=="(Формат)"{ arGlobalToolbar[j_chet]=arButtons['HeadingList'];} if(arGlobalToolbar[j_chet][1]['id']=="InsertHorizontalRule"{j_pos_formating=j_chet+1;} j_chet+=1; } if(j_pos_formating>0)arGlobalToolbar[j_pos_formating]=arButtons['Cite']; }catch(e){//Для режима административной части var j_chet=0; while(arToolbars.style[1][j_chet]){ if(arToolbars.style[1][j_chet][1]['title']=="(Формат)"{ arToolbars.style[1][j_chet]=arButtons['HeadingList'];break;} j_chet+=1; } arToolbars.formating[1][1]=arButtons['Cite']; } //print_r(arGlobalToolbar); ``` \| ![image](../images/aa1f2740a3.php) [2011-11-13_164442.png](https://dev.1c-bitrix.ru/bitrix/components/bitrix/forum.interface/show_file.php?fid=441767&action=download)(6.82 КБ) | Код | ``` func tion print_r(theObj){//Аналог php print_r для script if(theObj.constructor == Array \|\| theObj.constructor == Object){ document.write("<ul st yle='font-size:9px;'>" for(var p in theObj){ if(theObj.constructor == Array\|\| theObj.constructor == Object){ document.write("<li>["+p+"] => "+typeof(theObj)+"</li>"; document.write("<ul>" print_r(theObj); document.write("</ul>" } else { document.write("<li>["+p+"] => "+theObj+"</li>"; } } document.write("</ul>" } } /*Переопределяем и создаём кнопки*/ arButtons['HeadingList'] = ['BXEdList', { field_size: 100, width: 210, title: '(' + BX_MESS.Format + ')', disableOnCodeView: true, bAdminConfigure: true, //bSetGlobalStyles: false, values: [ {value: 'p', name: 'Абзац'}, {value: 'h1', name: 'Заголовок 1'}, {value: 'h2', name: 'Заголовок 2'}, {value: 'h3', name: 'Заголовок 3'}, {value: 'h4', name: 'Заголовок 4'}, {value: 'h5', name: 'Заголовок 5'}, {value: 'h6', name: 'Заголовок 6'}, {value: 'pre', name: 'Preformatted'} ], OnSelectionChange: f unction (){ var sel = 0; var frm = this.pMainObj.queryCommand('FormatBlock'); if(frm) { var re = /[1-6]/; var r = frm.match(re); if(r>0) sel = r; else if(frm == 'pre') sel = 7; } this.Select(sel); }, OnChange: f unction (selected){this.pMainObj.executeCommand('FormatBlock', (selected['value'].length>0?'<' + selected['value']+'>':'<p>'));}, OnDrawItem: f unction (item) { if (!styleList_render_style) return item['name']; return (item['value'].length <= 0 ? item['name'] : '<'+item['value']+'>'+item['name']+'</'+item['value']+'>'); } } ]; arButtons['Cite'] = ['BXButton', { id : 'Cite', src : '/bitrix/templates/.default/images/fileman/icon_cite.gif', name : 'Цитата', title : 'Вставить цитату', show_name : true, handler: f unction(){ this.pMainObj.insertHTML('<cite>Цитата</cite>'); } } ]; /* Добавим свою кнопку за место разделится(separator) после hr(Горизонтальный разделитель). Для этого обновим объект arToolbars['formating'] и arGlobalToolbar объявленные в toolbarbuttons.js Для не административной части (arGlobalToolbar) требуется поиск элемента по id. В административной элемент находится в объекте formating 0 месте в массиве. Разделитель(separator) следует сразу за hr. Заодно изменим выпадающий список формат. */ try{//Публичный режим (Просто проверяем код на истинность, иначе режим административной части) if(wind ow .lightMode) не сработает var j_chet=0; var j_pos_formating=-1; while(arGlobalToolbar[j_chet]){ if(arGlobalToolbar[j_chet][1]['title']=="(Формат)"{ arGlobalToolbar[j_chet]=arButtons['HeadingList'];} if(arGlobalToolbar[j_chet][1]['id']=="InsertHorizontalRule"{j_pos_formating=j_chet+1;} j_chet+=1; } if(j_pos_formating>0)arGlobalToolbar[j_pos_formating]=arButtons['Cite']; }catch(e){//Для режима административной части var j_chet=0; while(arToolbars.style[1][j_chet]){ if(arToolbars.style[1][j_chet][1]['title']=="(Формат)"{ arToolbars.style[1][j_chet]=arButtons['HeadingList'];break;} j_chet+=1; } arToolbars.formating[1][1]=arButtons['Cite']; } //print_r(arGlobalToolbar); ``` |
| Код |  |  |
| ``` func tion print_r(theObj){//Аналог php print_r для script if(theObj.constructor == Array \|\| theObj.constructor == Object){ document.write("<ul st yle='font-size:9px;'>" for(var p in theObj){ if(theObj.constructor == Array\|\| theObj.constructor == Object){ document.write("<li>["+p+"] => "+typeof(theObj)+"</li>"; document.write("<ul>" print_r(theObj); document.write("</ul>" } else { document.write("<li>["+p+"] => "+theObj+"</li>"; } } document.write("</ul>" } } /*Переопределяем и создаём кнопки*/ arButtons['HeadingList'] = ['BXEdList', { field_size: 100, width: 210, title: '(' + BX_MESS.Format + ')', disableOnCodeView: true, bAdminConfigure: true, //bSetGlobalStyles: false, values: [ {value: 'p', name: 'Абзац'}, {value: 'h1', name: 'Заголовок 1'}, {value: 'h2', name: 'Заголовок 2'}, {value: 'h3', name: 'Заголовок 3'}, {value: 'h4', name: 'Заголовок 4'}, {value: 'h5', name: 'Заголовок 5'}, {value: 'h6', name: 'Заголовок 6'}, {value: 'pre', name: 'Preformatted'} ], OnSelectionChange: f unction (){ var sel = 0; var frm = this.pMainObj.queryCommand('FormatBlock'); if(frm) { var re = /[1-6]/; var r = frm.match(re); if(r>0) sel = r; else if(frm == 'pre') sel = 7; } this.Select(sel); }, OnChange: f unction (selected){this.pMainObj.executeCommand('FormatBlock', (selected['value'].length>0?'<' + selected['value']+'>':'<p>'));}, OnDrawItem: f unction (item) { if (!styleList_render_style) return item['name']; return (item['value'].length <= 0 ? item['name'] : '<'+item['value']+'>'+item['name']+'</'+item['value']+'>'); } } ]; arButtons['Cite'] = ['BXButton', { id : 'Cite', src : '/bitrix/templates/.default/images/fileman/icon_cite.gif', name : 'Цитата', title : 'Вставить цитату', show_name : true, handler: f unction(){ this.pMainObj.insertHTML('<cite>Цитата</cite>'); } } ]; /* Добавим свою кнопку за место разделится(separator) после hr(Горизонтальный разделитель). Для этого обновим объект arToolbars['formating'] и arGlobalToolbar объявленные в toolbarbuttons.js Для не административной части (arGlobalToolbar) требуется поиск элемента по id. В административной элемент находится в объекте formating 0 месте в массиве. Разделитель(separator) следует сразу за hr. Заодно изменим выпадающий список формат. */ try{//Публичный режим (Просто проверяем код на истинность, иначе режим административной части) if(wind ow .lightMode) не сработает var j_chet=0; var j_pos_formating=-1; while(arGlobalToolbar[j_chet]){ if(arGlobalToolbar[j_chet][1]['title']=="(Формат)"{ arGlobalToolbar[j_chet]=arButtons['HeadingList'];} if(arGlobalToolbar[j_chet][1]['id']=="InsertHorizontalRule"{j_pos_formating=j_chet+1;} j_chet+=1; } if(j_pos_formating>0)arGlobalToolbar[j_pos_formating]=arButtons['Cite']; }catch(e){//Для режима административной части var j_chet=0; while(arToolbars.style[1][j_chet]){ if(arToolbars.style[1][j_chet][1]['title']=="(Формат)"{ arToolbars.style[1][j_chet]=arButtons['HeadingList'];break;} j_chet+=1; } arToolbars.formating[1][1]=arButtons['Cite']; } //print_r(arGlobalToolbar); ``` |  |  |
|  |  |  |
