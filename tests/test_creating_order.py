import allure
import json
import pytest
import requests
from methods.generating_unique_register_user import register_new_courier_and_return_login_password


class TestCreatingOrder:

    @allure.title('Проверка указания одного из цветов')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Пожалуйста, побыстрее', 'Бородинов', '2023-06-06', '89209234455',
                               'Ул.Академика Анохина, д.9'],
                              ['Предварительно позвоните', 'Космодемьянская', '2024-05-06', '+7 800 355 35 35',
                               'Ул.Шоколадная, д.55']])
    def test_one_color(self, comment, lastname, delivery_date, phone, address):
        new_login = register_new_courier_and_return_login_password()
        payload = {
            "firstName": f'{new_login[2]}',
            "lastName": f'{lastname}',
            "address": f'{address}',
            "metroStation": 4,
            "phone": f'{phone}',
            "rentTime": 5,
            "deliveryDate": f'{delivery_date}',
            "comment": f'{comment}',
            "color": [
                "BLACK"
            ]
        }
        json_string = json.dumps(payload)
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", data=json_string)
        assert 201 == response.status_code

    @allure.title('Проверка указания обоих цветов')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Пожалуйста, не торопитесь', 'Уткина', '2024-01-06', '89209554455',
                               'Ул.Академика Капитанова, д.92'],
                              ['Без комментариев', 'Шелтеков', '2024-03-10', '+7 900 355 25 35',
                               'Ул.Маслова, д.5']])
    def test_two_color(self, comment, lastname, delivery_date, phone, address):
        new_login = register_new_courier_and_return_login_password()
        payload = {
            "firstName": f'{new_login[2]}',
            "lastName": f'{lastname}',
            "address": f'{address}',
            "metroStation": 4,
            "phone": f'{phone}',
            "rentTime": 5,
            "deliveryDate": f'{delivery_date}',
            "comment": f'{comment}',
            "color": [
                "BLACK",
                "GREY"
            ]
        }
        json_string = json.dumps(payload)
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", data=json_string)
        assert 201 == response.status_code

    @allure.title('Проверка без указания цвета')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Ожидаю', 'Мохов', '2024-11-11', '89209234455',
                               'Ул.Праздничная, д.29'],
                              ['Предварительно позвоните на номер', 'Катков', '2024-10-05', '+7 800 355 35 35',
                               'Ул.Войкова, д.57']])
    def test_without_color(self, comment, lastname, delivery_date, phone, address):
        new_login = register_new_courier_and_return_login_password()
        payload = {
            "firstName": f'{new_login[2]}',
            "lastName": f'{lastname}',
            "address": f'{address}',
            "metroStation": 4,
            "phone": f'{phone}',
            "rentTime": 5,
            "deliveryDate": f'{delivery_date}',
            "comment": f'{comment}',
            "color": [
            ]
        }
        json_string = json.dumps(payload)
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", data=json_string)
        assert 201 == response.status_code

    @allure.title('Проверка тело ответа содержит track')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Не торопитесь', 'Марыскин', '2024-02-06', '89209234400',
                               'Ул.Московская, д.9'],
                              ['Буду недоступен до 12 утра', 'Сосунов', '2024-07-06', '+7 800 400 00 11',
                               'Ул.Петропавловская, д.55']])
    def test_response_body_contains_track(self, comment, lastname, delivery_date, phone, address):
        new_login = register_new_courier_and_return_login_password()
        payload = {
            "firstName": f'{new_login[2]}',
            "lastName": f'{lastname}',
            "address": f'{address}',
            "metroStation": 4,
            "phone": f'{phone}',
            "rentTime": 5,
            "deliveryDate": f'{delivery_date}',
            "comment": f'{comment}',
            "color": [
                "GREY"
            ]
        }
        json_string = json.dumps(payload)
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", data=json_string)
        assert 'track' in response.json()
