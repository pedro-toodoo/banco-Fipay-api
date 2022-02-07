from rest_framework import viewsets
from deposito.api import serializers
from deposito import models

class DepositoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DepositoSerializer
    queryset = models.Deposito.objects.all()