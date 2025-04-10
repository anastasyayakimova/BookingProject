import allure
import pytest
from pydantic import ValidationError
from core.models.booking import BookingResponse
from requests.exceptions import HTTPError


@allure.feature("Тест создания")
@allure.story('Успешное создание с предустановленными данными')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Ошибка валидации: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates'] == booking_data['bookingdates']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


@allure.feature("Тест создания")
@allure.story('Успешное создание с рандомными данными')
def test_create_booking_with_random_data(api_client, generate_random_booking_date):
    response_json = api_client.create_booking(generate_random_booking_date)
    try:
        BookingResponse(**response_json)
    except ValidationError as e:
        raise ValidationError(f'Ошибка валидации: {e}')

    assert response_json['booking']['firstname'] == generate_random_booking_date['firstname']
    assert response_json['booking']['lastname'] == generate_random_booking_date['lastname']
    assert response_json['booking']['totalprice'] == generate_random_booking_date['totalprice']
    assert response_json['booking']['depositpaid'] == generate_random_booking_date['depositpaid']
    assert response_json['booking']['bookingdates'] == generate_random_booking_date['bookingdates']
    assert response_json['booking']['additionalneeds'] == generate_random_booking_date['additionalneeds']


@allure.feature("Тест создания")
@allure.story("Успешное создание без необязательных полей")
def test_create_booking_with_custom_data_without_additionalneeds(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Ошибка валидации: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates'] == booking_data['bookingdates']


@allure.feature("Тест создания")
@allure.story('Неуспешное создание без обязательного поля firstname')
def test_create_booking_without_firstname(api_client):
    booking_data = {
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
        api_client.create_booking(booking_data)

    assert exc_info.value.response.status_code == 500


@allure.feature("Тест создания")
@allure.story('Неуспешное создание без обязательного поля lastname')
def test_create_booking_without_lastname(api_client):
    booking_data = {
        "firstname": "Jim",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.create_booking(booking_data)

    assert exc_info.value.response.status_code == 500


@allure.feature("Тест создания")
@allure.story('Неуспешное создание без обязательного поля totalprice')
def test_create_booking_without_totalprice(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.create_booking(booking_data)

    assert exc_info.value.response.status_code == 500


@allure.feature("Тест создания")
@allure.story('Неуспешное создание без обязательного поля bookingdates')
def test_create_booking_without_bookingdates(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.create_booking(booking_data)

    assert exc_info.value.response.status_code == 500

@allure.feature("Тест создания")
@allure.story('Неуспешное создание без обязательного поля depositpaid')
def test_create_booking_without_depositpaid(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.create_booking(booking_data)

    assert exc_info.value.response.status_code == 500

