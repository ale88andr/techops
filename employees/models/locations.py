"""Модуль описывающий модель Django"""

from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

from employees.constants import LOCATION_NAME, LOCATION_NAME_PLURAL
from employees.models.buildings import Building


class Location(models.Model):
    """Модель Django описывающая локацию рабочего места

    Attributes:
        room (str): Наименование помещения, в котором расположено рабочее место
        cabinet (int): Номер кабинета, в котором расположено рабочее место
        floor (int): Этаж на котором расположено рабочее место
        building (int): FK->Building, здание в котором расположено рабочее место

    """

    room = models.CharField('Помещение', max_length=25, null=True, blank=True)
    cabinet = models.PositiveIntegerField('Кабинет', null=True, blank=True)
    floor = models.PositiveIntegerField('Этаж', null=True, blank=True)
    building = models.ForeignKey(
        to=Building,
        on_delete=models.PROTECT,
        related_name='building_obj',
        verbose_name='Здание'
    )

    @property
    @admin.display(description="Рабочее место",)
    def name(self):
        """Функция, возвращающая строковое представление рабочего места"""
        location = f'Кабинет №{self.cabinet}' if self.cabinet else f'Помещение "{self.room}"'
        floor = f' (Этаж: {self.floor})' if self.floor else ''
        return f'{location} по адресу: {self.building.address}{floor}'

    def clean(self, *args, **kwargs):
        if self.room is None and self.cabinet is None:
            raise ValidationError(
                'Одно из полей "Помещение" или "Кабинет" должно быть заполнено!',
                code="invalid"
            )
        super().clean()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = LOCATION_NAME
        verbose_name_plural = LOCATION_NAME_PLURAL
        ordering = ('building', 'cabinet', )
