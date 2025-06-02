import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-testid='tours_searchblock_search_btn']")
    RESULTS_BLOCK = (By.CSS_SELECTOR, "[data-testid='issuance_overall_item_block']")
    HOTELS_LINK = (By.XPATH, "//a[@href='/searchhotel']")
    HOTELS_PAGE_HEADER = (By.XPATH, "//h1[contains(@class, 'meta-h1') and contains(text(), 'Бронирование отелей')]")
    PAGE_HEADER = (By.XPATH, "//h1[contains(@class, 'meta-h1')]")


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()

    def _wait_for_elements(self, locator, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))

    @allure.step("Проверка заголовка страницы")
    def check_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(EC.title_is(expected_title))
        return True

    @allure.step("Туры: клик на кнопку Найти")
    def search_default_tours(self):
        button = self._wait_for_elements(Locators.SEARCH_BUTTON)
        button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.RESULTS_BLOCK))

    @allure.step("Получаем количество элементов в результатах поиска")
    def get_search_results_count(self):
        elements = self._wait_for_elements(Locators.RESULTS_BLOCK, multiple=True)
        return len(elements)

    @allure.step("Переход на страницу отелей")
    def go_to_hotels_page(self):
        self._wait_for_elements(Locators.HOTELS_LINK).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/searchhotel"))

    @allure.step("Проверка URL страницы")
    def check_current_url(self, expected_url_part):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_url_part))
        return True

    @allure.step("Проверка заголовка страницы по тексту")
    def check_page_header(self, expected_text):
        headers = self._wait_for_elements(Locators.PAGE_HEADER, multiple=True)
        for header in headers:
            if header.text.strip() == expected_text:
                return header.is_displayed()
        return False
