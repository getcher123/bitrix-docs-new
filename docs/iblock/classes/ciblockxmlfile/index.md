# CIBlockXMLFile


### Описание и список методов

**CIBlockXMLFile** - класс для работы с файлами XML.


#### Методы класса


| Метод | Описание | С версии |
| --- | --- | --- |
| [DropTemporaryTables](droptemporarytables.md) | Удаляет таблицы, содержащие ранее загруженный файл. | 6.5.0 |
| [GetFilePosition](getfileposition.md) | Возвращает объем прочитанных байт. | 6.5.0 |
| [CreateTemporaryTables](createtemporarytables.md) | Создает таблицы для загрузки XML. | 6.5.0 |
| [ReadXMLToDatabase](readxmltodatabase.md) | Загрузка данных из файла в таблицы БД (пошаговая). | 6.5.0 |
| [IndexTemporaryTables](indextemporarytables.md) | Индексация таблиц для ускорения доступа. | 6.5.0 |
| [safeUnZip](safeunzip.md) | Метод распаковывает ZIP-архив из файла *fileName*. | 23.100.0 |

---
### Примеры использования


```
<?
$obXMLFile = new CIBlockXMLFile;
// Удаляем результат предыдущей загрузки
$obXMLFile->DropTemporaryTables();
// Подготавливаем БД
if(!$obXMLFile->CreateTemporaryTables())
	return "Ошибка создания БД.";
if($fp = fopen($FILE_NAME, "rb"))
{
	// Чтение содержимого файла за один шаг
	$obXMLFile->ReadXMLToDatabase($fp, $NS, 0);
	fclose($fp);
}
else
{
	// Файл открыть не удалось
	return "Ошибка открытия файла";
}
// Индексируем загруженные данные для ускорения доступа
if(!CIBlockXMLFile::IndexTemporaryTables())
	return "Ошибка создания индексов БД.";
?>
```

---




| ![image](../images/7dd82aba60.gif) 1 **dpechurkin**12.05.2017 18:11:53 |  |  |
| --- | --- | --- |
| $obXMLFile = new CIBlockXMLFile(#нужное название таблицы#) в данный момент у класса такой конструктор \| Код \| \| --- \| \| ``` function __construct($table_name = "b_xml_tree") { $this->_table_name = strtolower($table_name); if (defined("BX_UTF")) { if (function_exists("mb_orig_strpos") && function_exists("mb_orig_strlen") && function_exists("mb_orig_substr")) $this->_get_xml_chunk_function = "_get_xml_chunk_mb_orig"; else $this->_get_xml_chunk_function = "_get_xml_chunk_mb"; } else { $this->_get_xml_chunk_function = "_get_xml_chunk"; } } ``` \| Отсюда следует что если передать при объявлении экземпляра класса параметр с новым названием таблицы можно реализовать многопоточную загрузку xml файлов. | Код | ``` function __construct($table_name = "b_xml_tree") { $this->_table_name = strtolower($table_name); if (defined("BX_UTF")) { if (function_exists("mb_orig_strpos") && function_exists("mb_orig_strlen") && function_exists("mb_orig_substr")) $this->_get_xml_chunk_function = "_get_xml_chunk_mb_orig"; else $this->_get_xml_chunk_function = "_get_xml_chunk_mb"; } else { $this->_get_xml_chunk_function = "_get_xml_chunk"; } } ``` |
| Код |  |  |
| ``` function __construct($table_name = "b_xml_tree") { $this->_table_name = strtolower($table_name); if (defined("BX_UTF")) { if (function_exists("mb_orig_strpos") && function_exists("mb_orig_strlen") && function_exists("mb_orig_substr")) $this->_get_xml_chunk_function = "_get_xml_chunk_mb_orig"; else $this->_get_xml_chunk_function = "_get_xml_chunk_mb"; } else { $this->_get_xml_chunk_function = "_get_xml_chunk"; } } ``` |  |  |
|  |  |  |
