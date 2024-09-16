from django.shortcuts import render

# Create your views here.
def infoEmpleado(request):
    data = {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 25,
        'hobbies': ['futbol', 'videojuegos', 'leer'],
        'amigos': ['Pedro', 'Maria', 'Jose']
    }
    return render(request, 'empleadosApp/info.html', data)


def miTienda(request):
    return render(request, 'empleadosApp/tienda.html')

def electronica(request):
    data = {
        'seccion': 'Electronica',
    }
    return render(request, 'empleadosApp/detalle.html',data)

def jugueteria(request):
    data = {
        'seccion': 'Jugueteria',
    }
    return render(request, 'empleadosApp/detalle.html',data)