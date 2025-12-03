from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activa')
    list_filter = ('activa',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'cantidad_disponible', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('precio', 'cantidad_disponible', 'activo')
    ordering = ('-fecha_creacion',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'categoria', 'descripcion')
        }),
        ('Precio y Stock', {
            'fields': ('precio', 'cantidad_disponible')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )