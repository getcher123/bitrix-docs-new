# AJAX расширение


### Список методов


| Метод | Описание | С версии |
| --- | --- | --- |
| BX.ajax | Низкоуровневая функция для отправки аяксовых запросов. |  |
| BX.ajax.Setup | Устанавливает значения по умолчанию для параметров аяксовых запросов. |  |
| BX.ajax.get | Простая отправка GET-запроса и передача результата обработчику . |  |
| BX.ajax.post | Простая отправка POST-запроса и передача результата обработчику. |  |
| BX.ajax.insertToNode | Запрашивает данные по указанному адресу и вставляет ответ в указанный контейнер. |  |
| BX.ajax.load | Загружает очередь ресурсов и вызывает обработчик. |  |
| BX.ajax.loadJSON | Загружает json-объект из заданного url и передаёт его обработчику. |  |
| BX.ajax.loadScriptAjax | Загружает и выполняет скрипт или серию скриптов. |  |
| BX.ajax.runAction | Метод для запуска аякс-действий в модуле. |  |
| BX.ajax.runComponentAction | Метод для запуска аякс-действий в компоненте. |  |

---
### Примеры


```
<?
require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
$APPLICATION->SetTitle("AJAX");
	CJSCore::Init(array('ajax'));
	$sidAjax = 'testAjax';
if(isset($_REQUEST['ajax_form']) && $_REQUEST['ajax_form'] == $sidAjax){
	$GLOBALS['APPLICATION']->RestartBuffer();
	echo CUtil::PhpToJSObject(array(
		'RESULT' => 'HELLO',
		'ERROR' => ''
	));
	die();
}

?>
<div class="group">
	<div id="block"></div >
	<div id="process">wait ... </div >
</div>
<script>
	window.BXDEBUG = true;
function DEMOLoad(){
	BX.hide(BX("block"));
	BX.show(BX("process"));
	BX.ajax.loadJSON(
		'<?=$APPLICATION->GetCurPage()?>?ajax_form=<?=$sidAjax?>',
		DEMOResponse
	);
}
function DEMOResponse (data){
	BX.debug('AJAX-DEMOResponse ', data);
	BX("block").innerHTML = data.RESULT;
	BX.show(BX("block"));
	BX.hide(BX("process"));

	BX.onCustomEvent(
		BX(BX("block")),
		'DEMOUpdate'
	);
}

BX.ready(function(){
	/*
	BX.addCustomEvent(BX("block"), 'DEMOUpdate', function(){
		window.location.href = window.location.href;
	});
	*/
	BX.hide(BX("block"));
	BX.hide(BX("process"));

	BX.bindDelegate(
		document.body, 'click', {className: 'css_ajax' },
		function(e){
			if(!e)
				e = window.event;

		DEMOLoad();
		return BX.PreventDefault(e);
		}
	);

});

</script>
<div class="css_ajax">click Me</div>
<?require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");?>
```

---
