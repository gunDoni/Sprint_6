import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть вопрос №{index} в блоке «Вопросы о важном»")
    def click_question(self, index):
        by, value = MainPageLocators.QUESTION_HEADING
        value = value.format(index)
        self.driver.find_element(by, value).click()

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        by, value = MainPageLocators.QUESTION_PANEL
        value = value.format(index)
        return self.driver.find_element(by, value).text

    @allure.step("Принять куки")
    def accept_cookies(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.COOKIE_BUTTON
            )
        ).click()

    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        ).click()
