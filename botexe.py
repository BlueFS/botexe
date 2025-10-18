import discord
from discord.ext import commands
from discord import app_commands
import json
from pathlib import Path
import os
import sys

# Allows other files to be imported from the command file
current_dir = os.path.dirname(os.path.abspath(__file__))
commands_dir = os.path.join(current_dir, 'commands')

sys.path.insert(0, commands_dir)

from commands import basic

# Try to open the json file to read the token data
try:
    config_path = Path(__file__).parent / 'config.json'
    with open(config_path, 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
        token = config_data["token"]
        clientId = config_data["clientId"]
        guildId = config_data["guildId"]
        print('Information loaded!')
except FileNotFoundError: 
    print('Critical error: File not found!')
except json.JSONDecodeError:
    print('Invalid format: File must be .json!')   

# Define client and tree
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='/', intents=intents)

# Logs bot in
@client.event
async def on_ready():
    await client.tree.sync(guild=discord.Object(id=guildId))
    await client.tree.sync(guild=None)
    print(f'Logged in as {client.user}')


# Command links and names
basic.greet(client, guildId)

basic.ping(client, guildId)

basic.cmds(client, guildId)

basic.dev(client, guildId)

@client.tree.command(
    name='help',
    description='Will tell you who to contact',
    # remove line under later
    guild=discord.Object(guildId)
)
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message('Please contact BlueFS or SlipperyBooney')

@client.tree.command(
    name='bug',
    description='This doesn\'t work yet.',
    # remove line under later
    guild=discord.Object(guildId)
)
async def bug_command(interaction: discord.Interaction):
    await interaction.response.send_message('NOT WORKING YET')

@client.tree.command(
    name='bugs',
    description='Can be used to ping Slipperybooney.',
    # remove line under later
    guild=discord.Object(guildId)
)
@app_commands.describe(user='The user you want to ping.')
async def bugs_command(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f'{user.mention}')

# Token secret goes here
client.run(token)