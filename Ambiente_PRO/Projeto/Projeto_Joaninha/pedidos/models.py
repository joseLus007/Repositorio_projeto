from django.db import models
from datetime import datetime
from django.urls import reverse_lazy

class Pedidos(models.Model):
    dinheiro= 'Dinheiro'
    Cartao = 'Cartão'
    formaPagamento=[('','Selecione'),(dinheiro, 'Dinheiro'),(Cartao, 'Debito'),(Cartao, 'Credito')]
    pratos=[('','Selecione'),('Virado a Paulista', 'Virado a Paulista'),('Bife','Bife'),('Filé de frango','Filé de frango'),('Frango ao molho','Frango ao molho'),('Carne de panela','Carne de panela'),('Figado acebolado','Figado acebolado'),('Bife acebolado','Bife acebolado'),('Feijoada','Feijoada'),('Calabresa','Calabresa')]
    acompanhamentos=[('','Selecione'),('Banana frita, linguiça, ovo, couve (virado)','Banana frita, linguiça, ovo, couve (virado)'),('Legumes refogados','Legumes refogados'),('Escarola','Escarola'),('Fritas', 'Fritas')]
    saladas=[('','Selecione'),('Alface e pepino','Alface e pepino'),('Repolho e cenoura','Repolho e cenoura')]
    
    nome_cliente=models.CharField('nome_cliente',max_length=100)
    email=models.CharField('E-mail',max_length=200,unique=True)
    prato=models.CharField(max_length=20,choices=pratos, default='Selecione',)
    acompanhamentos=models.CharField(max_length=100,choices=acompanhamentos, default='Selecione',)
    saladas=models.CharField(max_length=50,choices=saladas, default='Selecione',)
    forma_de_pagamento=models.CharField(max_length=20,choices=formaPagamento, default='Selecione',)
    endereco=models.CharField('endereço',max_length=2000)
    numero_contato=models.CharField('contato',max_length=12)
    
    class Meta:
        ordering=("prato",)

    def __str__(self):
        return self.prato 

    def get_absolute_url(self):
        return reverse_lazy("pedidos:pedidos_detail",kwargs={'pk':self.pk})
    
    

        
