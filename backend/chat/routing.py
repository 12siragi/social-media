from django.urls import path
from chat.consumers import PrivateChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<str:username>/", PrivateChatConsumer.as_asgi()),
]
