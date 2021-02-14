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
    elements = Element.object.all()
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



