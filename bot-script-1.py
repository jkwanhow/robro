from pickle import FALSE
import discord
import os
import time
from dotenv import load_dotenv
from choice import Choice

choice = Choice()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    choice = Choice()
    servers_string = client.guilds[0].name
    if len(client.guilds)!=1:
        for guild in client.guilds[1:]:
            servers_string += f", {guild.name}"
        

    print(f"Logged in as {client.user}!\nconnected to servers: {servers_string}")
    
@client.event
async def on_message(message):
    slurs = set(["fuck", "shit", "cunt", "bitch", "bastard"])
    if message.author == client.user:
        return

    if slurs.intersection(set(message.content.split())):
        await message.channel.send('No swearing here please...')
        await message.channel.send('`bitch`')


    if message.content.startswith('hello chungi'):
        await message.channel.send('Hello!')

    if message.content.startswith('-chooser'):
        global choice
        if message.content[:13] == '-chooser add ':
            to_add = message.content[13:]
            if to_add:
                await message.channel.send(choice.add(to_add))
            else:
                await message.channel.send(choice.about("add"))
        elif message.content[:16] == '-chooser remove ':
            to_remove = message.content[16:]
            if to_remove:
                await message.channel.send(choice.remove(to_remove))
            else:
                await message.channel.send(choice.about("remove"))
        elif message.content == "-chooser current":
            await message.channel.send(choice.show_current())
        elif message.content == "-chooser pick":
            await message.channel.send(choice.pick())
        elif message.content == "-chooser reset":
            choice = Choice()
            await message.channel.send("Choice list has been reset")
        else:
            await message.channel.send("to use chooser:\n(to add):-chooser add *item*\n(to remove):-chooser remove *item*\
\n(to show current list):-chooser current\n(to pick an item:-chooser pick\n(to reset list):-chooser reset")


client.run(TOKEN)