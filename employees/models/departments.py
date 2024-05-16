"""Модуль описывающий модель Django"""

from django.db import models

from employees.constants import DEPARTMENT_NAME, DEPARTMENT_NAME_PLURAL
from employees.models.structures import Structure


class Department(models.Model):
    """Модель Django описывающая структурное подразделение сотрудника

    Attributes:
        name (str): Наименование подразделения.
        structure (int): FK->Structure, Организационная структура подразделения.

    """

    name = models.CharField('Наименование', max_length=255)
    structure = models.ForeignKey(
        to=Structure,
        on_delete=models.PROTECT,
        related_name='structure_departments',
        verbose_name='Организационное подразделение'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = DEPARTMENT_NAME
        verbose_name_plural = DEPARTMENT_NAME_PLURAL
        ordering = ('name', )
