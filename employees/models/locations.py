from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

from employees.models.buildings import Building


class Location(models.Model):
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
        location = f'Кабинет №{self.cabinet}' if self.cabinet else f'Помещение "{self.room}"'
        floor = f' (Этаж: {self.floor})' if self.floor else ''
        return f'{location} по адресу: {self.building.address}{floor}'

    def clean(self, *args, **kwargs):
        if self.room is None and self.cabinet is None:
            raise ValidationError(
                'Одно из полей "Помещение" или "Кабинет" должно быть заполнено!',
                code="invalid"
            )
        super(Location, self).clean()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'
        ordering = ('building', 'cabinet', )
