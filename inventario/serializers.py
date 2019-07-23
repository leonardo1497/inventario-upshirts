from .models import Inventario
from rest_framework import serializers

class InventarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Inventario
        fields = ('id','Modelo','Imagen','Precio','Cantidad')