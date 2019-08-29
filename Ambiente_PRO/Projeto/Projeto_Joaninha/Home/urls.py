from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.Home, name='Home'),
    path('somos/',v.QuemSomos, name='QuemSomos'),
    path('local/',v.Localizacao, name='Localizacao'),
    path('cardapio/', v.Cardapio, name='Cardapio')  
]
