from django.shortcuts import render
from .models import Message

def chat_index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
         
        message = Message.last_50_messages(room_name)
        return render(request, 'chat/room.html', {'room_name':room_name})




