import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.list_customers_page import ListCustomersPage
from pages.manager_page import ManagerPage


@allure.feature('globalsqa.com')
@allure.title('Сортировка клиентов по имени (First Name)')
@allure.description("""
    Цель: Проверить сортировка клиентов по имени

    Предусловие: Открыть браузер

    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"    
    2. Дважды нажать на заголовок таблицы "First Name" для сортировки пользователей по имени
    3. Проверить, что имена отсортирована в алфавитном порядке
    """)
def test_sort_by_first_name(driver: WebDriver) -> None:
    with allure.step("Открытие страницу 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'"):
        list_customers_page = ListCustomersPage(driver)
        list_customers_page.open()

    with allure.step("Сортировка пользователей по имени"):
        manager_page = ManagerPage(driver)
        manager_page.click_on_item_menu("Customers")
        list_customers_page.sort_by_first_name()

    with allure.step("Проверка, что имена отсортированы в алфавитном порядке "):
        all_customers = list_customers_page.get_all_data_customers()
        sorted_all_customers = sorted(all_customers, key=lambda first_name: first_name[0])
        assert all_customers == sorted_all_customers, "Клиенты не отсортированы по имени"
