from dataclasses import fields
from rest_framework import serializers
from notificacao import models

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Notificacao
        fields = '__all__'
        

