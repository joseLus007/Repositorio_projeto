from django.shortcuts import render
import django

def Home(request):
    return render(request,'Home/Home.html')

def QuemSomos(request):
    return render(request,'Home/QuemSomos.html')

def Localizacao(request):
    return render(request, 'Home/Contatos.html')

def CardapioLocal(request):
    return render(request, 'Home/CardapioLocal.html')

def CardapioEntrega(request):
    return render(request, 'Home/CardapioEntrega.html')

def TipoPedido(request):
    return render(request, 'Home/Tipo de pedido.html')

def Agradecimentos(request):
    return render(request, 'Home/Agradecimentos.html')
