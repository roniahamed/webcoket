from django.urls import path 
from .views import websocket_front_end



urlpatterns = [
    path('websocket', websocket_front_end, name='websocket'),
]