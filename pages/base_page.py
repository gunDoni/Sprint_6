import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.wait_clickable(locator).click()

    def type_text(self, locator, text):
        self.wait_visible(locator).send_keys(text)
