from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('apps.app_projects.urls')),
    path('api/users/', include('apps.app_users.urls')),
    path('api/payments/', include('apps.app_payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
