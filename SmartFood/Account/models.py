# En models.py de la aplicación 'account'

from django.db import models
from django.contrib.auth.models import AbstractUser
from recetario.models import Alimento2

class CustomUser(AbstractUser):
    edad = models.IntegerField()
    pesoActual = models.FloatField()
    pesoObjetivo = models.FloatField()

    # Relación con el modelo RelacionUsuarioComida
    comidas_relacionadas = models.ManyToManyField('RelacionUsuarioComida', related_name='usuarios_relacionados')



class RelacionUsuarioComida(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comida = models.ForeignKey(Alimento2, on_delete=models.CASCADE)
