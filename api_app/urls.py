from django.urls import path
from django.urls.conf import include
from .views import get_users, create_user

from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('get/', get_users, name='get_users'),
    path('add/', create_user, name='create_user'),
    path('', include(router.urls)),
]
