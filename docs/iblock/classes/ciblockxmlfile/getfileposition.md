# GetFilePosition


```
int
CIBlockXMLFile::GetFilePosition(
);
```

Метод возвращает объем прочитанных байт. Нестатический метод.


#### Параметры вызова

Отсутствуют.
#### Смотрите также


- [CIBlockXMLFile](index.md)


#### Примеры использования


```
if ($obXMLFile->ReadXMLToDatabase($fp, $NS, 10, 1024) ) {
	echo 'Файл прочитан полностью.';
} else {
	echo 'Файл прочитан не полностью: '.round($obXMLFile->GetFilePosition()/$total*100, 2).'%.';
}
```


```
//пример пошагового разбора файла:
echo 'Парсим файл';
	$NS = &$_SESSION["BX_IMPORT_NS"];
	$ABS_FILE_NAME = $DOCUMENT_ROOT."/upload/TakeMe.xml";
	$total = filesize($ABS_FILE_NAME);
	if($fp = fopen($ABS_FILE_NAME, "rb")) {
		// Чтение содержимого файла шагом в 10 секунд
		if ($obXMLFile->ReadXMLToDatabase($fp, $NS, 10, 1024) ) {
			echo 'Файл прочитан полностью.';
		} else {
			echo 'Файл прочитан не полностью: '.round($obXMLFile->GetFilePosition()/$total*100, 2).'%.';
		}
		fclose($fp);
	} else {
		// Файл открыть не удалось
		echo "Ошибка открытия файла";
	}
```
