import discord
import os
import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

now = datetime.datetime.now()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

#affiche ready sur le terminal quand le bot est OP

@client.event
async def on_ready(): 
    print("Ready!")
    

#affiche not ready sur le terminal quand le bot est HS    

@client.event
async def on_disconnect(): 
    print("Not ready!")

#afficher date quand !date est taper

@client.event
async def on_message(message):

        if message.content.lower() == "!date": 
          await message.channel.send(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))

#afficher pong quand !ping est taper

        if message.content.lower() == "!ping": 
          await message.channel.send("Pong!")
        
     
 #envoyer bienvenue à l'arrivé d'un membre dans le discord

@client.event
async def on_member_join(member):
    acceuil_channel: discord.TextChannel = client.get_channel(1042922943354773657)     #definir sur quel salon agit le member_join et definir le type de salon
    await acceuil_channel.send(content=f"Bienvenue {member.display_name} !")          



client.run (os.getenv("discord_token"))
