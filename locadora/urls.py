from django.urls import path
from . import views 

app_name = "locadora"

urlpatterns = [
    path("home/", views.main, name="pagina_principal"),
    path("venda/", views.compra_lista, name="compra_lista"),
    path("locacao/", views.locacao_lista, name="locacao_lista"),
    path("create/", views.ticket, name="alugel_criar"),
]
