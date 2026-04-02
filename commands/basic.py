# This file contains all the basic commands
import discord
from discord import app_commands, Embed
from commands import qr
import os

# Responds with hello
def greet(client, guildId):
    @client.tree.command(
     name='hello',
     description='Responds with hello!',
     # THE GUILDID IS ONLY WHEN TESTING WITH THE EXE SERVER
     # REMOVE THE NEXT LINE WHEN OPENING COMMANDS TO EVERYONE
     guild=discord.Object(guildId)
    )
    async def hello_command(interaction: discord.Interaction):
        await interaction.response.send_message('Hello!')
        print('Printed hello')

# Responds with pong
def ping(client, guildId):
    @client.tree.command(
        name='ping',
        description='Responds with pong.',
        # THE GUILDID IS ONLY WHEN TESTING WITH THE EXE SERVER
        # REMOVE THE NEXT LINE WHEN OPENING COMMANDS TO EVERYONE
        guild=discord.Object(guildId)
    )
    async def ping_command(interaction: discord.Interaction):
        await interaction.response.send_message('Pong!')
        print('Printed pong')

# Lists the commands
def cmds(client, guildId):
    @client.tree.command(
    name='cmds',
    description='Lists the commands',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def cmds_command(interaction: discord.Interaction):
        embed = Embed(
            title='Commands',
            description='Here are all the commands',
            # This is the color on the side
            color=0x000000
        )
        commands = [
            'greet', 'ping', 'cmds', 'dev',
            'help', 'bug', 'bugs', 'destruction'
        ]
        description = [
            'Says hello.',
            'Replies with pong.',
            'Displays all cmds',
            'Sends \'idk\'',
            'Tells you who to contact',
            'Nothing implemented yet. Kinda just a placeholder',
            'Will ping a user of choice',
            'Will ping everyone 10 times.'
        ]
        for i in range(len(commands)):
            embed.add_field(name=commands[i], value=description[i], inline=False)
        await interaction.response.send_message(embed=embed)
        print('Printed commands')


# Literally nothing
def dev(client, guildId):
    @client.tree.command(
    name='dev',
    description='Idk, just says idk. This does not actually do anything',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def dev_command(interaction: discord.Interaction):
        await interaction.response.send_message('Idk')
        print('Printed IDK')

# Tells you who to contact
def help_command_setup(client, guildId):
    @client.tree.command(
    name='help',
    description='Will tell you who to contact',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def help_command_setup_command(interaction: discord.Interaction):
        await interaction.response.send_message('Please contact BlueFS or SlipperyBooney')
        print('Told to contact moderator')

# Nothing yet
def bug(client, guildId):
    @client.tree.command(
    name='bug',
    description='This doesn\'t work yet.',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def bug_command(interaction: discord.Interaction):
        await interaction.response.send_message('NOT WORKING YET')

# Just pings a user
def bugs(client, guildId):
    @client.tree.command(
    name='bugs',
    description='Can be used to ping Slipperybooney.',
    # remove line under later
    guild=discord.Object(guildId)
    )
    @app_commands.describe(user='The user you want to ping.')
    async def bugs_command(interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f'{user.mention}')
        print('Bugged slipperybooney')

# 10x pinger
def destruction(client, guildId):
    @client.tree.command(
        name='destruction',
        description='Pings everyone ten times',
        guild=discord.Object(guildId)
    )
    async def destruction_command(interaction: discord.Interaction):
        await interaction.response.send_message('@everyone')
        for _ in range(9):
            await interaction.followup.send('@everyone')
        print('Pinged everyone 10 times')

# QR Code generator
def qrcode(client, guildId):
    @client.tree.command(
        name='qrcode',
        description='Creates a QR code based off a URL',
        guild=discord.Object(guildId)
    )
    async def qr_command(interaction: discord.Interaction, url: str, name: str):
        filename = qr.generate(url, name)
        qr_bytes = qr.qr_storage[filename]
        qr_bytes.seek(0)

        file = discord.File(fp=qr_bytes, filename=filename)
        await interaction.response.send_message(file=file)
        print('QRCode generated')

''' This is the start of a comment

def INSERT NAME HERE (client, guildId):
    @client.tree.command(
        name='',
        description='',
        guild=discord.Object(guildId)
    )
    async def name(interaction: discord.Interaction):
        await interaction.response.send_message('enter message here')

'''