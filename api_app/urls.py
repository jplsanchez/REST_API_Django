from django.urls import path
from .views import list_elements

urlpatterns = [
    path('', list_elements, name='list_element'),
]

#CRUD - CREATE, READ, UPDATE, DELETE