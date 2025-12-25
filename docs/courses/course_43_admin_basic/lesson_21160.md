# Практика. Советы

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 14014 — Контроллеры и компонент](lesson_14014.md)
- [Следующий: 2192 — Практика. Взаимодействие с контроллерами из Javascript →](lesson_2192.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=21160

Для удобной отладки ошибок в жизненном цикле AJAX включайте `debug => true` в `.settings.php`, тогда вы сможете увидеть трейс ошибок, исключений.

### Если нужно:

- отдать файл, то воспользуйтесь классами *\Bitrix\Main\Engine\Response\File* и *\Bitrix\Main\Engine\Response\BFile*:
  ```
  class Controller extends Engine\Controller
  	{
  	public function downloadAction($orderId)
  		{
  		//... find attached fileId by $orderId
  			return \Bitrix\Main\Engine\Response\BFile::createByFileId($fileId);
  		}
  	public function downloadGeneratedTemplateAction()
  		{
  		//... generate file ... $generatedPath
  		return new \Bitrix\Main\Engine\Response\File(
  			$generatedPath,
  			'Test.pdf',
  			\Bitrix\Main\Web\MimeType::getByFileExtension('pdf')
  		);
  		}
  	public function showImageAction($orderId)
  		{
  		//... find attached imageId by $orderId
  		return \Bitrix\Main\Engine\Response\BFile::createByFileId($imageId)
  			->showInline(true)
  		;
  		}
  	}
  ```
- отдать отресайзенное изображение, то используйте *\Bitrix\Main\Engine\Response\ResizedImage*.
  > Помните, что нельзя давать пользователю запрашивать произвольные размеры для ресайза. Всегда подписывайте параметры или явно указывайте в коде размеры.
  ```
  class Controller extends Engine\Controller
  	{
  	public function showAvatarAction($userId)
  		{
  		//... find attached imageId by $userId
  		return \Bitrix\Main\Engine\Response\ResizedImage::createByImageId($imageId, 100, 100);
  		}
  	}
  ```
- сгенерировать ссылку в контроллере на действие из этого же контроллера, то используйте *\Bitrix\Main\Engine\Controller::getActionUri*
  ```
  public function getAction(File $file)
  	{
  		return [
  			'file' => [
  				'id' => $file->getId(),
  				'name' => $file->getName(),
  				'links' => [
  					'rename' => $this->getActionUri('rename', array('fileId' => $file->getId())),
  				]
  			]
  		];
  	}
  public function renameAction(File $file)
  	{
  		...
  	}
  ```
- сгенерировать ссылку в контроллере на действие, которое будет отдавать контент, например, скачивание файла, то используйте *\Bitrix\Main\Engine\Response\DataType\ContentUri*. Это нужно для интеграции с модулем REST.
  ```
  public function getAction(File $file)
  	{
  		return [
  			'file' => [
  			'id' => $file->getId(),
  			'name' => $file->getName(),
  			'links' => [
  				'download' => new ContentUri($this->getActionUri('download', array('fileId' => $file->getId()))),
  				]
  			]
  		];
  	}
  public function downloadAction(File $file)
  	{
  		...
  	}
  ```
- преобразовать данные `SNAKE_CASE` по стандарту в `camelCase`, то можно воспользоваться вспомогательными методами контроллера *\Bitrix\Main\Engine\Controller::convertKeysToCamelCase*, либо явной настройкой *\Bitrix\Main\Engine\Response\Converter*:
  ```
  public function getAction(File $file)
  	{
  		return [
  			'file' => $this->convertKeysToCamelCase($fileData)
  		];
  	}
  public function showInformationAction(File $file)
  	{
  		$converter = new \Bitrix\Main\Engine\Response\Converter(Converter::OUTPUT_JSON_FORMAT & ~Converter::RECURSIVE);
  		return $converter->process($data);
  	}
  ```
