from django.shortcuts import render

def Home(request):
    return render(request,'Home/Home.html')

def QuemSomos(request):
    return render(request,'Home/Quem Somos.html')

def Localizacao(request):
    return render(request, 'Home/Contatos.html')

def Cardapio(request):
    return render(request, 'Home/Cardápio_joaninha.html')
