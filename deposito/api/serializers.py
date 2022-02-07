from dataclasses import fields
from rest_framework import serializers
from deposito import models

class DepositoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Deposito
        fields = '__all__'
        

