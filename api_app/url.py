from django.urls import path

urlpatterns = [
    path('', list_elements, name='list_element'),
]

#CRUD - CREATE, READ, UPDATE, DELETE