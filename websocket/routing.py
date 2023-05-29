from django.urls import path
from .consumers import DashboardAluguelConsumer

websocket_urlpatterns = [
    path("ws/<str:dashboard_slug>/", DashboardAluguelConsumer.as_asgi()),
]
