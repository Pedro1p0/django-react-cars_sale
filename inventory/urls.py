from django.urls import path
from .views import CarroCreateView, CarroListView, detalhes_carro

app_name = 'inventory'

urlpatterns = [
    path('create/', CarroCreateView.as_view(), name='carro-create'),
    path('list/', CarroListView.as_view(), name='carro-list'),
    path('carro/<int:carro_id>/', detalhes_carro, name='detalhes_carro'),
]