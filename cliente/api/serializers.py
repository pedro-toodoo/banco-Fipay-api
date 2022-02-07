from rest_framework import serializers
from cliente import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Cliente
        fields = '__all__'
        

