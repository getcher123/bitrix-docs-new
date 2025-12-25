# GetByID


```
CIBlockResult
CIBlockSection::GetByID(
	int ID
);
```

Возвращает параметры раздела по его коду *ID*. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| ID | Код раздела. |


#### Возвращаемое значение

Возвращается объект [CIBlockResult](../ciblockresult/index.md). Пользовательские поля не возвращаются.
#### Смотрите также


- [CIBlockResult](../ciblockresult/index.md)
- [Поля раздела](../../fields.md#fsection)


#### Примеры использования


```
<?
$res = CIBlockSection::GetByID($_GET["GID"]);
if($ar_res = $res->GetNext())
	echo $ar_res['NAME'];
?>
```






| ![image](../images/7dd82aba60.gif) 3 **Никита Кургалин**24.04.2017 10:29:10 |
| --- |
| Если вызываете через агент, то лучше использовать **CIBlockSection::GetList**с параметром **"CHECK_PERMISSIONS" => "N"**так как в CIBlockSection по умолчанию включена проверка прав (при этом в CIBlockElement отключена ![:\|](../images/b040cedad7.png) ) |
|  |
