from rest_framework import viewsets
from transferencia.api import serializers
from transferencia import models

class TransferenciaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransferenciaSerializer
    queryset = models.Transferencia.objects.all()