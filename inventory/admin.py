from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from inventory.models.equipment import Equipment
from inventory.models.equipment_logs import EquipmentLog
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
    list_display = ('__str__', 'owner_link', 'status')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'get_logs')
    list_select_related = ('owner', 'equipment_model')
    search_fields = ['inv', 'serial', ]
    list_filter = ['status', 'equipment_model__equipment_type']
    radio_fields = {'status': admin.HORIZONTAL}
    exclude = ['logs']

    @admin.display(description='Аудит')
    def get_logs(self, obj):
        return '\n'.join([str(log) for log in obj.logs.all()])

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def owner_link(self, obj):
        link = reverse('admin:employees_worker_change', args=[obj.owner.id])
        return format_html('<a href="{}">{}</a>', link, obj.owner)


@admin.register(EquipmentLog)
class EquipmentLogAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_by', 'created_at')
    readonly_fields = ('__str__', 'created_by', 'created_at')
