import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from config import MAIN_URL, MAIN_PAGE_TITLE


@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    page = MainPage(driver, MAIN_URL)
    yield page
    driver.quit()


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(MAIN_PAGE_TITLE)


@allure.feature("Поиск тура")
@allure.story("UI")
@allure.title("Поиск тура с данными по умолчанию")
@pytest.mark.positive
@pytest.mark.ui
def test_search_default_tours(main_page):
    with allure.step("Поиск тура с данными по умолчанию"):
        main_page.search_default_tours()
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0


@allure.feature("Отели")
@allure.story("UI")
@allure.title("Переход на страницу отелей и проверка элементов")
@pytest.mark.positive
@pytest.mark.ui
def test_hotels_page(main_page):
    with allure.step("Переходим на страницу отелей"):
        main_page.go_to_hotels_page()

    with allure.step("Проверяем URL страницы"):
        assert main_page.check_current_url("/searchhotel")

    with allure.step("Проверяем заголовок страницы"):
        assert main_page.check_page_header("Бронирование отелей")
