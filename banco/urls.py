from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from cliente.api import viewsets as vsc
from deposito.api import viewsets as vsd
from transferencia.api import viewsets as vst
from compra.api import viewsets as vscom
from financeiro.api import viewsets as vsfinan
from notificacao.api import viewsets as vsn

from cliente.views import ClienteAPIView, PesquisaSaldoCliente
from deposito.views import DepositoAPIView, PesquisaDepositoCliente
from compra.views import CompraAPIView, PesquisaComprasClienteAPIView
from transferencia.views import TransferenciaAPIView, PesquisaTransferenciaCliente
from financeiro.views import FinanceiroAPIView, RendimentoAPIView


route = routers.DefaultRouter()
route.register(r'cadastrar_cliente', vsc.ClienteViewset, basename='cliente')
route.register(r'fazer_deposito', vsd.DepositoViewset, basename='deposito')
route.register(r'fazer_transferencia', vst.TransferenciaViewSet, basename='transferencia')
route.register(r'fazer_compra', vscom.CompraViewSet, basename='compra')
route.register(r'analise_moedas', vsfinan.FinanceiroViewset, basename='financeiro')
route.register(r'notificacoes', vsn.NotificacaoViewSet, basename='notificacoes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('clientes/', ClienteAPIView.as_view(), name='clientes'),
    path('depositos/', DepositoAPIView.as_view(), name='depositos'),
    path('transferencia/', TransferenciaAPIView.as_view(), name='transferencia'),
    path('compra/', CompraAPIView.as_view(), name='compra'),
    path('financeiro/', FinanceiroAPIView.as_view(), name='financeiro'),
    path('rendimento/<int:valor>/<int:dias>', RendimentoAPIView.as_view(), name='rendimento'),

    path('cliente-compra/<str:cpf>/', PesquisaComprasClienteAPIView.as_view(), name='cliente-compra'),
    path('cliente-deposito/<str:cpf>/', PesquisaDepositoCliente.as_view(), name='cliente-deposito'),
    path('cliente-transf/<str:cpf>/', PesquisaTransferenciaCliente.as_view(), name='cliente-transf'),
    path('cliente-saldo/<str:cpf>/', PesquisaSaldoCliente.as_view(), name='cliente-saldo')
]
