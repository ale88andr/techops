import os

from django.db import models
from django.utils.functional import cached_property
from django.utils.html import format_html


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

    # @TODO remove hardcoded values
    @cached_property
    def display_logo(self):
        if self.logo:
            return format_html(f'<img src="{self.logo.url}" width="45">')
        return format_html('<strong>Изображение отсутствует<strong>')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inventory_equipment_manufacturer'
        verbose_name = 'Производителя оборудования'
        verbose_name_plural = 'Производители оборудования'
        ordering = ('name', )
