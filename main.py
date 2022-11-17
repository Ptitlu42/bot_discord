import discord
import datetime

from discord.ext import commands

now = datetime.datetime.now()

TOKEN = 'MTA0Mjc1NDA0ODc3Mzg2OTU3OQ.G_MX5d.cIErcGJjuHA-rHfdtGEDAw0sdIbPqbIEHHIeC8'

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='', intents=intents)

a = False

@client.event
async def on_ready():
    print("Ready!")
    

@client.event
async def on_disconnect():
    print("Not ready!")

@client.event
async def on_message(date):
    if date.content.lower() == "date":
        await date.channel.send("date!")

@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("Pong!")
        





client.run ("MTA0Mjc1NDA0ODc3Mzg2OTU3OQ.G_MX5d.cIErcGJjuHA-rHfdtGEDAw0sdIbPqbIEHHIeC8")
