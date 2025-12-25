# Чтение (get, require, remindActual, primary, collectValues, runtime)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 11693 — Приведение типов](lesson_11693.md)
- [Следующий: 11697 — Запись (set, reset, unset) →](lesson_11697.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=11695

- *get*
  Чтение данных реализовано несколькими методами. Самый простой из них возвращает значение поля либо *null* в случае его отсутствия (например, если поле не было указано в *select* при выборке):
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $title = $book->getTitle();
  ```
- *require*
  Если вы уверены, что поле должно быть заполнено значением, и без этого значения продолжать выполнение сценария не имеет смысла, можете требовать это значение методом *require*:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $title = $book->requireTitle();
  ```
  В данном случае результат *requireTitle()* не будет отличаться от вышеприведенного *getTitle()*. А следующий пример уже закончится исключением, поскольку поле не будет заполнено значением:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1, ['select' => ['ID', 'PUBLISHER_ID', 'ISBN']])
  	->fetchObject();
  $title = $book->requireTitle();
  // SystemException: "TITLE value is required for further operations"
  ```
- *remindActual*
  Еще один "геттер" *remindActual* пригодится вам при переустановке значения, чтобы отличить оригинальное значение от установленного в процессе сеанса и еще несохраненного в базу данных:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  echo $book->getTitle();
  // выведет "Title 1"
  $book->setTitle("New title");
  echo $book->getTitle();
  // выведет "New title"
  echo $book->remindActualTitle();
  // выведет "Title 1"
  ```
  В качестве альтернативы можно использовать универсальные неименованные методы:
  ```
  $fieldName = 'TITLE';
  $title = $book->get($fieldName);
  $title = $book->require($fieldName);
  $title = $book->remindActual($fieldName);
  ```
- *primary*
  Системный "геттер" *primary* реализован в виде виртуального read-only свойства, чтобы не использовать метод *getPrimary()*, резервируя тем самым имя поля *PRIMARY* с соответствующим именованным геттером. Свойство возвращает значения первичного ключа в формате массива независимо от того, составной ли первичный ключ или одиночный:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $primary = $book->primary;
  // вернет ['ID' => 1]
  $id = $book->getId();
  // вернет 1
  ```
- *collectValues*
  Метод *collectValues* используется для получения всех значений объекта в виде массива.
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $values = $book->collectValues();
  ```
  В данном примере вернутся все имеющиеся значения. Если для некоторых полей значения были переустановлены через "сеттер", но еще не сохранены, то вернутся именно эти значения. Для неизмененных полей будут взяты актуальные значения.
  Можно воспользоваться необязательными фильтрами, чтобы уточнить набор полей и тип данных:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $values = $book->collectValues(\Bitrix\Main\ORM\Objectify\Values::ACTUAL);
  // вернет только актуальные значения, без учета еще не сохраненных
  $values = $book->collectValues(\Bitrix\Main\ORM\Objectify\Values::CURRENT);
  // вернет только текущие значения, еще не сохраненные в базу данных
  $values = $book->collectValues(\Bitrix\Main\ORM\Objectify\Values::ALL);
  // равнозначно вызову collectValues() без параметров - сначала CURRENT, затем ACTUAL
  ```
  Вторым аргументом передается маска, аналогичная используемой в [fill](lesson_11705.md), определяющая типы полей:
  ```
  $book = \Bitrix\Main\Test\Typography\BookTable::getByPrimary(1)
  	->fetchObject();
  $values = $book->collectValues(
  	\Bitrix\Main\ORM\Objectify\Values::CURRENT,
  	\Bitrix\Main\ORM\Fields\FieldTypeMask::SCALAR
  );
  // вернутся только измененные значения скалярных полей
  $values = $book->collectValues(
  	\Bitrix\Main\ORM\Objectify\Values::ALL,
  	\Bitrix\Main\ORM\Fields\FieldTypeMask::ALL & ~\Bitrix\Main\ORM\Fields\FieldTypeMask::USERTYPE
  );
  // вернутся значения всех полей, кроме пользовательских
  ```
- *runtime*
  Для *runtime* полей, создаваемых в рамках отдельных запросов, предусмотрен только универсальный "геттер" *get*:
  ```
  $author = \Bitrix\Main\Test\Typography\AuthorTable::query()
  	->registerRuntimeField(
  		new \Bitrix\Main\Entity\ExpressionField(
  			'FULL_NAME', 'CONCAT(%s, " ", %s)', ['NAME', 'LAST_NAME']
  		)
  	)
  	->addSelect('ID')
  	->addSelect('FULL_NAME')
  	->where('ID', 17)
  	->fetchObject();
  echo $author->get('FULL_NAME');
  // выведет 'Name 17 Last name 17'
  ```
  Внутри объекта такие значения хранятся изолированно от значений штатных полей, и соответственно для них неактуальны все остальные методы по работе с данными.
