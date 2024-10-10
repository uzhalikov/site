from django.contrib import admin
from django.urls import path, include
from backend import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('adminpan/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)