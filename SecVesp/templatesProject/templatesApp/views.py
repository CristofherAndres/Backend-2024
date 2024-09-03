from django.shortcuts import render
#importar httpresponse
from django.http import HttpResponse

# Create your views here.

def holaMundo(request):
    return HttpResponse("<h1>Hola Mundo 😊</h1>")

def miPrimerTemplate(request):
    return render(request,'templatesApp/miPrimerTemplate.html')

def templateConData(request):
    data = {'nombre':'Juan','edad':25, 'ciudad':'Lima', 'estatura':1.75}
    return render(request, 'templatesApp/miSegundoTemplate.html', data)
