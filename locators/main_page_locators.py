from selenium.webdriver.common.by import By

class MainPageLocators:
    YANDEX_LOGO = By.XPATH, "//*[@alt='Yandex']"  # Лого "Яндекс"
    SCOOTER_LOGO = By.XPATH, "//*[@alt='Scooter']"  # Лого "Самокат"
    LOCATOR_FAQ = By.XPATH, "//div[contains(@class, 'Home_FAQ_')]"  # Раздел "Вопросы о важном"
    LOCATOR_QUESTIONS = By.XPATH, "//div[contains(@class, 'accordion__item')]"  # Вопросы
    LOCATOR_RESPONSE = By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]"  # Отображаемый ответ
    COOKIES_BUTTON = By.ID, "rcc-confirm-button"  # Кнопка принять куки
    HEADER_TEXT = By.XPATH, "//div[contains(@class, 'Home_Header')]"  # Заголовок на главной странице
    HEADER_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']"  # Кнопка "Заказать" в шапке
    # либо HEADER_ORDER_BUTTON = By.XPATH, "//button[text()='Заказать'][1]"
    ORDER_BUTTON_MAIN_PAGE = By.XPATH, "//div[contains(@class, 'Finish')]//button[text()='Заказать']"  # Кнопка "Заказать" на странице
    # либо ORDER_BUTTON_MAIN_PAGE = By.XPATH, "//button[text()='Заказать'][2]"

