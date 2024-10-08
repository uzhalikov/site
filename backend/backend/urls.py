from django.contrib import admin
from django.urls import path, include
from backend import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminpan/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)