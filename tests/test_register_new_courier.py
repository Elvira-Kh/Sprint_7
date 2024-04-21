import pytest
import requests
from Info import Login, Response
from locators.courier import Courier
import allure
from faker import Faker
fake = Faker()

login = fake.name()
password = fake.password()
name = fake.first_name()


class TestCourier:
    @allure.title('создание курьера')
    def test_create_courier(self):
        post = {
            "login": login,
            "password": password,
            "firstName": name
                }
        courier = Courier()
        response = courier.post_v1_create_courier(Login.URL, data=post)
        assert response.status_code == 201 and response.json() == Response.OK_TRUE

    @allure.title('нельзя создать двух одинаковых курьеров')
    def test_cant_create_two_couriers_with_the_same_login(self):
        post = {
            "login": Login.LOGIN,
            "password": password,
            "firstName": name
        }
        courier = Courier()
        response = courier.post_v1_create_courier(Login.URL, post)
        assert response.status_code == 409 and response.json() == Response.WRONG_LOGIN

    @allure.title('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @pytest.mark.parametrize("test_login, test_password", [("", password), (login, "")])
    def test_create_courier_without_required_fields(self, test_login, test_password):
        post = {
            "login": test_login,
            "password": test_password,
            "firstName": name
        }
        courier = Courier()
        response = courier.post_v1_courier(Login.URL, post)
        assert response.status_code == 400 and response.json() == Response.WITHOUT_DATA_TO_CREATE

    @allure.title('удаление курьера')
    def test_delete_courier(self, prepare_courier_for_delete):
        courier = Courier()
        courier_id = prepare_courier_for_delete.json()["id"]
        response = courier.delete_v1_courier(courier_id)
        assert response.status_code == 200 and response.json() == Response.OK_TRUE

    @allure.title('нельзя удалить курьера без айди')
    def test_delete_courier_without_id(self):
        courier = Courier()
        response = courier.delete_v1_courier(Login.URL, "")
        assert response.status_code == 404 and response.json() == Response.NOT_FOUND

    @allure.title('нельзя удалить курьера с неверным айди')
    def test_delete_courier_with_wrong_id(self):
        courier = Courier()
        response = courier.delete_v1_courier("88999")
        assert response.status_code == 404 and response.json() == Response.WRONG_ID