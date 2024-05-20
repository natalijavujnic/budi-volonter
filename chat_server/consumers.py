from datetime import datetime, timezone
from django.shortcuts import render
from django.http import HttpRequest
from asgiref.sync import async_to_sync



import json
import asyncio

from channels.generic.websocket import WebsocketConsumer

from chat_server import models 




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.chat_id = None #inicijalno user nije otvorio ni jedan chat, a la whatsapp web
        user = self.scope['user']
        self.idkor = user.idkor
        print("CONNECTED")
        print(self.idkor)
        print(user)
        async_to_sync(self.channel_layer.group_add)( #dodajemo korisnika u grupu idkor, da bi mogli da saljemo poruke iz servera
            "U"+str(self.idkor),
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'status':'connection OK'
            }))

    def disconnect(self, code):
        if self.chat_id:
            async_to_sync(self.channel_layer.group_discard)( #izbacujemo korisnika iz grupe, ako je u nekoj grupi
                str(self.chat_id),
                self.channel_name
            )
        async_to_sync(self.channel_layer.group_discard)( #izbacujemo korisnika iz grupe idkor
            "U"+str(self.idkor),
            self.channel_name
        )

    def receive(self, text_data): #text dolazi u server iz clienta
        event = json.loads(text_data)
        type = event['type']
        if type == 'open_chat':
            self.chat_id = event['chat_id']
            print("RECEIVE OPEN, my chat id",self.chat_id, "my id",self.idkor)
            async_to_sync(self.channel_layer.group_add)( #dodajemo korisnika u grupu
                str(self.chat_id),
                self.channel_name
            )
        elif type == 'close_chat':
            print("RECEIVE CLOSE, my chat id",self.chat_id, "my id",self.idkor)
            async_to_sync(self.channel_layer.group_discard)( #izbacujemo korisnika iz grupe
                str(self.chat_id),
                self.channel_name
            )
            self.chat_id = None
        elif type == 'chat':
            message = event['message']
            prep = models.Prepiska.objects.filter(idpre=self.chat_id).first()
            redbr = models.Poruka.objects.filter(idpre=prep).count() + 1
            poruka = models.Poruka(idsender=models.Korisnik.objects.filter(idkor = self.idkor).first(), idpre=prep, tekst=message, status='U', redbr=redbr, time=datetime.now(timezone.utc))
            poruka.save()
            print("RECEIVE MESSAGE, my chat id",self.chat_id, "my id",self.idkor)
            async_to_sync(self.channel_layer.group_send)( #saljemo poruku iz servera u grupu
                str(self.chat_id),
                {
                    'type':'chat.message',
                    'message': message,
                    'redbr': redbr,
                    'sender': self.idkor,
                }
            )
            other_user_id = prep.idkor1_id if self.idkor == prep.idkor2_id else prep.idkor2_id
            print("OTHER USER ID",other_user_id)
            print("MY ID",self.idkor)
            print("SENDING UPDATE TO OTHER USER")
            async_to_sync(self.channel_layer.group_send)( #saljemo poruku iz servera u grupu
                "U"+str(other_user_id),
                {
                    'type':'update',
                    'sender': self.idkor,
                }
            )

    def chat_message(self, event): #event tipa chat.message dolazi u server iz grupe
        type = event['type']
        print("CHAT MESSAGE")
        sender = event['sender']
        if sender == self.idkor:
            print("SEND MESSAGE MY ID IS SENDER, my id",self.idkor)
            print(event)
            return
        if type == 'chat.message': #ako je tip chat, poslata je u grupu chata sobe, prosledjuje klijentu se kao poruka
            message = event['message']
            redbr = event['redbr']
            
            print("SEND MESSAGE, my chat id",self.chat_id, "my id",self.idkor)
            poruka = models.Poruka.objects.get(idpre=self.chat_id, redbr=redbr)
            poruka.status = 'R'
            poruka.save()

            self.send(text_data=json.dumps({
                'type':'chat',
                'message':message
            }))

    def update(self, event): #event tipa update dolazi u server iz grupe
        print("UPDATE")
        self.send(text_data=json.dumps({
            'type':'update'
        }))