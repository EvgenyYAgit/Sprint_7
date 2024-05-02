import allure
import json
import pytest
import requests
import methods.generating_unique_register_user
from data.url import url_creating_order


class TestCreatingOrder:

    @allure.title('Проверка указания одного из цветов')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Пожалуйста, побыстрее', 'Бородинов', '2023-06-06', '89209234455',
                               'Ул.Академика Анохина, д.9'],
                              ['Предварительно позвоните', 'Космодемьянская', '2024-05-06', '+7 800 355 35 35',
                               'Ул.Шоколадная, д.55']])
    def test_one_color(self, comment, lastname, delivery_date, phone, address):
        new_login = methods.generating_unique_register_user.register_new_courier_and_return_login_password('yes')
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
        response = requests.post(url_creating_order, data=json_string)
        assert 201 == response.status_code and "track" in response.json()

    @allure.title('Проверка указания обоих цветов')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Пожалуйста, не торопитесь', 'Уткина', '2024-01-06', '89209554455',
                               'Ул.Академика Капитанова, д.92'],
                              ['Без комментариев', 'Шелтеков', '2024-03-10', '+7 900 355 25 35',
                               'Ул.Маслова, д.5']])
    def test_two_color(self, comment, lastname, delivery_date, phone, address):
        new_login = methods.generating_unique_register_user.register_new_courier_and_return_login_password('yes')
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
        response = requests.post(url_creating_order, data=json_string)
        assert 201 == response.status_code and "track" in response.json()

    @allure.title('Проверка без указания цвета')
    @pytest.mark.parametrize('comment, lastname, delivery_date, phone, address',
                             [['Ожидаю', 'Мохов', '2024-11-11', '89209234455',
                               'Ул.Праздничная, д.29'],
                              ['Предварительно позвоните на номер', 'Катков', '2024-10-05', '+7 800 355 35 35',
                               'Ул.Войкова, д.57']])
    def test_without_color(self, comment, lastname, delivery_date, phone, address):
        new_login = methods.generating_unique_register_user.register_new_courier_and_return_login_password('yes')
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
        response = requests.post(url_creating_order, data=json_string)
        assert 201 == response.status_code and "track" in response.json()
