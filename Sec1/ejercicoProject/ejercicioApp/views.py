from django.shortcuts import render

# Create your views here.

def miTienda(request):
    return render(request, 'ejercicioApp/miTienda.html')

def electronica(request):
    data = {
        'seccion': 'Electrónica',
        'productos': [
            {
            'id':1,
            'nombre': 'Smartphone',
            'descripcion': 'Teléfono inteligente con cámara de 48MP',
            'precio': '$800',
            'imagen': 'https://via.placeholder.com/150/ff0000'
            },
            {
            'id':2,
            'nombre': 'Smartwatch',
            'descripcion': 'Reloj inteligente con GPS',
            'precio': '$200',
            'imagen': 'https://via.placeholder.com/150/00ff00'
            },
            {
            'id':3,
            'nombre': 'Tablet',
            'descripcion': 'Tablet con pantalla de 10 pulgadas',
            'precio': '$500',
            'imagen': 'https://via.placeholder.com/150/0000ff'
            }
        ]
    }
    return render(request, 'ejercicioApp/productos.html', data)

def detallesProducto(request, idProducto):
    productos = [
            {
            'id':1,
            'nombre': 'Smartphone',
            'descripcion': 'Teléfono inteligente con cámara de 48MP',
            'precio': '$800',
            'imagen': 'https://via.placeholder.com/150/ff0000'
            },
            {
            'id':2,
            'nombre': 'Smartwatch',
            'descripcion': 'Reloj inteligente con GPS',
            'precio': '$200',
            'imagen': 'https://via.placeholder.com/150/00ff00'
            },
            {
            'id':3,
            'nombre': 'Tablet',
            'descripcion': 'Tablet con pantalla de 10 pulgadas',
            'precio': '$500',
            'imagen': 'https://via.placeholder.com/150/0000ff'
            }
    ]

    # Buscar el producto por su id
    producto = None
    for p in productos:
        if p['id'] == idProducto:
            producto = p
            break
    return render(request, 'ejercicioApp/detalles.html', {'producto' : producto})