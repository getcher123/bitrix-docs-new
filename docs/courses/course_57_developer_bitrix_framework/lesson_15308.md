# Работа с пользовательским полем сотрудника из БП

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 2172 — Вычисление ID начальника](lesson_2172.md)
- [Следующий: 1898 — Получение списка пользователей →](lesson_1898.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=57&LESSON_ID=15308

|  | ### Работа с пользовательскими полями |
| --- | --- |




Имеется пользовательское поле объекта USER типа данных «Привязка к сотруднику». Как  вставить данные из поля внутрь бизнес процесса:




```
$documentService = $this->workflow->getService('DocumentService');
$document = $documentService->getDocument($this->getDocumentId());

$userId = CBPHelper::ExtractUsers($document['CREATED_BY'], $this->getDocumentId(), true);


$filter = ['ID' => $userId];
$params['SELECT'] = ['UF_поле'];

$listResult = CUser::GetList('id', 'asc', $filter, $params);

if ($row = $listResult->fetch())
{
    if (is_numeric($row['UF_поле']) && $row['UF_поле'] > 0)
    {
        $this->SetVariable('MyVar', 'user_' . $row['UF_поле']);
    }
}
```
