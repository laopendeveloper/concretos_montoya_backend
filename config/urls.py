"""Main URLs module."""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('clients/', include(('clients.urls', 'clients'), namespace='clients')),
    path('machines/', include(('machines.urls', 'machines'), namespace='machines'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
