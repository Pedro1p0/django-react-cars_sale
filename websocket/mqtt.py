import paho.mqtt.client as mqtt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("Teste_Loja1")
    else:
        print("Failed to connect to MQTT broker")

def on_message(client, userdata, msg):
    print('publicaram algo')
    print("Received message:", msg.payload.decode())

    # Enviar a mensagem recebida para o consumidor WebSocket
    async_to_sync(channel_layer.group_send)("Teste_Loja1", {
        "type": "enviar_mensagem",
        "mensagem": msg.payload.decode(),
    })

def setup_and_activate_mqtt():
    client = mqtt.Client()
    client.enable_logger()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883, 60)

    
    client.loop_start()

setup_and_activate_mqtt()
