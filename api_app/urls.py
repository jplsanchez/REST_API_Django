from django.urls import path
from django.urls.conf import include
from .views import description, get_users, create_user
from . import views

from rest_framework import routers
from .views import UserViewSet, UserTypeViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('user_type', UserTypeViewSet)

urlpatterns = [
    path('get/', get_users, name='get_users'),
    path('add/', create_user, name='create_user'),
    path('', include(router.urls)),
    path('home/', views.home, name='home'),
    path('<int:user_id>/', views.description, name='description'),
    path('<int:user_id>/created_recently/', views.created_recently, name='created_recently'),
]
