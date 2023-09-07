from django.db import models
from geo.models import City, Street


class Shop(models.Model):
    """Модель магазина. Добавлены поля, чтобы хранить время октрытия и закрытия в UTC"""
    name = models.CharField(max_length=100, verbose_name="Название магазина")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name="Улица")
    house = models.PositiveSmallIntegerField(verbose_name="Дом")
    open = models.TimeField(verbose_name="Время открытия")
    close = models.TimeField(verbose_name="Время закрытия")
    open_utc = models.TimeField(blank=True, null=True)
    close_utc = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
