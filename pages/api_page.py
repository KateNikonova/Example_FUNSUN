import allure
import requests
from faker import Faker
from config import MY_HEADERS


class ApiPage:
    def __init__(self):
        self.base_url = "https://auth2.fstravel.com/api/v1/account/"
        self.fake = Faker()
        self.headers = MY_HEADERS

    @allure.step("Отправка запроса на регистрацию")
    def register_user(self, email=None, password=None, phone_number=None, emailing="true"):
        """Универсальный метод для регистрации пользователя"""
        url = f"{self.base_url}sign-up-buyer"

        # Генерация данных, если они не переданы
        email = email or f"{self.fake.user_name()}@{self.fake.free_email_domain()}"
        password = password or self.fake.password(length=10)
        phone_number = phone_number or f"+7{self.fake.msisdn()[3:]}"

        data = {
            "email": email,
            "password": password,
            "phoneNumber": phone_number,
            "emailing": emailing,
            "clientId": "b2c:ru",
            "grant_type": "client_credentials",
            "clientType": "b2c.public.client"
        }
        return requests.post(url, headers=self.headers, data=data)
