from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("<h1>Hola Mundo 😎👍</h1>")

def template(request):
    return render(request, 'templatesApp/miPrimerTemplate.html')

def templateConData(request):
    data = {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 30
    }
    return render(request, 'templatesApp/miSegundoTemplate.html', data)