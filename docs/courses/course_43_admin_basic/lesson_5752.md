# Короткие вызовы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 5753 — getList](lesson_5753.md)
- [Следующий: 5751 — Объект Query →](lesson_5751.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=5752

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/orm/querying-data.html). В ней улучшена структура, описание, примеры.

В дополнении к *GetList* существует еще ряд методов, которые позволяют в более короткой форме получить определенные данные:

- *getById($id)* - производит выборку по первичному ключу;
- *getByPrimary($primary, array $parameters)* - выборка по первичному ключу с возможностью указания дополнительных параметров;
  **Примечание**: в обоих методах мы можем как передать `id` в виде числа, так и явно указать какой элемент является ключом, передав массив. Массив необходимо использовать, если у вас есть несколько `primary` полей. Если вы передаете в массиве элемент, который не является первичным ключом, то это будет ошибкой.
  ```
  BookTable::getById(1);
  BookTable::getByPrimary(array('ID' => 1));
  // такие вызовы будут аналогичны следующему вызову getList:
  BookTable::getList(array(
  	'filter' => array('=ID' => 1)
  ));
  ```
- *getRowById($id)* - производит выборку по первичному ключу, но возвращается массив данных;
  ```
  $row = BookTable::getRowById($id);
  // аналогичный результат можно получить так:
  $result = BookTable::getById($id);
  $row = $result->fetch();
  // или так
  $result = BookTable::getList(array(
  	'filter' => array('=ID' => $id)
  ));
  $row = $result->fetch();
  ```
- *getRow(array $parameters)* - производит выборку не по первичному ключу, а по каким-то другим параметрам. При этом возвращается только одна запись.
  ```
  $row = BookTable::getRow(array(
  	'filter' => array('%=TITLE' => 'Patterns%'),
  	'order' => array('ID')
  ));
  // аналогичный результат можно получить так:
  $result = BookTable::getList(array(
  	'filter' => array('%=TITLE' => 'Patterns%'),
  	'order' => array('ID')
  	'limit' => 1
  ));
  $row = $result->fetch();
  ```
