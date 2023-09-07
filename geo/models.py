import pytz
from django.db import models


class City(models.Model):
    """в модель Города добавлено поле с часовым поясом - для дальнейшего
    отслеживания работы магазина в текущий момент времени"""
    name = models.CharField(max_length=100, verbose_name="Название города")
    tz = models.CharField(max_length=50, default="Europe/Moscow",
                          choices=((t, t) for t in pytz.common_timezones),
                          verbose_name="Часовой пояс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Street(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название улицы")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
