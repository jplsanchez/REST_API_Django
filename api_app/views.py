from django.http.response import HttpResponse
from django.core import serializers as django_serializers

from .models import User, UserType
from rest_framework import viewsets
from .serializers import UserSerializer, UserTypeSerializer

# Create your views here.

def get_users(request):
    users = User.objects.all()
    users_list = django_serializers.serialize('json', users) # converte o QuerySet para lista
    return HttpResponse(users_list, content_type="text/json-comment-filtered")
    
    # return render(request, 'list.html',{'elements':elements})

def create_user(request):
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer