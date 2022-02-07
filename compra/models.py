from django.db import models
from cliente.models import Cliente
from uuid import uuid4


class Compra(models.Model):
    id_compra = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    valor = models.FloatField()
    descricao = models.CharField(max_length=255)
    data_compra = models.DateField()
    cliente_cpf_compra = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

