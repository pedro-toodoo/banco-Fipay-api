from rest_framework import serializers
from transferencia import models

class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Transferencia
        fields = '__all__'
        

