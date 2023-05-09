from django.contrib import admin
from myblog.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('myblog.urls')),
    path('admin/', admin.site.urls),
    path("ckeditor/", include('ckeditor_uploader.urls')),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Ловим пустые страницы.
# handler404 = pageNotFound
