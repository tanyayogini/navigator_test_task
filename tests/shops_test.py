import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_shop(client, get_city2, get_street2):
    response = client.post('/shop/', data={
        "name": "тест-создание-магазин",
        "city": get_city2.id,
        "street": get_street2.id,
        "house": 1,
        "open": "9:00",
        "close": "21:00"},
                           content_type='application/json')

    expected_response = {"id": 1}
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_list_shop(client, get_shop1, get_shop2):
    response = client.get("/shop/")
    expected_response = [
        {
            "name": "тест-магазин",
            "city": "Екатеринбург",
            "street": "Мира",
            "house": 1,
            "open": "09:00:00",
            "close": "21:00:00"
        },
        {
            "name": "тест-магазин2",
            "city": "Москва",
            "street": "Ленина",
            "house": 11,
            "open": "09:00:00",
            "close": "21:00:00"}]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
