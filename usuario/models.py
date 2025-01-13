from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=50, null=False)
    cargo = models.CharField(max_length=30, null=False)
    class Meta:
       db_table = 'usuarios'
    