# BX.UI.StepProcessing.ProcessManager

Источник: https://dev.1c-bitrix.ru/api_d7/bitrix/ui/stepprocessing/javascript_api/process_manager.php

Реестр экземпляров процессов на странице.

| Название | Описание |
| --- | --- |
| **static create(props: ProcessOptions): Process** | Создает новый инстанс объекта класса [Process](process.php.md). Входные параметры [ProcessOptions](types.php.md). |
| **static get(id: string): ?Process** | Возвращает инстанс объекта класса [Process](process.php.md) по его уникальному коду в рамках страницы. |
| **static has(id: string): boolean** | Проверяет наличие объекта, соответствующего коду. |
| **static delete(id: string): void** | Удаляет объект процесса, соответствующего коду. |
