# 7. Использование бета-версии BitrixEnv (7. Enable or disable bitrix-env beta versions)

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8839 — 6. Обновление локального сервера (6. Update server)](lesson_8839.md)
- [Следующий: 9317 — 1. Обновить настройки для всех MySQL-серверов (1. Update settings for all MySQL servers) →](lesson_9317.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=20722

### Бета-версии




**Внимание!** Для операций, описанных в данной главе, необходимы знания администрирования *nix-систем. Перед началом проведения данных операций рекомендуется сделать полный бекап *«Виртуальной машины»*.




При разработке своих решений на основе виртуальной машины *BitrixEnv/VMBitrix.CRM*, может понадобиться отслеживание изменений в ее версиях файлов и новых возможностей. Для этого вы можете включить репозиторий бета-версии *BitrixEnv/VMBitrix.CRM* или подключить репозиторий исходников виртуальной машины и отслеживать все изменения.





**Внимание!**

- Сама бета и ее исходные коды доступны для *BitrixEnv/VMBitrix.CRM*, начиная с **7.3.10**.
- Обратного отката установленной бета-версии *BitrixEnv/VMBitrix.CRM* к стабильной нет. Чтобы перейти на стабильную, нужно дождаться релиза стабильной версии, новее беты, или установить её заново. Например, для бета-версии 7.3.10, нужно ждать стабильную 7.4.









#### Нумерация бета-версий



Мы решили оставить небольшой запас для возможности выпускать стабильные версии. Поэтому беты будут иметь номер выше, чем текущая стабильная *BitrixEnv/VMBitrix.CRM*. Например, текущая – 7.3.2, бета – 7.3.10. До 7.3.10 могут быть выпущены стабильные версии, а с 7.3.10 и выше – беты. Для нового релиза, например 7.4.xx, порядок тот же: до 7.4.10 – стабильные, 7.4.10 и выше – беты и т.д.





#### Функционал бета-версий



Все исправления, дополнения и новый функционал, выпускаемый в бете, выйдет в следующей стабильной версии.





#### Жизненный цикл


Ориентировочно 2-4 месяца, после чего все изменения должны уйти в релиз стабильной версии.






### Включение/выключение



#### Как включить или выключить бета-версию BitrixEnv/VMBitrix.CRM




1. Если у вас стабильная версия машины, вам нужно [обновить BitrixEnv/VMBitrix.CRM](lesson_8839.md) до 7.3.2 или выше.
2. Далее есть 2 пути:

  - **если пул не создан:**

    - **включить**: 2. Configure localhost settings &gt; 7. Enable or disable beta version of bitrix-env &gt; 1. Enable bitrix-env beta versions.
    - **выключить**: 2. Configure localhost settings &gt; 7. Enable or disable beta version of bitrix-env &gt; 1. Disable bitrix-env beta versions.
  - **если пул создан:**
    или:
    Для VMBitrix.CRM (т.к пул создается сразу при установке машины):

    - **включить**: 1. Manage Hosts in the pool &gt; 10. Enable or disable bitrix-env beta versions &gt; 1. Enable bitrix-env beta versions.
    - **выключить**: 1. Manage Hosts in the pool &gt; 10. Enable or disable bitrix-env beta versions &gt; 1. Disable bitrix-env beta versions.

    - **включить**: 2. Configure localhost settings &gt; 7. Enable or disable beta version of bitrix-env &gt; 1. Enable bitrix-env beta versions.
    - **выключить**: 2. Configure localhost settings &gt; 7. Enable or disable beta version of bitrix-env &gt; 1. Disable bitrix-env beta versions.

    - **включить**: 2. Configure localhost settings &gt; 7. Enable or disable beta version of bitrix-env &gt; 1. Enable bitrix-env beta versions
    - **выключить**: 2. Configure localhost settings &gt; 7. Enable or disable beta version of bitrix-env &gt; 1. Disable bitrix-env beta versions
3. Затем необходимо **обязательно обновить пакеты** [через меню машины](lesson_8839.md) либо командой:
  ```
  yum clean all && yum update
  ```






### Бета или стабильный?



#### Как определить, какой репозиторий используется: бета или стабильный?




Выполнить команду:



```

yum clean all
```



В строке со списком репозиториев для беты будет `bitrix-beta`, для стабильной `bitrix`. Например:

```

Cleaning repos: base bitrix-beta bitrix-source epel ...
```







#### Как вернуть стабильную версию


Обратного отката установленной беты к стабильной нет. В этом случае, чтобы перейти на стабильную, нужно дождаться её релиза, новее беты, или установить стабильную версию заново. Например для беты 7.3.10, нужно ждать стабильную версию 7.4.






#### Как получить исходники


Скачать исходники можно так же, как и [исходники стабильной версии](lesson_11161.md).





#### Где посмотреть список изменений


Список изменений публикуется в главе [Что нового?](/learning/course/index.php?COURSE_ID=37&CHAPTER_ID=011219). Обсуждение бета версии происходит [на форуме](https://dev.1c-bitrix.ru/community/forums/forum32/topic112215/).
