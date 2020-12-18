from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
@login_required
def listaCliente(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    if nome and sobrenome:
        clientes = Cliente.objects.filter(first_name__icontains=nome, last_name__icontains=sobrenome)
    elif nome or sobrenome:
        clientes = Cliente.objects.filter(first_name__icontains=nome) | Cliente.objects.filter(last_name__icontains=sobrenome)
    else:
        clientes = Cliente.objects.all()

    return render(request, 'lista-cliente.html', {'clientes': clientes})

@login_required
def adicionarCliente(request):
    form = ClienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listarCliente')

    return render(request, 'adiciona-cliente.html', {'form': form})

@login_required
def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listarCliente')

    return render(request, 'editar-cliente.html', {'form': form})

@login_required
def excluirCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listarCliente')

    return render(request, 'excluir-cliente.html', {'cliente': cliente})