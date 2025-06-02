import pytest
import allure
from pages.api_page import ApiPage


@pytest.fixture
def api_page():
    return ApiPage()


@allure.feature("Регистрация пользователя")
@allure.story("API")
@allure.title("Регистрация с email в домене .ru")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
def test_register_with_ru_email(api_page):
    with allure.step("Отправляем запрос на регистрацию с email  в домене ru"):
        response = api_page.register_user(email=f"test_{api_page.fake.user_name()}@ya.ru")
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 201, "Ожидается статус код 201"


@allure.feature("Регистрация пользователя")
@allure.story("API")
@allure.title("Регистрация с email в домене .com")
@pytest.mark.positive
@pytest.mark.api
def test_register_with_com_email(api_page):
    with allure.step("Отправляем запрос на регистрацию с email  в домене ru"):
        response = api_page.register_user(email=f"test_{api_page.fake.user_name()}@gmail.com")
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 201, "Ожидается статус код 201"


@allure.feature("Регистрация пользователя")
@allure.story("API")
@allure.title("Попытка регистрации с email в виде иероглифов")
@pytest.mark.negative
@pytest.mark.api
def test_register_with_hieroglyph_email(api_page):
    with allure.step("Отправляем запрос на регистрацию с email с иероглифами"):
        response = api_page.register_user(email="级字表@mail.ru")
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 500, "Ожидается статус код 500"
