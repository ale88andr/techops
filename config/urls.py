"""Module providing urls for django app."""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('backend/', admin.site.urls),
    path('employees/', include('employees.urls')),
    path('equipments/', include('inventory.urls')),
]

# url rule for media root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
