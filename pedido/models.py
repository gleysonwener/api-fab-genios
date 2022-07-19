from django.db import models
from cliente.models import  Cliente
from produto.models import Produto
from django.db.models import F


class Pedido(models.Model):
    numero = models.CharField(max_length=7)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, default='')

    def __str__(self):
        return str(self.cliente)

    @property
    def total(self):
        queryset = self.itens.all().aggregate(total=models.Sum(F('quantidade') * F('produto__preco')))
        return queryset['total']

    @property
    def faturamento_total(self):
        queryset = self.itens.filter().aggregate(faturamento_total=models.Sum('total'))
        return queryset['faturamento_total']


class ItemDoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


    def __str__(self):
        return str(self.produto)