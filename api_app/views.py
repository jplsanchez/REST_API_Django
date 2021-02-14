from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Element

# Create your views here.

def list_elements(request):
    elements = Element.objects.all()
    elements_list = serializers.serialize('json', elements) # converte o QuerySet para lista
    return HttpResponse(elements_list, content_type="text/json-comment-filtered")
    
    # return render(request, 'list.html',{'elements':elements})