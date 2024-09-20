from pages.base_page import BasePage


class ManagerPage(BasePage):
    """Страница менеджера.

    Attributes:
        BTN_MENU_LIST (tuple): Локатор списка кнопок меню.
    """

    BTN_MENU_LIST = ("xpath", "(//div[@class='center']//button)")

    def click_on_item_menu(self, item_title: str) -> None:
        """Нажимает на элемент меню с указанным заголовком.

        Args:
            item_title (str): Заголовок элемента меню.
        """
        btn_menu_elements = self.presence_of_all_elements_located(self.BTN_MENU_LIST)
        for i in btn_menu_elements:
            if i.text == item_title:
                i.click()
                break
