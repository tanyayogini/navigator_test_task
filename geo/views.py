from rest_framework import viewsets

from geo.models import City, Street
from geo.serializers import CitySerializer, StreetSerializer


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class StreetViewSet(viewsets.ModelViewSet):
    serializer_class = StreetSerializer

    def get_queryset(self):
        return Street.objects.filter(city=self.kwargs['city_pk'])


