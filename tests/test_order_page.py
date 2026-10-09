import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from settings import BASE_URL


class TestOrderPage:
    @allure.title("Заказ самоката: {name} {surname}")
    @allure.description(
        "Позитивный флоу заказа: нажать «Заказать», заполнить обе формы, "
        "подтвердить заказ, проверить окно об успешном заказе, вернуться "
        "на главную по логотипу Самоката и проверить редирект на Дзен "
        "по логотипу Яндекса."
    )
    @pytest.mark.parametrize(
        "order_locator, name, surname, address, num_val, phone, date, lease, colour, comment",
        [
            (MainPageLocators.ORDER_UP, "Иван", "Петров", "Москва, ул. Ленина, 1", 4,
             "+79991234567", "25.10.2026", "сутки", "black", "Позвоните за час"),
            (MainPageLocators.ORDER_DOWN, "Анна", "Сидорова", "Москва, ул. Мира, 5", 10,
             "+79997654321", "28.10.2026", "двое суток", "grey", "Домофон не работает"),
        ],
    )
    def test_order_flow(self, driver, order_locator, name, surname, address,
                        num_val, phone, date, lease, colour, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button(order_locator)
        order_page.fill_form(name, surname, address, phone, num_val)
        order_page.click_next_button()
        order_page.fill_form_second(date, lease, colour, comment)
        order_page.click_order()
        order_page.click_confirm_yes()

        with allure.step("Проверить окно об успешном оформлении заказа"):
            assert "Заказ оформлен" in order_page.get_success_header().text

        order_page.click_status_button()
        order_page.click_scooter_logo()

        with allure.step("Проверить переход на главную страницу Самоката"):
            order_page.wait_url_equals(BASE_URL)

        order_page.click_yandex_logo()

        with allure.step("Проверить, что открылась главная страница Дзена"):
            assert "dzen" in order_page.get_current_url()
