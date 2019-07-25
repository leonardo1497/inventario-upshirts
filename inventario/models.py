from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Inventario(models.Model):
    Modelo = models.CharField(max_length=200,null=False)
    Imagen = models.TextField(null=False)
    Precio = models.FloatField(null=False)
    Cantidad = JSONField()