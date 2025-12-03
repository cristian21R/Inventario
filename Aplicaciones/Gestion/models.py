from django.db import models

class Categoria(models.Model):
    # El id AutoField se crea automáticamente, no necesitas declararlo
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # El id AutoField se crea automáticamente
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(max_length=500, blank=True, null=True, verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10,  # Aumentado a 10 para precios más altos
        decimal_places=2,
        verbose_name="Precio"
    )
    cantidad_disponible = models.IntegerField(default=0, verbose_name="Cantidad Disponible")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    activo = models.BooleanField(default=True, verbose_name="¿Activo?")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"