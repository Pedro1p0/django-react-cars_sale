from django.urls import path
from . import views 

app_name = "locadora"

urlpatterns = [
    path("home/", views.main, name="pagina_principal"),
    path("venda/", views.compra_lista, name="compra_lista"),
    path("locacao/", views.locacao_lista, name="locacao_lista"),
    path("ticket/criar/", views.TicketCreateView.as_view(), name="aluguel_criar"),
    path("ticket/lista/",views.TicketListView.as_view(), name="aluguel_list"),
    path('ticket/editar/<int:ticket_id>/', views.TicketUpdateView.as_view(), name='aluguel_editar'),
]
