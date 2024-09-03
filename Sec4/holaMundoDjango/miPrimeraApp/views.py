from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.

def miPrimeraVista(request):
    return HttpResponse("<h1>Hola mundo desde Django 😊</h1>")

def miSegundaVista(request):
    dt = datetime.datetime.now()
    salida = "<b>Fecha y hora actual:</b>" + str(dt)
    return HttpResponse(salida)