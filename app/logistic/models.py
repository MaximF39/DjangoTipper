from django.db import models


class ModelTipper(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название модели", unique=True)
    max_load_capacity = models.IntegerField(verbose_name="Максимальная грузоподъёмность")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель самосвала"
        verbose_name_plural = "Модели самосвалов"
        ordering = ["-id"]


class Tipper(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="Бортовой номер")
    model = models.ForeignKey(ModelTipper, on_delete=models.PROTECT, verbose_name="Модель")
    current_load_capacity = models.IntegerField(verbose_name="Текущий вес")

    @property
    def overload_capacity(self):
        load_percent = self.current_load_capacity / self.model.max_load_capacity * 100
        overload_percent = max([0, load_percent - 100])
        return round(overload_percent, 2)

    overload_capacity.fget.short_description = "Перегруз, %"

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Самосвал"
        verbose_name_plural = "Самосвалы"
        ordering = ["-id"]
