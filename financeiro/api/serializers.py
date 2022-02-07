from rest_framework import serializers
from financeiro import models

class FinanceiroSerializer(serializers.Serializer):
    moeda = serializers.JSONField()
    mercado = serializers.JSONField()
    bitcoin = serializers.JSONField()
        

