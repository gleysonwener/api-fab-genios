from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return str(self.nome)