from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = 'astramedClinic'

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('astramedClinic.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


