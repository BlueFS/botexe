import discord
from discord.ext import commands
import json
from pathlib import Path
import os

# Allows other files to be imported from the command file
current_dir = os.path.dirname(os.path.abspath(__file__))
sounds_dir = os.path.join(current_dir, 'sounds')

from commands import basic, bell, automated

# Try to open the json file to read the token data
try:
    config_path = Path(__file__).parent / 'config.json'
    with open(config_path, 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
        token = config_data['token']
        clientId = config_data['clientId']
        guildId = int(config_data['guildId'])
        welcomeId = int(config_data['welcomeId'])
        generalId = int(config_data['generalId'])
        logId = int(config_data['logId'])
        print('Information loaded!')
except FileNotFoundError: 
    print('Error 1: Critical error: File not found!')
except json.JSONDecodeError:
    print('Error 2: Invalid format: File must be .json!')   

# Define client and tree
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='/', intents=intents)

# Logs bot in
# TODO Make sure not everything is in on_ready. If bot disconnects, it will redo this
# and send all the messages again. We don't want that
Started = False

@client.event
async def on_ready(): 

    if Started == False:
        await automated.online(client, generalId)
        automated.member_join(client)
        
        basic_commands = [
            basic.greet,
            basic.ping, 
            basic.cmds, 
            basic.dev, 
            basic.help_command_setup, 
            basic.bug, 
            basic.bugs, 
            basic.destruction,
            basic.qrcode
            # Add a new command under this line
            # Should be formatted as basic.command_name
        ]
        for command in basic_commands:
            command(client, guildId)

        # Commands from bell.py
        bell.dingdong(client, guildId, sounds_dir)

        await client.tree.sync(guild=discord.Object(guildId))
        # Remove the comment when ready to publish and remove the guildID part
        # await client.tree.sync(guild=None)
        print(f'Logged in as {client.user}')
        message = 'Bot joined'
    else:
        pass

# Run the client
client.run(token)