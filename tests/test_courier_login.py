import requests
import allure
import methods.generating_unique_register_user
from data.url import url_courier_login


class TestCourierLogin:

    @allure.title('Проверка авторизации курьера')
    def test_courier_can_log_in(self):
        new_login = methods.generating_unique_register_user.register_new_courier_and_return_login_password('yes')
        payload = {
            "login": f'{new_login[0]}',
            "password": f'{new_login[1]}'
        }
        response = requests.post(url_courier_login, data=payload)
        assert 200 == response.status_code

    @allure.title('Проверка несуществующего пользователя')
    def test_non_existent_user(self):
        payload = {
            "login": "nobody",
            "password": "123456",
        }
        response = requests.post(url_courier_login, data=payload)
        assert 'Учетная запись не найдена' == response.json()["message"]

    @allure.title('Проверка отсутствия поля')
    def test_missing_field(self):
        payload = {
            "password": "123456",
        }
        response = requests.post(url_courier_login, data=payload)
        assert 'Недостаточно данных для входа' == response.json()["message"]

    @allure.title('Проверка успешный запрос возвращает id')
    def test_validation_successful_request_returns_id(self):
        new_login = methods.generating_unique_register_user.register_new_courier_and_return_login_password('yes')
        payload = {
            "login": f'{new_login[0]}',
            "password": f'{new_login[1]}'
        }
        response = requests.post(url_courier_login, data=payload)
        assert 'id' in response.json()
