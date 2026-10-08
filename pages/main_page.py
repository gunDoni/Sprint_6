import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
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
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self, locator):
        self.click(locator)
