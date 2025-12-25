# OnStartIBlockElementAdd


```
bool функция-обработчик(
	array &arParams
);
```

Событие вызывается в методе [CIBlockElement::Add](../classes/ciblockelement/add.md) до добавления элемента инфоблока перед проверкой правильности заполнения полей.


#### Параметры


| Параметр | Описание |
| --- | --- |
| *arParams* | [Массив полей](../fields.md#felement) нового элемента информационного блока. |

**Обратите внимание, что**все параметры данного обработчика являются ссылками на исходные переменные. Поэтому если вы измените значение параметра внутри обработчика, это приведет к смене значения исходной переменной поступившей на вход функции-обработчика.

<h4>Возвращаемое значение</h4>
Для отмены добавления и прекращении выполнения метода <a class="link" href="/api_help/iblock/classes/ciblockelement/add.php">CIBlockElement::Add</a> необходимо в функции-обработчике создать исключение методом <nobr>$APPLICATION-&gt;<a class="link" href="/api_help/main/reference/cmain/throwexception.php">ThrowException()</a></nobr> и вернуть <i>false</i>.

#### Смотрите также


- [CIBlockElement::Add](../classes/ciblockelement/add.md) **Обработка событий**
