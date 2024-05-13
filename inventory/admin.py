from django.contrib import admin

from inventory.models.equipment import Equipment
from inventory.models.equipment_manufacturer import EquipmentManufacturer
from inventory.models.equipment_model import EquipmentModel
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


@admin.register(EquipmentModel)
class EquipmentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'equipment_type')
    list_select_related = ('manufacturer', 'equipment_type')
    list_filter = ['equipment_type', 'manufacturer']
    search_fields = ['name', 'manufacturer', 'equipment_type']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner')
    readonly_fields = ('created_at', 'updated_at')
    exclude = ['created_by']
    list_select_related = ('owner', 'equipment_model')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
