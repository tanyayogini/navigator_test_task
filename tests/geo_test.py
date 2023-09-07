import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_city_list(client, get_city1, get_city2):
    response = client.get("/city/")
    expected_response = [
        {
            "id": 1,
            "name": "Екатеринбург"
        },
        {
            "id": 2,
            "name": "Москва"
        }]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_get_city_list(client, get_street1):
    response = client.get("/city/1/street/")
    expected_response = [
        {
            "id": 1,
            "name": "Мира"
        }]

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
