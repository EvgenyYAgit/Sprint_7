import requests
import allure


class TestOrderList:

    @allure.title('Проверка в тело ответа возвращается список заказов')
    def test_list_of_orders_is_returned_in_response_body(self):
        response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=296290")
        assert 'orders' in response.json()
