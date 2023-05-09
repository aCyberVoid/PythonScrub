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

# Creating the bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Confirming connection to Discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Creating a command group - hello
@bot.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hey {interaction.user.name}!')

# Creating a command group - ping
# Check the latency of the bot
@bot.tree.command(name='ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! {round(bot.latency * 1000)}ms')

# Creating a command group - say
# Tell the bot what to say
@bot.tree.command(name='say')
@app_commands.describe(say='What should I say?')
async def say(interaction: discord.Interaction, say: str):
    await interaction.response.send_message(f'{interaction.user.name} says: {say}')

# Creating a command group - dadjoke
# Get a random dad joke from the Dadjokes.io API
@bot.tree.command(name='dadjoke')
async def dadjoke(interaction: discord.Interaction):
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