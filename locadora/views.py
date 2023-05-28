from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from inventory.models import Carro
from django.views.generic import ListView
from .forms import AluguelForm
from .models import Aluguel
from django.urls import reverse
from django.views import View
from usuarios.models import FuncionarioProfile
from datetime import datetime
from django.http import HttpResponse
import os


def main(request):
    return render(
        request,
        "index.html",
        {'user': request.user}
    )


def compra_lista(request):

    carros = Carro.objects.filter(disponibilidade=True, venda=True)
    return render(request, 'locadora/lista_carros_venda.html', {'carros': carros})


def locacao_lista(request):

    carros = Carro.objects.filter(disponibilidade=True, locacao=True)
    return render(request, 'locadora/lista_carros_locacao.html', {'carros': carros})


class TicketListView(View):
    
    template_name = 'locadora/lista_tickets.html'

    def get(self, request):
        funcionario = FuncionarioProfile.objects.filter(
            user=request.user).first()
        if funcionario is None:
            # Trate o caso em que não há um perfil associado ao usuário
            # Redirecione o usuário ou mostre uma mensagem de erro
            # Por exemplo:
            file_path = os.path.join(settings.BASE_DIR, 'locadora/templates/locadora/no_auth_type_user.html')
            with open(file_path, 'r') as file:
                content = file.read()
            return HttpResponse(content, content_type='text/html')
        loja = funcionario.loja
        tickets = Aluguel.objects.filter(loja=loja)
        return render(request, self.template_name, {'tickets': tickets})


class TicketCreateView(View):
    template_name = 'locadora/criar_ticket.html'

    def get(self, request):
        funcionario = FuncionarioProfile.objects.filter(
            user=request.user).first()

        if funcionario is None:
            # Trate o caso em que não há um perfil associado ao usuário
            # Redirecione o usuário ou mostre uma mensagem de erro
            # Por exemplo:
            file_path = os.path.join(settings.BASE_DIR, 'locadora/templates/locadora/no_auth_type_user.html')
            with open(file_path, 'r') as file:
                content = file.read()
            return HttpResponse(content, content_type='text/html')

        initial_data = {
            'loja':funcionario.loja,
            'data_retirada': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'data_entrega': datetime.now().strftime('%Y-%m-%d %H:%M'),
        }
        form = AluguelForm(initial=initial_data)
        return render(request, 'locadora/criar_ticket.html', {'form': form})

    def post(self, request):
        
        form = AluguelForm(request.POST)
        if form.is_valid():
            aluguel = form.save(commit=False)  # Não salvar no banco de dados ainda
            funcionario = FuncionarioProfile.objects.filter(user=request.user).first()
            if funcionario:
                aluguel.loja = funcionario.loja
            aluguel.save()  # Salvar no banco de dados
            return redirect(reverse('locadora:aluguel_list'))
        return render(request, 'locadora/criar_ticket.html', {'form': form})


class TicketUpdateView(View):
    template_name = 'locadora/editar_ticket.html'

    def get(self, request, ticket_id):
        ticket = get_object_or_404(Aluguel, id=ticket_id)
        form = AluguelForm(instance=ticket)
        return render(request, self.template_name, {'form': form})

    def post(self, request, ticket_id):
        ticket = get_object_or_404(Aluguel, id=ticket_id)
        form = AluguelForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect(reverse('locadora:aluguel_list'))
        return render(request, self.template_name, {'form': form})



class TicketDeleteView(View):
    def post(self, request, ticket_id):
        ticket = get_object_or_404(Aluguel, id=ticket_id)
        ticket.delete()
        return redirect(reverse('locadora:aluguel_list'))