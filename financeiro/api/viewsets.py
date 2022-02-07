from rest_framework import viewsets
from financeiro.api import serializers
from financeiro import models

class FinanceiroViewset(viewsets.ModelViewSet):
    serializer_class = serializers.FinanceiroSerializer
    queryset = models.Financeiro.objects.all()
    