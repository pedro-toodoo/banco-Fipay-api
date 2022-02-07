from django.db import models
from cliente.models import Cliente
from uuid import uuid4


class Deposito(models.Model):
    id_dep = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quantia = models.FloatField()
    data_dep = models.DateField()
    cliente_cpf_dep = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

