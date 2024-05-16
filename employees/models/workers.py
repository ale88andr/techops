"""Модуль описывающий модель Django"""

from django.db import models
from django.contrib import admin

from employees.constants import WORKER_NAME, WORKER_NAME_PLURAL
from employees.models.departments import Department
from employees.models.locations import Location
from employees.models.positions import Position


class Worker(models.Model):
    """Модель Django описывающая сотрудника организации

    Attributes:
        surname (str): Фамилия.
        name (str): Имя.
        patronymic (str): Отчество.
        phone (str): Номер телефона.
        domain_sid (str): Учетная запись домена
        position (int):  FK->Position, Должность сотрудника.
        location (int):  FK->Location, Рабочее место сотрудника.
        department (int):  FK->Department, Отдел сотрудника.

    """

    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20, null=True, blank=True)
    phone = models.CharField('Внутренний телефон', max_length=20, null=True, blank=True)
    domain_sid = models.CharField('Учётная запись в домене', max_length=50, null=True, blank=True)
    position = models.ForeignKey(
        to=Position,
        on_delete=models.CASCADE,
        related_name='position_workers',
        verbose_name='Должность'
    )
    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE,
        related_name='location_workers',
        verbose_name='Рабочее место'
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        related_name='department_workers',
        verbose_name='Отдел'
    )

    @property
    def full_name(self):
        """Функция, возвращающая полное имя сотрудника"""
        patronymic = self.patronymic if self.patronymic else ''
        return f'{self.surname} {self.name} {patronymic}'

    @property
    @admin.display(description="Сотрудник",)
    def short_name(self):
        """Функция, возвращающая фамилию и инициалы сотрудника"""
        patronymic = f'{self.patronymic[0]}.' if self.patronymic else ''
        return f'{self.surname} {self.name[0]}. {patronymic}'

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = WORKER_NAME
        verbose_name_plural = WORKER_NAME_PLURAL
        ordering = ('name', )
