import discord
from discord import app_commands, Embed

# Basic commands

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

def cmds(client, guildId):
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

def dev(client, guildId):
    @client.tree.command(
    name='dev',
    description='Idk, just says idk. This does not actually do anything',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def dev_command(interaction: discord.Interaction):
        await interaction.response.send_message('Idk')

def help(client, guildId):
    @client.tree.command(
    name='help',
    description='Will tell you who to contact',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def help_command(interaction: discord.Interaction):
        await interaction.response.send_message('Please contact BlueFS or SlipperyBooney')

def bug(client, guildId):
    @client.tree.command(
    name='bug',
    description='This doesn\'t work yet.',
    # remove line under later
    guild=discord.Object(guildId)
    )
    async def bug_command(interaction: discord.Interaction):
        await interaction.response.send_message('NOT WORKING YET')

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