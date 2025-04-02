import allure
import pytest
import requests


@allure.feature("Тест Ping")
@allure.story("Тест соединения")
def test_ping(api_client):
    status_code = api_client.ping()
    assert status_code == 201, f"Результат не совпал с ожидаемым, {status_code}"

@allure.feature("Тест Ping")
@allure.story("Тест Server_unavailable")
def test_ping_server_unavailable(api_client, mocker):
    mocker.patch.object(api_client.session, 'get', side_effect=Exception('Server_unavailable'))
    with pytest.raises(Exception, match="Server_unavailable"):
        api_client.ping()


@allure.feature("Тест Ping")
@allure.story("Тест ошибка в теле ответа")
def test_ping_wrong_method(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 405
    mocker.patch.object(api_client.session, 'get', return_value = mock_response)
    with pytest.raises(AssertionError, match="Expected status 201 but got 405"):
        api_client.ping()


@allure.feature("Тест Ping")
@allure.story("Ошибка сервера")
def test_ping_internal_server_error(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mocker.patch.object(api_client.session, 'get', return_value = mock_response)
    with pytest.raises(AssertionError, match="Expected status 201 but got 500"):
        api_client.ping()


@allure.feature("Тест Ping")
@allure.story("Тест Wrong URL")
def test_ping_internal_server_error(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch.object(api_client.session, 'get', return_value = mock_response)
    with pytest.raises(AssertionError, match="Expected status 201 but got 404"):
        api_client.ping()


@allure.feature("Тест Ping")
@allure.story("Тест Timeout")
def test_ping_internal_server_error(api_client, mocker):
    mocker.patch.object(api_client.session, 'get', side_effect=requests.Timeout)
    with pytest.raises(requests.Timeout):
        api_client.ping()