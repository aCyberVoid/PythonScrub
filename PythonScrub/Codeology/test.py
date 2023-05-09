# Author: aCyberVoid#0007
# Application: @Dad#1349
# Platform: Discord
# Python Version: 3.10.6
# Creation Date: 2021-09-13
# Last Updated: 2021-09-13
# Description: A Discord bot that uses the Dadjokes.io API to get random dad jokes

# Importing the necessary libraries
import discord
import requests
import json
from discord import app_commands
from discord.ext import commands
from config import TOKEN
from config import url
from config import headers

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Confirming connection to the Dadjokes.io API
# response = requests.request("GET", url, headers=headers)
# print(response.text)

# Confirming connection to Discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Creating a command group - yomomma
# Get a random Yo Momma joke from the Yo Mama Jokes API
@bot.tree.command(name='yomomma')
async def yomomma(interaction: discord.Interaction):
    # Get a random joke from the API
    response = requests.request("GET", ymurl, ymheaders=ymheaders)
    data = json.loads(response.text)
    # Try to get a joke from the API
    try:
        # Format the joke
        ymjoke = (f"**Yo Momma**\n||{data['joke']}||")
    # If there is no joke found, send a message to the user
    except KeyError:
        await interaction.response.send_message("No joke found")
    # If there is a joke found, send the joke to the user
    await interaction.response.send_message(ymjoke)

# Run the bot
bot.run(TOKEN)