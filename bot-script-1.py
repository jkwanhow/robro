import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    servers_string = client.guilds[0].name
    if len(client.guilds)!=1:
        for guild in client.guilds[1:]:
            servers_string += f", {guild.name}"
        

    print(f"Logged in as {client.user}!\nconnected to servers: {servers_string}")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)