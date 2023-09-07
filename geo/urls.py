from django.urls import path, include
from rest_framework_nested import routers

from geo.views import CityViewSet, StreetViewSet

city_router = routers.SimpleRouter()
city_router.register(r"", CityViewSet, basename='city')

streets_router = routers.NestedSimpleRouter(city_router, r'', lookup='city')
streets_router.register(r"street", StreetViewSet, basename="streets")

urlpatterns = [
    path('', include(city_router.urls)),
    path('', include(streets_router.urls)),
]
