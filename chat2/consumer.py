

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pk = self.scope['url_route']['kwargs']['pk']
        print(pk)
        self.roomGroupName = "group_chat"+pk
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        time = text_data_json["time"]
        name = text_data_json["name"]
        msgtype = text_data_json["msgtype"]
        
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "time": time,
                "name": name,
                "msgtype":msgtype
            })

    async def sendMessage(self, event):
        message = event["message"]
        time = event["time"]
        name = event["name"]
        msgtype = event["msgtype"]
        print(name,message)
        await self.send(text_data=json.dumps({"message": message,'name':name, "time": time,"msgtype":msgtype}))