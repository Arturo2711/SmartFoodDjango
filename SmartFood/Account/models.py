from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    edad = models.IntegerField()
    pesoActual = models.FloatField()
    pesoObjetivo = models.FloatField()
