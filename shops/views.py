from datetime import datetime

from django.db.models import F, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shops.models import Shop
from shops.serializers import ShopListSerializer, ShopCreateSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    default_serializer = ShopListSerializer
    serializers = {
        "list": ShopListSerializer,
        "create": ShopCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"id": serializer.data["id"]}, status=status.HTTP_200_OK, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        street = request.GET.get('street')
        if street:
            self.queryset = self.queryset.filter(street__id=int(street))

        city = request.GET.get('city')
        if city:
            self.queryset = self.queryset.filter(city__id=int(city))

        """Если задан параметр open, сравниваем текущее время сервера и время работы магазина.
        Рассмотрены две ситуации, с учетом возможного смещения времени работы на следующие сутки"""
        open = request.GET.get('open')
        if open:
            time_now = datetime.now().time()
            if open == "1":
                self.queryset = self.queryset.filter(
                    Q(open_utc__lt=F("close_utc")) & Q(open_utc__lte=time_now, close_utc__gt=time_now)
                    | Q(open_utc__gt=F("close_utc")) & (Q(open_utc__lt=time_now) | Q(close_utc__gt=time_now)))
            elif open == "0":
                self.queryset = self.queryset.filter(
                    Q(open_utc__lt=F("close_utc")) & (Q(open_utc__gt=time_now) | Q(close_utc__lte=time_now))
                    | Q(open_utc__gt=F("close_utc")) & Q(open_utc__gt=time_now, close_utc__lt=time_now))

        return super().list(request, *args, **kwargs)
