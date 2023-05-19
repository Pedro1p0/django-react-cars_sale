from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import CarroForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Carro
from usuarios.models import FuncionarioProfile

class CarroCreateView(View):
    def get(self, request):
        form = CarroForm()
        return render(request, 'carro_create.html', {'form': form})

    def post(self, request):
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inventory:carro-list'))
        return render(request, 'carro_create.html', {'form': form})



class CarroListView(View):
    template_name = 'carro_list.html'

    def get(self, request):
        # Obtém a loja do usuário da requisição
        print(request.user)
        funcionario_profile = FuncionarioProfile.objects.filter(user=request.user).first()

        loja = funcionario_profile.loja
        carros = Carro.objects.filter(loja=loja)
        print(funcionario_profile.loja)
        
        return render(request, 'carro_list.html', {'carros': carros})
    

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'detalhes_carro.html', {'carro': carro})