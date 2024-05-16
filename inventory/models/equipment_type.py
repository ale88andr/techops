"""Модуль описывающий модель Django"""

from django.db import models

from inventory.constants import EQUIPMENT_TYPE_NAME, EQUIPMENT_TYPE_NAME_PLURAL


class EquipmentType(models.Model):
    """Модель Django описывающая тип оборудования

    Attributes:
        name (str): Наименование здания.

    """

    name = models.CharField(
        'Тип оборудования',
        max_length=50,
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inventory_equipment_type'
        verbose_name = EQUIPMENT_TYPE_NAME
        verbose_name_plural = EQUIPMENT_TYPE_NAME_PLURAL
        ordering = ('name', )
