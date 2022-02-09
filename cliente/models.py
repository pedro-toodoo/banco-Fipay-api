from django.db import models


class Cliente(models.Model):    
    cpf = models.CharField(primary_key=True, max_length=11, editable=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    senha = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    estado = models.CharField(max_length=20, blank=False, null=False)
    pais = models.CharField(max_length=20, blank=False, null=False)
    nascimento = models.DateField(blank=False, null=False)
    saldo = models.FloatField(default=0, editable=False)