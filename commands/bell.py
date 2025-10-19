import discord
from discord import app_commands, Embed
from playsound import playsound
from pathlib import Path

def dingdong(client, guildId, sounds_dir):
    doorbell= Path(sounds_dir) / 'doorbell.wav'

    @client.tree.command(
     name='bell',
     description='Rings the doorbell!',
     # THE GUILDID IS ONLY WHEN TESTING WITH THE EXE SERVER
     # REMOVE THE NEXT LINE WHEN OPENING COMMANDS TO EVERYONE
     guild=discord.Object(guildId)
    )
    async def hello_command(interaction: discord.Interaction):
        await interaction.response.send_message('Doorbell rung!')
        try:
            playsound(str(doorbell))
        except Exception as e:
            await interaction.followup.send(f"Error playing sound: {e}")
    
