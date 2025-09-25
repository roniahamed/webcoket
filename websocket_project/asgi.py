"""
ASGI config for websocket_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import echo_app.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            echo_app.routing.websocket_urlpatterns
        )
    ),
})


# websocket_project/asgi.py

# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import re_path

# # আমরা সরাসরি Consumer ইম্পোর্ট করছি
# from echo_app.consumers import EchoConsumer 

# # import echo_app.routing  # এই লাইনটিকে কমেন্ট আউট করে দিন

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_project.settings')

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter([ # আমরা routing.py এর পরিবর্তে সরাসরি এখানে একটি লিস্ট তৈরি করছি
#             re_path(r'ws/echo/$', EchoConsumer.as_asgi()),
#         ])
#     ),
# })


# # websocket_project/asgi.py
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import echo_app.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_project.settings')

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             echo_app.routing.websocket_urlpatterns
#         )
#     ),
# })