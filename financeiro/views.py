import enum
from rest_framework.views import APIView
import requests
from financeiro.api import serializers
from rest_framework.response import Response

def conexao():
    url = "https://api.hgbrasil.com/finance?key=95d8801e"
    requisicao = requests.get(url)
    dados = requisicao.json()

    return dados

def dados_banco():
    lista_completa = []
    
    dicio_completo = {}
    dicio = {}

    dados = conexao()

    dicio_completo = {
        'moeda': dados['results']['currencies'],
        'mercado': dados['results']['stocks'],
        'bitcoin': dados['results']['bitcoin'],
        'taxas': dados['results']['taxes']
    }

    lista_completa.append(dicio_completo)

    dicio['infos'] = lista_completa 

    return dicio

class FinanceiroAPIView(APIView):
    def get(self, request):
        requisicao = dados_banco()
        infos = serializers.FinanceiroSerializer(requisicao['infos'], many=True).data

        return Response(infos)

class RendimentoAPIView(APIView):
    def get(self, request, valor, dias):
        requisicao = dados_banco()

        v = requisicao['infos'][0]['taxas'][0]['cdi_daily']
        cdi_percent = v/100
        
        rendimento_diario = (cdi_percent/12)/30
        rendimento = rendimento_diario * valor * dias

        print(rendimento)
        return Response(rendimento)