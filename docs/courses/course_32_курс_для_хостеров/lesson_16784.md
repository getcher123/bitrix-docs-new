# Установка пакетов

**Навигация**
- [← Оглавление курса](index.md)
- [← Предыдущий: 3743 — Установка и настройка ОС](lesson_3743.md)
- [Следующий: 5335 — Конфигурация Nginx →](lesson_5335.md)

Официальная страница урока: https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=32&LESSON_ID=16784

Весь список пакетов, который нам понадобится для работы *"Битрикс24"* (для *"1С-Битрикс: Управление сайтом"* push сервер не нужен.):




- mariadb
- PHP
- Apache
- nginx
- push-server
- redis




**mariadb**




Подключите репозитории в файле `/etc/apt/sources.list`, добавив запись вида:




```
# Основной репозиторий
deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-main/
1.7_x86-64 main contrib non-free
# Оперативные обновления основного репозитория
deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-update/
1.7_x86-64 main contrib non-free
# Базовый репозиторий
deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-base/
1.7_x86-64 main contrib non-free
# Расширенный репозиторий
deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-extended/
1.7_x86-64 main contrib non-free
# Расширенный репозиторий (компонент astra-ce)
deb https://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-extended/
1.7_x86-64 astra-ce
```




Обновитесь:




```
apt update && apt upgrade
```




Установите необходимые пакеты:




```
apt install mariadb-server mariadb-client
```




**PHP** и **Apache**




Для начала уставите **apache2**:




```
apt install apache2 apache2-dev
```




Рекомендуется использовать PHP 8.0. В дефолтном репозитории его нет и необходимо собрать его самостоятельно.




```
apt install -y lsb-release ca-certificates apt-transport-https software-properties-common gnupg2 \
    autoconf build-essential curl libtool libssl-dev libcurl4-openssl-dev libxml2-dev libreadline7 \
    libreadline-dev libzip-dev libzip4 \
    openssl pkg-config zlib1g-dev libsqlite3-dev sqlite3 libonig-dev \
    libpq-dev git autoconf bison re2c libpng-dev libldap2-dev \
    libfreetype6-dev libfreetype6 libjpeg-dev libxslt1-dev
```




Скачайте исходники:




```
cd /usr/local/src
wget https://www.php.net/distributions/php-8.0.23.tar.gz
cd php-8.0.23

./configure \
        --prefix=/usr \
        --with-config-file-path=/etc/php/8.0 \
        --sysconfdir=/etc/php/8.0 \
        --enable-mysqlnd \
        --with-pdo-mysql \
        --with-pdo-mysql=mysqlnd \
        --enable-bcmath \
        --enable-cli \
        --with-apxs2=/usr/bin/apxs2 \
        --with-fpm-user=www-data \
        --with-fpm-group=www-data \
        --enable-mbstring \
        --enable-phpdbg \
        --enable-shmop \
        --enable-sockets \
        --enable-sysvmsg \
        --enable-sysvsem \
        --enable-sysvshm \
        --with-zlib \
        --with-curl \
        --with-pear \
        --with-openssl \
        --enable-pcntl \
        --enable-gd \
        --with-jpeg \
        --with-mysqli \
        --with-readline \
        --with-freetype \
        --enable-session \
        --with-xsl \
        --with-openssl \
        --enable-opcache

make

make test

make install

cp php.ini-development /etc/php/8.0/php.ini
```




**nginx**




Установите **nginx** (1.18 версия)




```
apt install nginx -y
```




**push-server**




Установите **node** и **npm** (push-server) - 12.22




```
apt install nodejs npm -y
```




**redis**




Установите **redis** - 6.0




```
apt install redis -y
```
