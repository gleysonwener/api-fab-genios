from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco_custo = models.DecimalField(max_digits=7, decimal_places=2, default='')
    preco = models.DecimalField(max_digits=7, decimal_places=2)


    def __str__(self):
        return str(self.descricao)