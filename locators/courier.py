import allure
import requests
from Info import Login

class Courier:
    @allure.step('создание карточки курьера')
    def post_v1_create_courier(self, data):
        return requests.post(Login.COURIER, data)


    @allure.step('получение логина курьера')
    def post_v1_login_courier(self, data):
        return requests.post(Login.COURIER_LOGIN, data)

    @allure.step('удаление курьера')
    def delete_v1_courier(self, data):
        return requests.delete(Login.COURIER_LOGIN)
