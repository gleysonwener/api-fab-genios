from .models import Pedido, ItemDoPedido
from rest_framework import serializers


class ItemDoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDoPedido
        fields = ('id', 'pedido', 'produto', 'quantidade',)
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.produto.preco

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemDoPedidoSerializer(many=True)
    class Meta:
        model = Pedido
        fields = ('id', 'numero', 'cliente', 'itens', 'total',)


class ListaPedidoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'cliente',)

class FaturamentoTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('faturamento_total',)
