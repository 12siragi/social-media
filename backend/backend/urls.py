from django.contrib import admin
from django.conf import settings  # Add this import
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('useraccounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Fixed this line
