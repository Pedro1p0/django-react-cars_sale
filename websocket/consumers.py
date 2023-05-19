from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class CarrosDisponiveisConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("conection sucessfull")
        await self.accept()

    async def disconnect(self, code):
        print(f"Conection close due code {code}")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]

        print(message, sender)

        await self.send(text_data=json.dumps({"message": message, "sender": sender}))
