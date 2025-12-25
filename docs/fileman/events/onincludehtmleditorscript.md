# OnIncludeHTMLEditorScript


```
функция-обработчик();
```

Событие "OnIncludeHTMLEditorScript" вызывается после подключения файлов визуального редактора.
Может использоваться в тех случаях, когда для модификации редактора недостаточно стандартного подключения внешних JavaScript файлов ( [Событие "OnBeforeHTMLEditorScriptsGet"](onbeforehtmleditorscriptsget.md)). **Внимание**. Событие работает только в рамках старого визуального редактора.


#### Смотрите также


- [Событие "OnBeforeHTMLEditorScriptsGet"](onbeforehtmleditorscriptsget.md)


#### Пример функции-обработчика:


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("fileman", "OnIncludeHTMLEditorScript", "OnIncludeHTMLEditorHandler");
public static function OnIncludeHTMLEditorHandler()
{
	?>
	<script>
	//Переопределение функции установки полноэкранного режима редактора
	BXHTMLEditor.prototype.SetFullscreen_ = BXHTMLEditor.prototype.SetFullscreen;
	BXHTMLEditor.prototype.SetFullscreen = function (bFull)
	{
		alert('My alert!');
		this.SetFullscreen_(bFull);
	}
	</script>
	<?
}
?>
```
