from django.db import models

from inventory.constants import EQUIPMENT_MODEL_NAME, EQUIPMENT_MODEL_NAME_PLURAL
from inventory.models.equipment_manufacturer import EquipmentManufacturer
from inventory.models.equipment_type import EquipmentType


class EquipmentModel(models.Model):
    name = models.CharField(
        'Модель оборудования',
        max_length=50,
        unique=True,
        db_index=True
    )
    description = models.TextField('Описание', null=True, blank=True)
    manufacturer = models.ForeignKey(
        to=EquipmentManufacturer,
        on_delete=models.PROTECT,
        related_name='manufacturer_models',
        verbose_name='Производитель'
    )
    equipment_type = models.ForeignKey(
        to=EquipmentType,
        on_delete=models.PROTECT,
        related_name='type_models',
        verbose_name='Тип оборудования'
    )


    def __str__(self):
        return f'{self.equipment_type}: {self.manufacturer} {self.name}'

    class Meta:
        db_table = 'inventory_equipment_model'
        verbose_name = EQUIPMENT_MODEL_NAME
        verbose_name_plural = EQUIPMENT_MODEL_NAME_PLURAL
        ordering = ('equipment_type', 'manufacturer', 'name', )
