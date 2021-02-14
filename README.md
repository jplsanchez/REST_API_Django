# O que estou aprendendo nesse projeto

* Git
* Markdown
* Django
* Django REST Framework - DRF
* *Docker (Futuramente)*
* *PostgreSQL (Futuramente - Integrado com Django)*


<br>

# Criando projeto Django

$ conda activate Django_env

$ Django-admin startproject api .

$ python manage.py runserver

# Git
$ git init

$ git status

$ git add .

$ git commit -m "Configurações iniciais"

### - Adicionar gitignore (Python) e adicionar a ele .vscode/

<br>

# Criando APP

$ Django-admin startapp api_app

### - Adicionar app no settings.py do projeto

### - Setar a url.py no projeto (importar include) e adicionar:

``` Python
path('', include('api_app.urls'))
```
### - Criar um urls.py no app:

``` Python
from django.urls import path

urlpatterns = [
    path('', list_element, name='list_element'),
]
```
### - Adicionar a view no views.py no app:
``` Python
def list_elements(request):
    elements = Element.objects.all()
    return render(request, 'list.html',{'elements':elements})
```
### - Importar as views no urls.py no app 

### - Adicionar o model no model.py no app:
``` Python
class Element(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=true)

    def __str__(self):
         return self.description
```

### - Importar os models no views.py no app 
<br>

# Migrations

$ python manage.py makemigrations

$ python manage.py migrate

# Super User

$ python manage.py createsuperuser

### - Registrar o model no admin.py do app

``` Python
from django.contrib import admin
from .models import Element

# Register your models here.
admin.site.register(Element)
```

# REST Framework

[Link Django REST Base](https://www.django-rest-framework.org/)

[Link Django Rest Extra Tutorial](https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa)


### - Adicionar o app 'rest_framework' no settings.py


### - Criar o serializer.py no app:
``` Python
from rest_framework import  serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','adress','age','description')
```

### - Adicionar a view serializada ao view.py no app:
``` Python
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

### -Adicionar rotas no url.py (adicionei no app, mas pode ser no project):
``` Python
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    ... ,
    path('route',include(router.urls))
]
```

> Adicionar mais um model