"""Модуль описывающий модель Django"""

from django.db import models

from employees.constants import ORGANISATION_NAME, ORGANISATION_NAME_PLURAL


class Organisation(models.Model):
    """Модель Django описывающая организацию

    Attributes:
        name (str): Наименование организации.
        short_name  (str): Краткое наименование.
        address (str): Адрес организации.
        director (str): Управляющий организацией

    """

    name = models.CharField('Наименование', max_length=255)
    short_name = models.CharField('Краткое наименование', max_length=50, null=True, blank=True)
    address = models.CharField('Адрес', max_length=150, null=True, blank=True)
    director = models.CharField('Управляющий', max_length=70, null=True, blank=True)

    def __str__(self) -> str:
        return self.short_name

    class Meta:
        verbose_name = ORGANISATION_NAME
        verbose_name_plural = ORGANISATION_NAME_PLURAL
        ordering = ('name', )
