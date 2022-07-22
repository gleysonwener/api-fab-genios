from django.db import models
from cliente.models import  Cliente
from produto.models import Produto
from django.db.models import F, Sum


class Pedido(models.Model):
    numero = models.CharField(max_length=7)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, default='')
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)



    def __str__(self):
        return str(self.cliente)

    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total=models.Sum(F('quantidade') * F('produto__preco')))
        return queryset['total']

    @property
    def faturamento_total(self):
        total_venda = self.itens.all().aggregate(
            total=models.Sum(F('quantidade') * F('produto__preco')))

        self.valor = total_venda

        faturamento_total = self.itens.all().aggregate(faturamento_total=Sum('valor'))

        return faturamento_total['faturamento_total']


    @property
    def lucro(self):
        queryset = self.itens.all().aggregate(lucro=models.Sum(F('produto__preco') - F('produto__preco_custo')))
        return queryset['lucro']

class ItemDoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


    def __str__(self):
        return str(self.produto)