import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver

random_digits = ''.join(random.choices(string.digits, k=5))
email = f'stepan_shalagin_6345402_{random_digits}@yandex.ru'

def test_go_to_lk(driver):
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))


def test_go_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(By.XPATH, ' //p[contains(text(),"Конструктор")]').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')))

def test_logout(driver):
    #Проверяем первую страницу и нажимаем на Личный кабинет
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
    #Переходим на страницу Регистрации
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(
        By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']").send_keys('stepan')
    driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(
        By.CSS_SELECTOR, "input[name='Пароль']").send_keys('123456')
    driver.find_element(
        By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()
    #Заходим по созданному аккаунту
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Вход')]")))
    driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(
        By.XPATH, '//input[@type="password" and @name="Пароль"]').send_keys('123456')
    driver.find_element(
        By.XPATH, '//button[contains(text(), "Войти")]').click()
    #Проверяем логин
    WebDriverWait(driver, 3).until(expected_conditions.url_matches("https://stellarburgers.nomoreparties.site/"))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Выход')]")))
    driver.find_element(By.XPATH, '//button[contains(text(),"Выход")]').click()
    WebDriverWait(driver, 3).until(expected_conditions.url_matches("https://stellarburgers.nomoreparties.site/login"))