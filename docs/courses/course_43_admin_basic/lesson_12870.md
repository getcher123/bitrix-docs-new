# События и кастомные типы свойств

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 12868 — Чтение и запись](lesson_12868.md)
- [Следующий: 23152 — Наследование →](lesson_23152.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=12870

#### События

Для подписи на события сущности инфоблоков можно использовать штатные механизмы ORM:

```
use Bitrix\Main\ORM\Data\DataManager;

// ID инфоблока
$iblockId = 32;

// объект инфоблока
$iblock = \Bitrix\Iblock\Iblock::wakeUp($iblockId);

// диспетчер событий
$em = \Bitrix\Main\ORM\EventManager::getInstance();

$em->registerEventHandler(
	$iblock->getEntityDataClass(),
	DataManager::EVENT_ON_BEFORE_ADD,
	'mymodule',
	'MyClass',
	'method'
);
```

**Внимание**! Поддержка событий информационных блоков, относящихся к старому ядру, в данный момент **не реализована**.

#### Кастомные типы свойств

Чтобы добавить свои поля в сущность свойства, при описании свойства нужно задать отдельный коллбэк **GetORMFields**:

```
public static function GetUserTypeDescription()
{
	return [
	 ...
	"GetORMFields" => array(__CLASS__, "GetORMFields"),
	];
}

/**
 * @param \Bitrix\Main\ORM\Entity $valueEntity
 * @param \Bitrix\Iblock\Property $property
 */
public static function GetORMFields($valueEntity, $property)
{
	$valueEntity->addField(
	...
	);
}
```
