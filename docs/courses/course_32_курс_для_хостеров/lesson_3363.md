# Дополнительные рекомендации для двухуровневой конфигурации

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3362 — Сжатие страниц](lesson_3362.md)
- [Следующий: 3364 — Достигнутые результаты →](lesson_3364.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=3363

По умолчанию, при работе в двухуровневой конфигурации, в качестве адреса клиента будет указываться адрес, на котором работает *NGINX* или другой акселератор. Для правильной работы модуля статистики необходимо обеспечить передачу реального IP адреса с **Front-end** в **Back-end**.




Например, для *NGINX* используется следующая технология: сервер *NGINX* устанавливает специальный заголовок в запросе, а специальный модуль *Apache* (*rpaf* или *real_ip*) учитывает этот заголовок вместо стандартного.




Если же такой модуль не установлен, то вы можете сами изменить адрес клиента. Например, если адрес клиента передается в переменной `HTTP_X_FORWARDED_FOR` (так делает прокси-сервер SQUID) или `HTTP_X_REAL_IP`, то для замены переменной в продукте необходимо в файле **/bitrix/php_interface/dbconn.php** вставить подобный пример кода:




```

if(isset($_SERVER['HTTP_X_FORWARDED_FOR']) || isset($_SERVER['HTTP_X_REAL_IP'])) {
    foreach(array('HTTP_X_FORWARDED_FOR', 'HTTP_X_REAL_IP') as $key => $value) {
        if(
            isset($_SERVER[$value])
            &&  strlen($_SERVER[$value]) > 0
            &&  strpos($_SERVER[$value], "127.") !== 0
        ) {
            if($p = strrpos($_SERVER[$value], ","))
            {
                $_SERVER["REMOTE_ADDR"] = $REMOTE_ADDR = trim(substr($_SERVER[$value], $p+1));
                $_SERVER["HTTP_X_FORWARDED_FOR"] = substr($_SERVER[$value], 0, $p);
            }
            else
                $_SERVER["REMOTE_ADDR"]= $REMOTE_ADDR = $_SERVER[$value];

            break;
        }
    }
}
```



Кроме того, в конфигурации *Apache* на *Back-end* желательно отключить `KeepAlive`. Поскольку **Front-end** находится или на этой машине, или "рядом", более быстрое высвобождение ресурсов предпочтительнее.
