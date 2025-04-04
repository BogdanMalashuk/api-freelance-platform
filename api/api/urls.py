from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('freelance_api.urls')),
    path('projects/', include('app_projects.urls')),
    path('api/', include('freelance_api.urls')),

]
