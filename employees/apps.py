"""Module providing an employee app settings."""

from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    """Class representing settings for employees app"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'
    verbose_name = 'Штатное расписание'
