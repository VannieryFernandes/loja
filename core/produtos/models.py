from django.db import models
from clientes.models import Cliente


class Produto(models.Model):

    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    tipo = models.CharField(max_length=15)
    data_compra = models.DateField()