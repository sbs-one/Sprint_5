import random
import string

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from data import Pages
from locators import RegistrationPageLocators


class TestRegistration:

    @pytest.fixture
    def random_email(self):
        random_digits = ''.join(random.choices(string.digits, k=5))
        return f'stepan_shalagin_6345402_{random_digits}@yandex.ru'

    def test_registration(self, driver, random_email):

        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            RegistrationPageLocators.LK_LINK))
        driver.find_element(*RegistrationPageLocators.LK_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            RegistrationPageLocators.REGISTER_LINK))
        driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            RegistrationPageLocators.REGISTER_BUTTON))
        driver.find_element(
            *RegistrationPageLocators.NAME_INPUT).send_keys(Data.name)
        driver.find_element(
            *RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(
            *RegistrationPageLocators.PASSWORD_INPUT).send_keys(Data.password)
        driver.find_element(
            *RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            RegistrationPageLocators.LOGIN_HEADER))
        driver.find_element(
            *RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(
            *RegistrationPageLocators.PASSWORD_INPUT).send_keys(Data.password)
        driver.find_element(
            *RegistrationPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_matches(Pages.home_page))
        driver.find_element(*RegistrationPageLocators.LK_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_value(
            RegistrationPageLocators.LOGIN_INPUT, random_email)) is not None

    def test_incorrect_password(self, driver, random_email):

        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            RegistrationPageLocators.LK_LINK))
        driver.find_element(*RegistrationPageLocators.LK_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            RegistrationPageLocators.REGISTER_LINK))
        driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            RegistrationPageLocators.REGISTER_BUTTON))
        driver.find_element(
            *RegistrationPageLocators.NAME_INPUT).send_keys(Data.name)
        driver.find_element(
            *RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(
            *RegistrationPageLocators.PASSWORD_INPUT).send_keys(Data.password)
        driver.find_element(
            *RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            RegistrationPageLocators.LOGIN_HEADER))
        driver.find_element(
            *RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(
            *RegistrationPageLocators.PASSWORD_INPUT).send_keys(Data.wrong_password)
        driver.find_element(
            *RegistrationPageLocators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.url_matches(Pages.login_page)) is not None
