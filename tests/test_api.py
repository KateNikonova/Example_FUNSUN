import pytest
import allure
from pages.api_page import ApiPage


@pytest.fixture
def api_page():
    return ApiPage()


@allure.feature("API Тесты")
@allure.story("Регистрация пользователя")
class TestRegistration:
    @allure.title("Позитивный тест: Регистрация с email в домене .ru")
    @pytest.mark.positive
    @pytest.mark.api
    def test_register_with_ru_email(self, api_page):
        response = api_page.register_user(email=f"test_{api_page.fake.user_name()}@ya.ru")

        assert response.status_code == 201, "Ожидается статус код 201"


    @allure.title("Позитивный тест: Регистрация с email в домене .com")
    @pytest.mark.positive
    @pytest.mark.api
    def test_register_with_com_email(self, api_page):
        response = api_page.register_user(email=f"test_{api_page.fake.user_name()}@gmail.com")

        assert response.status_code == 201, "Ожидается статус код 201"


    @allure.title("Негативный тест: Попытка регистрации с email в виде иероглифов")
    @pytest.mark.negative
    @pytest.mark.api
    def test_register_with_hieroglyph_email(self, api_page):
        response = api_page.register_user(email="级字表@mail.ru")

        assert response.status_code == 500, "Ожидается статус код 500"
