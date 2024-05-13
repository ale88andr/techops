from django.contrib import admin
from django.utils.html import format_html

from inventory.models.equipment_manufacturer import EquipmentManufacturer
from inventory.models.equipment_type import EquipmentType


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(EquipmentManufacturer)
class EquipmentManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo', )
    list_display_links = ('name', 'display_logo', )
    readonly_fields = ['display_logo']

    @admin.display(description='Логотип')
    def display_logo(self, obj):
        return obj.display_logo
