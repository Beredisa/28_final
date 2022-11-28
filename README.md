Введение
------------

Этот репозиторий содержит базовые тесты для страницы авторизации Ростелеком ИТ ttps://b2c.passport.rt.ru .
Тесты разработаны с использованием шаблона  PageObject с Selenium и Python (PyTest + Selenium).
Разработчик : Оксана Бреде 

Файлы
-----

[pages/conftest.py](../../28_final/pages/conftest.py) содержит код для отлова падающих тестов

[pages/base.py](pages/base.py) содержит PageObject pattern для Python.

[pages/rostelecom.py](pages/rostelecom.py) содержит web elements (селекторы) на страницах

[tests/*](tests) содержит Web UI тесты для  страницы авторизации Ростелеком ИТ ttps://b2c.passport.rt.ru .




Как запустить тесты
----------------

1) Установите все зависимости:

    ```bash
    pip3 install -r requirements.txt
    ```


2) Запустите тесты:

    ```bash
    py -m pytest -v --driver Chrome --driver-path chromedriver.exe tests
    ```


