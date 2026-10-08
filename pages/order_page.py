import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    # --- Экран 1: «Для кого самокат» ---
    @allure.step("Ввести имя: {name}")
    def set_name(self, name):
        self.type_text(OrderPageLocators.NAME_INPUT, name)

    @allure.step("Ввести фамилию: {surname}")
    def set_surname(self, surname):
        self.type_text(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step("Ввести адрес: {address}")
    def set_address(self, address):
        self.type_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Ввести телефон: {phone_number}")
    def set_phone_number(self, phone_number):
        self.type_text(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

    @allure.step("Открыть список станций метро")
    def click_metro_button(self):
        self.click(OrderPageLocators.METRO_BUTTON)

    @allure.step("Выбрать станцию метро (value={num_val})")
    def select_metro(self, num_val):
        by, value = OrderPageLocators.LIST_OF_METRO
        self.click((by, value.format(num_val)))

    @allure.step("Заполнить первый экран формы заказа")
    def fill_form(self, name, surname, address, phone_number, num_val):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_button()
        self.select_metro(num_val)
        self.set_phone_number(phone_number)

    @allure.step("Нажать «Далее»")
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    # --- Экран 2: «Про аренду» ---
    @allure.step("Ввести дату доставки: {date}")
    def set_delivery_date(self, date):
        self.wait_visible(OrderPageLocators.DELIVERY_DATE).send_keys(
            date, Keys.ENTER
        )

    @allure.step("Открыть список сроков аренды")
    def click_lease_term(self):
        self.click(OrderPageLocators.LEASE_TERM)

    @allure.step("Выбрать срок аренды: {lease}")
    def set_lease_term(self, lease):
        by, value = OrderPageLocators.RENT_OPTION
        self.click((by, value.format(lease)))

    @allure.step("Выбрать цвет: {colour}")
    def set_colour(self, colour):
        by, value = OrderPageLocators.COLOUR_SELECT
        self.click((by, value.format(colour)))

    @allure.step("Ввести комментарий для курьера: {comment}")
    def set_comment(self, comment):
        self.type_text(OrderPageLocators.COMMENT, comment)

    @allure.step("Заполнить второй экран формы заказа")
    def fill_form_second(self, date, lease, colour, comment):
        self.set_delivery_date(date)
        self.click_lease_term()
        self.set_lease_term(lease)
        self.set_colour(colour)
        self.set_comment(comment)

    # --- Оформление заказа ---
    @allure.step("Нажать «Заказать» в форме")
    def click_order(self):
        self.click(OrderPageLocators.ORDER_FORM_BUTTON)

    @allure.step("Подтвердить заказ: «Да»")
    def click_confirm_yes(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Получить заголовок окна об успешном заказе")
    def get_success_header(self):
        return self.wait_visible(OrderPageLocators.SUCCESS_HEADER)

    @allure.step("Нажать «Посмотреть статус»")
    def click_status_button(self):
        self.click(OrderPageLocators.STATUS_BUTTON)

    # --- Шапка ---
    @allure.step("Нажать на логотип «Самокат»")
    def click_scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип «Яндекс» и перейти на Дзен")
    def click_yandex_logo(self):
        self.click(OrderPageLocators.YANDEX_LOGO)
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen"))
