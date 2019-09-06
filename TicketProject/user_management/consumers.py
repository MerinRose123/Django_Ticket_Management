from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotConsumer(AsyncJsonWebsocketConsumer):
    """
    Connecting asynchronous communication via websockets
    """

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)

    async def user_gossip(self, event):
        await self.send_json(event)





