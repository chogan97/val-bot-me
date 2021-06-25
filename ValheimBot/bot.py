# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = client.guilds[0]
    channel = guild.text_channels[2]
    await channel.send('At your command')


@client.event
async def on_message(message):
    guild = client.guilds[0]
    channel = guild.text_channels[2]
    
    if message.channel != channel:
        return
    
    if message.author == client.user:
        return
    
    if message.content == '?start':
        response = 'Starting server'
        await message.channel.send(response)
        #TODO: Thor make the shit work with the server
        serverInfo = 'this is thor\'s job'
        await message.channel.send(serverInfo)
    
    if message.content == '?stop':
        response = 'Stopping server'
        await message.channel.send(response)
        #TODO: Thor make this shit work
    


client.run(TOKEN)

    