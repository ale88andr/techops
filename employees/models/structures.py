from django.db import models

from employees.models.organisations import Organisation


class Structure(models.Model):
    name = models.CharField('Наименование', max_length=255)
    organisation = models.ForeignKey(
        to=Organisation,
        on_delete=models.PROTECT,
        related_name='organisation_structure',
        verbose_name='Организация'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Организационную структуру'
        verbose_name_plural = 'Организационные структуры'
        ordering = ('name', )
