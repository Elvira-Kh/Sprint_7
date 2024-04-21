class Login:
    URL = 'http://qa-scooter.praktikum-services.ru'
    LOGIN = 'Yung Lean'
    PASSWORD = 'sadboys'
    COURIER = 'http://qa-scooter.praktikum-services.ru/api/v1/courier'
    COURIER_LOGIN = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    ORDER = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'

class Rent:
    Order = {
        "firstName": 'Kendrick' ,
        "lastName": 'Lamar',
        "address": 'butovo',
        "metroStation": 3,
        "phone": '89123456789',
        "rentTime": 4,
        "deliveryDate": "2024-04-19",
        "comment": "Sit down, be humble"
    }

class Response:
    NOT_FOUND = {"code": 404, "message": "Not Found."}
    WRONG_ID = {"code": 404, "message": "Курьера с таким id нет."}
    OK_TRUE = {"ok": True}
    WITHOUT_DATA_TO_CREATE = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    WRONG_LOGIN = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    ID_DATA = {"id": 260399}
    WITHOUT_DATA_TO_LOGIN = {"code": 400, "message": "Недостаточно данных для входа"}
    WRONG_DATA_TO_LOGIN = {"code": 404, "message": "Учетная запись не найдена"}