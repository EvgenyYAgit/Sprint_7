import requests
import allure
from methods.generating_unique_user_data import generate_random_account_data


class TestCreatingCourier:

    @allure.title('Проверка создания курьера с правильным кодом ответа')
    def test_courier_can_be_created(self):
        new_login = generate_random_account_data()
        payload = {
            "login": f'{new_login[0]}',
            "password": f'{new_login[1]}',
            "firstName": f'{new_login[2]}'
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert 201 == response.status_code

    @allure.title('Проверка возврата тела ответа "ok"')
    def test_is_returned_to_the_response_body_ok(self):
        new_login = generate_random_account_data()
        payload = {
            "login": f'{new_login[0]}',
            "password": f'{new_login[1]}',
            "firstName": f'{new_login[2]}'
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert 'ok' in response.json()

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_cannot_create_two_identical_couriers(self):
        new_login = generate_random_account_data()
        payload = {
            "login": f'{new_login[0]}',
            "password": f'{new_login[1]}',
            "firstName": f'{new_login[2]}'
        }
        requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert 'Этот логин уже используется. Попробуйте другой.' == response.json()["message"]

    @allure.title('Проверка создания курьера если одного из полей нет')
    def test_if_none_of_the_query_fields_is_present(self):
        payload = {
            "login": "uzumaki",
            "firstName": "naruto"
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert 'Недостаточно данных для создания учетной записи' == response.json()["message"]

    @allure.title('Проверка ошибки если логин уже существует')
    def test_error_is_login_that_already_exists(self):
        new_login = generate_random_account_data()
        payload = {
            "login": 'naruto',
            "password": f'{new_login[1]}',
            "firstName": f'{new_login[2]}'
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert 409 == response.status_code
