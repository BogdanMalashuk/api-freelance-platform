from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('apps.projects.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/payments/', include('apps.bookings.urls')),
]
