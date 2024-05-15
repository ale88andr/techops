from django.conf import settings
from django.db import models

from employees.models.workers import Worker
from inventory.constants import EQUIPMENT_NAME, EQUIPMENT_NAME_PLURAL
from inventory.models.equipment_logs import EquipmentLog
from inventory.models.equipment_model import EquipmentModel


class Equipment(models.Model):
    class EquipmentStatuses(models.IntegerChoices):
        USE = 1, 'В эксплуатации'
        WRITEOFF = 2, 'Списан'
        REPAIR = 3, 'В ремонте'

    serial = models.CharField(
        'Серийный номер',
        max_length=50,
        db_index=True,
        null=True,
        blank=True
    )
    inv = models.CharField(
        'Инвентарный номер',
        max_length=50,
        db_index=True,
        unique=True
    )
    owner = models.ForeignKey(
        to=Worker,
        on_delete=models.PROTECT,
        related_name='owner_equipments',
        verbose_name='В пользовании у'
    )
    equipment_model = models.ForeignKey(
        to=EquipmentModel,
        on_delete=models.PROTECT,
        related_name='model_equipments',
        verbose_name='Модель оборудования'
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        related_name='child_equipments',
        verbose_name='В составе оборудования',
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name='created_by',
        verbose_name='Добавил пользователь'
    )
    status = models.SmallIntegerField(
        'Статус оборудования',
        choices=EquipmentStatuses,
        default=EquipmentStatuses.USE
    )
    logs = models.ManyToManyField(to=EquipmentLog)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.inv}] {self.equipment_model}'

    # @TODO Refactor!
    def save(self, *args, **kwargs):
        prev_state = Equipment.objects.filter(pk=self.pk).first() if self.pk else None
        super().save(*args, **kwargs)
        if prev_state:
            if prev_state.serial != self.serial:
                self.logs.create(
                    action='Изменение',
                    target_field='Серийный номер',
                    old_value=prev_state.serial,
                    new_value=self.serial,
                    created_by=self.created_by
                )
            if prev_state.inv != self.inv:
                self.logs.create(
                    action='Изменение',
                    target_field='Инвентарный номер',
                    old_value=prev_state.inv,
                    new_value=self.inv,
                    created_by=self.created_by
                )
            if prev_state.owner != self.owner:
                self.logs.create(
                    action='Изменение',
                    target_field='Владелец',
                    old_value=str(prev_state.owner),
                    new_value=str(self.owner),
                    created_by=self.created_by
                )
            if prev_state.status != self.status:
                self.logs.create(
                    action='Изменение',
                    target_field='Статус',
                    old_value=prev_state.get_status_display(),
                    new_value=self.get_status_display(),
                    created_by=self.created_by
                )
        else:
            self.logs.create(action=f'Создание записи об оборудовании "{str(self)}"')

    class Meta:
        verbose_name = EQUIPMENT_NAME
        verbose_name_plural = EQUIPMENT_NAME_PLURAL
        ordering = ('inv', )
