import allure
import pytest
from core.clients.endpoints import Endpoints

@allure.feature("Тест создания")
@allure.story('Успешное создание')
def test_create_booking(api_client, generate_random_booking_date):
    response_json = api_client.post(Endpoints.BOOKING_ENDPOINT.value, generate_random_booking_date, 200)
    assert response_json['firstname'] == generate_random_booking_date['firstname']
    assert response_json['lastname'] == generate_random_booking_date['lastname']
    assert response_json['totalprice'] == generate_random_booking_date['totalprice']
    assert response_json['depositpaid'] == generate_random_booking_date['depositpaid']
    assert response_json['bookingdates'] == generate_random_booking_date['bookingdates']
    assert response_json['additionalneeds'] == generate_random_booking_date['additionalneeds']