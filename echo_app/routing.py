from django.urls import re_path
from .consumers import EchoConsumer
print("--- ECHO_APP/ROUTING.PY IS BEING LOADED ---") 
websocket_urlpatterns = [
    re_path(r'ws/echo/$', EchoConsumer.as_asgi()),
]