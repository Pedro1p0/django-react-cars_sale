from django.shortcuts import render
from inventory.models import Carro
from django.views.generic import ListView
# Create your views here.


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