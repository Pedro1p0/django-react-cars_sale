from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from inventory.models import Loja
from django.http import HttpResponseRedirect
# Create your views here.

def salaView(request):
    loja_qs = Loja.objects.all()
    return render(request, 'websocket/sala.html', {'loja_qs':loja_qs})

# View que está com o WEBSOCKET
def dashboard_aluguel(request, slug):
    return render(request, 'websocket/dashboard_aluguel.html')



@login_required
def redirecionar_dashboard(request):
    # Verificar se o usuário é um administrador
    if request.user.is_staff:
        # Obter todas as lojas
        lojas = Loja.objects.all()
        return render(request, 'websocket/sala.html', {'lojas': lojas})

    # Verificar se o usuário tem uma loja associada
    if hasattr(request.user, 'funcionarioprofile') and request.user.funcionarioprofile.loja:
        loja = request.user.funcionarioprofile.loja
        print('entrei no redirect')
        return redirect('websocket:dashboard_aluguel', slug=loja.slug)

    # Caso o usuário não tenha uma loja associada ou não seja um administrador
    return render(request, 'sem_acesso.html')