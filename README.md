# Тестовое задание в UТF.tесh
Я создал тестовый json файл с даннымм для проверки, а также сделал скрипт для загрузки этих данных в базу используя DjangoORM.
Для удобства я также опубликовал ```.env```, я понимаю что так делать нельзя😊
## Для проверки понадобится:
Python, Docker Compose и git.
## Шаги для запуска сервера:
1. Клонируйте репозиторий: ```git clone https://github.com/Aserold/test_u.git```
2. Создайте виртуальное окружение в репозитории: ```python -m venv venv``` или на linux - ```python3 -m venv venv```
3. Активируйте его: ```.\venv\Scripts\activate``` или на linux - ```source venv/bin/activate```
4. Установите зависимости: ```pip install -r requirements.txt```
5. Запустите ```docker-compose.yml``` командой: ```docker-compose up -d```
6. Активируйте миграцию в базу данных: ```python manage.py migrate```
7. Запустите скрипт ```insert.py``` для загрузки пробных данных: ```python insert.py```
8. И наконец запустите сервер: ```python manage.py runserver``` и зайдите по ссылке на путь /api/v1/foods/

Надеюсь что я справился с заданием. Жду фидбека!
