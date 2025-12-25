# AddPanelButtons


```
CIBlock::AddPanelButtons(
	string mode,
	string componentName,
	array arButtons
);
```

Метод добавляет в панель управления кнопки, отвечающие за управление элементами инфоблока (в методе производится вызов CMain::AddPanelButton). Нестатический метод.


#### Параметры вызова


| Параметр | Описание |
| --- | --- |
| mode | Режим отображения административной панели. Возвращается методом CMain::GetPublicShowMode. |
| componentName | Название компонента, который регистрирует кнопки. Возвращается методом CBitrixComponent::GetName. |
| arButtons | Массив кнопок, которые можно зарегистрировать с учётом текущих прав пользователя. Формируется методом [CIBlock::GetPanelButtons](getpanelbuttons.md). |


#### Смотрите также


- CMain::AddPanelButton
- CMain::GetPublicShowMode
- CBitrixComponent::GetName
- [CIBlock::GetPanelButtons](getpanelbuttons.md)
