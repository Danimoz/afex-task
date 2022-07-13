import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Client

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        cid = text_data_json['cid']
        total_balance = text_data_json['total_balance']
        available_balance = text_data_json['available_balance']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'cid': cid,
                'total_balance': total_balance,
                'available_balance': available_balance 
            }
        )
    
    def chat_message(self, event):
        cid = event['cid']
        total_balance = event['total_balance']
        available_balance = event['available_balance']
        try:
            acct = Client.objects.get(cid = cid)
            acct.clientwallet.total_balance = total_balance
            acct.clientwallet.available_balance = available_balance
            acct.save()
        except:
            successmsg = f'Error, no account found with that account number'
            
        self.send(text_data=json.dumps({
            'type': 'chat',
            'cid': cid,
            'total_balance': total_balance,
            'available_balance': available_balance
        }))