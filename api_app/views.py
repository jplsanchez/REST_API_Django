from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Element

# Create your views here.

def list_elements(request):
    elements = Element.object.all()
    elements_list = list(elements) # converte o QuerySet para lista
    return JsonResponse(elements_list, safe=False)
    
    # return render(request, 'list.html',{'elements':elements})