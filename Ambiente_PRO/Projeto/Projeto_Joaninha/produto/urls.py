from django.urls import path
from Projeto_Joaninha.produto import views as v


app_name = 'produto'


urlpatterns = [
    path('',v.Produto_list, name='Produto_list'),
]
