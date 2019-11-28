
from django.urls import path
from Projeto_Joaninha.pedidos import views as v

app_name="pedidos"

urlpatterns=[
    path('',v.pedidos_list,name='pedidos_list'),
    path('cardapio/',v.pedido_create_view,name="pedido_create_view"),
    path('<int:pk>/',v.pedidos_detail,name='pedidos_detail'),
    path('adicionar/',v.PedidoCreate.as_view(),name='pedido_add'),
    path('<int:pk>/delete/',v.deleteDado,name='delete'),

    

]