import requests
import os
from dotenv import load_dotenv
from core.setting.environments import Environment
from core.clients.endpoints import Endpoints
from core.setting.config import Users, Timeouts
from requests.auth import HTTPBasicAuth
import allure

load_dotenv()

class APIClient:

    def __init__(self):
        environment_str = os.getenv("ENVIRONMENT")
        try:
            environment = Environment[environment_str]
        except KeyError:
            raise ValueError(f'Unsupported environment value: {environment_str}')

        self.base_url = self.get_base_url(environment)
        self.session = requests.Session()

    def get_base_url(self, environment: Environment) -> str:
        if environment == Environment.TEST:
            return os.getenv('TEST_BASE_URL')
        elif environment == Environment.PROD:
            return os.getenv('PROD_BASE_URL')
        else:
            raise ValueError(f'Unsupported environment: {environment}')

    def get(self, endpoint, params=None, status_code=200):
        url = self.base_url + endpoint
        response = requests.get(url, headers=self.headers, params=params)
        if status_code:
            assert response.status_code == status_code
        return response.json()

    def post(self, endpoint, data=None, status_code=200):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers, json=data)
        if status_code:
            assert response.status_code == status_code
        return response.json()

    def ping(self):
        with allure.step("Пинг"):
            url = f'{self.base_url}{Endpoints.PING_ENDPOINT.value}'
            response = self.session.get(url)
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 201, f'Ожидали 201, но получили {response.status_code}'
        return response.status_code

    def auth(self):
        with allure.step("Получить аутентификацию"):
            url = f'{self.base_url}{Endpoints.AUTH_ENDPOINT.value}'
            payload = {"username": Users.USERNAME.value, "password": Users.PASSWORD.value}
            response = self.session.post(url, json=payload, timeout=Timeouts.TIMEOUT.value)
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидали 201, но получили {response.status_code}'
        token = response.json().get("token")
        with allure.step("Обновление хэдера с записью об авторизации"):
            self.session.headers.update({"Authorization": f"Bearer{token}"})

    def get_booking_ids_endpoint(self, params=None):
        with allure.step("Отправка запроса на получение BokindIds"):
            url = f'{self.base_url}{Endpoints.BOOKING_ENDPOINT.value}'
            response = self.session.get(url, params=params)
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидали 200, но получили {response.status_code}'
        return response.json()


    def get_booking_for_id(self, id):
        with allure.step("Отправка запроса на получние booking по id"):
            url = f'{self.base_url}{Endpoints.BOOKING_ENDPOINT.value}/{id}'
            response = self.session.get(url)
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидали 200, но получили {response.status_code}'
        return response.json()

    def delete_booking(self, booking_id):
        with allure.step("Удаление"):
            url = f'{self.base_url}{Endpoints.BOOKING_ENDPOINT.value}/{booking_id}'
            response = self.session.delete(url, auth=HTTPBasicAuth(Users.USERNAME.value, Users.PASSWORD.value))
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 201, f'Ожидали 200, но получили {response.status_code}'

    def create_booking(self, booking_data):
        with allure.step("Создание"):
            url = f"{self.base_url}{Endpoints.BOOKING_ENDPOINT.value}"
            response = self.session.post(url, json=booking_data)
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидали 200, но получили {response.status_code}'
        return response.json()


    def update_booking(self, booking_id, booking_data):
        with allure.step("Редактирование"):
            url = f"{self.base_url}{Endpoints.BOOKING_ENDPOINT.value}/{booking_id}"
            response = self.session.put(url, json=booking_data, auth=HTTPBasicAuth(Users.USERNAME.value, Users.PASSWORD.value))
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидали 200, но получили {response.status_code}'
        return response.json()

    def partial_update_booking(self, booking_id, booking_data):
        with allure.step("Частичное редактирование"):
            url = f"{self.base_url}{Endpoints.BOOKING_ENDPOINT.value}/{booking_id}"
            response = self.session.patch(url, json=booking_data, auth=HTTPBasicAuth(Users.USERNAME.value, Users.PASSWORD.value))
            response.raise_for_status()
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидали 200, но получили {response.status_code}'
        return response.json()