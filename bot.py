# bot.py
import os

import requests
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    r = requests.post('http://localhost:5005/webhooks/rest/webhook',
                      json={"sender": message.author.display_name, "message": message.content})
    lines = r.json()
    message_for_user = ''
    for line in lines:
        message_for_user = message_for_user + '\n' + line.get('text')
    await message.channel.send(message_for_user)


client.run(TOKEN)
