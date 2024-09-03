from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("<h1>Hola Mundo 👌😊</h1>")

def miPrimerTemplate(request):
    return render(request, 'templatesApp/miPrimerTemplate.html')

def miSegudnoTemplate(request):
    return render(request, 'templatesApp/miSegundoTemplate.html')

def templateConData(request):
    data = {'nombre': 'Juan', 'edad': 25}
    return render(request, 'templatesApp/miTercerTemplate.html', data)