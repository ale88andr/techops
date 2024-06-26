"""Модуль описывающий модель Django"""

from django.db import models

from employees.constants import POSITION_NAME, POSITION_NAME_PLURAL


class Position(models.Model):
    """Модель Django описывающая должности сотрудников

    Attributes:
        name (str): Наименование должности.

    """

    name = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = POSITION_NAME
        verbose_name_plural = POSITION_NAME_PLURAL
        ordering = ('name', )
