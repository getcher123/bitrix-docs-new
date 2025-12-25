# Вывод свойств элемента инфоблока

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5761 — Получение суммы значений полей связанных инфоблоков](lesson_5761.md)
- [Следующий: 2915 — Практика. Копирование инфоблока →](lesson_2915.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3484

**Задача**

Выбрать свойство(-а) элемента инфоблока и вывести его на экран.

**Решение**

Решение первой части банально: метод [GetProperty](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/getproperty.php) класса [CIBlockElement](http://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/index.php) подробно описан в документации.

Решение второй части. Возьмём свойство типа **HTML\текст**. Для этого свойства нельзя просто вывести его значение (ключ `VALUE`), т.к. это — массив, содержащий «сырое» значение и его тип (HTML или текст). Всего один вызов метода [GetDisplayValue](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockformatproperties/getdisplayvalue.php) класса [CIBlockFormatProperties](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockformatproperties/index.php):

```
$arResult['DISPLAY_PROPERTIES'][$pid] = CIBlockFormatProperties::GetDisplayValue($arResult, $prop);
```

Теперь в шаблоне мы можем писать так:

```
echo $arResult['DISPLAY_PROPERTIES'][$pid]['DISPLAY_VALUE'];
```

И любое свойство, тип которого предполагает форматирование значения перед выводом, будет соответствующим образом преобразовано.
