from django.db import models

from employees.models.structures import Structure


class Department(models.Model):
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
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('name', )
