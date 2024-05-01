import requests
import allure
import methods.generating_unique_register_user
from data.url import url_courier_login
from data.data import account_not_found, insufficient_login_information


class TestCourierLogin:

    @allure.title('Проверка авторизации курьера')
    def test_courier_can_log_in(self):
        payload = {
            "login": "sarutobi22",
            "password": "123456"
        }
        response = requests.post(url_courier_login, data=payload)
        assert 200 == response.status_code and 296275 == response.json()["id"]

    @allure.title('Проверка несуществующего пользователя')
    def test_non_existent_user(self):
        payload = {
            "login": "nobody",
            "password": "123456",
        }
        response = requests.post(url_courier_login, data=payload)
        assert account_not_found == response.json()["message"]

    @allure.title('Проверка отсутствия поля')
    def test_missing_field(self):
        payload = {
            "password": "123456",
        }
        response = requests.post(url_courier_login, data=payload)
        assert insufficient_login_information == response.json()["message"]

    @allure.title('Проверка успешный запрос возвращает id')
    def test_validation_successful_request_returns_id(self):
        new_login = methods.generating_unique_register_user.register_new_courier_and_return_login_password('yes')
        payload = {
            "login": f'{new_login[0]}',
            "password": f'{new_login[1]}'
        }
        response = requests.post(url_courier_login, data=payload)
        assert 'id' in response.json()
