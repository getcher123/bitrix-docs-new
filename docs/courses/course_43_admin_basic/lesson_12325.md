# Вложенные библиотеки

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 13376 — @bitrix/cli: сборка проекта с NPM](lesson_13376.md)
- [Следующий: 11985 — Использование ES6 →](lesson_11985.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=12325

Библиотеки могут содержать вспомогательные библиотеки. Вспомогательные библиотеки можно подключить отдельно.

Полный путь в файловой системе:

```

`/bitrix/modules/<module_name>/install/js/<module_name>/<library_name>/<sub_library_name>/`
```

В таком формате вызов вашей библиотеки будет таким:

```

\Bitrix\Main\UI\Extension::load('<module_name>.<library_name>.<sub_library_name>');
```

Количество вложенных папок не ограничено. Каждая новая папка должно быть указана в названии расширения через точку:

```

<module_name>.<library_name>.<sub_library_name>.<sub_library_name_2>.<sub_library_name_3>
```

В данном случае путь будет таким:

```

/bitrix/modules/<module_name>/install/js/<module_name>/<library_name>/<sub_library_name>/<sub_library_name_2>/<sub_library_name_3>/
```
