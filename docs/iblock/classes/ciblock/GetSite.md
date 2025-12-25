# GetSite


### Описание и параметры


```
CDBResult
CIBlock::GetSite(
	int iblock_id
);
```

Метод возвращает список сайтов к которым привязан инфоблок. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| iblock_id | Идентификатор информационного блока. |


#### Возвращаемое значение

Возвращается объект [CDBResult.](../../../main/reference/cdbresult/index.md)


#### Смотрите также


- [CDBResult](../../../main/reference/cdbresult/index.md)
- Поля CSite

---
### Примеры использования


```
<?
$SITES = '';
$rsSites = CIBlock::GetSite($IBLOCK_ID);
while($arSite = $rsSites->Fetch())
	$SITES .= ($SITES!=""?" / ":"").htmlspecialchars($arSite["SITE_ID"]);
?>
```

---
