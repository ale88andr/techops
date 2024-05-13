from django.conf import settings
from django.db import models

from employees.models.workers import Worker
from inventory.models.equipment_model import EquipmentModel


class Equipment(models.Model):
    class EquipmentStatuses(models.IntegerChoices):
        USE = 1, 'В эксплуатации'
        WRITEOFF = 2, 'Списан'
        REPAIR = 3, 'В ремонте'

    serial = models.CharField(
        'Серийный номер',
        max_length=50,
        db_index=True,
        null=True,
        blank=True
    )
    inv = models.CharField(
        'Инвентарный номер',
        max_length=50,
        db_index=True,
        unique=True
    )
    owner = models.ForeignKey(
        to=Worker,
        on_delete=models.PROTECT,
        related_name='owner_equipments',
        verbose_name='В пользовании у'
    )
    equipment_model = models.ForeignKey(
        to=EquipmentModel,
        on_delete=models.PROTECT,
        related_name='model_equipments',
        verbose_name='Модель оборудования'
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        related_name='child_equipments',
        verbose_name='В составе оборудования',
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name='created_by',
        verbose_name='Добавил пользователь'
    )
    status = models.SmallIntegerField(
        'Статус оборудования',
        choices=EquipmentStatuses,
        default=EquipmentStatuses.USE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.inv}] {self.equipment_model}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ('inv', )
