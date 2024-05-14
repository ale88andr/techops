from django.db import models
from django.contrib import admin

from employees.constants import BUILDING_NAME, BUILDING_NAME_PLURAL


class Building(models.Model):
    name = models.CharField('Наименование', max_length=100, null=True, blank=True)
    city = models.CharField('Город', max_length=50)
    street = models.CharField('Улица', max_length=50)
    number = models.CharField('Номер', max_length=10)
    index = models.CharField('Индекс', max_length=10)

    @property
    @admin.display(description="Адрес",)
    def address(self):
        return f'{self.index}, г. {self.city}, ул. {self.street}, д. {self.number}'

    @property
    def default_name(self):
        return self.name if self.name else f'Здание по адресу: {self.address}'

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = BUILDING_NAME
        verbose_name_plural = BUILDING_NAME_PLURAL
        ordering = ('city', 'index', )
