"""Модуль описывающий модель Django"""

import os

from django.db import models
from django.utils.functional import cached_property
from django.utils.html import format_html

from inventory.constants import (
    EQUIPMENT_MANUFACTURER_NAME,
    EQUIPMENT_MANUFACTURER_NAME_PLURAL,
    LOGO_IMG_WIDTH,
    MANUFACTURER_MEDIA_DIR,
    NO_IMAGE_HTML
)


""" Change original file name to Manufacturer model field 'name' """
def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(MANUFACTURER_MEDIA_DIR, f'{instance.name}.{ext}')


class EquipmentManufacturer(models.Model):
    """Модель Django описывающая производителя оборудования

    Attributes:
        name (str): Наименование производителя.
        logo (str): Логотип производителя.

    """

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

    @cached_property
    def display_logo(self):
        """Функция, возвращающая HTML тег img с логотипом"""
        return format_html(
            f'<img src="{self.logo.url}" width="{LOGO_IMG_WIDTH}">' if self.logo else NO_IMAGE_HTML
        )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inventory_equipment_manufacturer'
        verbose_name = EQUIPMENT_MANUFACTURER_NAME
        verbose_name_plural = EQUIPMENT_MANUFACTURER_NAME_PLURAL
        ordering = ('name', )
