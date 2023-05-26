from django.shortcuts import render, redirect
from inventory.models import Carro
from django.views.generic import ListView
from .forms import AluguelForm
from .models import Aluguel

def main(request):
    return render(
        request,
        "index.html",
        {'user': request.user}
    )



def compra_lista(request):

    carros = Carro.objects.filter(disponibilidade = True, venda = True)
    return render(request, 'locadora/lista_carros_venda.html', {'carros':carros})

def locacao_lista(request):

    carros = Carro.objects.filter(disponibilidade = True, locacao = True)
    return render(request, 'locadora/lista_carros_locacao.html', {'carros':carros})


def ticket(request):

    if request.method == 'GET':
        ticket = Aluguel.objects.all()

        form = AluguelForm()

        context = {
            'ticket': ticket,
            'form': form,
        }
        return render(request, './locadora/criar_ticket.html', context)
    elif request.method == 'POST':
        form = AluguelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            ticket = Aluguel.objects.all()

            context = {
                'ticket': ticket,
                'form': form,
            }
            return render(request, './locadora/criar_ticket.html', context)


""" def update(request, pessoa_id):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        pessoa = Pessoa.objects.filter(id=pessoa_id).first()
        form = PessoaForm(instance=pessoa)
        context = {
            'pessoas': pessoas,
            'form': form,
        }
        return render(request, 'exemplo/index.html', context)

    elif request.method == 'POST':
        pessoa = Pessoa.objects.filter(id=pessoa_id).first()
        form = PessoaForm(request.POST, instance=pessoa)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            pessoas = Pessoa.objects.all()

            context = {
                'pessoas': pessoas,
                'form': form,
            }
            return render(request, 'exemplo/index.html', context)
 """