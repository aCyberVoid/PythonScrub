# Author: aCyberVoid#0007
# Application: YoMama#5946
# Platform: Discord
# Python Version: 3.10.6
# Creation Date: 2021-09-13
# Last Updated: 2021-09-13
# Description: A Discord bot that uses the Yo Mama Jokes API to get random Yo Mama jokes

# Importing the necessary libraries
import discord
import requests
import json
from discord import app_commands
from discord.ext import commands
from config import TOKEN
from config import url
from config import headers

# Creating the bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Creating a the joke variable
joke = ""

# Confirming connection to Discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Creating a command group - ping
# Check the latency of the bot
@bot.tree.command(name='ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! {round(bot.latency * 1000)}ms')

# Creating a command group - yomama
# Get a random yo mama joke from the YoMama API
@bot.tree.command(name='yomama')
async def yomama(interaction: discord.Interaction):
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    # Try to get a joke from the API
    try:
        # Format the joke
        joke = (f"**{data['body'][0]['setup']}**\n||{data['body'][0]['punchline']}||")
    # If there is no joke found, send a message to the user
    except KeyError:
        await interaction.response.send_message("No joke found")
    # If there is a joke found, send the joke to the user
    await interaction.response.send_message(joke)

# Run the bot
bot.run(TOKEN)