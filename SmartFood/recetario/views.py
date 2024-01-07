from django.shortcuts import render

def recetario_view(request):
    return render(request, 'recetario/index_2.html')