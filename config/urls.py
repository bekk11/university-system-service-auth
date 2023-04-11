# Django
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .yasg import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('apps/', include('apps.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += swagger_urls
