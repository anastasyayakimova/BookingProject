import allure
import pytest
from requests.exceptions import HTTPError

@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование firstname")
def test_partial_update_booking_with_firstname(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "firstname": "James"
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['firstname'] == data['firstname']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование lastname")
def test_partial_update_booking_with_lastname(api_client, create_random_booking):
    id = create_random_booking
    data = {
        "lastname": "Brown"
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['lastname'] == data['lastname']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование totalprice")
def test_partial_update_booking_with_totalprice(api_client, create_random_booking):
    id = create_random_booking
    data = {
         "totalprice": 111
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['totalprice'] == data['totalprice']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование depositpaid")
def test_partial_update_booking_with_depositpaid(api_client, create_random_booking):
    id = create_random_booking
    data = {
         "depositpaid": True
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['depositpaid'] == data['depositpaid']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование bookingdates")
def test_partial_update_booking_with_bookingdates(api_client, create_random_booking):
    id = create_random_booking
    data = {
         "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['bookingdates'] == data['bookingdates']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование bookingdates random")
def test_partial_update_booking_with_bookingdates_random(api_client, create_random_booking, booking_dates):
    id = create_random_booking
    data = {
         "bookingdates": booking_dates
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['bookingdates'] == data['bookingdates']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование additionalneeds")
def test_partial_update_booking_with_additionalneeds(api_client, create_random_booking, booking_dates):
    id = create_random_booking
    data = {
         "additionalneeds": "Breakfast"
    }
    response_json = api_client.partial_update_booking(id, data)
    assert response_json['additionalneeds'] == data['additionalneeds']


@allure.feature("Тест частичного редактирования")
@allure.story("Редактирование несуществующего")
def test_partial_update_booking_with_additionalneeds(api_client, create_random_booking, booking_dates):
    id = create_random_booking+1
    data = {
         "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError) as exc_info:
        api_client.partial_update_booking(id, data)

    assert exc_info.value.response.status_code == 405