from rest_framework.response import Response
from rest_framework import viewsets
from .models import Pedido
from .serializers import PedidoSerializer, ListaPedidoClienteSerializer, FaturamentoTotalSerializer, LucroSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ListaPedidoClienteViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.filter()
    serializer_class = ListaPedidoClienteSerializer

    def retrieve(self, request, pk=None):
        queryset = Pedido.objects.all()
        pedidos = queryset.filter(cliente=pk)
        serializer = ListaPedidoClienteSerializer(pedidos, many=True)
        return Response(serializer.data)


class FaturamentoTotalViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = FaturamentoTotalSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        faturamento_total = queryset.faturamento_total
        serializer = FaturamentoTotalSerializer(faturamento_total)
        return Response(serializer.data)

class LucroViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = LucroSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        lucro = queryset.lucro
        serializer = LucroSerializer(lucro)
        return Response(serializer.data)
