## Установка и запуск проекта

1. Склонировать репозиторий
```
git clone https://github.com/GHMan2021/task1_ui-tests.git
```
2. Перейти в директорию проекта
3. Создать вируальное окружение
```
python -m venv venv
```
4. Активировать окружение
```
venv\Scripts\activate
```
5. Установка зависимостей
```
pip install -r requirements.txt
```
6. Запуск тестов
```
pytest -n auto --alluredir=allure-results
```
7. Запуск отчета allure по тестам
```
allure serve allure-results
```