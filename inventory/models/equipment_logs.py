from django.conf import settings
from django.contrib import admin
from django.db import models
from django.utils.timezone import localtime

from inventory.constants import EQUIPMENT_LOG_NAME, EQUIPMENT_LOG_NAME_PLURAL


class EquipmentLog(models.Model):
    action = models.CharField('Событие', max_length=250)
    target_field = models.CharField(
        'Измененный параметр',
        max_length=250,
        null=True,
        blank=True
    )
    old_value = models.CharField(
        'Старое значение',
        max_length=250,
        null=True,
        blank=True
    )
    new_value = models.CharField(
        'Новое значение',
        max_length=250,
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        verbose_name='Инициатор',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def _format_created_at(self, format='%Y-%m-%d %H:%M'):
        return localtime(self.created_at).strftime(format)

    @property
    def log(self):
        log_list = [f'Дата: {self._format_created_at()}', self.action]
        if self.target_field:
            log_list.append(f'поле "{self.target_field}"')
            log_list.append(f'старое значение: "{self.old_value}"')
            log_list.append(f'новое значение: "{self.new_value}"')
        if self.created_by:
            log_list.append(f'Инициатор: {self.created_by}')
        return ', '.join(log_list)

    def __str__(self):
        return self.log

    class Meta:
        db_table = 'inventory_logs'
        verbose_name = EQUIPMENT_LOG_NAME
        verbose_name_plural = EQUIPMENT_LOG_NAME_PLURAL
        ordering = ('-created_at', )
