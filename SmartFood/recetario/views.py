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

import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging

from Account.models import RelacionUsuarioComida
from django.http import JsonResponse

logger = logging.getLogger(__name__)

@csrf_exempt
def guardarid(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Accede al nombre de usuario del usuario autenticado
        username_value = request.user.username

        # Imprime el valor en la consola o realiza otras operaciones
        print(f'Valor de username: {username_value}')

        # Accede al id del usuario autenticado
        id_value = request.user.id

        # Imprime el valor en la consola o realiza otras operaciones
        print(f'Valor de id: {id_value}')

        # Verifica si el método es POST
        if request.method == 'POST':
            alimento_id = request.POST.get('id')

            # Guarda el ID en la sesión
            request.session['id_alimento_seleccionado'] = alimento_id

            # Imprime el valor en la consola o realiza otras operaciones
            print(f'ID guardado: {alimento_id}')
            logger.info(f'ID guardado: {alimento_id}')

            # Crea una nueva instancia de RelacionUsuarioComida y la guarda en la base de datos
            relacion_usuario_comida = RelacionUsuarioComida(usuario_id=id_value, comida_id=alimento_id)
            relacion_usuario_comida.save()

            return JsonResponse({'success': True})
    
    # En caso de que el usuario no esté autenticado o el método no sea POST
    return JsonResponse({'success': False})
