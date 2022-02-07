from rest_framework import viewsets
from compra.api import serializers
from compra import models

class CompraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompraSerializer
    queryset = models.Compra.objects.all()