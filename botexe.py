import discord
from discord.ext import commands
from discord import app_commands, Embed
import json
from pathlib import Path

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


# Commands
@client.tree.command(
     name='ping',
     description='Responds with pong.',
     # THE GUILDID IS ONLY WHEN TESTING WITH THE EXE SERVER
     # REMOVE THE NEXT LINE WHEN OPENING COMMANDS TO EVERYONE
     guild=discord.Object(guildId)
)
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')

@client.tree.command(
    name='cmds',
    description='Lists the commands',
    # remove line under later
    guild=discord.Object(guildId)
)
async def cmds_command(interaction: discord.Interaction):
    embed = Embed(
        title="Commands",
        description="Here are all the commands",
        # This is the color on the side
        color=0x000000
    )

    embed.add_field(name="/cmd", value="Displays all the commands.", inline=False)
    embed.add_field(name="/ping", value="Replies with pong.", inline=False)
    embed.add_field(name="/bug", value="NOT YET IMPLEMENTED -- Will allow users to submit bug reports.", inline=False)
    embed.add_field(name="/dev", value="Idk.", inline=False)
    embed.add_field(name="/bugs", value="Will bug slipperybooney.", inline=True)

    await interaction.response.send_message(embed=embed)

@client.tree.command(
    name='dev',
    description='Idk, just says idk. This does not actually do anything',
    # remove line under later
    guild=discord.Object(guildId)
)
async def dev_command(interaction: discord.Interaction):
    await interaction.response.send_message('Idk')

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