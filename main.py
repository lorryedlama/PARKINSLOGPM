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

client = MyClient()

@client.event
async def on_message(message):
    if message.author.id == 1150448986264698980 and (message.guild.id == 1239293213525803048):# or message.guild.id == 930591458682081301):
        print("Message from bot.")
        for embed in message.embeds:
            if client.user.mentioned_in(message) and "### 🎟️\xa0\xa0Raffle ended!" in embed.description:
                print("Raffle ended.")
                response = random.choice(responses)
                async with message.channel.typing():
                    await asyncio.sleep(random.randint(5, 20))
                    await message.channel.send(response)
            if "### 🎟️  Raffle created!" in embed.description:
                for component in message.components:
                    for child in component.children:
                        if child.label == "Enter":
                            await asyncio.sleep(random.randint(3, 15))
                            await child.click()  # Uncomment this line if you want to simulate clicking the "Enter" button
        for component in message.components:
            for child in component.children:
                if child.label == "Enter":
                    await asyncio.sleep(random.randint(3, 15))
              #     await child.click()

if __name__ == "__main__":
    client.run(os.environ['TOKEN'])
