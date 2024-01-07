from django.shortcuts import render
from django.db.models import Q
from .models import Alimento2


def recetario_view(request):
    return render(request, 'recetario/index_2.html')

def buscar(request):
    termino_busqueda = request.GET.get('termino_busqueda', '')

    if termino_busqueda:
        # Realizar la búsqueda utilizando Q objects para hacer consultas OR
        resultados = Alimento2.objects.filter(Q(nombre_del_alimento__icontains=termino_busqueda) | Q(codigomex2__icontains=termino_busqueda))
    else:
        resultados = Alimento2.objects.all()

    return render(request, 'recetario/busqueda_resultados.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda})
