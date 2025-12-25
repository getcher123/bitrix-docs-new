# Перенос сайтов в многосайтовой конфигурации

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 30130 — Ошибка: Удалите настройку PHP mbstring.func_overload](lesson_30130.md)
- [Следующий: 3293 — Возможные ошибки при переносе сайта →](lesson_3293.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=2559

<!-- видео скрыто из-за хостинга Beget, его нельзя показывать
&lt;div class="tab"&gt;

&lt;h3 class="tab-title"&gt;&lt;i style="font-size: 25px;" class="fa fa-video-camera fa-border" aria-hidden="true"&gt;&lt;/i&gt;Видеоурок&lt;/h3&gt;

&lt;p&gt;Лицензия допускает создание двух и более сайтов на одном экземпляре системы. Перенос системы на другой хостинг в двухсайтовой конфигурации имеет свои особенности. &lt;/p&gt;

  &lt;p&gt;&lt;iframe title=" Перенос сайтов в многосайтовой конфигурации " src="//www.youtube.com/embed/dOXNMA3Xzec?feature=oembed&rel=0" allowfullscreen="" width="720" height="405" frameborder="0"&gt;
&lt;/iframe&gt;
&lt;/p&gt;
&lt;p&gt;&lt;iframe src="https://rutube.ru/play/embed/eeb80f7ed46d02d57b0d108e6d7c7cb0" frameborder="0" allowfullscreen="" width="720" height="405" frameborder="0"&gt;&lt;/iframe&gt;&lt;/p&gt;


&lt;/div&gt; -->



### Порядок действий




Прежде всего, многосайтовость должна быть настроена на [разных доменах](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=103&LESSON_ID=287).




Во-вторых, несколько меняется общий порядок действий:




1. Создайте [резервную копию](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=5330) главного сайта с ядром, файлами и базой:
  ![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/dump/multisate_buckup_1.png)
2. Перенесите главный сайт через [restore.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&CHAPTER_ID=02014).
3. Создайте [резервную копию](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=5330) второго и других сайтов без ядра и базы, только файлы. При создании копии исключите из архива папки `/bitrix` и `/upload`:
  ![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/dump/multisate_buckup_2.png)
4. Перенесите второй и другие сайты через [restore.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&CHAPTER_ID=02014).
5. С помощью файла [symlink.php](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=103&LESSON_ID=287#simlink) сделайте связку с первым сайтом.
6. Настройте пути и доменные имена для каждого сайта:
  ![](../../../images/courses/32/dev.1c-bitrix.ru/images/admin_start/install/dump/multisate_buckup_3.png)
