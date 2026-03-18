# This holds the automated files that do not require user input
import discord
from discord.ext import commands
from datetime import date, datetime

intents = discord.Intents.default()

# Display IDs
Welcome_ID = 1483877177287250031
General_ID = 1420242677772845129
Log_ID = 1483891119048626218

# Welcome user
def member_join(client):
    @client.event
    async def on_member_join(member):
        welcome_channel = client.get_channel(Welcome_ID)
        log_channel = client.get_channel(Log_ID)
        # Check if the channel exists and the bot has permission to send messages
        try:
            if (welcome_channel and welcome_channel.permissions_for(welcome_channel.guild.me).send_messages 
                and log_channel and log_channel.permissions_for(log_channel.guild.me).send_messages):

                await welcome_channel.send(f'Welcome {member.mention} to the server!')
                print(f'{member.name} joined the server and was greeted.')
                await log_channel.send(f'{member.name} joined the server on {date.today()} at {datetime.now()}.')
        except:
            print('Error 3: Bot does not have permission to post in the channel!')

def online(client):
    @client.event
    async def on_ready():
        channel = client.get_channel(General_ID)
        # Channel checks
        try:
            if channel and channel.permissions_for(channel.guild.me).send_messages:
                await channel.send('Bot has been connected!')
        except: 
            print("Error 3: Bot does not have permission to post in the channel!")