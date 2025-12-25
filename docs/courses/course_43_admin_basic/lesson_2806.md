# Способы передачи данных между компонентами

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3031 — Разработка верстки шаблона компонента](lesson_3031.md)
- [Следующий: 2305 — Простой пример создания компонента →](lesson_2305.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2806

Способы передачи данных между компонентами:

1. Глобальные переменные, Например:
  ```
  $GLOBALS['mycomponent_variable'] = $arResult["ID"];
  ```
  Кроме `GLOBALS` можно использовать `$_SESSION` при условиях, что:

  - данные небольшого объема;
  - сразу после передачи данные будут удалены из `$_SESSION`, так как в противном случае будут жить, пока сессия жива.
2. Класс обертка, например:
  ```
  Class GarbageStorage{
  	private static $storage = array();
  	public static function set($name, $value){ self::$storage[$name] = $value;}
  	public static function get($name){ return self::$storage[$name];}
  }
  ```
  соответственно, использование:
  ```
  \GarbageStorage::set('MyCustomID', $arResult["ID"]); #установить значение
  \GarbageStorage::get('MyCustomID'); #получить значение
  ```

Выбор способа зависит от компонентов и от того что именно вы хотите передать в другой компонент и есть ли необходимые данные в некешируемых файлах (речь идет о [component_epilog.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&CHAPTER_ID=02975)). Использование класса обертки сложнее, но гораздо правильнее, особенно в свете создаваемого нового ядра.
