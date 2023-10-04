from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Pages
from locators import LoginPageLocators


class TestLogin:

    def test_login_by_enter_by_account(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)) is not None

    def test_login_by_personal_kabinet(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            LoginPageLocators.PERSONAL_KABINET_LINK))
        driver.find_element(*LoginPageLocators.PERSONAL_KABINET_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            LoginPageLocators.REGISTER_LINK)) is not None

    def test_login_by_registration_form(self, driver):
        driver.get(Pages.reg_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            LoginPageLocators.REGISTER_BUTTON))
        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            LoginPageLocators.LOGIN_BUTTON)) is not None

    def test_login_by_forget_password(self, driver):
        driver.get(Pages.password_recovery_page)
        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            LoginPageLocators.LOGIN_BUTTON)) is not None
