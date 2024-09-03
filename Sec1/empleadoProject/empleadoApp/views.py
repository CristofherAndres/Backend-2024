from django.shortcuts import render

# Create your views here.
def pruebaTemplate(request):
    data = {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 25,
        'hobbies': ['futbol', 'videojuegos', 'leer'],
        'amigos': ['Pedro', 'Maria', 'Jose']
    }
    return render(request, 'empleadoApp/info.html', data)

def tienda(request):
    return render(request, 'empleadoApp/tienda.html')


def jugueteria(request):
    data = {
        'nombre': 'Juguetes'
    }
    return render(request, 'empleadoApp/detalle.html',data)

def electronica(request):
    data = {
        'nombre': 'Electronica'
    }
    return render(request, 'empleadoApp/detalle.html',data)
