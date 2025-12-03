from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion')
    
    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo")
        return value
    
    def validate_cantidad_disponible(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad disponible no puede ser negativa")
        return value

# Serializer para listados más simples
class ProductoListSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'cantidad_disponible', 'categoria_nombre', 'activo']