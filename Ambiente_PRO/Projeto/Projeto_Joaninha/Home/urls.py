from django.urls import path
from . import views as v

app_name='home'
urlpatterns = [
    path('',v.Home, name='Home'),
    path('somos/',v.QuemSomos, name='QuemSomos'),
    path('local/',v.Localizacao, name='Localizacao'),
    path('CardapioEntrega/', v.CardapioEntrega, name='CardapioEntrega'),
    path('CardapioLocal/', v.CardapioLocal,name='CardapioLocal'),
    path('TipoPedido/', v.TipoPedido, name='TipoPedido'),
    path('Agradecimentos/', v.Agradecimentos, name='Agradecimentos')
]
