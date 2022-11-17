import discord
import datetime

from discord.ext import commands

now = datetime.datetime.now()

TOKEN = 'MTA0Mjc1NDA0ODc3Mzg2OTU3OQ.GOakq5.AUf6-ld_s0zoTF9wsmQurFt56ZdhkIMDJeoLfU'

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='', intents=intents)


@client.event
async def on_ready():
    print("Ready!")
    

@client.event
async def on_disconnect():
    print("Not ready!")

@client.event
async def on_message(message):
        if message.content.lower() == "date":
          await message.channel.send(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
        if message.content.lower() == "ping":
          await message.channel.send("Pong!")
        

client.run ("MTA0Mjc1NDA0ODc3Mzg2OTU3OQ.GOakq5.AUf6-ld_s0zoTF9wsmQurFt56ZdhkIMDJeoLfU")
