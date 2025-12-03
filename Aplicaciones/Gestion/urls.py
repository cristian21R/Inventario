from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    # URLs con ViewSet
    path('', include(router.urls)),
    
    # URLs con vistas basadas en funciones
    path('func/productos/', views.lista_productos, name='lista_productos'),
    path('func/productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('func/productos/crear/', views.crear_producto, name='crear_producto'),
    
    # Estadísticas
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    
    # Home
    path('', views.api_home, name='api_home'),
]