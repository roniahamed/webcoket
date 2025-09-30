import json 
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

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

    @database_sync_to_async
    def save_message(self, author, room_name, content):
        Message.objects.create(author = author, room_name = room_name, content = content)


    async def receive(self, text_data):

        if self.scope['user'].is_authenticated:
            return
        

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        await self.save_message(author=user, room_name=self.room_name, content=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                'message': message,
                'username': user.username,
            }
        )


    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send( text_data=json.dumps({"message": message, "username":username }))

