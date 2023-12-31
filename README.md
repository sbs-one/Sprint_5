# Selenium Тесты для StellarBurgers

Этот репозиторий содержит автоматизированные тесты, написанные с использованием библиотеки Selenium, для веб-приложения StellarBurgers.

## Описание

Проект содержит тесты, которые проверяют навигацию по разным страницам веб-приложения StellarBurgers, а также тесты для регистрации, входа в аккаунт и другие сценарии использования.

## Структура проекта

- `conftest.py`: Файл с фикстурой для инициализации веб-драйвера и открытия веб-сайта перед выполнением тестов.
- `test_navigation.py`: Тесты для навигации по разным страницам приложения.
- `test_login.py`: Тесты для входа в аккаунт и связанных сценариев.
- `test_registration.py`: Тесты для регистрации пользователей.
- `test_logout.py`: Тесты для выхода из аккаунта.
- `test_incorrect_password.py`: Тесты для проверки входа с неправильным паролем.

## Запуск тестов

1. Убедитесь, что у вас установлен Python и библиотека Selenium.
2. Запустите тесты с помощью команды, например:

   ```shell
   pytest test_navigation.py
# Sprint_5
