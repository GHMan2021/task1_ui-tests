from typing import Tuple, List

from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class ListCustomersPage(BasePage):
    """Страница со списком клиентов.

    Attributes:
        TABLE_DATA_ROWS_LIST (tuple): Локатор списка строк таблицы данных.
        FIRST_NAME_TITLE (tuple): Локатор заголовка "First Name".
        FIRST_NAMES_LIST (tuple): Локатор списка элементов "First Name".
        LAST_NAMES_LIST (tuple): Локатор списка элементов "Last Name".
        POST_CODE_LIST (tuple): Локатор списка элементов "Post Code".
        DELETE_BTN_LIST (tuple): Локатор списка кнопок удаления записей.
    """
    TABLE_DATA_ROWS_LIST = ("xpath", "(//table//tbody//tr)")
    FIRST_NAME_TITLE = ("xpath", "//a[contains(text(),'First Name')]")

    FIRST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[1])")
    LAST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[2])")
    POST_CODE_LIST = ("xpath", "(//tr[@class='ng-scope']//td[3])")
    DELETE_BTN_LIST = ("xpath", "(//button[@ng-click='deleteCust(cust)'])")

    def sort_by_first_name(self) -> None:
        """Сортирует записи по имени."""
        column = self.element_to_be_clickable(self.FIRST_NAME_TITLE)
        column.click()
        column.click()

    def delete_customers(self) -> None:
        """Удаляет выбранных клиентов."""
        delete_records_element_list = self.get_delete_records_element_list()
        for elem in delete_records_element_list:
            elem[3].click()

    def get_all_records_elements_list(self) -> List[Tuple[WebElement, ...]]:
        """Получает список всех элементов записей.

        Returns:
            List[Tuple[WebElement, ...]]: Список кортежей элементов записей.
        """
        count_data_row = len(self.presence_of_all_elements_located(self.TABLE_DATA_ROWS_LIST))

        all_records_elements_list = []
        for i in range(1, count_data_row + 1):
            first_name_element_locator = ("xpath", f"{self.FIRST_NAMES_LIST[1]}[{i}]")
            last_name_element_locator = ("xpath", f"{self.LAST_NAMES_LIST[1]}[{i}]")
            post_code_element_locator = ("xpath", f"{self.POST_CODE_LIST[1]}[{i}]")
            delete_btn_element_locator = ("xpath", f"{self.DELETE_BTN_LIST[1]}[{i}]")

            record = tuple(self.presence_of_element_located(i) for i in [
                first_name_element_locator,
                last_name_element_locator,
                post_code_element_locator,
                delete_btn_element_locator
            ])
            all_records_elements_list.append(record)

        return all_records_elements_list

    def get_delete_records_element_list(self) -> List[Tuple[WebElement, ...]]:
        """Получает список элементов записей, подлежащих удалению.

        Returns:
            List[Tuple[WebElement, ...]]: Список кортежей элементов записей для удаления.
        """
        all_records_element_list = self.get_all_records_elements_list()
        if not all_records_element_list:
            return []

        lengths_names_list = [len(elem[0].text) for elem in all_records_element_list]
        comparison_value = self._value_with_min_deviation_from_avg(lengths_names_list)

        delete_records_element_list = [
            elem for elem in all_records_element_list if len(elem[0].text) == comparison_value
        ]

        return delete_records_element_list

    def get_all_data_customers(self) -> List[Tuple[str, ...]]:
        """"""
        all_records_element_list = self.get_all_records_elements_list()
        if not all_records_element_list:
            return []

        all_data_element_list = [i[:-1] for i in all_records_element_list]
        all_data_customers = [tuple(i.text for i in elem) for elem in all_data_element_list]
        return all_data_customers

    @staticmethod
    def _value_with_min_deviation_from_avg(number_list: List[int]) -> int:  # type: ignore
        """Находит значение с минимальным отклонением от среднего.

        Args:
            number_list (List[int]): Список чисел.

        Returns:
            int: Значение с минимальным отклонением от среднего.

        Raises:
            ValueError: Если список чисел пуст.
        """
        if not number_list:
            raise ValueError("List of numbers must not be empty")

        avg_value = sum(number_list) / len(number_list)
        min_deviation_value = min(list(map(lambda x: abs(x - avg_value), number_list)))

        for number in number_list:
            if abs(number - avg_value) == min_deviation_value:
                return number
