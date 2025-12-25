# Публичный диалог показа файлов

-<p>Расширение <b>viewer</b> (<b>core_viewer.js</b>)</p> Диалог работает только с файлами, которые размещены на корпоративном портале. Вьювер открывается на элементах, содержащих атрибуты **data-viewer** и **data-viewer-group-by** (см. `/bitrix/js/ui/viewer.js`). Чтобы viewer работал, нужно подключить его:


```
CJSCore::Init([ 'ui.viewer' ]);
```

Итоговый код выглядит примерно так:


```
<? CJSCode::Init([ 'ui.viewer' ]); ?>
<button
	class="ui-btn ui-btn-link"
	data-viewer="null"
	data-object-id="1234"
	data-viewer-type="document"
	data-src="/disk/downloadFile/1234/?&ncc=1&filename=ИмяФайла.pdf"
	data-title="ИмяФайла.pdf"
	data-actions='[{"type":"download"}]'
>ОТКРЫТЬ ФАЙЛ</button>
```

Где: 1234 - ID файла на диске ИмяФайла.pdf - название файла во вьювере.


#### Пример


```
<?
require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
$APPLICATION->SetTitle("Просмотр изображений");
	CJSCore::Init(Array("viewer"));
?>
	<div id="db-items" >
		<span class="feed-com-img-wrap" style="width:548px;">
			<img
				onload="this.parentNode.className='feed-com-img-wrap';"
				src="http://www.1c-bitrix.ru.images.1c-bitrix-cdn.ru/upload/iblock/28b/box_cms_125_143x158.jpg"
				data-bx-viewer="image"
				data-bx-title="CMS"
				data-bx-src="http://www.1c-bitrix.ru/images/gr/bus125_2/02.jpg"
				data-bx-download="http://www.1c-bitrix.ru/images/gr/bus125_2/02.jpg"
				data-bx-width="548"
				data-bx-height="346"
			/>
		</span>
		<span class="feed-com-img-wrap" style="width:548px;">
			<img
				onload="this.parentNode.className='feed-com-img-wrap';"
				src="http://www.1c-bitrix.ru.images.1c-bitrix-cdn.ru/upload/iblock/d5b/box_cp_125_143x158.jpg"
				data-bx-viewer="image"
				data-bx-title="KP"
				data-bx-src="http://www.1c-bitrix.ru/images/new/cp11/meeting/podg.png"
				data-bx-download="http://www.1c-bitrix.ru/images/new/cp11/meeting/podg.png"
				data-bx-width="548"
				data-bx-height="346"
			/>
		</span>
	</div>
<script>
BX.ready(function(){
	var obImageView = BX.viewElementBind(
		'db-items',
		{showTitle: true, lockScroll: false},
		function(node){
			return BX.type.isElementNode(node) && (node.getAttribute('data-bx-viewer') || node.getAttribute('data-bx-image'));
		}
	);
});
</script>
<?require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");?>
```
