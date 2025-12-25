# Практика. Постраничная навигация

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2192 — Практика. Взаимодействие с контроллерами из Javascript](lesson_2192.md)
- [Следующий: 21158 — Практика. Интеграция с модулем REST →](lesson_21158.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2692

Чтобы организовать в аякс-действии постраничную навигацию, нужно в параметрах метода внедрить [\Bitrix\Main\UI\PageNavigation](https://dev.1c-bitrix.ru/api_d7/bitrix/main/ui/pagenavigation/index.php) и вернуть *\Bitrix\Main\Engine\Response\DataType\Page*.

Пример:

```
use \Bitrix\Main\Engine\Response;
use \Bitrix\Main\UI\PageNavigation;
public function listChildrenAction(Folder $folder, PageNavigation $pageNavigation)
{
	$children = $folder->getChildren([
		'limit' => $pageNavigation->getLimit(),
		'offset' => $pageNavigation->getOffset(),
	]);
	return new Response\DataType\Page('files', $children, function() use ($folder) {
		//отложенный подсчет количества всего записей по фильтру
		return $folder->countChildren();
	});
}
```

Чтобы передать номер страницы в JS API, обратите внимание на [navigation](https://dev.1c-bitrix.ru/api_help/js_lib/ajax/bx_ajax_runaction.php).

```
BX.ajax.runAction('vendor:someController.listChildren', {
	data: {
		folderId: 12
	},
	navigation: {
		page: 3
	}
});
```

**Внимание!** В `Response\DataType\Page($id, $items, $totalCount)` **$totalCount** может быть как числом, так и \Closure, которое может быть вычислено отложено. Это сделано из соображений производительности..

Например, для rest вычисление общего количества требуется всегда, а для обычного аякса - это необязательно. Куда производительней и удобнее сделать отдельное аякс-действие для получения количества записей по определенном фильтру.
