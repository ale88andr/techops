import os

from django.db import models


# @TODO Move to settings or env and rename
UPLOAD_DIR = 'images/manufacturer/logo'


""" Change original file name to Manufacturer model field 'name' """
def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(UPLOAD_DIR, f'{instance.name}.{ext}')


class EquipmentManufacturer(models.Model):
    name = models.CharField(
        'Производитель',
        max_length=50,
        unique=True,
        db_index=True
    )
    logo = models.ImageField(
        upload_to=wrapper,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inventory_equipment_manufacturer'
        verbose_name = 'Производитель оборудования'
        verbose_name_plural = 'Производители оборудования'
        ordering = ('name', )
