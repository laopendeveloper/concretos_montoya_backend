"""Clients URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import MachineViewSet, MachineTypeViewSet, MachineFilesViewSet

router = DefaultRouter()
router.register(r'machines', MachineViewSet, basename='machines')
router.register(r'machine_type', MachineTypeViewSet, basename='machine_type')
router.register(r'machine_files', MachineFilesViewSet, basename='machine_files')

urlpatterns = [
    path('', include(router.urls))
]
