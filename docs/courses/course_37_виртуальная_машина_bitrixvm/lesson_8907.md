# Скрипт работы с провайдерами

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 8905 — Провайдеры](lesson_8905.md)
- [Следующий: 30542 — Веб-кластер: конфигурация, бэкапы, восстановление →](lesson_30542.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8907

Данный скрипт нужен для встраивания [плагинов провайдеров](lesson_8905.md) в web- интерфейс продуктов «1C-Битрикс».




На текущий момент реализованы следующие методы:



- **list** - отображает список всех провайдеров, для которых существуют подкаталоги в директории /opt/webdir/providers на машине:
  ```
  {
    "params": {
      "providers": {
        "superprovider": {
          "status": "enabled"
        },
        "amazon": {
          "error": 1,
          "message": "bxProvider::optionsProvider: Provider amazon not exist on the host"
        }
      }
    }
  }
  ```
  В данном случае, это только включено или выключено, а так же ошибки, который возникли при запросе статуса.
  В случае если провайдеров нет на хосте, список будет пустым:
  ```
  {
    "params": {
      "providers": {
      }
    }
  }
  ```
- **status** - покажет статус для провайдера:
  ```
  /opt/webdir/bin/bx-provider -a status --provider superprovider -o json
  {
    "params": {
      "provider_options": {
        "superprovider": {
          "options": {
            "order_status": 1,
            "order": 1,
            "help": 1,
            "configs": 1,
            "init": 0
          },
          "status": "enabled",
          "files": {
            "execute": "/opt/webdir/providers/superprovider/bin/superprovider",
            "holder": "/opt/webdir/providers/superprovider",
            "config": "/opt/webdir/providers/superprovider/etc/superprovider.conf"
          },
          "name": "superprovider",
          "config": "exists"
        }
      }
    }
  }
  ```
  В данном случае печатает внутреннюю информацию (используется как есть внутри обработчика), по сути, такой статус больше подходит для отладки работы провайдера, чем для использования в web-интерфейсе.
- **install** и **uninstall** - создает/удаляет данные для провайдера (на текущий момент больше для отладки, возможно, в дальнейшем с помощью этих методов хостеры смогут установить свой плагин на сервер и удалить его):
  ```
  /opt/webdir/bin/bx-provider -a install --provider amazon --archive /tmp/amazon-v01.tar.gz
  ```
- **configs** - отображает список всех конфигураций провайдера:
  ```
  /opt/webdir/bin/bx-provider -a configs --provider superprovider -o json
  {
    "params": {
      "provider_configs": {
        "superprovider": {
          "configurations": [
            {
              "id": "1",
              "descr": "Bitrix-env, 1 month, Centos-6 x86_64, CPU 2x1.0 Ghz, Memory 1Gb, HDD 20Gb"
            }
          ],
          "status": "enabled"
        }
      }
    }
  }
  ```
- **order** - заказывает виртуальный сервер или VPS:
  ```
  /opt/webdir/bin/bx-provider -a order --provider superprovider --config_id 1 -o json
  {
    "params": {
      "provider_order": {
        "superprovider": {
          "task_id": "25"
        }
      }
    }
  }
  ```
- **order_status** - отображает статус заказа:
  ```
  /opt/webdir/bin/bx-provider -a order_status --provider superprovider --task_id 25 -o json
  {
    "params": {
      "provider_order": {
        "superprovider": {
          "server_password": "XXXXXXXXXXXXXXX",
          "status": "complete",
          "server": "xxx.xxx.xxx.xxx"
          "task_id": "25"
        }
      }
    }
  }
  ```
- **orders_list** - список всех заказов, сделанных на хосте:
  ```
  /opt/webdir/bin/bx-provider -a orders_list --provider superprovider -o json
  {
    "params": {
      "provider_order_list": {
        "superprovider": {
          "25": {
            "status": "finished",
            "mtime": 1403445981,
            "error": 0,
            "message": ""
          },
          "22": {
            "status": "error",
            "mtime": 1403441000,
            "error": 1,
            "message": "cannot add ssh key to the server"
          },
          "21": {
            "status": "complete",
            "mtime": 1403440979,
            "error": 0,
            "message": ""
          },
          "23": {
            "status": "finished",
            "mtime": 1403441229,
            "error": 0,
            "message": ""
          }
        }
      }
    }
  }
  ```
  Тут добавлен еще один статус по задаче: **complete** - это значит, что сервер из данного задания был добавлен в пул.
- **order_to_host** - запускает процедуру добавления сервера в пул с параметрами, переданными в статусе заказа:
  ```
  /opt/webdir/bin/bx-provider -a order_to_host --provider superprovider --task_id 25 -o json
  ```
