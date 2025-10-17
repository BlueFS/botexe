import discord
from discord.ext import commands
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


intents = discord.Intents.default()
intents.message_content = True # Required for prefix commands and message content access
client = commands.Bot(intents=intents)

# Logs bot in
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Token secret goes here
client.run(token)