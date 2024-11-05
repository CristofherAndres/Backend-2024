from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'titulo': 'Repaso Django envio de datos',
        'comidaTipica': ['Humitas', 'Empanadas', 'Completos', 'Asado', 'Cazuela'],
        'paises' : [
                {
                'nombre':'Chile',
                'capital':'Santiago',
                },
                {
                'nombre':'Argentina',
                'capital':'Buenos Aires',
                }
        ]
    }
    return render(request, 'repasoApp/index.html', data)

def empleadoData(request):
    empleados = Empleados.objects.all()