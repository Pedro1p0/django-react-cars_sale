from django.apps import AppConfig
from . import mqtt


class WebsocketConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "websocket"

def ready(self):
        mqtt.setup_and_activate()