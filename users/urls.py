"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


# Views
from .views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'users_type', user_views.UserTypeViewSet, basename='users_type')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', user_views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
