from selenium.webdriver.common.by import By


class OrderPageLocators:
    # --- Экран 1: «Для кого самокат» ---
    # Поле ввода имени
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")

    # Поле ввода фамилии
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Поле ввода адреса
    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']",
    )

    # Поле выбора станции метро (открывает список)
    METRO_BUTTON = (By.CLASS_NAME, "select-search__input")

    # Шаблон станции метро (в {} подставляем value)
    LIST_OF_METRO = (By.XPATH, "//li/button[@value='{}']")

    # Поле ввода номера телефона
    PHONE_NUMBER_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )

    # Кнопка «Далее»
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # --- Экран 2: «Про аренду» ---
    # Поле ввода даты доставки самоката
    DELIVERY_DATE = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']",
    )

    # Раскрывающийся список срока аренды
    LEASE_TERM = (By.CLASS_NAME, "Dropdown-placeholder")

    # Шаблон варианта срока аренды (в {} подставляем текст)
    RENT_OPTION = (
        By.XPATH,
        "//div[@class='Dropdown-option' and text()='{}']",
    )

    # Шаблон чекбокса цвета (в {} подставляем id: black / grey)
    COLOUR_SELECT = (By.ID, "{}")

    # Комментарий для курьера
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка «Заказать» на втором экране формы
    ORDER_FORM_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle') and text()='Заказать']",
    )

    # --- Модальные окна ---
    # Кнопка «Да» в окне подтверждения заказа
    CONFIRM_YES_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]//button[text()='Да']",
    )

    # Заголовок окна об успешном заказе
    SUCCESS_HEADER = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') "
        "and contains(text(), 'Заказ оформлен')]",
    )

    # Кнопка «Посмотреть статус»
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    # --- Шапка ---
    # Логотип Самоката
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    # Логотип Яндекса (ссылка с target="_blank")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
