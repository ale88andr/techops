"""Общие настройки для админ панели Django"""

from django.contrib import admin

from common.constants import PROJECT_NAME, DEFAULT_NULL_VALUE


admin.site.site_header = PROJECT_NAME
admin.site.empty_value_display = DEFAULT_NULL_VALUE
