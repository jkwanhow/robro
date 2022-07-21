from pickle import FALSE
import discord
import os
import time
from dotenv import load_dotenv
from choice import Choice
from leo import Leo
from fishing import FishingGame

choice = Choice()
leo = Leo("leo_phrases.txt")
fish = FishingGame()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    leo = Leo("leo_phrases.txt")
    choice = Choice()
    fish = FishingGame()
    servers_string = client.guilds[0].name
    if len(client.guilds)!=1:
        for guild in client.guilds[1:]:
            servers_string += f", {guild.name}"
        

    print(f"Logged in as {client.user}!\nconnected to servers: {servers_string}")
    
@client.event
async def on_message(message):
    global fish
    slurs = set(["fuck", "shit", "cunt", "bitch", "bastard"])
    if message.author == client.user:
        return

    if message.content == "-clear":
        ids = []
        for msg in await message.channel.history(limit=1000).flatten():
            await msg.delete()
        

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

    if message.content == "-fish cast":
        user = message.author
        await message.channel.send(fish.catch(str(user)))
    if message.content == "-fish inv":
        user = message.author
        await message.channel.send(fish.players_fish(str(user)))


    if message.content.startswith('-leo'):
        global leo
        if message.content[:10] == "-leo says ":
            verb = message.content[10:]
            await message.channel.send(leo.use_verb(verb))
        elif message.content[:9] == "-leo add ":
            phrase = message.content[9:]
            await message.channel.send(leo.add_phrase("leo_phrases.txt" ,phrase))
            leo = Leo("leo_phrases.txt")
        elif message.content == "-leo phrases":
            await message.channel.send(leo.all_phrases())
        elif message.content == '-leo random':
            await message.channel.send(leo.random_line())
        else:
            await message.channel.send("I can be a bot, but I can also be like Leo\n\
(use a verb to create a leo phrase):-leo says _____\n(see all leo phrases)-leo phrases\n\
(get a random leo sentence)-leo random\n(add a new leo phrase needs to contain -verb- where the verbs should go, see -leo phrases for example):-leo add ________")




client.run(TOKEN)