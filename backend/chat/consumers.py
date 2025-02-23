import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract the username of the connected user from the WebSocket URL
        self.username = self.scope["url_route"]["kwargs"]["username"]

        # Create a unique channel for this user
        await self.channel_layer.group_add(
            self.username,  # Each user has a unique group name
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from their unique channel
        await self.channel_layer.group_discard(
            self.username,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")
        receiver = data.get("receiver", "")  # Identify the recipient

        # Send message only to the recipient's WebSocket channel
        await self.channel_layer.group_send(
            receiver,
            {
                "type": "send_message",
                "message": message,
                "sender": self.username,
                "receiver": receiver
            }
        )

    async def send_message(self, event):
        # Send the private message only to the recipient
        await self.send(text_data=json.dumps({
            "sender": event["sender"],
            "receiver": event["receiver"],
            "message": event["message"]
        }))
