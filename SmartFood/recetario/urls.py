from django.urls import path
from .views import recetario_view
from .views import buscar

urlpatterns = [
    path('', recetario_view, name='recetario'),
     path('buscar/', buscar, name='buscar'),
    
    
]
