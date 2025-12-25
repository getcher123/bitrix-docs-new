# GetNavChain


### Описание и параметры


```
CIBlockResult CIBlockSection::GetNavChain(
	int IBLOCK_ID,
	int SECTION_ID,
	array arSelect = array(),
	$arrayResult = false
);
```

Метод возвращает путь по дереву от корня до раздела *SECTION_ID*(пользовательские поля не возвращаются). Метод статический.
#### Параметры вызова


| Параметр | Описание | С версии |
| --- | --- | --- |
| IBLOCK_ID | Код информационного блока, служит для проверки что раздел *SECTION_ID*, находится в заданном информационном блоке. Если значение *IBLOCK_ID* ноль, то проверка не будет выполнена и код информационного блока не будет учитываться. |  |
| SECTION_ID | Код раздела информационного раздела, путь до которого будет выбран. |  |
| arSelect | Массив возвращаемых полей раздела. Необязательный параметр. По умолчанию будут возвращены все доступные поля. | 12.5.0 |
| arResult | Необязательный параметр. По умолчанию - *false*. Если передать в него *true* - вернет массив элементов, описывающих позиции, а не CDBResult. Это производительнее. | 12.5.0 |


#### Возвращаемое значение

Возвращается объект [CIBlockResult](../ciblockresult/index.md)с полями [раздела информационного блока.](../../fields.md#fiblocksection)---
### Примеры использования


```
<?
$nav = CIBlockSection::GetNavChain(false, $SECTION_ID);
while($nav->ExtractFields("nav_")):
?> &raquo;
	<?if($SECTION_ID == $nav_ID):?>
		<?echo $nav_NAME?>
	<?else:?>
		<a class="navchain" href="<?=$application->getcurpage()?>?iblock_id=<?=$iblock_id?>&section_id=<?=$nav_id?>#tb"><?echo $nav_NAME?></a>
	<?endif?>
<?endwhile;?>
```

Показать полный массив данных:


```
$list = CIBlockSection::GetNavChain(false,$Section['ID'], array(), true);
foreach ($list as $arSectionPath){
	echo '<pre>';print_r($arSectionPath);echo '</pre>';
}
```

---
#### Смотрите также


- [CIBlockResult](../ciblockresult/index.md)
- [Поля раздела информационного блока](../../fields.md#fiblocksection)






| ![](../images/c799b2d65f.png) 3 **Алексей Попович**12.05.2014 16:45:07 |  |  |
| --- | --- | --- |
| еще один пример: \| Код \| \| --- \| \| ``` $nav = CIBlockSection::GetNavChain(false,$Section['ID']); while($arSectionPath = $nav->GetNext()){ if ($GLOBALS['USER']->IsAdmin()){ echo '<pre>';print_r($arSectionPath);echo '</pre>';} } ``` \| покажет полный массив данных, а то разброс по переменным как-то не очень наглядный ... | Код | ``` $nav = CIBlockSection::GetNavChain(false,$Section['ID']); while($arSectionPath = $nav->GetNext()){ if ($GLOBALS['USER']->IsAdmin()){ echo '<pre>';print_r($arSectionPath);echo '</pre>';} } ``` |
| Код |  |  |
| ``` $nav = CIBlockSection::GetNavChain(false,$Section['ID']); while($arSectionPath = $nav->GetNext()){ if ($GLOBALS['USER']->IsAdmin()){ echo '<pre>';print_r($arSectionPath);echo '</pre>';} } ``` |  |  |
|  |  |  |


| ![](../images/37bfe58294.jpg) 2 **Максим Месилов**03.03.2009 15:27:54 |  |  |
| --- | --- | --- |
| По всей видимости можно пользоваться и функцией-обёрткой из \bitrix\modules\iblock\iblock.php строки 892 - 895 \| Код \| \| --- \| \| ``` function GetIBlockSectionPath($IBLOCK, $SECT_ID) { return CIBlockSection::GetNavChain(IntVal($IBLOCK), IntVal($SECT_ID)); } ``` \| | Код | ``` function GetIBlockSectionPath($IBLOCK, $SECT_ID) { return CIBlockSection::GetNavChain(IntVal($IBLOCK), IntVal($SECT_ID)); } ``` |
| Код |  |  |
| ``` function GetIBlockSectionPath($IBLOCK, $SECT_ID) { return CIBlockSection::GetNavChain(IntVal($IBLOCK), IntVal($SECT_ID)); } ``` |  |  |
|  |  |  |
