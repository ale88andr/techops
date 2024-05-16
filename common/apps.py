"""Module providing common app settings."""

from django.apps import AppConfig


class CommonConfig(AppConfig):
    """Class representing a common app config"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'
