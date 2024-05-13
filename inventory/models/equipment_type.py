from django.db import models


class EquipmentType(models.Model):
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
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'
        ordering = ('name', )
