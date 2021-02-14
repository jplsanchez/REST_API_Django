from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.core import serializers
from .models import User

# Create your views here.

def get_users(request):
    users = User.objects.all()
    users_list = serializers.serialize('json', users) # converte o QuerySet para lista
    return HttpResponse(users_list, content_type="text/json-comment-filtered")
    
    # return render(request, 'list.html',{'elements':elements})

def create_user(request):
    pass