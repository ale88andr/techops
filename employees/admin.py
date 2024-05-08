from django.contrib import admin

from employees.models.departments import Department
from employees.models.organisations import Organisation
from employees.models.structures import Structure


admin.site.empty_value_display = "(Нет данных)"


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
