import discord
import random
import time

# Replace with your own Discord bot token
TOKEN = "MTA0MjE1MDE0MDQzNTIzNDg0Ng.G3FU9o.Qj6S8_UNCczdp4dcLI5JnF8WwPuAquwb0VxVOE"

# Replace with the channel ID of the channel you want to send the dad jokes to
CHANNEL_ID = "<1042171537719037972>"

# List of dad jokes to choose from
DAD_JOKES = [
    "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
    "What do you call a belt with a watch on it? A waist of time.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Did you hear about the cheese factory that exploded? There was nothing left but de-brie.",
    "Why do chickens lay eggs? To get cracking!",
]

client = discord.Client()

@client.event
async def on_ready():
    # Get the channel object
    channel = client.get_channel(CHANNEL_ID)

    while True:
        # Choose a random dad joke
        joke = random.choice(DAD_JOKES)

        # Send the dad joke to the channel
        await channel.send(joke)

        # Wait 5 minutes before sending the next dad joke
        time.sleep(5 * 60)

client.run(TOKEN)
