from django.contrib import admin

from inventory.models.equipment_manufacturer import EquipmentManufacturer
from inventory.models.equipment_type import EquipmentType


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(EquipmentManufacturer)
class EquipmentManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', )
