import discord
import random
import os
import asyncio
from flask import Flask
from keep_alive import keep_alive

responses = [
    "Thx",
    "Thanks",
    "Ty",
    "thx",
    "ty",
    "thanks",
    "thank you",
    "Thank you",
    "lfg",
    "Thank you",
    "tysm",
    "thankss",
]

keep_alive()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

port = os.environ.get('PORT', 8080)  # Default to 5000 if PORT environment variable is not set

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def join_voice_channel(self, channel_id):
        voice_channel = self.get_channel(channel_id)
        if voice_channel:
            if not self.voice_clients:
                await voice_channel.connect()
            else:
                await self.voice_clients[0].move_to(voice_channel)

    async def leave_voice_channel(self):
        if self.voice_clients:
            await self.voice_clients[0].disconnect()

client = MyClient()

@client.event
async def on_message(message):
    if message.content == '!aji' and message.author.id == 740547277164249089:
        print("Command received from correct user.")
        await asyncio.sleep(random.randint(5, 20))
        await client.join_voice_channel(1239293213525803052)

    if message.content == '!st9':  # New condition for leaving voice channel
        print("Leaving voice channel.")
        await asyncio.sleep(random.randint(1, 6))
        await client.leave_voice_channel()

    if message.author.id == 1150448986264698980 and message.guild.id != 1236380949663711313:
        print("Message from bot.")
        for embed in message.embeds:
            if client.user.mentioned_in(message) and "### 🎟️\xa0\xa0Raffle ended!" in embed.description:
                print("Raffle ended.")
                response = random.choice(responses)
                async with message.channel.typing():
                    await asyncio.sleep(random.randint(5, 20))
                    await message.channel.send(response)

        for component in message.components:
            for child in component.children:
                if child.label == "Enter":
                    await asyncio.sleep(random.randint(3, 7))
             #      await child.click()

if __name__ == "__main__":
    client.run(os.environ['TOKEN'])
