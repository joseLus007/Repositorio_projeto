from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.Home, name='Home'),
    path('somos/',v.QuemSomos, name='QuemSomos'),
    path('local/',v.Localizacao, name='Localizacao'),
    path('post_list/',v.post_list, name='post_list'),
    
]
