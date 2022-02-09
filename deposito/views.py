from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from deposito.models import Deposito
from deposito.api import serializers
from cliente.models import Cliente


class DepositoAPIView(APIView):
    """
    API de depósitos do banco
    """
    def get(self, request):
        depositos = Deposito.objects.all()
        infos = serializers.DepositoSerializer(depositos, many=True)
        return Response(infos.data)

    def post(self, request):        
        cliente = Cliente.objects.get(cpf=request.data['cliente_cpf_dep'])
        cliente.saldo += request.data['quantia']
        cliente.save()
        
        infos = serializers.DepositoSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)

class PesquisaDepositoCliente(APIView):
    """
    API que lista depósito feitos para o cliente
    """
    def get(self, request, cpf):
        depositos_cpf = Deposito.objects.filter(cliente_cpf_dep=cpf)
        infos = serializers.DepositoSerializer(depositos_cpf, many=True)
        return Response(infos.data)
