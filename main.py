import discord
import random
import os
import asyncio
from flask import Flask
from keep_alive import keep_alive

keep_alive()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

port = os.environ.get('PORT', 5000)  # Default to 5000 if PORT environment variable is not set

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if (message.author.id == 1150448986264698980):
            print(f'Message received user {message.author.name}: {message.content}')
            for component in message.components:
                for child in component.children:
                    if child.label == "Enter":
                    #    await asyncio.sleep(random.randint(5, 10))
                        await child.click()

if __name__ == "__main__":
    client = MyClient()
    client.run(os.environ['TOKEN'])
