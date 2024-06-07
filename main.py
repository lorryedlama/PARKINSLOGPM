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
    if message.author.id == 1150448986264698980:
        # Check if the bot is mentioned and the message contains the embed title
        for embed in message.embeds:
            if client.user.mentioned_in(message) and "### 🎟️\xa0\xa0Raffle ended!" in embed.description:
                response = random.choice(responses)
                async with message.channel.typing():
                         await asyncio.sleep(random.randint(5, 20))
                         await message.channel.send(response)

        # Your existing code for the raffle functionality with components
        for component in message.components:
            for child in component.children:
                if child.label == "Enter":
                    # Add random chance for child.click()
                    if random.random() < 0.75:  # 75% chance of clicking
                        await asyncio.sleep(random.randint(8, 16))
                        await child.click()
                        if random.random() < 0.4:  # 40% chance of responding
                            response = random.choice(responses)
                            if random.random() < 0.1:  # 50% chance of using message.reply
                             async with message.channel.typing():
                                await asyncio.sleep(random.randint(5, 20))
                                await message.reply(response)
                            else:
                             async with message.channel.typing():
                                await asyncio.sleep(random.randint(5, 20))
                                await message.channel.send(response)

if __name__ == "__main__":
    client.run(os.environ['TOKEN'])
