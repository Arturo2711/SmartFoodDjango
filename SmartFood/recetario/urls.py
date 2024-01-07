from django.urls import path
from .views import recetario_view

urlpatterns = [
    path('recetario/', recetario_view, name='recetario'),
]