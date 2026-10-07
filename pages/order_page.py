import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # --- Вспомогательные методы ---
    def _click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    # --- Экран 1: «Для кого самокат» ---
    @allure.step("Ввести имя: {name}")
    def set_name(self, name):
        self._visible(OrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step("Ввести фамилию: {surname}")
    def set_surname(self, surname):
        self._visible(OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step("Ввести адрес: {address}")
    def set_address(self, address):
        self._visible(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Ввести телефон: {phone_number}")
    def set_phone_number(self, phone_number):
        self._visible(OrderPageLocators.PHONE_NUMBER_INPUT).send_keys(
            phone_number
        )

    @allure.step("Открыть список станций метро")
    def click_metro_button(self):
        self._click(OrderPageLocators.METRO_BUTTON)

    @allure.step("Выбрать станцию метро (value={num_val})")
    def select_metro(self, num_val):
        by, value = OrderPageLocators.LIST_OF_METRO
        value = value.format(num_val)
        self._click((by, value))

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
        self._click(OrderPageLocators.NEXT_BUTTON)

    # --- Экран 2: «Про аренду» ---
    @allure.step("Ввести дату доставки: {date}")
    def set_delivery_date(self, date):
        self._visible(OrderPageLocators.DELIVERY_DATE).send_keys(
            date, Keys.ENTER
        )

    @allure.step("Открыть список сроков аренды")
    def click_lease_term(self):
        self._click(OrderPageLocators.LEASE_TERM)

    @allure.step("Выбрать срок аренды: {lease}")
    def set_lease_term(self, lease):
        by, value = OrderPageLocators.RENT_OPTION
        value = value.format(lease)
        self._click((by, value))

    @allure.step("Выбрать цвет: {colour}")
    def set_colour(self, colour):
        by, value = OrderPageLocators.COLOUR_SELECT
        value = value.format(colour)
        self._click((by, value))

    @allure.step("Ввести комментарий для курьера: {comment}")
    def set_comment(self, comment):
        self._visible(OrderPageLocators.COMMENT).send_keys(comment)

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
        self._click(OrderPageLocators.ORDER_FORM_BUTTON)

    @allure.step("Подтвердить заказ: «Да»")
    def click_confirm_yes(self):
        self._click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Получить заголовок окна об успешном заказе")
    def get_success_header(self):
        return self._visible(OrderPageLocators.SUCCESS_HEADER)

    @allure.step("Нажать «Посмотреть статус»")
    def click_status_button(self):
        self._click(OrderPageLocators.STATUS_BUTTON)

    # --- Шапка ---
    @allure.step("Нажать на логотип «Самокат»")
    def click_scooter_logo(self):
        self._click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип «Яндекс» и перейти на Дзен")
    def click_yandex_logo(self):
        self._click(OrderPageLocators.YANDEX_LOGO)
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen"))
