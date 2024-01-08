from django.urls import path
from .views import recetario_view
from .views import buscar
from .views import guardarid

urlpatterns = [
    path('', recetario_view, name='recetario'),
    path('buscar/', buscar, name='buscar'),
    path('guardarid/', guardarid, name='guardarid'),
        
]
