import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Прокрутить страницу к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        self.wait_clickable(locator).click()

    @allure.step("Ввести текст «{text}» в элемент {locator}")
    def type_text(self, locator, text):
        self.wait_visible(locator).send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @staticmethod
    @allure.step("Подставить значение «{value}» в шаблон локатора")
    def format_locator(locator, value):
        by, template = locator
        return by, template.format(value)

    @allure.step("Дождаться, что URL содержит «{text}»")
    def wait_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(EC.url_contains(text))

    @allure.step("Дождаться, что URL равен {url}")
    def wait_url_equals(self, url):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url.rstrip("/") == url.rstrip("/")
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
