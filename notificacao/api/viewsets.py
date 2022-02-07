from rest_framework import viewsets
from notificacao.api import serializers
from notificacao import models

class NotificacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NotificacaoSerializer
    queryset = models.Notificacao.objects.all()