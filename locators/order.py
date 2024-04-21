import allure
from Info import Login


class Order:
    @allure.step('создание заказа')
    def post_v1_create_order(self, data):
        return requests.post(Login.ORDER, json=data)

    @allure.step('получение информации о заказе')
    def get_v1_orders_list(self):
        return requests.get(Login.ORDER)