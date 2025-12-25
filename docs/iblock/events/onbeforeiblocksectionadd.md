# OnBeforeIBlockSectionAdd


### Описание и параметры


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlockSection::Add](../classes/ciblocksection/add.md)до вставки информационного блока,
и может быть использовано для отмены вставки или переопределения некоторых полей.
#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#fsection) нового раздела информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.


#### Возвращаемое значение

Для отмены добавления и прекращении выполнения метода [CIBlockSection::Add](../classes/ciblocksection/add.md)необходимо в функции-обработчике создать исключение методом $APPLICATION-> ThrowException()и вернуть *false*.
---
### Смотрите также


- [Событие "OnAfterIBlockSectionAdd"](onafteriblocksectionadd.md) [CIBlockSection::Add](../classes/ciblocksection/add.md)**Обработка событий**

---
### Пример функции-обработчика


```
<?
// файл /bitrix/php_interface/init.php
// регистрируем обработчик
AddEventHandler("iblock", "OnBeforeIBlockSectionAdd", Array("MyClass", "OnBeforeIBlockSectionAddHandler"));
class MyClass
{
	// создаем обработчик события "OnBeforeIBlockSectionAdd"
	public static function OnBeforeIBlockSectionAddHandler(&$arFields)
	{
		if(strlen($arFields["CODE"])<=0)
		{
			global $APPLICATION;
			$aMsg = array();
			$aMsg[] = array("id"=>"CODE", "text"=>"Введите символьный код.");
			$e = new CAdminException($aMsg);
			$APPLICATION->throwException($e);
			return false;
		}
	}
}
?>
```

---



