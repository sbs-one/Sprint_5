from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Pages
from data import Data
from locators import NavigationPageLocators



class TestNavigation:
    def test_go_to_lk(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            NavigationPageLocators.LK_LINK))
        driver.find_element(*NavigationPageLocators.LK_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationPageLocators.REGISTER_LINK)) is not None

    def test_go_to_constructor(self, driver):
        driver.get(Pages.login_page)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationPageLocators.REGISTER_LINK))
        driver.find_element(*NavigationPageLocators.CONSTRUCTOR_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            NavigationPageLocators.BURGER_HEADER)) is not None

    def test_logout(self, driver):

        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            NavigationPageLocators.LK_LINK))
        driver.find_element(*NavigationPageLocators.LK_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationPageLocators.REGISTER_LINK))
        driver.find_element(*NavigationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            NavigationPageLocators.REGISTER_BUTTON))
        driver.find_element(
            *NavigationPageLocators.NAME_INPUT).send_keys(Data.name)
        driver.find_element(
            *NavigationPageLocators.EMAIL_INPUT).send_keys(Data.email)
        driver.find_element(
            *NavigationPageLocators.PASSWORD_INPUT).send_keys(Data.password)
        driver.find_element(
            *NavigationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            NavigationPageLocators.LOGIN_HEADER))
        driver.find_element(
            *NavigationPageLocators.EMAIL_INPUT).send_keys(Data.email)
        driver.find_element(
            *NavigationPageLocators.PASSWORD_INPUT).send_keys(Data.password)
        driver.find_element(
            *NavigationPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_matches(Pages.home_page))
        driver.find_element(*NavigationPageLocators.LK_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationPageLocators.LOGOUT_BUTTON))
        driver.find_element(*NavigationPageLocators.LOGOUT_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.url_matches(Pages.login_page)) is not None
