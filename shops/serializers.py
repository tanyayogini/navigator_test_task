from datetime import datetime

from pytz import timezone
from rest_framework import serializers

from shops.models import Shop


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'open', 'close']

    def create(self, validated_data):
        """При создании магазина заполняем поля, которые хранят данные о времени работы в UTC.
        Чтобы возпользоваться смещением по времени из данных таймзоны, создаем дату с необходимым временем"""
        open = validated_data["open"]
        close = validated_data["close"]
        city = validated_data["city"]

        date = datetime(2023,1,1).astimezone(timezone(city.tz)).replace(
            hour=open.hour,
            minute=open.minute)
        date_utc = date.astimezone(timezone("UTC"))
        validated_data["open_utc"] = date_utc.time()

        date = datetime(2023, 1, 1).astimezone(timezone(city.tz)).replace(
            hour=close.hour,
            minute=close.minute)
        date_utc = date.astimezone(timezone("UTC"))
        validated_data["close_utc"] = date_utc.time()

        shop = Shop.objects.create(**validated_data)
        shop.save()
        return shop


class ShopListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Shop
        fields = ['name', 'city', 'street', 'house', 'open', 'close']
