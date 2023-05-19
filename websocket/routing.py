from django.urls import path
from .consumers import CarrosDisponiveisConsumer

websocket_urlpatterns = [
    path("ws/<str:carros_disponiveis_slug>/", CarrosDisponiveisConsumer.as_asgi()),
]
