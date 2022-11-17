import discord
import datetime

from discord.ext import commands

now = datetime.datetime.now()

TOKEN = 'MTA0Mjc1NDA0ODc3Mzg2OTU3OQ.GOakq5.AUf6-ld_s0zoTF9wsmQurFt56ZdhkIMDJeoLfU'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True


client = commands.Bot(command_prefix='', intents=intents)


@client.event
async def on_ready(): #affiche ready sur le terminal quand le bot est OP
    print("Ready!")
    

@client.event
async def on_disconnect(): #affiche not ready sur le terminal quand le bot est HS
    print("Not ready!")

@client.event
async def on_message(message):
        if message.content.lower() == "!date": #afficher date quand date est taper
          await message.channel.send(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
        if message.content.lower() == "!ping": #afficher pong quand ping est taper
          await message.channel.send("Pong!")
        

@client.event
async def on_member_join(member):
    acceuil_channel: discord.TextChannel = client.get_channel(1042922943354773657) #definir sur quel salon agit le member_join et definir le type de salon
    await acceuil_channel.send(content=f"Bienvenue {member.display_name} !") #envoyer bienvenue à l'arrivé d'un membre dans le discord

    













client.run ("MTA0Mjc1NDA0ODc3Mzg2OTU3OQ.GOakq5.AUf6-ld_s0zoTF9wsmQurFt56ZdhkIMDJeoLfU")
