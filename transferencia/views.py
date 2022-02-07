from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from transferencia.models import Transferencia
from transferencia.api import serializers
from cliente.models import Cliente
from notificacao.models import Notificacao

class TransferenciaAPIView(APIView):
    """
    API de transferências do banco
    """
    def get(self, request):
        transferencia = Transferencia.objects.all()
        infos = serializers.TransferenciaSerializer(transferencia, many=True)
        return Response(infos.data)

    def post(self, request):
        cliente1 = Cliente.objects.get(cpf=request.data['cliente1_cpf_transf'])
        cliente2 = Cliente.objects.get(cpf=request.data['cliente2_cpf_transf'])
        valor = request.data['quantia']
        
        if cliente1.saldo >= valor :
            cliente1.saldo -= valor 
            cliente1.save()

            cliente2.saldo += valor 
            cliente2.save()

            Notificacao.objects.create(cpf_remetente=cliente1, cpf_destinatario=cliente2, valor=valor )
            #for item in notificacao1:
            #    item.save()

            
        else:
            return Response("Saldo insuficiente para realizar a transferência")
            

        infos = serializers.TransferenciaSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)