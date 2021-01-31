"""Clients URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import clients as client_views

router = DefaultRouter()
router.register(r'clients', client_views.ClientViewSet, basename='clients')
router.register(r'contacts', client_views.ContactViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls))
]
