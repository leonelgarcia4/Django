from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    codigo = models.IntegerField(max_length=10, blank=False, null=False)
    inscrito = models.BooleanField(blank=False, null=True)


class dias(models.Model):
    nombre = models.CharField(primary_key=True, max_length=15)

    def __str__(self):
        return '{}'.format(self.nombre)


class Horario(models.Model):
    estudiante = models.OneToOneField(User, on_delete=models.CASCADE)
    dias = models.ManyToManyField(dias)
    sede = models.CharField(max_length=15, blank=False, null=False)
    jornada = models.CharField(max_length=15, blank=False, null=False)
