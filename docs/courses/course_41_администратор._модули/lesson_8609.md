# Настройка и запуск push сервера на стороннем окружении

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2033 — Настройки модуля и сервера очередей](lesson_2033.md)
- [Следующий: 21580 — Переход с Bitrix Push server 1.0 на Bitrix Push server 2.0 →](lesson_21580.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=8609

Для работы *"1С-Битрикс: Управление сайтом"* и *"Битрикс24 в коробке"* рекомендуется использовать

			BitrixVM

                    **«1C-Битрикс: Виртуальная машина»** - бесплатный программный продукт, готовый к немедленному использованию виртуальный сервер, полностью настроенный, протестированный и адаптированный для оптимальной работы как с продуктами «1С-Битрикс», так и с любыми PHP-приложениями. Имеется в версии для Windows и для Unix систем.
[Подробнее...](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37)

		, где всё уже настроено. Если по каким-то причинам использование BitrixVM невозможно, то в используемом окружении необходимо настроить push-сервер и окружение.

### Настройка push-сервера

Настройка push-сервера зависит от используемой ОС. Универсального способа для любой операционной системы не существует. Ниже приведены ссылки на настройки окружений, которые протестированы

			вендором

                    Вендор - это компания, которая разрабатывает и владеет неким ПО, и которая продает лицензии на него другим.
Вендор у "1С-Битрикс: Управление сайтом" и "Битрикс24 в коробке" единый: компания "1С:Битрикс".

		. Если вы используете другие ОС, то настраивать push-сервер вам придётся самостоятельно.

Настройка push-сервера для:

1. [Debian 11](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=2376)
2. [Astra 1.7](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=2381)
3. [SLES 15](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20888)
4. [RedHat8](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20932)
5. [РЕД ОС 8](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=9673)
6. [РЕД ОС 7.3](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=15294)
7. [ALT 8 SP Server](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20410)

### Настройка Redis сервера

Настройка Redis сервера зависит от используемой ОС. Универсального способа для любой операционной системы не существует. Ниже приведены ссылки на настройки окружений, которые протестированы вендором. Если вы используете другие ОС, то настраивать Redis сервер вам придётся самостоятельно.

Настройка Redis для:

1. [Debian 11](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=2374)
2. [Astra 1.7](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=16788)
3. [SLES 15](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20886)
4. [RedHat8](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20930)
5. [РЕД ОС 8](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=9419)
6. [РЕД ОС 7.3](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=15278)
7. [ALT 8 SP Server](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20408)

### Конфигурация NGINX

Настройка NGINX зависит от используемой ОС. Универсального способа для любой операционной системы не существует. Ниже приведены ссылки на настройки окружений, которые протестированы вендором. Если вы используете другие ОС, то настраивать NGINX вам придётся самостоятельно.

Настройка NGINX для:

1. [Debian 11](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=8455)
2. [Astra 1.7](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=5335)
3. [SLES 15](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20878)
4. [RedHat8](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20922)
5. [РЕД ОС 8](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=9227)
6. [РЕД ОС 7.3](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=16824)
7. [ALT 8 SP Server](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=135&LESSON_ID=20400)
