from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('backend/', admin.site.urls),
    path('employees/', include('employees.urls'))
]
