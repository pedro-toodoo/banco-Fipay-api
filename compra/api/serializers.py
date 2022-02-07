from rest_framework import serializers
from compra import models

class CompraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Compra
        fields = '__all__'
        

