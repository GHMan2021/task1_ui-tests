from typing import Literal

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import WAIT_TIMEOUT


class BasePage:
    """Базовый класс для всех страниц.

    Attributes:
        PAGE_URL (str): URL страницы по умолчанию.
    """
    PAGE_URL: str = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует экземпляр страницы.

        Args:
            driver (WebDriver): Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=WAIT_TIMEOUT, poll_frequency=1)

    def open(self) -> None:
        """Открывает страницу."""
        self.driver.get(self.PAGE_URL)

    def element_to_be_clickable(self, locator: tuple[str, str]) -> WebElement:
        """Ожидает, что элемент станет кликабельным.

        Args:
            locator (tuple[str, str]): Локатор элемента.

        Returns:
            WebElement: Кликабельный элемент.
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def alert_is_present(self) -> Alert | Literal[False]:
        """Проверяет наличие алерта.

        Returns:
            Alert | False: Экземпляр Alert, если алерт присутствует, иначе False.
        """
        return self.wait.until(EC.alert_is_present())

    def presence_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        """Ожидает присутствие элемента.

        Args:
            locator (tuple[str, str]): Локатор элемента.

        Returns:
            WebElement: Элемент, если он присутствует.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator: tuple[str, str]) -> list[WebElement]:
        """Ожидает присутствие всех элементов.

        Args:
            locator (tuple[str, str]): Локатор элементов.

        Returns:
            list[WebElement]: Список элементов, если они присутствуют.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
