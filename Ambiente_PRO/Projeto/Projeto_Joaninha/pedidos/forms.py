from django import forms
from .models import Pedidos

class PedidosForm(forms.ModelForm):
    dinheiro='Dinheiro'
    cartao= 'Cartão'
    escolhasPag=[('','Selecione'),(dinheiro, 'Dinheiro'), (cartao,'Debito'),(cartao,'Credito')]
    pratos=[('','Selecione'),('Virado a Paulista', 'Virado a Paulista'),('Bife','Bife'),('Filé de frango','Filé de frango'),('Frango ao molho','Frango ao molho'),('Carne de panela','Carne de panela'),('Figado acebolado','Figado acebolado'),('Bife acebolado','Bife acebolado'),('Feijoada','Feijoada'),('Calabresa','Calabresa')]
    acompanhamentos=[('','Selecione'),("Banana frita, linguiça, ovo, couve (virado)","Banana frita, linguiça, ovo, couve (virado)"),('Legumes refogados','Legumes refogados'),('Escarola','Escarola'),('Fritas', 'Fritas')]
    saladas=[('','Selecione'),('Alface e pepino','Alface e pepino'),('Repolho e cenoura','Repolho e cenoura')]

    nome_cliente=forms.CharField(label='Nome', 
                    widget=forms.TextInput(attrs={"placeholder": "Nome Completo"}))

    email= forms.EmailField(label='Email', 
                    widget=forms.TextInput(attrs={"placeholder": "ex@mail.com"}))
    
    prato=forms.ChoiceField(choices=pratos, required=True)

    acompanhamentos=forms.ChoiceField(choices=acompanhamentos, required=True)

    saladas=forms.ChoiceField(choices=saladas, required=True)
                    
    forma_de_pagamento=forms.ChoiceField(choices=escolhasPag, required=True)

    endereco=forms.CharField(label='Endereço', 
                    widget=forms.TextInput(attrs={"placeholder": "rua X"}))

    numero_contato=forms.CharField(label='contato', 
                    widget=forms.TextInput(attrs={"placeholder": "1234-5678"}))
    class Meta:
        model=Pedidos
        fields="__all__"




