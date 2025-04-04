from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('apps.app_projects.urls')),
    path('api/users/', include('apps.app_users.urls')),
    path('api/payments/', include('apps.app_payments.urls')),
]
