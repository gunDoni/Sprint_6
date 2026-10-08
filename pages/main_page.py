import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть вопрос №{index} в блоке «Вопросы о важном»")
    def click_question(self, index):
        self.click(self.format_locator(MainPageLocators.QUESTION_HEADING, index))

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        return self.get_text(
            self.format_locator(MainPageLocators.QUESTION_PANEL, index)
        )

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self, locator):
        self.click(locator)
