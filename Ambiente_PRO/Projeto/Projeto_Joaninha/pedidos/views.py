from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import CreateView
from .models import Pedidos
from .forms import PedidosForm
from django.urls import reverse_lazy
from django.utils import timezone


def pedidos_list(request):
    template_name='pedidos_list.html'
    objects=Pedidos.objects.all()
    search=request.GET.get("search")
    if search:
        objects=objects.filter(prato__icontains=search)
    context={'object_list':objects}
    return render (request,template_name,context)

def pedidos_detail(request,pk):
    template_name="pedidos_detail.html"
    obj=Pedidos.objects.get(pk=pk)
    context={'object':obj}
    return render(request,template_name,context)
    
def pedido_add(request):
    template_name="pedidosform.html"
    return render(request,template_name)

class PedidoCreate(CreateView):
    model=Pedidos
    template_name="pedidosform.html"
    form_class=PedidosForm



def pedido_create_view(request):
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            Pedidos.horario = timezone.now()
            form.save()
            form = PedidosForm()
            return redirect("/home/Agradecimentos/")
    else:
        form= PedidosForm()
    return render(request, "CardapioEntrega.html", {'form': form})

def deleteDado(request,pk):
    template_name='pedidos_list.html'
    obj=get_object_or_404(Pedidos,pk=pk)
    obj.delete()
    return render(request,template_name)
    