Проект "Employee Lunch"

Запуск проекта через Docker
Требования
- Docker
- Docker Compose
- 
Клонирование репозитория
git clone git@github.com:Denys-Bezsmertnyi/lunch_program.git
cd employee_lunch

Настройка .env файла
Создайте файл .env в корне проекта и добавьте следующие переменные:
DB_NAME=MYDB
DB_USER=SADMIN
DB_PASSWORD=123
DB_HOST=db
DB_PORT=5432
SECRET_KEY=SECRET_KEY
DEBUG=True

Запуск Docker Compose
docker-compose up --build

Применение миграций
docker-compose exec web python manage.py migrate

Создание суперпользователя
docker-compose exec web python manage.py createsuperuser

