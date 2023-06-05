import paho.mqtt.client as mqtt
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
from inventory.models import Carro

class DashboardAluguelConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'loja1'      # DINAMICO 

        # Criar e conectar ao cliente MQTT
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_message = self.on_mqtt_message
        self.mqtt_client.connect('test.mosquitto.org', 1883, 60)
        self.mqtt_client.loop_start()

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        self.mqtt_client.disconnect()
        self.mqtt_client.loop_stop()

    async def receive(self, text_data):
        # Não é necessário implementar isso para esse caso
        pass

    def on_mqtt_connect(self, client, userdata, flags, rc):
        # Inscrever-se no tópico MQTT desejado
        client.subscribe('Teste_Loja1') # DINAMICO 
        

    def on_mqtt_message(self, client, userdata, msg):
        # Decodificar a mensagem recebida
        message = msg.payload.decode('utf-8')

        # Enviar a mensagem recebida para todos os clientes WebSocket no grupo da sala
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_mqtt_message',
                'message': message,
            }
        )


    async def send_mqtt_message(self, event):
        print(event)
        #carro = Carro.objects.filter(placa=event['placa_do_carro'])

        if 'mensagem' in event:
            mensagem = event['mensagem']
            await self.send(text_data=json.dumps({
                'mensagem': 'Mensagem recebida e processada: ' + mensagem,
            }))
        else:
            # Tratar o caso em que a chave 'message' está ausente no evento
            await self.send(text_data=json.dumps({
                'error': 'Mensagem invalida recebida',
            }))


    async def enviar_mensagem(self, event):
        # Manipular a mensagem recebida do tipo "enviar_mensagem"
        message = event['message']
        # Faça o que desejar com a mensagem recebida
        # Por exemplo, você pode enviar a mensagem para os clientes WebSocket no grupo da sala

        await self.send(text_data=json.dumps({
            'message': 'Mensagem recebida e processada: ' + message,
        }))
