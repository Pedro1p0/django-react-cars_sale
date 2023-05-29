from django.shortcuts import render

# Create your views here.

def salaView(request):
    return render(request, 'websocket/sala.html')

def dashboard_aluguel(request, slug):
    return render(request, 'websocket/dashboard_aluguel.html')