import pytest
from selenium import webdriver

from pages.main_page import MainPage
from settings import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    main_page = MainPage(driver)
    main_page.accept_cookies()
    yield driver
    driver.quit()
