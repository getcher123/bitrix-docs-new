# Практика. Внедрение зависимостей

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 21158 — Практика. Интеграция с модулем REST](lesson_21158.md)
- [Следующий: 13766 — Маршруты →](lesson_13766.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=21162

### Скалярные и нескалярные параметры

Рассмотрим на примере ajax-действие, в котором есть параметры:

```

public function renameUserAction($userId, $newName = 'guest', array $groups = array(2))
{
	$user = User::getById($userId);
	...
	$user->rename($newName);

	return $user;
}
```

### Как будут получены параметры метода?

Скалярные параметры `$userId`, `$newName`, `$groups` будут получены автоматически из `REQUEST`.

- Сопоставление **регистрозависимое**.
- Если поиск не удался, но есть значение по умолчанию - оно будет использовано.
- Сначала поиск в `$_POST`, после в `$_GET`.

Если параметр не удалось найти, то действие не будет запущено, сервер пошлёт ответ с сообщением об ошибке, что не указан обязательный параметр.

### Как внедрить объекты (нескалярные параметры)?

По умолчанию внедрить можно:

- \Bitrix\Main\Engine\[CurrentUser](https://dev.1c-bitrix.ru/api_d7/bitrix/main/engine/currentuser/index.php)
- \Bitrix\Main\UI\[PageNavigation](lesson_2692.md)
- \CRestServer

При этом имя параметра может быть произвольное. Связывание идёт по классу:

```

public function listChildrenAction(Folder $folder, PageNavigation $pageNavigation);
public function listChildrenAction(Folder $folder, PageNavigation $navigation);
public function listChildrenAction(Folder $folder, PageNavigation $nav, \CRestServer $restServer);
```

### Внедрение своих типов

Начнем с примера:

```

class Folder extends Controller
{
	public function renameAction($folderId)
	{
		$folder = Folder::getById($folderId);
		if (!$folder)
		{
			return null;
		}
		...
	}

	public function downloadAction($folderId)
	{
		$folder = Folder::getById($folderId);
		...
	}

	public function deleteAction($folderId)
	{
		$folder = Folder::getById($folderId);
		...
	}
}
```

У нас есть обычный ajax-контроллер для некой папки `Folder`. Но все действия у нас в итоге производятся над объектом и везде у нас идёт попытка загрузки папки и т.д. Было бы здорово получать на вход метода сразу `Folder $folder`.

```

class Folder extends Controller
{
	public function renameAction(Folder $folder);
	public function downloadAction(Folder $folder);
	public function deleteAction(Folder $folder);
}
```

И теперь это возможно:

```

class Folder extends Controller
{
	public function getPrimaryAutoWiredParameter()
	{
		return new ExactParameter(
			Folder::class, //полное имя класса подклассы, которого нужно создавать
			'folder', //конкретное имя параметра, который будет внедряться
			function($className, $id){ //функция, которая создаст объект для внедрения. На вход приходит конкретный класс и $id
				return Folder::loadById($id);
			}
		);
	}
}
```

В js вызов:

```

BX.ajax.runAction('folder.rename', {
	data: {
		id: 1
	}
});
```

Важно, в создающем замыкании после `$className` можно указывать сколько угодно параметров, которые требуются для создания объекта. При этом они будут связываться с данными из `$_REQUEST` так же, как и скаляры в обычных методах-действиях.

```

class Folder extends Controller
{
	public function getPrimaryAutoWiredParameter()
	{
		return new ExactParameter(
			Folder::class,
			'folder',
			function($className, $entityId, $entityType){
				return $className::buildByEntity($entityId, $entityType);
			}
		);
	}

	public function workAction(Folder $folder);
}
```

В js вызов:

```

BX.ajax.runAction('folder.work', {
	data: {
		entityId: 1,
		entityType: 'folder-type'
	}
});
```

Если требуется описать несколько параметров, которые нужно создавать:

```

class Folder extends Controller
{
	/**
	 * @return Parameter[]
	 */
	public function getAutoWiredParameters()
	{
		return [
			new ExactParameter(
				Folder::class,
				'folder',
				function($className, $id){
					return $className::loadById($id);
				}
			),
			new ExactParameter(
				File::class,
				'file',
				function($className, $fileId){
					return $className::loadById($fileId);
				}
			),
		];
	}

	public function workAction(Folder $folder, File $file);
}
```

Есть ещё обобщенный способ описания внедрений:

```

new \Bitrix\Main\Engine\AutoWire\Parameter(
	Folder::class,
	function($className, $mappedId){
		return $className::buildById($mappedId);
	}
);
```

Чуть подробнее: сначала объявили имя класса, подклассы которого мы будем пытаться создавать, когда встретим их в ajax-действиях. Анонимная функция будет заниматься созданием экземпляра.

- `$className` - это конкретное имя класса, которое указано в type-hinting'e.
- `$mappedId` - это значение, которое получено из `$_REQUEST`. При этом в `$_REQUEST` будет искаться `folderId`. Имя параметра, который мы будем искать в `$_REQUEST`, по умолчанию создается как `{имя переменной} + Id`.
