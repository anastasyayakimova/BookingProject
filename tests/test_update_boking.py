import allure
import pytest
from requests.exceptions import HTTPError

@allure.feature("Тест редактирования")
@allure.story("Успешное редактирование с предустановленными данными")
def test_update_booking_with_custom_data(api_client, create_random_booking):
    id = create_random_booking
    booking_data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_json = api_client.update_booking(id, booking_data)
    assert response_json['firstname'] == booking_data['firstname']
    assert response_json['lastname'] == booking_data['lastname']
    assert response_json['totalprice'] == booking_data['totalprice']
    assert response_json['depositpaid'] == booking_data['depositpaid']
    assert response_json['bookingdates'] == booking_data['bookingdates']
    assert response_json['additionalneeds'] == booking_data['additionalneeds']

@allure.feature("Тест редактирования")
@allure.story("Успешное редактирование с предустановленными данными")
def test_update_booking_with_random_data(api_client, create_random_booking, generate_random_booking_date):
    id = create_random_booking
    response_json = api_client.update_booking(id, generate_random_booking_date)
    assert response_json['firstname'] == generate_random_booking_date['firstname']
    assert response_json['lastname'] == generate_random_booking_date['lastname']
    assert response_json['totalprice'] == generate_random_booking_date['totalprice']
    assert response_json['depositpaid'] == generate_random_booking_date['depositpaid']
    assert response_json['bookingdates'] == generate_random_booking_date['bookingdates']
    assert response_json['additionalneeds'] == generate_random_booking_date['additionalneeds']


@allure.feature("Тест редактирования")
@allure.story("Eспешное редактирование без необязательного поля additionalneeds")
def test_update_without_additionalneeds(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }
    response_json = api_client.update_booking(id, data)
    assert response_json['firstname'] == data['firstname']
    assert response_json['lastname'] == data['lastname']
    assert response_json['totalprice'] == data['totalprice']
    assert response_json['depositpaid'] == data['depositpaid']
    assert response_json['bookingdates'] == data['bookingdates']


@allure.feature("Тест редактирования")
@allure.story("Не успешное редактирование без обязательного поля firstname")
def test_update_without_firstname(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.update_booking(id, data)

    assert exc_info.value.response.status_code == 400


@allure.feature("Тест редактирования")
@allure.story("Не успешное редактирование без обязательного поля lastname")
def test_update_without_lastname(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "firstname": "James",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.update_booking(id, data)

    assert exc_info.value.response.status_code == 400


@allure.feature("Тест редактирования")
@allure.story("Не успешное редактирование без обязательного поля totalprice")
def test_update_without_totalprice(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "firstname": "James",
        "lastname": "Brown",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.update_booking(id, data)

    assert exc_info.value.response.status_code == 400


@allure.feature("Тест редактирования")
@allure.story("Не успешное редактирование без обязательного поля depositpaid")
def test_update_without_depositpaid(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.update_booking(id, data)

    assert exc_info.value.response.status_code == 400


@allure.feature("Тест редактирования")
@allure.story("Не успешное редактирование без обязательного поля bookingdates")
def test_update_without_bookingdates(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.update_booking(id, data)

    assert exc_info.value.response.status_code == 400


@allure.feature("Тест редактирования")
@allure.story("Редактировнаие не существующего")
def test_update_booking_with_random_data(api_client, create_random_booking, generate_random_booking_date):
    id = create_random_booking+1
    with pytest.raises(HTTPError) as exc_info:
        api_client.update_booking(id, generate_random_booking_date)

    assert exc_info.value.response.status_code == 405




