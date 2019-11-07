from django.db import models


class Cliente(models.Model):

    tipo_sexo = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('I', 'Indefinido'),
    ]
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1, choices=tipo_sexo)
    localizacao_rua = models.CharField(max_length=30)
    localizacao_cep = models.CharField(max_length=30) 
    
