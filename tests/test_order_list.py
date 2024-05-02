import requests
import allure
from data.url import url_order_list


class TestOrderList:

    @allure.title('Проверка в тело ответа возвращается список заказов')
    def test_list_of_orders_is_returned_in_response_body(self):
        response = requests.get(url_order_list)
        assert 'orders' in response.json()
