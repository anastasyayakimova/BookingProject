from core.clients.api_client import APIClient
import pytest
from _datetime import datetime, timedelta
from faker import Faker

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    client.auth()
    return client

@pytest.fixture()
def booking_dates():
    tooday = datetime.today()
    chekin_date = tooday + timedelta(days=10)
    checkout_data = chekin_date + timedelta(days=5)

    return {
        "checkin": chekin_date.strftime("%Y-%m-%d"),
        "checkout": checkout_data.strftime("%Y-%m-%d")
    }

@pytest.fixture()
def generate_random_booking_date(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprise = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprise,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates,
        "additionalneeds": additionalneeds
    }
    return data
