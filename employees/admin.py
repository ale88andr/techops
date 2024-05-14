from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db.models import Count

from employees.models.buildings import Building
from employees.models.departments import Department
from employees.models.locations import Location
from employees.models.organisations import Organisation
from employees.models.positions import Position
from employees.models.structures import Structure
from employees.models.workers import Worker
from inventory.models.equipment import Equipment


class WorkerEquipmentsInline(TabularInline):
    model = Equipment
    fields = ('equipment_model', 'status', )


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'address')


@admin.register(Structure)
class OrganisationStructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'organisation')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'structure', 'structure_organisation')
    list_select_related = ('structure', 'structure__organisation')
    list_filter = ['structure', 'structure__organisation']

    @admin.display(description="Организация")
    def structure_organisation(self, obj):
        return obj.structure.organisation


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('default_name', )
    list_filter = ['city']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ['building']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'position', 'department', 'equipments_count')
    list_filter = ['department', 'position', 'location']

    inlines = [
        WorkerEquipmentsInline
    ]

    @admin.display(description="Кол-во оборудования")
    def equipments_count(self, obj):
        return obj.equipments_count

    def get_queryset(self, request):
        queryset = Worker.objects.annotate(
            equipments_count = Count('owner_equipments')
        )

        return queryset
