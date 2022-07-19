from django.contrib import admin
from django.urls import path, include
from pedido.views import PedidoViewSet, ListaPedidoClienteViewSet, FaturamentoTotalViewSet
from cliente.views import ClienteViewSet
from produto.views import ProdutoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename='Cliente')
router.register(r'produto', ProdutoViewSet, basename='Produto')
router.register(r'pedido', PedidoViewSet, basename='Pedido')
router.register(r'pedido/cliente', ListaPedidoClienteViewSet, basename='ListaPedidoCliente')
router.register(r'pedido/faturamento', FaturamentoTotalViewSet, basename='FaturamentoTotal')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]