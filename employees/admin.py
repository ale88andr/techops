from django.contrib import admin

from employees.models.buildings import Building
from employees.models.departments import Department
from employees.models.locations import Location
from employees.models.organisations import Organisation
from employees.models.positions import Position
from employees.models.structures import Structure


admin.site.site_header = 'TechOps'
admin.site.empty_value_display = '(Нет данных)'


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
