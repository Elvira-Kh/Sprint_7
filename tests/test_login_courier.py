import pytest
from Info import Login, Response
from locators.courier import Courier
import allure
from faker import Faker
fake = Faker()

fake_login = fake.name()
fake_password = fake.password()

class TestLoginCourier:
    @allure.title('курьер может авторизоваться')
    def test_courier_login(self):
        courier = Courier()
        name = {
            "login": Login.TEST_LOGIN,
            "password": Login.TEST_PASSWORD,
        }
        response = courier.post_v1_login_courier(Login.URL, data=name)
        assert response.status_code == 200 and response.json() == Response.ID_DATA

    @allure.title('для авторизации нужно передать все обязательные поля')
    @pytest.mark.parametrize("test_login, test_password", [("", Login.PASSWORD), (Login.LOGIN, "")])
    def test_courier_with_wrong_data(self, test_login, test_password):
        courier = Courier()
        name = {
            "login": test_login,
            "password": test_password,
        }
        response = courier.post_v1_login_courier(Login.URL, data=name)
        assert response.status_code == 400 and response.json() == Response.WITHOUT_DATA_TO_LOGIN

    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize("test_login, test_password", [(Login.LOGIN, fake_password), (fake_login, Login.PASSWORD)])
    def test_courier_login_with_wrong_login_or_password(self, test_login, test_password):
        courier = Courier()
        name = {
            "login": test_login,
            "password": test_password,
        }
        response = courier.post_v1_login_courier(Login.URL, data=name)
        assert response.status_code == 404 and response.json() == Response.WRONG_DATA_TO_LOGIN