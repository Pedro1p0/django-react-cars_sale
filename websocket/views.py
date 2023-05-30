from django.shortcuts import render

# Create your views here.

def salaView(request):
    return render(request, 'websocket/sala.html')

# View que está com o WEBSOCKET
def dashboard_aluguel(request, slug):
    return render(request, 'websocket/dashboard_aluguel.html')