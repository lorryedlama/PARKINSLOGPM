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

port = os.environ.get('PORT', 8080)  # Default to 5000 if PORT environment variable is not set

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

client = MyClient()
 

if __name__ == "__main__":
#    client.run(os.environ['TOKEN'])
