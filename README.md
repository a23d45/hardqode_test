# Тестовое задание HardQode

## Установка
Для запуска приложения требуется Python и установленный пакетный менеджер pip. Следуйте инструкциям ниже, чтобы установить зависимости и запустить приложение:

**1. Клонируйте репозиторий на свой компьютер:**
```
git clone https://github.com/a23d45/hardqode_test.git
```
**2. Перейдите в директорию проекта**

*Создайте виртуальное окружение:*
```
python -m venv venv
```
*Активируйте виртуальное окружение:*

**Windows:**
```
venv\Scripts\activate
```
**macOS и Linux:**
```
source env/bin/activate
```
**3. Установите зависимости:**
```
pip install -r requirements.txt
```
**4. Выполните миграции**
```
python manage.py makemigrations

python manage.py migrate
```
**5. Запустите локальный сервер**
```
python manage.py runserver
```
**6. Заполните базу данных тестовыми значениями**
```
python manage.py fill_db
```
___
## Эндпоинты:
+ GET products/ - получение списка продуктов
+ GET lessons/<int:student_id>/<int:product_id>/ - получение списка уроков по продукту для пользователя
+ POST add_student_to_product/ - добавление студента к продукту. Передается user_id и product_id
