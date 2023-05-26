from django.shortcuts import render, redirect
from inventory.models import Carro
from django.views.generic import ListView
from .forms import AluguelForm
from .models import Aluguel
from django.urls import reverse
from django.views import View
from usuarios.models import FuncionarioProfile
from datetime import datetime

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





class TicketListView(View):
    template_name = 'locadora/lista_tickets.html'

    def get(self, request):
        funcionario = FuncionarioProfile.objects.filter(user=request.user).first()
        loja = funcionario.loja
        tickets = Aluguel.objects.filter(loja=loja)
        return render(request, self.template_name, {'tickets': tickets})
        





class TicketCreateView(View):
    template_name = 'locadora/criar_ticket.html'
    
    def get(self, request):
        funcionario = FuncionarioProfile.objects.filter(user=request.user).first()
        
        initial_data = {
            'loja': funcionario.loja,
            'data_retirada': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'data_entrega': datetime.now().strftime('%Y-%m-%d %H:%M'),
        }
        form = AluguelForm(initial=initial_data)
        return render(request, 'locadora/criar_ticket.html', {'form':form})

    def post(self,request):
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('locadora:aluguel_list'))
        return render(request, 'locadora/criar_ticket.html', {'form':form})















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