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

    def get_text(self, locator):
        return self.wait_visible(locator).text

    @staticmethod
    def format_locator(locator, value):
        by, template = locator
        return by, template.format(value)

    def wait_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(EC.url_contains(text))

    def wait_url_equals(self, url):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url.rstrip("/") == url.rstrip("/")
        )

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
