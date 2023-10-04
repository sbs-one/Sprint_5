from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ConstructorPageLocators


class TestConstructorNavigation:

    def test_constructor_navigation_to_adds(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.HEADER))
        driver.find_element(*ConstructorPageLocators.ADDS_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.MEAT_DESCRIPTION)) is not None

    def test_constructor_navigation_to_sous(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.HEADER))
        driver.find_element(*ConstructorPageLocators.SOUS_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.SPICY_X_DESCRIPTION)) is not None

    def test_constructor_navigation_to_bread(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.HEADER))
        driver.find_element(*ConstructorPageLocators.ADDS_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.MEAT_DESCRIPTION))
        driver.find_element(*ConstructorPageLocators.BREAD_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorPageLocators.R2D3_DESCRIPTION)) is not None
