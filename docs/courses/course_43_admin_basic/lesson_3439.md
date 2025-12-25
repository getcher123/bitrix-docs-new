# Как добавить поле к любому объекту

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3483 — Выборка, фильтрация и сортировка](lesson_3483.md)
- [Следующий: 3083 — Сдача проекта →](lesson_3083.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3439

Пользовательские поля можно добавить к любому объекту, который изначально их не поддерживает. Например, для объекта `BLOG_RATING` необходимо добавить поле `Рейтинг`.

1. Создайте поле с помощью метода `Add` класса `CUserTypeEntity`. В параметрах обязательно передайте:
  ```
  $type = new CUserTypeEntity();
  $type->Add([
      'ENTITY_ID' => 'BLOG_RATING',
      'FIELD_NAME' => 'UF_RATING',
      'USER_TYPE_ID' => 'double',
      // необязательно
      'SETTINGS' => [
          'DEFAULT_VALUE' => 5,
      ],
      'LIST_COLUMN_LABEL' => [
          'ru' => 'Рейтинг',
      ],
      'LIST_FILTER_LABEL' => [
         'ru' => 'Рейтинг',
      ],
      'EDIT_FORM_LABEL' => [
          'ru' => 'Рейтинг',
      ],
      'HELP_MESSAGE' => [
          'ru' => 'Подсказка',
      ],
  ]);
  ```

  - `ENTITY_ID` — объект. Укажите `BLOG_RATING`.
  - `FIELD_NAME` — код поля, например, `UF_RATING`.
  - `USER_TYPE_ID` — тип данных. Укажите `double` — число.
2. Запишите значение с помощью менеджера полей.
  ```
  /**
   * @var \CUserTypeManager $manager
   */
  $manager = \Bitrix\Main\UserField\Internal\UserFieldHelper::getInstance()->getManager();
  $entityId = 'BLOG_RATING';
  $itemId = 123;
  $fields = [
   'UF_RATING' => 50,
  ];
  $manager->Update($entityId, $itemId, $fields);
  ```
3. Прочитайте данные с помощью методов `GetUserFieldValue` и `GetUserFields`.
  ```
  /**
   * @var \CUserTypeManager $manager
   */
  $manager = \Bitrix\Main\UserField\Internal\UserFieldHelper::getInstance()->getManager();
  $entityId = 'BLOG_RATING';
  $itemId = 123;
  $specificValue = $manager->GetUserFieldValue($entityId, 'UF_RATING', $itemId);
  $allFields = $manager->GetUserFields($entityId, $itemId);
  ```

Такой способ требует ручного управления данными и не работает с методом `GetList`, но позволяет использовать поля в собственных компонентах и модулях.
