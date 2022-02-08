from django.db import models
from uuid import uuid4
from cliente.models import Cliente

class Notificacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cpf_remetente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='remetente_notifica')
    cpf_destinatario = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='destinatario_notifica')
    valor = models.FloatField()