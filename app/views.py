from django.shortcuts import render, redirect
from app.forms import PedidosForm
from app.models import Pedidos


# Create your views here.
def home(request):  
    data = {'db': Pedidos.objects.all()}
    return render(request, 'tabela2.html', data)


def form(request):
    data = {'form': PedidosForm()}
    return render(request, 'form.html', data)


def index(request):  
    data = {'db': Pedidos.objects.all()}
    return render(request, 'index.html', data)


def create(request):
    form = PedidosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')


def view(request, pk):
    data = {'db': Pedidos.objects.get(pk=pk)}
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {'db': Pedidos.objects.get(pk=pk)}
    data['form'] = PedidosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {'db': Pedidos.objects.get(pk=pk)}
    form = PedidosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('index')


def delete(request, pk):
        db = Pedidos.objects.get(pk=pk)
        db.delete()
        return redirect('index')
