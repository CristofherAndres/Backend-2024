from django.shortcuts import render

# Create your views here.
def infoEmpleados(request):
    data= {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 25,
        'hobbies': ['Futbol', 'Pintura', 'Cine'],
        'amigos': ['Pedro', 'Maria', 'Jose']
    }
    return render(request, 'empleadosApp/info.html', data) 

def tienda(request):
    return render(request, 'empleadosApp/tienda.html')

def electronica(request):
    data = {
        'seccion': 'Electronica',
    }
    return render(request, 'empleadosApp/detalle.html', data)

def jugueteria(request):
    data = {
        'seccion': 'jugueteria',
    }
    return render(request, 'empleadosApp/detalle.html', data)