from django.shortcuts import render
from .models import Pedidos

def pedidos_list(request):
    template_name='pedidos_list.html'
    objects=Pedidos.objects.all()
    context={'object_list':objects}
    return render (request,template_name,context)

def pedidos_detail(request,pk):
    template_name="pedidos_detail.html"
    obj=Pedidos.objects.get(pk=pk)
    context={'object':obj}
    return render(request,template_name,context)
