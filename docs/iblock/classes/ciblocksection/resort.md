# ReSort


```
CIBlockSection::ReSort(
	int IBLOCK_ID
);
```

Метод пересчитывает параметры левой и правой границ для всех разделов информационного блока *IBLOCK_ID*. Должен использоваться после применения серии добавлений или изменений разделов при помощи методов [CIBlockSection](index.md)::[Add](add.md)() или [CIBlockSection](index.md)::[Update](update.md)() c отключенным параметром *bReSort*, в целях повышения производительности. Метод статический.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| IBLOCK_ID | код информационного блока. |


#### Смотрите также

[CIBlockSection](index.md):: [Add](add.md)() [CIBlockSection](index.md):: [Update](update.md)()
#### Примеры использования


```
<?
$obSect = new CIBlockSection;
for($i=0; $i<100; $i++)
{
	$obSect->Add(Array('NAME'=>'Section #'.$i, 'IBLOCK_ID'=>$IBLOCK_ID), false);
}

CIBlockSection::ReSort($IBLOCK_ID);
?>
```






| ![](../images/599e64eab3.JPG) 2 **xolegator**17.02.2017 13:02:09 |  |  |
| --- | --- | --- |
| На сайте неожиданно стала возникать ошибка "Нельзя перенести раздел внутрь себя." при любой попытке изменить раздел каталога товаров. Много времени было потрачено на поиск источника проблемы. Решением оказалось выполнить в консоли PHP в админке Битрикса код: \| Код \| \| --- \| \| ``` CIBlockSection::ReSort(2); ``` \| где 2 - инфоблок товаров. | Код | ``` CIBlockSection::ReSort(2); ``` |
| Код |  |  |
| ``` CIBlockSection::ReSort(2); ``` |  |  |
|  |  |  |
