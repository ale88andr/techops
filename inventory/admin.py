from django.contrib import admin

from inventory.models.equipment_type import EquipmentType


@admin.register(EquipmentType)
class OrganisationStructureAdmin(admin.ModelAdmin):
    list_display = ('name', )
