from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/useraccounts/', include('useraccounts.urls')),  # User accounts API
    path('api/post/', include('post.urls')),  # Include the posts API
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
