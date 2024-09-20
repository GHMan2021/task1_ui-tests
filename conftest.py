import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope='module')
def driver() -> WebDriver:
    """Фикстура для инициализации WebDriver.

    Эта фикстура создает экземпляр WebDriver для использования в тестах. WebDriver инициализируется с параметрами,
    заданными в опциях Chrome. После завершения всех тестов экземпляр WebDriver завершает свою работу.

    Returns:
        WebDriver: Экземпляр WebDriver для управления браузером.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
