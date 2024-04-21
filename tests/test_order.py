import pytest
from locators.order import Order
from Info import Login
import allure
from faker import Faker
fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()

class TestOrder:
    @allure.title('создание заказа')
    @pytest.mark.parametrize("color", ['BLACK', 'GREY', ('BLACK ', 'GREY'), ""])
    def test_create_order(self, color):
        order = Order()
        response = order.post_v1_create_order(Login.URL, data)
        assert response.status_code == 201 and "track" in response.json()

    @allure.title('получение информации о заказе')
    def test_get_orders_list(self):
        order = Order()
        response = order.get_v1_orders_list(Login.URL)
        assert response.status_code == 200 and "orders" in response.json()
