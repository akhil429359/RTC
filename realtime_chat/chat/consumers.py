from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        print("WebSocket Connected")

    def disconnect(self, close_code):
        print("WebSocket Disconnected")

    def receive(self, text_data):
        data = json.loads(text_data)

        message = data["message"]

        self.send(text_data=json.dumps({
            "message": message
        }))