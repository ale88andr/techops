from django.contrib import admin

from employees.models.organisations import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'address')
