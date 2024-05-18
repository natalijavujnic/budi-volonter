from django.shortcuts import render
from django.http import HttpRequest




import json
import asyncio

from channels.generic.websocket import WebsocketConsumer 




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'status':'connection OK'
            }))
        pass

    def disconnect(self):
        pass

