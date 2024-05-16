"""Module providing an inventory app settings."""

from django.apps import AppConfig


class InventoryConfig(AppConfig):
    """Class representing settings for inventory app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"
    verbose_name = 'Учёт техники'
