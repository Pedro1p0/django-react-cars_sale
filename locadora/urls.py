from django.urls import path
from .views import main, compra_lista, locacao_lista

app_name = "locadora"

urlpatterns = [
    path("home/", main, name="pagina_principal"),
    path("venda/", compra_lista, name="compra_lista"),
    path("locacao/", locacao_lista, name="locacao_lista"),

]
