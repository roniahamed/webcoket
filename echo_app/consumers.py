import json
from channels.generic.websocket import AsyncWebsocketConsumer



class EchoConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        

        await self.send(
            text_data=json.dumps({'message':'Welcome to our Server'})
        )

    async def disconnect(self, code):
        pass 

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({'message':'server find your text data'}))