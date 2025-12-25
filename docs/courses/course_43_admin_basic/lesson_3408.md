# Санитайзер

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3053 — Кеширование в собственных компонентах](lesson_3053.md)
- [Следующий: 2922 — Защита от фреймов →](lesson_2922.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3408

Тему урока можно изучить в новом формате — [в документации по Bitrix Framework](https://docs.1c-bitrix.ru/pages/security/sanitizer.html). В ней улучшена структура, описание, примеры.

> **Санитайзер** - инструмент, анализирующий введённый пользователем html код. Основная задача санитайзера - предотвратить внедрение/вывод на экран потенциально опасного кода в HTML.

Санитайзер удобно использовать там, где пользователь вводит произвольный html. Например, в  визуальном редакторе или при копировании текста из *MS Word*. Кроме функций контроля введённого кода санитайзер частично отслеживает валидность вёрстки, в частности закрывает незакрытые теги.

#### Как фильтровать текст

Если необходимо отфильтровать текст (содержащий  HTML - тэги) введенный пользователем от нежелательных тэгов HTML с помощью санитайзера, то можно это сделать так:

```
$Sanitizer = new CBXSanitizer;

$Sanitizer->AddTags( array (
	'a' = > array('href','id','style','alt'...),
	'br' => array(),
	.... ));

$pureHtml = $Sanitizer->SanitizeHtml($html);
```

Санитайзер отфильтрует все тэги и атрибуты, которые не содержатся в "белом" списке, сформированном функцией [AddTags()](http://dev.1c-bitrix.ru/api_help/main/reference/cbxsanitizer/addtags.php).

В санитайзер включены 3 преднастроенных уровня фильтрации:

SECURE_LEVEL_HIGH (высокий уровень) включает следующий список:

```
$arTags = array(
	'b'        => array(),
	'br'        => array(),
	'big'        => array(),
	'blockquote'    => array(),
	'code'        => array(),
	'del'        => array(),
	'dt'        => array(),
	'dd'        => array(),
	'font'        => array(),
	'h1'        => array(),
	'h2'        => array(),
	'h3'        => array(),
	'h4'        => array(),
	'h5'        => array(),
	'h6'        => array(),
	'hr'        => array(),
	'i'        => array(),
	'ins'        => array(),
	'li'        => array(),
	'ol'        => array(),
	'p'        => array(),
	'small'        => array(),
	's'        => array(),
	'sub'        => array(),
	'sup'        => array(),
	'strong'    => array(),
	'pre'        => array(),
	'u'        => array(),
	'ul'        => array()
);
```

SECURE_LEVEL_MIDDLE (средний уровень) включает в себя:

```
$arTags = array(
	'a'        => array('href', 'title','name','alt'),
	'b'        => array(),
	'br'        => array(),
	'big'        => array(),
	'blockquote'    => array('title'),
	'code'        => array(),
	'caption'    => array(),
	'del'        => array('title'),
	'dt'        => array(),
	'dd'        => array(),
	'font'        => array('color','size'),
	'color'        => array(),
	'h1'        => array(),
	'h2'        => array(),
	'h3'        => array(),
	'h4'        => array(),
	'h5'        => array(),
	'h6'        => array(),
	'hr'        => array(),
	'i'        => array(),
	'img'        => array('src','alt','height','width','title'),
	'ins'        => array('title'),
	'li'        => array(),
	'ol'        => array(),
	'p'        => array(),
	'pre'        => array(),
	's'        => array(),
	'small'        => array(),
	'strong'    => array(),
	'sub'        => array(),
	'sup'        => array(),
	'table'        => array('border','width'),
	'tbody'        => array('align','valign'),
	'td'        => array('width','height','align','valign'),
	'tfoot'        => array('align','valign'),
	'th'        => array('width','height'),
	'thead'        => array('align','valign'),
	'tr'        => array('align','valign'),
	'u'        => array(),
	'ul'        => array()
);
```

SECURE_LEVEL_LOW (низкий уровень) включает в себя:

```
$arTags = array(
	'a'        => array('href', 'title','name','style','id','class','shape','coords','alt','target'),
	'b'        => array('style','id','class'),
	'br'        => array('style','id','class'),
	'big'        => array('style','id','class'),
	'blockquote'    => array('title','style','id','class'),
	'caption'    => array('style','id','class'),
	'code'        => array('style','id','class'),
	'del'        => array('title','style','id','class'),
	'div'        => array('title','style','id','class','align'),
	'dt'        => array('style','id','class'),
	'dd'        => array('style','id','class'),
	'font'        => array('color','size','face','style','id','class'),
	'h1'        => array('style','id','class','align'),
	'h2'        => array('style','id','class','align'),
	'h3'        => array('style','id','class','align'),
	'h4'        => array('style','id','class','align'),
	'h5'        => array('style','id','class','align'),
	'h6'        => array('style','id','class','align'),
	'hr'        => array('style','id','class'),
	'i'        => array('style','id','class'),
	'img'        => array('src','alt','height','width','title'),
	'ins'        => array('title','style','id','class'),
	'li'        => array('style','id','class'),
	'map'        => array('shape','coords','href','alt','title','style','id','class','name'),
	'ol'        => array('style','id','class'),
	'p'        => array('style','id','class','align'),
	'pre'        => array('style','id','class'),
	's'        => array('style','id','class'),
	'small'        => array('style','id','class'),
	'strong'    => array('style','id','class'),
	'span'        => array('title','style','id','class','align'),
	'sub'        => array('style','id','class'),
	'sup'        => array('style','id','class'),
	'table'        => array('border','width','style','id','class','cellspacing','cellpadding'),
	'tbody'        => array('align','valign','style','id','class'),
	'td'        => array('width','height','style','id','class','align','valign','colspan','rowspan'),
	'tfoot'        => array('align','valign','style','id','class','align','valign'),
	'th'        => array('width','height','style','id','class','colspan','rowspan'),
	'thead'        => array('align','valign','style','id','class'),
	'tr'        => array('align','valign','style','id','class'),
	'u'        => array('style','id','class'),
	'ul'        => array('style','id','class')
);
```

Воспользоваться санитайзером с одним из преднастроенных уровней можно так:

```
$Sanitizer = new CBXSanitizer;

$Sanitizer->SetLevel(CBXSanitizer::SECURE_LEVEL_MIDDLE);

$pureHtml = $Sanitizer->SanitizeHtml($html);
```



Для работы с санитайзером доступны функции класса [CBXSanitizer](http://dev.1c-bitrix.ru/api_help/main/reference/cbxsanitizer/index.php).
