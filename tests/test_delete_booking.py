import allure
import pytest
from requests.exceptions import HTTPError


@allure.feature("Тест Удаление")
@allure.story("Успешное удаление")
def test_delete_booking(api_client, generate_random_booking_date):
    response_json = api_client.create_booking(generate_random_booking_date)
    id = response_json['bookingid']
    api_client.delete_booking(id)

@allure.feature("Тест Удаление")
@allure.story("Удаление не суествующего")
def test_delete_booking(api_client, generate_random_booking_date):
    response_json = api_client.create_booking(generate_random_booking_date)
    id = response_json['bookingid']+1
    with pytest.raises(HTTPError) as exc_info:
        api_client.delete_booking(id)

    assert exc_info.value.response.status_code == 404
