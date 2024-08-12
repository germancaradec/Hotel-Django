from django.db import models

# Create your models here.
class Consulta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    texto = models.CharField(max_length=3000)