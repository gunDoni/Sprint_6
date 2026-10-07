from selenium.webdriver.common.by import By


class MainPageLocators:
    # --- FAQ «Вопросы о важном» ---
    # Заголовок вопроса (в {} подставляем индекс)
    QUESTION_HEADING = (By.XPATH, ".//div[@id='accordion__heading-{}']")

    # Панель с текстом ответа (в {} подставляем индекс)
    QUESTION_PANEL = (By.XPATH, ".//div[@id='accordion__panel-{}']")

    # --- Куки ---
    # Кнопка принятия куки
    COOKIE_BUTTON = (By.XPATH, ".//button[@id='rcc-confirm-button']")

    # --- Кнопки «Заказать» ---
    # Верхняя кнопка (первая «Заказать» в DOM)
    ORDER_UP = (By.XPATH, "(//button[text()='Заказать'])[1]")

    # Нижняя кнопка (внутри блока Home_FinishButton)
    ORDER_DOWN = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']",
    )
