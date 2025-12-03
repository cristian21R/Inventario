from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, ProductoListSerializer

# ViewSets para operaciones CRUD completas
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductoListSerializer
        return ProductoSerializer
    
    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        categoria_id = request.query_params.get('categoria_id')
        if categoria_id:
            productos = Producto.objects.filter(categoria_id=categoria_id)
        else:
            productos = Producto.objects.all()
        
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['patch'])
    def actualizar_stock(self, request, pk=None):
        producto = self.get_object()
        cantidad = request.data.get('cantidad')
        
        if cantidad is not None:
            producto.cantidad_disponible = cantidad
            producto.save()
            serializer = self.get_serializer(producto)
            return Response(serializer.data)
        
        return Response(
            {'error': 'Se requiere la cantidad'},
            status=status.HTTP_400_BAD_REQUEST
        )

# Vistas basadas en funciones simples
@api_view(['GET'])
def lista_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
def crear_producto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def estadisticas(request):
    total_productos = Producto.objects.count()
    productos_activos = Producto.objects.filter(activo=True).count()
    categorias_count = Categoria.objects.count()
    
    return Response({
        'total_productos': total_productos,
        'productos_activos': productos_activos,
        'total_categorias': categorias_count,
    })

# Vista de bienvenida
@api_view(['GET'])
def api_home(request):
    return Response({
        'mensaje': 'Bienvenido a la API de Inventario',
        'endpoints': {
            'categorias': '/api/categorias/',
            'productos': '/api/productos/',
            'estadisticas': '/api/estadisticas/',
        }
    })