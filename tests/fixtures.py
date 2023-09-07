import pytest

from geo.models import City, Street
from shops.models import Shop


@pytest.mark.django_db
@pytest.fixture
def get_city1():
    city = City.objects.create(name='Екатеринбург', tz='Asia/Yekaterinburg')
    return city


@pytest.mark.django_db
@pytest.fixture
def get_city2():
    city = City.objects.create(name='Москва', tz='Europe/Moscow')
    return city


@pytest.mark.django_db
@pytest.fixture
def get_street1(get_city1):
    street = Street.objects.create(name='Мира', city=get_city1)
    return street


@pytest.mark.django_db
@pytest.fixture
def get_street2(get_city2):
    street = Street.objects.create(name='Ленина', city=get_city2)
    return street


@pytest.mark.django_db
@pytest.fixture
def get_shop1(get_city1, get_street1):
    data = {"name": "тест-магазин",
            "city": get_city1,
            "street": get_street1,
            "house": 1,
            "open": "9:00",
            "close": "21:00"}
    shop = Shop.objects.create(**data)
    return shop


@pytest.mark.django_db
@pytest.fixture
def get_shop2(get_city2, get_street2):
    data = {"name": "тест-магазин2",
            "city": get_city2,
            "street": get_street2,
            "house": 11,
            "open": "9:00",
            "close": "21:00"}
    shop = Shop.objects.create(**data)
    return shop
