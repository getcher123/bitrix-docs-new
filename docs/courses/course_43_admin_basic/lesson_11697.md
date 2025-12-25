# Запись (set, reset, unset)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11695 — Чтение (get, require, remindActual, primary, collectValues, runtime)](lesson_11695.md)
- [Следующий: 11997 — Проверки (isFilled, isChanged, has) →](lesson_11997.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11697

- *set*
  Установка значения происходит схожим образом:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $book->setTitle("New title");
  ```
  При этом объект запоминает свои исходные значения. С этого момента доступ к текущему значению осуществляется через основной "геттер" *get*, а к изначальному, актуальному для базы данных значению, через вспомогательный "геттер" *remindActual*:
  ```
  $book->getTitle(); // текущее значение
  $book->remindActualTitle(); // актуальное для базы данных значение
  ```
  Значения первичного ключа *primary* можно устанавливать только в новых объектах, в существующих изменить его будет нельзя. При такой необходимости придется создать новый объект и удалить старый. Также не сработает установка полей *Bitrix\Main\ORM\Fields\ExpressionField*, поскольку их значения рассчитываются автоматически и не подлежат изменению извне.
  При установке значения, не отличающегося от актуального, значение фактически не будет изменено и не попадет в SQL-запрос при сохранении объекта.
- *reset*
  Чтобы отменить установку нового значения и вернуть исходное, можно воспользоваться вспомогательным "сеттером" *reset*:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  echo $book->getTitle();
  // выведет "Title 1"
  $book->setTitle("New title");
  echo $book->getTitle();
  // выведет "New title"
  $book->resetTitle();
  echo $book->getTitle();
  // выведет "Title 1"
  ```
- *unset*
  Еще один вспомогательный "сеттер" *unset* удалит значение объекта так, будто бы оно никогда не выбиралось из базы данных и не было установлено:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  echo $book->getTitle();
  // выведет "Title 1"
  $book->unsetTitle();
  echo $book->getTitle();
  // null
  ```
  Для "сеттеров" тоже есть универсальные варианты вызова с именем поля в качестве аргумента:
  ```
  $fieldName = 'TITLE';
  $book->set($fieldName, "New title");
  $book->reset($fieldName);
  $book->unset($fieldName);
  ```
  Все операции по изменению значения приводят к изменениям только во время сеанса. Чтобы зафиксировать изменения в базе данных, объект нужно сохранить - об этом читайте в уроке [Создание и редактирование (save, new)](lesson_11699.md).