| ![](../images/2068d63a6f.jpg) 0 **Алексей Попович**10.06.2019 12:43:30 |  |  |
| --- | --- | --- |
| Пример обработчика текста, вставляемого в поле "Описание" - ссылки на изображения заменяем на локальные изображения: \| Код \| \| --- \| \| ``` $eventManager = \Bitrix\Main\EventManager::getInstance();$eventManager->addEventHandler('iblock', 'OnBeforeIBlockSectionAdd', array('clInit', 'OnBeforeIBlockSectionAddHandler')); $eventManager->addEventHandler('iblock', 'OnBeforeIBlockSectionUpdate', array('clInit', 'OnBeforeIBlockSectionAddHandler')); class clInit{ function OnBeforeIBlockSectionAddHandler(&$arFields) { if(strlen($arFields["DESCRIPTION"])>0 && strpos($arFields["DESCRIPTION"],"<img")!==false ) { $pattern2="/(alt\\|src\\|title\\|width\\|height\\|align)=(\"\\|')(.+?)(\"\\|')/si"; $pattern="/<img([^>]*)\/?>/si"; preg_match_all($pattern,$arFields["DESCRIPTION"],$matches); foreach($matches[1] as $k=>$image){ preg_match_all($pattern2,$image,$Attrmatches); $attributes=array(); foreach($Attrmatches[1] as $kT=>$Tmp){ $attributes[$Tmp]=$Attrmatches[3][$kT]; } $modifiedImages[$matches[0][$k]]=$attributes; } if(!empty($modifiedImages)){ foreach ($modifiedImages as $image=>$attributes) { if(strpos($attributes['src'],"://")!==false){ $arFile = \CFile::MakeFileArray($attributes['src']); if(!empty($arFile)){ $fid = \CFile::SaveFile(array_merge($arFile,['MODULE_ID'=>'iblock']),'iblock'); if(intval($fid)>0){ $src = \CFile::GetPath($fid); if(file_exists($_SERVER['DOCUMENT_ROOT'].$src)){ $arFields['DESCRIPTION'] = str_replace($attributes['src'],$src,$arFields['DESCRIPTION']); } } } } } } } } } ``` \| Также можно не просто заменять ссылки на изображения, но и обрабатывать все атрибуты изображений: [https://pai-bx.com/wiki/1c-bitrix/47-image-processing-inside-detailtext/](https://pai-bx.com/wiki/1c-bitrix/47-image-processing-inside-detailtext/) | Код | ``` $eventManager = \Bitrix\Main\EventManager::getInstance();$eventManager->addEventHandler('iblock', 'OnBeforeIBlockSectionAdd', array('clInit', 'OnBeforeIBlockSectionAddHandler')); $eventManager->addEventHandler('iblock', 'OnBeforeIBlockSectionUpdate', array('clInit', 'OnBeforeIBlockSectionAddHandler')); class clInit{ function OnBeforeIBlockSectionAddHandler(&$arFields) { if(strlen($arFields["DESCRIPTION"])>0 && strpos($arFields["DESCRIPTION"],"<img")!==false ) { $pattern2="/(alt\|src\|title\|width\|height\|align)=(\"\|')(.+?)(\"\|')/si"; $pattern="/<img([^>]*)\/?>/si"; preg_match_all($pattern,$arFields["DESCRIPTION"],$matches); foreach($matches[1] as $k=>$image){ preg_match_all($pattern2,$image,$Attrmatches); $attributes=array(); foreach($Attrmatches[1] as $kT=>$Tmp){ $attributes[$Tmp]=$Attrmatches[3][$kT]; } $modifiedImages[$matches[0][$k]]=$attributes; } if(!empty($modifiedImages)){ foreach ($modifiedImages as $image=>$attributes) { if(strpos($attributes['src'],"://")!==false){ $arFile = \CFile::MakeFileArray($attributes['src']); if(!empty($arFile)){ $fid = \CFile::SaveFile(array_merge($arFile,['MODULE_ID'=>'iblock']),'iblock'); if(intval($fid)>0){ $src = \CFile::GetPath($fid); if(file_exists($_SERVER['DOCUMENT_ROOT'].$src)){ $arFields['DESCRIPTION'] = str_replace($attributes['src'],$src,$arFields['DESCRIPTION']); } } } } } } } } } ``` |
| Код |  |  |
| ``` $eventManager = \Bitrix\Main\EventManager::getInstance();$eventManager->addEventHandler('iblock', 'OnBeforeIBlockSectionAdd', array('clInit', 'OnBeforeIBlockSectionAddHandler')); $eventManager->addEventHandler('iblock', 'OnBeforeIBlockSectionUpdate', array('clInit', 'OnBeforeIBlockSectionAddHandler')); class clInit{ function OnBeforeIBlockSectionAddHandler(&$arFields) { if(strlen($arFields["DESCRIPTION"])>0 && strpos($arFields["DESCRIPTION"],"<img")!==false ) { $pattern2="/(alt\|src\|title\|width\|height\|align)=(\"\|')(.+?)(\"\|')/si"; $pattern="/<img([^>]*)\/?>/si"; preg_match_all($pattern,$arFields["DESCRIPTION"],$matches); foreach($matches[1] as $k=>$image){ preg_match_all($pattern2,$image,$Attrmatches); $attributes=array(); foreach($Attrmatches[1] as $kT=>$Tmp){ $attributes[$Tmp]=$Attrmatches[3][$kT]; } $modifiedImages[$matches[0][$k]]=$attributes; } if(!empty($modifiedImages)){ foreach ($modifiedImages as $image=>$attributes) { if(strpos($attributes['src'],"://")!==false){ $arFile = \CFile::MakeFileArray($attributes['src']); if(!empty($arFile)){ $fid = \CFile::SaveFile(array_merge($arFile,['MODULE_ID'=>'iblock']),'iblock'); if(intval($fid)>0){ $src = \CFile::GetPath($fid); if(file_exists($_SERVER['DOCUMENT_ROOT'].$src)){ $arFields['DESCRIPTION'] = str_replace($attributes['src'],$src,$arFields['DESCRIPTION']); } } } } } } } } } ``` |  |  |
|  |  |  |
