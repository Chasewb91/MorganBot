from discord import commands
import discord
import quandl
import keep_alive.py
import os
from dotenv import load_dotenv


quandl.ApiConfig.api_key = "TKsCj3PrxPF3guUZgqTN"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # pulls discord bot token from .env file

key = os.getenv('key')

wkey = os.getenv('wkey')


client = discord.Client()

client = commands.Bot(command_prefix='$')  #Makes the bot prefix.

client.run(TOKEN)

keep_alive.keep_alive()  #keep this at the end
