# This holds the automated files that do not require user input
import discord
from discord.ext import commands
from datetime import date, datetime

intents = discord.Intents.default()

# Send bot connected message
async def online(client, generalId):
    print('Trying to send connected message')
    # Channel checks
    try:
        channel = await client.fetch_channel(generalId)
        if channel and channel.permissions_for(channel.guild.me).send_messages:
            await channel.send('Bot has been connected!')
            print(f'Bot connected and message sent in {channel}')
    except Exception as e: 
        print('Error 3: Bot does not have permission to post in the channel!')
        print(f'Error: {e}')

# Welcome user
def member_join(client, welcomeId, logId):
    @client.event
    async def on_member_join(client, welcomeId, logId, member):
        welcome_channel = client.get_channel(welcomeId)
        log_channel = client.get_channel(logId)
        # Check if the channel exists and the bot has permission to send messages
        try:
            if (welcome_channel and welcome_channel.permissions_for(welcome_channel.guild.me).send_messages 
                and log_channel and log_channel.permissions_for(log_channel.guild.me).send_messages):

                await welcome_channel.send(f'Welcome {member.mention} to the server!')
                print(f'{member.name} joined the server and was greeted.')
                await log_channel.send(f'{member.name} joined the server on {datetime.now()} CST.')
        except:
            print('Error 3: Bot does not have permission to post in the channel!')