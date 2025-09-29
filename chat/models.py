from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message in {self.room_name} at {self.timestamp}'
    
    def last_50_messages(room_name):
        return Message.objects.filter(room_name=room_name).order_by('-timestamp').all()[:50]