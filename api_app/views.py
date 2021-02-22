from django import template
from django.http.response import HttpResponse
from django.core import serializers as django_serializers

from .models import User, UserType
from rest_framework import viewsets
from .serializers import UserSerializer, UserTypeSerializer

from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# VIEWS JSON

def get_users(request):
    users = User.objects.all()
    users_list = django_serializers.serialize('json', users) # converte o QuerySet para lista
    return HttpResponse(users_list, content_type="text/json-comment-filtered")
    
def create_user(request):
    pass

 # VIEWSET DOS SERIALIZERS

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

# VIEWS HTTP

def home(request): # versao explicita pro aprendizado de view com template
    users_list = User.objects.order_by('date_created')[:5]
    template = loader.get_template('api_app/home.html')
    context = {
        'users_list': users_list,
    }

    return HttpResponse(template.render(context, request))

def description(request, user_id): # versão aprimorada de view com template
    '''
    try:
        u = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("Usuário não existe")
    '''
    u = get_object_or_404(User, id=user_id)
    return render(request, 'api_app/description.html', {'user':u})


def created_recently(request, user_id): # versão de view fazendo o trabalho do template
    u = User.objects.get(id=user_id)
    if u.was_created_recently():
        return HttpResponse("O usuário {name} foi criado nos ultimos 7 dias".format(name=u.name))
    return HttpResponse("O usuário {name} foi criado a mais de 7 dias".format(name=u.name))