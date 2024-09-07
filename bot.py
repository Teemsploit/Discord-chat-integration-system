import discord
import asyncio

TOKEN = ''
CHANNEL_ID = 12345

intents = discord.Intents.default()
intents.messages = True

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.channel.id == CHANNEL_ID and not message.author.bot:
            print(f'Received message: {message.content}')

client = MyClient(intents=intents)
client.run(TOKEN)
