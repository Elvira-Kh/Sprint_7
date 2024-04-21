import pytest
from locators.courier import Courier
from Info import Login
from faker import Faker

fake = Faker()

@pytest.fixture()
def courier():
    login = fake.name()
    password = fake.password()
    name = fake.first_name()

    data_post = {
        "login": login,
        "password": password,
        "firstName": name
    }
    courier = Courier()
    courier.post_v1_create_courier(Data.URL, data=data_post)
    login_courier = courier.post_v1_login_courier(Login.URL, data={"login": login, "password": password})
    courier_id = login_courier.json()["id"]
    yield courier_id
    courier.delete_v1_courier(Login.URL, id=courier_id)

@pytest.fixture()
def courier_to_delete():
    login = fake.name()
    password = fake.password()
    name = fake.first_name()

    data_post = {
        "login": login,
        "password": password,
        "firstName": name
    }
    courier = Courier()
    create_courier = courier.post_v1_create_courier(Login.URL, data=data_post)
    login_courier = courier.post_v1_login_courier(Login.URL, data={"login": login, "password": password})
    courier_id = login_courier.json()["id"]
    yield courier_id
    courier.delete_v1_courier(Login.URL, id=courier_id)