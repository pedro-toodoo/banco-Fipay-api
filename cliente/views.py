from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cliente.models import Cliente
from cliente.api import serializers

class ClienteAPIView(APIView):
    """
    API de clientes do banco
    """
    def get(self, request):
        clientes = Cliente.objects.all()
        infos = serializers.ClienteSerializer(clientes, many=True)
        return Response(infos.data)

    def post(self, request):
        infos = serializers.ClienteSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)

class PesquisaSaldoCliente(APIView):
    """
    API que retorna o saldo de um cliente especificado
    """
    def get(self, request, cpf): 
        saldo_cliente = Cliente.objects.filter(cpf=cpf)
        infos = serializers.ClienteSerializer(saldo_cliente, many=True)
        print(infos.data)
        return Response(infos.data[0]['saldo'])