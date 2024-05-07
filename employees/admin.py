from django.contrib import admin

from employees.models.organisations import Organisation
from employees.models.structures import Structure


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'address')


@admin.register(Structure)
class OrganisationStructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'organisation')
